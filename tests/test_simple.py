#!/usr/bin/env python

"""Simple tests for `openai_image_api` package without torch dependency."""

import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

def test_input_types():
    """Test that INPUT_TYPES method works correctly."""
    from openai_image_api.nodes import OpenAIImageAPI
    
    input_types = OpenAIImageAPI.INPUT_TYPES()
    
    # Check required inputs
    assert "prompt" in input_types["required"]
    assert "model" in input_types["required"]
    assert "size" in input_types["required"]
    assert "quality" in input_types["required"]
    assert "provider" in input_types["required"]
    
    # Check optional inputs
    assert "image" in input_types["optional"]
    assert "api_key" in input_types["optional"]
    assert "azure_endpoint" in input_types["optional"]
    assert "azure_api_version" in input_types["optional"]
    assert "azure_deployment" in input_types["optional"]
    
    # Check provider options
    assert input_types["required"]["provider"][0] == ["openai", "azure"]
    
    # Check model options
    assert input_types["required"]["model"][0] == ["gpt-image-1"]

def test_node_metadata():
    """Test node metadata."""
    from openai_image_api.nodes import OpenAIImageAPI
    
    assert OpenAIImageAPI.RETURN_TYPES == ("IMAGE",)
    assert OpenAIImageAPI.FUNCTION == "generate_image"
    assert OpenAIImageAPI.CATEGORY == "image/OpenAI"

def test_node_mappings():
    """Test node class mappings."""
    from openai_image_api.nodes import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS
    
    assert "OpenAI Image API" in NODE_CLASS_MAPPINGS
    assert "OpenAI Image API" in NODE_DISPLAY_NAME_MAPPINGS
    assert NODE_DISPLAY_NAME_MAPPINGS["OpenAI Image API"] == "OpenAI/Azure OpenAI Image API with gpt-image-1"

def test_config_helper():
    """Test configuration helper classes."""
    from openai_image_api.config import AzureOpenAIConfig, OpenAIConfig
    
    # Test Azure config
    azure_config = AzureOpenAIConfig()
    assert hasattr(azure_config, 'endpoint')
    assert hasattr(azure_config, 'api_key')
    assert hasattr(azure_config, 'api_version')
    assert hasattr(azure_config, 'deployment')
    
    # Test OpenAI config  
    openai_config = OpenAIConfig()
    assert hasattr(openai_config, 'api_key')
    
    # Test validation methods
    assert callable(azure_config.validate)
    assert callable(openai_config.validate)

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
