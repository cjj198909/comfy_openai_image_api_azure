from inspect import cleandoc
import base64
import numpy as np
import torch
from PIL import Image
import io
import os
from openai import OpenAI, AzureOpenAI

# Try to load environment variables from .env file
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    # dotenv is optional, continue without it
    pass

# ANSI escape codes for colors
RED = "\033[91m"
RESET = "\033[0m"

class OpenAIImageAPI:
    """
    A node for generating images using OpenAI's Image API
    
    This node allows users to generate or edit images using OpenAI's DALL-E 3 or GPT-Image-1 models.
    It supports various output sizes, quality settings, and can work with both single and multiple input images.
    """
    def __init__(self):
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
                "size": (["1024x1024", "1536x1024", "1024x1536"],),
                "quality": (["low", "medium", "high"],),
                "provider": (["openai", "azure"],),
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
                    "default": "2024-12-01-preview"
                }),
                "azure_deployment": ("STRING", {
                    "multiline": False,
                    "default": "gpt-image-1"
                }),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "generate_image"
    CATEGORY = "image/OpenAI"

    def generate_image(self, prompt, model, size, quality, provider, image=None, 
                      api_key=None, azure_endpoint=None, azure_api_version=None, azure_deployment=None):
        # print(f"{RED}generate_image: {prompt}, {model}, {size}, {quality}, {provider}{RESET}")

        # Initialize client based on provider
        if provider == "azure":
            # For Azure OpenAI, use environment variables or provided parameters
            endpoint = azure_endpoint or os.getenv("AZURE_OPENAI_ENDPOINT")
            key = api_key or os.getenv("AZURE_OPENAI_API_KEY")
            api_version = azure_api_version or os.getenv("AZURE_OPENAI_API_VERSION", "2024-12-01-preview")
            deployment = azure_deployment or os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-image-1")
            
            if not endpoint:
                raise RuntimeError("Azure OpenAI endpoint is required. Set AZURE_OPENAI_ENDPOINT environment variable or provide azure_endpoint parameter.")
            if not key:
                raise RuntimeError("Azure OpenAI API key is required. Set AZURE_OPENAI_API_KEY environment variable or provide api_key parameter.")
            
            client = AzureOpenAI(
                api_key=key,
                api_version=api_version,
                azure_endpoint=endpoint
            )
            model_name = deployment  # Use deployment name for Azure
        else:
            # For OpenAI, use api_key or environment variable
            key = api_key or os.getenv("OPENAI_API_KEY")
            if not key:
                raise RuntimeError("OpenAI API key is required. Set OPENAI_API_KEY environment variable or provide api_key parameter.")
            
            client = OpenAI(api_key=key)
            model_name = model  # Use model name for OpenAI
        
        try:
            if image is None or (isinstance(image, torch.Tensor) and image.numel() == 0):
                # If no input image, use generate API
                result = client.images.generate(
                    model=model_name,
                    prompt=prompt,
                    size=size,
                    quality=quality
                )
            else:
                # Convert ComfyUI image tensor(s) to PIL Images
                images = []
                if len(image.shape) == 4:  # Batch of images
                    for i, img in enumerate(image):
                        # Convert PyTorch tensor to NumPy array
                        img_np = img.detach().cpu().numpy()
                        img_np = (img_np * 255).astype(np.uint8)
                        pil_image = Image.fromarray(img_np)
                        # Convert PIL Image to bytes with filename
                        img_byte_arr = io.BytesIO()
                        pil_image.save(img_byte_arr, format='PNG')
                        img_byte_arr_value = img_byte_arr.getvalue()
                        images.append((f"image_{i}.png", img_byte_arr_value))
                else:
                    # Single image
                    # Convert PyTorch tensor to NumPy array
                    img_np = image.detach().cpu().numpy()
                    img_np = (img_np * 255).astype(np.uint8)
                    pil_image = Image.fromarray(img_np)
                    # Convert PIL Image to bytes with filename
                    img_byte_arr = io.BytesIO()
                    pil_image.save(img_byte_arr, format='PNG')
                    img_byte_arr_value = img_byte_arr.getvalue()
                    images.append(("image_0.png", img_byte_arr_value))
                
                # Call edit API
                result = client.images.edit(
                    model=model_name,
                    image=images,
                    prompt=prompt,
                    size=size,
                    quality=quality
                )
            
            # Get the generated image
            image_base64 = result.data[0].b64_json
            image_bytes = base64.b64decode(image_base64)
            
            # Convert to PIL Image
            generated_image = Image.open(io.BytesIO(image_bytes))
            
            # Convert to numpy array
            image_np = np.array(generated_image).astype(np.float32) / 255.0
            image_np = np.expand_dims(image_np, axis=0)  # Add batch dimension
            
            # Convert to torch tensor
            image_tensor = torch.from_numpy(image_np)
            
            return (image_tensor,)
            
        except Exception as e:
            error_message = f"{str(e)}"
            print(f"{RED}Error calling Image API: {error_message}{RESET}")
            # Raise an exception to signal the error to the ComfyUI frontend
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
