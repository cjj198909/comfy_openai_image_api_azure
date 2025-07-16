"""
Azure OpenAI 配置管理模块

该模块提供了 Azure OpenAI 服务的配置管理功能，包括：
- 环境变量管理
- 配置验证
- 安全的凭证处理
- 错误处理和日志记录

遵循 Azure 最佳实践：
- 使用环境变量存储敏感信息
- 实施适当的错误处理
- 提供详细的日志记录
- 支持配置验证
"""

import os
import logging
from typing import Optional, Dict, Any
from dataclasses import dataclass

# 配置日志
logger = logging.getLogger(__name__)

@dataclass
class AzureOpenAIConfig:
    """Azure OpenAI 配置数据类"""
    endpoint: str
    api_key: str
    api_version: str
    deployment: str
    timeout: int = 60
    max_retries: int = 3

class AzureConfigManager:
    """Azure OpenAI 配置管理器"""
    
    # 默认配置
    DEFAULT_CONFIG = {
        "api_version": "2025-04-01-preview",
        "deployment": "gpt-image-1",
        "timeout": 60,
        "max_retries": 3
    }
    
    # 环境变量映射
    ENV_MAPPINGS = {
        "endpoint": [
            "AZURE_OPENAI_ENDPOINT",
            "AZURE_OPENAI_ENDPOINT_IMAGE",
            "AZURE_ENDPOINT"
        ],
        "api_key": [
            "AZURE_OPENAI_API_KEY",
            "AZURE_OPENAI_API_KEY_IMAGE",
            "AZURE_API_KEY"
        ],
        "api_version": [
            "AZURE_OPENAI_API_VERSION",
            "AZURE_API_VERSION"
        ],
        "deployment": [
            "AZURE_OPENAI_DEPLOYMENT",
            "AZURE_DEPLOYMENT"
        ]
    }
    
    @classmethod
    def get_env_value(cls, key: str) -> Optional[str]:
        """
        从环境变量获取值，支持多个候选变量名
        
        Args:
            key: 配置键名
            
        Returns:
            环境变量值，如果未找到则返回 None
        """
        env_keys = cls.ENV_MAPPINGS.get(key, [])
        for env_key in env_keys:
            value = os.getenv(env_key)
            if value and value.strip():
                logger.debug(f"Found {key} from environment variable: {env_key}")
                return value.strip()
        return None
    
    @classmethod
    def create_config(cls, 
                     endpoint: Optional[str] = None,
                     api_key: Optional[str] = None,
                     api_version: Optional[str] = None,
                     deployment: Optional[str] = None,
                     timeout: Optional[int] = None,
                     max_retries: Optional[int] = None) -> AzureOpenAIConfig:
        """
        创建 Azure OpenAI 配置
        
        Args:
            endpoint: Azure OpenAI 端点
            api_key: API 密钥
            api_version: API 版本
            deployment: 部署名称
            timeout: 请求超时时间
            max_retries: 最大重试次数
            
        Returns:
            配置好的 AzureOpenAIConfig 对象
            
        Raises:
            ValueError: 当必需的配置缺失时
        """
        # 从环境变量或参数获取配置
        config_endpoint = endpoint or cls.get_env_value("endpoint")
        config_api_key = api_key or cls.get_env_value("api_key")
        config_api_version = api_version or cls.get_env_value("api_version") or cls.DEFAULT_CONFIG["api_version"]
        config_deployment = deployment or cls.get_env_value("deployment") or cls.DEFAULT_CONFIG["deployment"]
        config_timeout = timeout or cls.DEFAULT_CONFIG["timeout"]
        config_max_retries = max_retries or cls.DEFAULT_CONFIG["max_retries"]
        
        # 验证必需的配置
        if not config_endpoint:
            raise ValueError(
                "Azure OpenAI endpoint is required. Please set one of the following environment variables: "
                f"{', '.join(cls.ENV_MAPPINGS['endpoint'])} or provide endpoint parameter."
            )
        
        if not config_api_key:
            raise ValueError(
                "Azure OpenAI API key is required. Please set one of the following environment variables: "
                f"{', '.join(cls.ENV_MAPPINGS['api_key'])} or provide api_key parameter."
            )
        
        # 确保端点有正确的协议
        if not config_endpoint.startswith(('http://', 'https://')):
            config_endpoint = 'https://' + config_endpoint
        
        # 验证端点格式
        if not config_endpoint.endswith('.openai.azure.com') and not config_endpoint.endswith('.openai.azure.com/'):
            logger.warning(f"Endpoint {config_endpoint} may not be a valid Azure OpenAI endpoint")
        
        config = AzureOpenAIConfig(
            endpoint=config_endpoint,
            api_key=config_api_key,
            api_version=config_api_version,
            deployment=config_deployment,
            timeout=config_timeout,
            max_retries=config_max_retries
        )
        
        logger.info(f"Created Azure OpenAI config - Endpoint: {config.endpoint}, API Version: {config.api_version}, Deployment: {config.deployment}")
        return config
    
    @classmethod
    def validate_config(cls, config: AzureOpenAIConfig) -> None:
        """
        验证 Azure OpenAI 配置
        
        Args:
            config: 要验证的配置对象
            
        Raises:
            ValueError: 当配置无效时
        """
        if not config.endpoint:
            raise ValueError("Azure OpenAI endpoint cannot be empty")
        
        if not config.api_key:
            raise ValueError("Azure OpenAI API key cannot be empty")
        
        if not config.api_version:
            raise ValueError("Azure OpenAI API version cannot be empty")
        
        if not config.deployment:
            raise ValueError("Azure OpenAI deployment cannot be empty")
        
        if config.timeout <= 0:
            raise ValueError("Timeout must be greater than 0")
        
        if config.max_retries < 0:
            raise ValueError("Max retries must be non-negative")
        
        logger.debug("Azure OpenAI configuration validation passed")
    
    @classmethod
    def get_config_summary(cls, config: AzureOpenAIConfig) -> Dict[str, Any]:
        """
        获取配置摘要（隐藏敏感信息）
        
        Args:
            config: 配置对象
            
        Returns:
            配置摘要字典
        """
        return {
            "endpoint": config.endpoint,
            "api_key": f"***{config.api_key[-4:]}" if len(config.api_key) > 4 else "***",
            "api_version": config.api_version,
            "deployment": config.deployment,
            "timeout": config.timeout,
            "max_retries": config.max_retries
        }
