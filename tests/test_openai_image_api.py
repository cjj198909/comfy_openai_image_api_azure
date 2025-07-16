#!/usr/bin/env python

"""Tests for `openai_image_api` package."""

import pytest
from src.openai_image_api.nodes import OpenAIImageAPI

@pytest.fixture
def openai_image_api_node():
    """Fixture to create an OpenAIImageAPI node instance."""
    return OpenAIImageAPI()

def test_openai_image_api_node_initialization(openai_image_api_node):
    """Test that the node can be instantiated."""
    assert isinstance(openai_image_api_node, OpenAIImageAPI)

def test_return_types():
    """Test the node's metadata."""
    assert OpenAIImageAPI.RETURN_TYPES == ("IMAGE",)
    assert OpenAIImageAPI.FUNCTION == "generate_image"
    assert OpenAIImageAPI.CATEGORY == "image/OpenAI"

def test_input_types():
    """Test the node's input types."""
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
