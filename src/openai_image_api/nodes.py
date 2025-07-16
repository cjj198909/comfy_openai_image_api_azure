from inspect import cleandoc
import base64
import numpy as np
import torch
from PIL import Image
import io
import os
import logging
from typing import Optional, Union, Tuple, List
from openai import OpenAI, AzureOpenAI

# 导入本地模块
from .azure_config import AzureConfigManager, AzureOpenAIConfig
from .image_utils import ImageProcessor

# Try to load environment variables from .env file
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    # dotenv is optional, continue without it
    pass

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# ANSI escape codes for colors
RED = "\033[91m"
RESET = "\033[0m"

class OpenAIImageAPI:
    """
    A node for generating images using OpenAI's Image API
    
    This node allows users to generate or edit images using OpenAI's DALL-E 3 or GPT-Image-1 models.
    It supports various output sizes, quality settings, and can work with both single and multiple input images.
    
    Features:
    - Image generation from text prompts
    - Image editing with Azure OpenAI integration
    - Robust error handling and logging
    - Support for multiple image formats and sizes
    - Environment variable configuration
    """
    
    # 配置参数
    CONFIG = {
        "default_api_version": "2025-04-01-preview",
        "default_model": "gpt-image-1",
        "supported_sizes": ["1024x1024", "1536x1024", "1024x1536"],
        "supported_qualities": ["low", "medium", "high"],
        "supported_providers": ["openai", "azure"],
        "max_retries": 3,
        "timeout": 60
    }
    
    def __init__(self):
        logger.info("Initializing OpenAI Image API node")
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "prompt": ("STRING", {
                    "multiline": True,
                    "default": "A beautiful image"
                }),
                "model": (["gpt-image-1"],),
                "size": (s.CONFIG["supported_sizes"],),
                "quality": (s.CONFIG["supported_qualities"],),
                "provider": (s.CONFIG["supported_providers"],),
            },
            "optional": {
                "image": ("IMAGE",),
                "api_key": ("STRING", {
                    "multiline": False,
                    "default": ""
                }),
                "azure_endpoint": ("STRING", {
                    "multiline": False,
                    "default": ""
                }),
                "azure_api_version": ("STRING", {
                    "multiline": False,
                    "default": s.CONFIG["default_api_version"]
                }),
                "azure_deployment": ("STRING", {
                    "multiline": False,
                    "default": s.CONFIG["default_model"]
                }),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "generate_image"
    CATEGORY = "image/OpenAI"

    def _create_azure_client(self, config: AzureOpenAIConfig) -> AzureOpenAI:
        """
        创建 Azure OpenAI 客户端
        
        Args:
            config: Azure OpenAI 配置
            
        Returns:
            配置好的 Azure OpenAI 客户端
        """
        try:
            client = AzureOpenAI(
                api_key=config.api_key,
                api_version=config.api_version,
                azure_endpoint=config.endpoint,
                timeout=config.timeout
            )
            logger.info(f"Azure OpenAI client created successfully for endpoint: {config.endpoint}")
            return client
        except Exception as e:
            logger.error(f"Failed to create Azure OpenAI client: {e}")
            raise RuntimeError(f"Failed to create Azure OpenAI client: {e}")

    def _create_openai_client(self, api_key: str) -> OpenAI:
        """
        创建 OpenAI 客户端
        
        Args:
            api_key: OpenAI API 密钥
            
        Returns:
            配置好的 OpenAI 客户端
        """
        try:
            client = OpenAI(
                api_key=api_key,
                timeout=self.CONFIG["timeout"]
            )
            logger.info("OpenAI client created successfully")
            return client
        except Exception as e:
            logger.error(f"Failed to create OpenAI client: {e}")
            raise RuntimeError(f"Failed to create OpenAI client: {e}")

    def _validate_openai_config(self, api_key: str) -> None:
        """验证 OpenAI 配置参数"""
        if not api_key:
            raise RuntimeError("OpenAI API key is required. Set OPENAI_API_KEY environment variable or provide api_key parameter.")

    def generate_image(self, prompt: str, model: str, size: str, quality: str, provider: str, 
                      image: Optional[torch.Tensor] = None, api_key: Optional[str] = None, 
                      azure_endpoint: Optional[str] = None, azure_api_version: Optional[str] = None, 
                      azure_deployment: Optional[str] = None) -> Tuple[torch.Tensor]:
        """
        生成或编辑图像
        
        Args:
            prompt: 图像生成/编辑提示
            model: 使用的模型
            size: 图像尺寸
            quality: 图像质量
            provider: 服务提供商 (openai 或 azure)
            image: 可选的输入图像（用于编辑）
            api_key: API 密钥
            azure_endpoint: Azure 端点
            azure_api_version: Azure API 版本
            azure_deployment: Azure 部署名称
            
        Returns:
            生成的图像张量
        """
        operation_type = "editing" if image is not None and image.numel() > 0 else "generation"
        logger.info(f"Starting image {operation_type} with prompt: {prompt[:50]}...")
        
        try:
            # 初始化客户端
            if provider == "azure":
                # 创建 Azure 配置
                config = AzureConfigManager.create_config(
                    endpoint=azure_endpoint,
                    api_key=api_key,
                    api_version=azure_api_version,
                    deployment=azure_deployment
                )
                
                # 验证配置
                AzureConfigManager.validate_config(config)
                
                # 创建客户端
                client = self._create_azure_client(config)
                model_name = config.deployment
                
                # 记录配置摘要（隐藏敏感信息）
                config_summary = AzureConfigManager.get_config_summary(config)
                logger.info(f"Using Azure OpenAI config: {config_summary}")
                
            else:
                # 处理 OpenAI 配置
                key = api_key.strip() if api_key else None
                key = key or os.getenv("OPENAI_API_KEY")
                
                self._validate_openai_config(key)
                client = self._create_openai_client(key)
                model_name = model
            
            # 调用相应的 API
            if operation_type == "generation":
                logger.info("Calling image generation API")
                result = client.images.generate(
                    model=model_name,
                    prompt=prompt,
                    size=size,
                    quality=quality
                )
            else:
                logger.info("Calling image editing API")
                images = ImageProcessor.prepare_images_for_api(image)
                
                result = client.images.edit(
                    model=model_name,
                    image=images,
                    prompt=prompt,
                    size=size,
                    quality=quality
                )
            
            # 处理响应
            image_tensor = ImageProcessor.base64_to_tensor(result.data[0].b64_json)
            logger.info(f"Image {operation_type} completed successfully")
            
            return (image_tensor,)
            
        except Exception as e:
            error_message = f"Error in image {operation_type}: {str(e)}"
            logger.error(error_message)
            print(f"{RED}{error_message}{RESET}")
            raise RuntimeError(error_message) from e

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "OpenAI Image API": OpenAIImageAPI
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "OpenAI Image API": "OpenAI/Azure OpenAI Image API with gpt-image-1"
}
