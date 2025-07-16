from openai import AzureOpenAI
import os
import requests
from PIL import Image
import json
from dotenv import load_dotenv
from datetime import datetime
import base64

load_dotenv()

client = AzureOpenAI(
    api_version="2025-04-01-preview",  
    api_key=os.environ["AZURE_OPENAI_API_KEY_IMAGE"],  
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT_IMAGE"],
)

# result = client.images.generate(
#     model="gpt-image-1", # the name of your DALL-E 3 deployment
#     prompt="a close-up of a bear walking throughthe forest",
#     n=1,
#     size="1024x1024",  # Specify the size of the image
#     quality="high",  # Specify the quality of the image
# )
result = client.images.edit(
    model="gpt-image-1",
    image=[
        open("./images/generated_image_20250426_231216.png", "rb"),
    ],
    prompt="make it in the style of Studio Ghibli."
)

json_response = json.loads(result.model_dump_json())

# Set the directory for the stored image
image_dir = os.path.join(os.curdir, 'images')

# If the directory doesn't exist, create it
if not os.path.isdir(image_dir):
    os.mkdir(image_dir)

# Initialize the image path (note the filetype should be png)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
image_path = os.path.join(image_dir, f'generated_image_{timestamp}.png')

# 从响应中获取base64编码的图像数据

image_b64 = json_response["data"][0]["b64_json"]  # 提取base64数据
generated_image = base64.b64decode(image_b64)  # 解码base64数据
with open(image_path, "wb") as image_file:
    image_file.write(generated_image)

# Display the image in the default image viewer
image = Image.open(image_path)
image.show()