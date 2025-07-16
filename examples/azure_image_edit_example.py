#!/usr/bin/env python3
"""
Azure OpenAI 图像编辑示例脚本

该脚本演示如何使用改进的 Azure OpenAI 图像编辑功能。
包含完整的错误处理、日志记录和配置管理。

使用方法:
    python examples/azure_image_edit_example.py

环境变量:
    AZURE_OPENAI_ENDPOINT - Azure OpenAI 端点
    AZURE_OPENAI_API_KEY - Azure OpenAI API 密钥
    AZURE_OPENAI_API_VERSION - API 版本 (可选)
    AZURE_OPENAI_DEPLOYMENT - 部署名称 (可选)
"""

import os
import sys
import logging
from pathlib import Path
from typing import Optional

# 添加项目根目录到 Python 路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.openai_image_api.azure_config import AzureConfigManager
from src.openai_image_api.image_utils import ImageProcessor
from openai import AzureOpenAI
from PIL import Image
import torch

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('azure_image_edit.log')
    ]
)
logger = logging.getLogger(__name__)

class AzureImageEditExample:
    """Azure OpenAI 图像编辑示例类"""
    
    def __init__(self):
        """初始化示例"""
        self.config = None
        self.client = None
        self.setup_client()
    
    def setup_client(self):
        """设置 Azure OpenAI 客户端"""
        try:
            # 创建配置
            self.config = AzureConfigManager.create_config()
            
            # 验证配置
            AzureConfigManager.validate_config(self.config)
            
            # 创建客户端
            self.client = AzureOpenAI(
                api_key=self.config.api_key,
                api_version=self.config.api_version,
                azure_endpoint=self.config.endpoint,
                timeout=self.config.timeout
            )
            
            logger.info("Azure OpenAI client setup completed")
            
        except Exception as e:
            logger.error(f"Failed to setup Azure OpenAI client: {e}")
            raise
    
    def edit_image_from_path(self, image_path: str, prompt: str, 
                           size: str = "1024x1024", quality: str = "high") -> Optional[torch.Tensor]:
        """
        从文件路径编辑图像
        
        Args:
            image_path: 图像文件路径
            prompt: 编辑提示
            size: 图像尺寸
            quality: 图像质量
            
        Returns:
            编辑后的图像张量
        """
        try:
            # 检查文件是否存在
            if not os.path.exists(image_path):
                logger.error(f"Image file not found: {image_path}")
                return None
            
            # 加载图像
            pil_image = Image.open(image_path)
            logger.info(f"Loaded image: {pil_image.size}, mode: {pil_image.mode}")
            
            # 转换为张量
            image_tensor = ImageProcessor.pil_to_tensor(pil_image)
            
            # 准备 API 调用数据
            images = ImageProcessor.prepare_images_for_api(image_tensor.squeeze(0))
            
            logger.info(f"Editing image with prompt: {prompt}")
            
            # 调用 API
            result = self.client.images.edit(
                model=self.config.deployment,
                image=images,
                prompt=prompt,
                size=size,
                quality=quality
            )
            
            # 处理响应
            edited_tensor = ImageProcessor.base64_to_tensor(result.data[0].b64_json)
            logger.info("Image editing completed successfully")
            
            return edited_tensor
            
        except Exception as e:
            logger.error(f"Error editing image: {e}")
            return None
    
    def save_tensor_as_image(self, tensor: torch.Tensor, output_path: str) -> bool:
        """
        将张量保存为图像文件
        
        Args:
            tensor: 图像张量
            output_path: 输出文件路径
            
        Returns:
            是否保存成功
        """
        try:
            # 转换为 PIL 图像
            pil_image = ImageProcessor.tensor_to_pil(tensor.squeeze(0))
            
            # 保存图像
            pil_image.save(output_path)
            logger.info(f"Image saved to: {output_path}")
            
            return True
            
        except Exception as e:
            logger.error(f"Error saving image: {e}")
            return False
    
    def run_example(self):
        """运行示例"""
        try:
            logger.info("Starting Azure OpenAI image editing example")
            
            # 示例配置
            examples = [
                {
                    "input_image": "images/generated_image_20250426_231216.png",
                    "prompt": "make it in the style of Studio Ghibli",
                    "output": "images/edited_ghibli_style.png"
                },
                {
                    "input_image": "images/generated_image_20250426_231216.png", 
                    "prompt": "convert to a cyberpunk style with neon lights",
                    "output": "images/edited_cyberpunk_style.png"
                },
                {
                    "input_image": "images/generated_image_20250426_231216.png",
                    "prompt": "make it look like a watercolor painting",
                    "output": "images/edited_watercolor_style.png"
                }
            ]
            
            # 确保输出目录存在
            os.makedirs("images", exist_ok=True)
            
            for i, example in enumerate(examples, 1):
                logger.info(f"Processing example {i}/{len(examples)}")
                
                # 编辑图像
                edited_tensor = self.edit_image_from_path(
                    example["input_image"], 
                    example["prompt"]
                )
                
                if edited_tensor is not None:
                    # 保存结果
                    success = self.save_tensor_as_image(edited_tensor, example["output"])
                    if success:
                        logger.info(f"Example {i} completed successfully")
                    else:
                        logger.error(f"Example {i} failed to save")
                else:
                    logger.error(f"Example {i} failed to edit image")
                
                print("-" * 50)
            
            logger.info("All examples completed")
            
        except Exception as e:
            logger.error(f"Error running example: {e}")
            raise

def main():
    """主函数"""
    try:
        # 检查环境变量
        required_env_vars = ["AZURE_OPENAI_ENDPOINT", "AZURE_OPENAI_API_KEY"]
        missing_vars = [var for var in required_env_vars if not os.getenv(var)]
        
        if missing_vars:
            print(f"❌ Missing required environment variables: {', '.join(missing_vars)}")
            print("Please set these environment variables and try again.")
            sys.exit(1)
        
        # 运行示例
        example = AzureImageEditExample()
        example.run_example()
        
        print("✅ Azure OpenAI image editing example completed successfully!")
        
    except Exception as e:
        logger.error(f"Example failed: {e}")
        print(f"❌ Example failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
