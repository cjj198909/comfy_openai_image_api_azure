"""
Azure OpenAI Configuration Helper

This module provides helper functions for Azure OpenAI configuration and validation.
"""

import os
from typing import Optional, Dict, Any

class AzureOpenAIConfig:
    """Configuration helper for Azure OpenAI"""
    
    def __init__(self):
        self.endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
        self.api_key = os.getenv("AZURE_OPENAI_API_KEY")
        self.api_version = os.getenv("AZURE_OPENAI_API_VERSION", "2024-12-01-preview")
        self.deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-image-1")
    
    def validate(self) -> bool:
        """Validate that all required Azure OpenAI configuration is present"""
        return bool(self.endpoint and self.api_key)
    
    def get_client_kwargs(self) -> Dict[str, Any]:
        """Get keyword arguments for AzureOpenAI client initialization"""
        return {
            "api_key": self.api_key,
            "api_version": self.api_version,
            "azure_endpoint": self.endpoint
        }
    
    def get_missing_config(self) -> list:
        """Get list of missing configuration items"""
        missing = []
        if not self.endpoint:
            missing.append("AZURE_OPENAI_ENDPOINT")
        if not self.api_key:
            missing.append("AZURE_OPENAI_API_KEY")
        return missing

class OpenAIConfig:
    """Configuration helper for OpenAI"""
    
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
    
    def validate(self) -> bool:
        """Validate that all required OpenAI configuration is present"""
        return bool(self.api_key)
    
    def get_client_kwargs(self) -> Dict[str, Any]:
        """Get keyword arguments for OpenAI client initialization"""
        return {
            "api_key": self.api_key
        }
    
    def get_missing_config(self) -> list:
        """Get list of missing configuration items"""
        missing = []
        if not self.api_key:
            missing.append("OPENAI_API_KEY")
        return missing
