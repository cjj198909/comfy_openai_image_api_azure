"""
Azure OpenAI Image Generation Examples

This file contains examples of how to use the ComfyUI OpenAI Image API node
with Azure OpenAI. The examples show different configurations and use cases.
"""

# Example 1: Basic Azure OpenAI setup using environment variables
azure_openai_env_example = {
    "prompt": "A beautiful sunset over mountains",
    "model": "gpt-image-1",
    "size": "1024x1024",
    "quality": "high",
    "provider": "azure",
    # These will be loaded from environment variables:
    # AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
    # AZURE_OPENAI_API_KEY=your-api-key
    # AZURE_OPENAI_DEPLOYMENT=gpt-image-1
}

# Example 2: Azure OpenAI with explicit parameters
azure_openai_explicit_example = {
    "prompt": "A futuristic city with flying cars",
    "model": "gpt-image-1",
    "size": "1536x1024",
    "quality": "medium",
    "provider": "azure",
    "azure_endpoint": "https://your-resource.openai.azure.com/",
    "api_key": "your-azure-api-key",
    "azure_deployment": "gpt-image-1",
    "azure_api_version": "2024-12-01-preview"
}

# Example 3: OpenAI with environment variables
openai_env_example = {
    "prompt": "A magical forest with glowing mushrooms",
    "model": "gpt-image-1",
    "size": "1024x1536",
    "quality": "high",
    "provider": "openai",
    # This will be loaded from environment variable:
    # OPENAI_API_KEY=your-openai-api-key
}

# Example 4: OpenAI with explicit API key
openai_explicit_example = {
    "prompt": "A space station orbiting Earth",
    "model": "gpt-image-1",
    "size": "1024x1024",
    "quality": "low",
    "provider": "openai",
    "api_key": "your-openai-api-key"
}

# Example 5: Image editing with Azure OpenAI
azure_image_editing_example = {
    "prompt": "Add a rainbow in the sky",
    "model": "gpt-image-1",
    "size": "1024x1024",
    "quality": "high",
    "provider": "azure",
    "image": "[Connect an input image here]",
    "azure_endpoint": "https://your-resource.openai.azure.com/",
    "api_key": "your-azure-api-key",
    "azure_deployment": "gpt-image-1"
}

# Environment variable template
env_template = """
# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key_here

# Azure OpenAI Configuration
AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/
AZURE_OPENAI_API_KEY=your_azure_openai_api_key_here
AZURE_OPENAI_API_VERSION=2024-12-01-preview
AZURE_OPENAI_DEPLOYMENT=gpt-image-1
"""

print("Azure OpenAI Image API Examples")
print("=" * 40)
print("This file contains examples for using the ComfyUI OpenAI Image API node.")
print("Copy the .env.example file to .env and fill in your credentials.")
print("Then use the examples above as reference for your node configurations.")
