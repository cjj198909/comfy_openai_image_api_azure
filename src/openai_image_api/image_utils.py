"""
图像处理工具模块

该模块提供了图像处理相关的工具函数，包括：
- 图像格式转换
- 张量和 PIL 图像之间的转换
- 图像数据验证
- 错误处理和日志记录

遵循 Azure 最佳实践：
- 高效的图像处理
- 适当的错误处理
- 详细的日志记录
- 类型提示支持
"""

import io
import base64
import logging
from typing import List, Tuple, Optional, Union
import numpy as np
import torch
from PIL import Image

# 配置日志
logger = logging.getLogger(__name__)

class ImageProcessor:
    """图像处理工具类"""
    
    # 支持的图像格式
    SUPPORTED_FORMATS = ['PNG', 'JPEG', 'JPG', 'WEBP']
    
    # 默认配置
    DEFAULT_CONFIG = {
        "image_format": "PNG",
        "image_quality": 95,
        "max_image_size": (2048, 2048),
        "min_image_size": (64, 64)
    }
    
    @classmethod
    def tensor_to_pil(cls, tensor: torch.Tensor) -> Image.Image:
        """
        将 PyTorch 张量转换为 PIL 图像
        
        Args:
            tensor: 输入张量 (H, W, C) 或 (C, H, W)
            
        Returns:
            PIL 图像对象
            
        Raises:
            ValueError: 当张量格式不支持时
        """
        try:
            # 确保张量在 CPU 上
            if tensor.is_cuda:
                tensor = tensor.cpu()
            
            # 转换为 numpy 数组
            img_np = tensor.detach().numpy()
            
            # 处理不同的张量格式
            if len(img_np.shape) == 3:
                # 检查是否为 (C, H, W) 格式
                if img_np.shape[0] <= 4:  # 通道数应该小于等于 4
                    img_np = np.transpose(img_np, (1, 2, 0))
            elif len(img_np.shape) == 2:
                # 灰度图像
                pass
            else:
                raise ValueError(f"Unsupported tensor shape: {img_np.shape}")
            
            # 确保值在 [0, 1] 范围内
            if img_np.max() <= 1.0:
                img_np = (img_np * 255).astype(np.uint8)
            else:
                img_np = img_np.astype(np.uint8)
            
            # 处理通道数
            if len(img_np.shape) == 3:
                if img_np.shape[2] == 1:
                    # 单通道转换为灰度
                    img_np = img_np.squeeze(axis=2)
                elif img_np.shape[2] == 4:
                    # RGBA 图像
                    pass
                elif img_np.shape[2] == 3:
                    # RGB 图像
                    pass
                else:
                    raise ValueError(f"Unsupported number of channels: {img_np.shape[2]}")
            
            pil_image = Image.fromarray(img_np)
            logger.debug(f"Converted tensor to PIL image: {pil_image.size}, mode: {pil_image.mode}")
            return pil_image
            
        except Exception as e:
            logger.error(f"Error converting tensor to PIL image: {e}")
            raise ValueError(f"Error converting tensor to PIL image: {e}")
    
    @classmethod
    def pil_to_tensor(cls, pil_image: Image.Image) -> torch.Tensor:
        """
        将 PIL 图像转换为 PyTorch 张量
        
        Args:
            pil_image: PIL 图像对象
            
        Returns:
            PyTorch 张量 (1, H, W, C)
            
        Raises:
            ValueError: 当图像格式不支持时
        """
        try:
            # 确保图像是 RGB 模式
            if pil_image.mode != 'RGB':
                pil_image = pil_image.convert('RGB')
            
            # 转换为 numpy 数组
            img_np = np.array(pil_image).astype(np.float32) / 255.0
            
            # 添加批次维度
            img_np = np.expand_dims(img_np, axis=0)
            
            # 转换为 torch 张量
            tensor = torch.from_numpy(img_np)
            
            logger.debug(f"Converted PIL image to tensor: {tensor.shape}")
            return tensor
            
        except Exception as e:
            logger.error(f"Error converting PIL image to tensor: {e}")
            raise ValueError(f"Error converting PIL image to tensor: {e}")
    
    @classmethod
    def tensor_to_bytes(cls, tensor: torch.Tensor, format: str = "PNG") -> bytes:
        """
        将张量转换为字节数据
        
        Args:
            tensor: 输入张量
            format: 图像格式
            
        Returns:
            图像字节数据
        """
        try:
            pil_image = cls.tensor_to_pil(tensor)
            
            img_byte_arr = io.BytesIO()
            pil_image.save(img_byte_arr, format=format, quality=cls.DEFAULT_CONFIG["image_quality"])
            img_byte_arr_value = img_byte_arr.getvalue()
            
            logger.debug(f"Converted tensor to bytes: {len(img_byte_arr_value)} bytes")
            return img_byte_arr_value
            
        except Exception as e:
            logger.error(f"Error converting tensor to bytes: {e}")
            raise ValueError(f"Error converting tensor to bytes: {e}")
    
    @classmethod
    def bytes_to_tensor(cls, image_bytes: bytes) -> torch.Tensor:
        """
        将字节数据转换为张量
        
        Args:
            image_bytes: 图像字节数据
            
        Returns:
            PyTorch 张量
        """
        try:
            pil_image = Image.open(io.BytesIO(image_bytes))
            tensor = cls.pil_to_tensor(pil_image)
            
            logger.debug(f"Converted bytes to tensor: {tensor.shape}")
            return tensor
            
        except Exception as e:
            logger.error(f"Error converting bytes to tensor: {e}")
            raise ValueError(f"Error converting bytes to tensor: {e}")
    
    @classmethod
    def base64_to_tensor(cls, base64_str: str) -> torch.Tensor:
        """
        将 base64 字符串转换为张量
        
        Args:
            base64_str: base64 编码的图像字符串
            
        Returns:
            PyTorch 张量
        """
        try:
            image_bytes = base64.b64decode(base64_str)
            tensor = cls.bytes_to_tensor(image_bytes)
            
            logger.debug(f"Converted base64 to tensor: {tensor.shape}")
            return tensor
            
        except Exception as e:
            logger.error(f"Error converting base64 to tensor: {e}")
            raise ValueError(f"Error converting base64 to tensor: {e}")
    
    @classmethod
    def prepare_images_for_api(cls, image: torch.Tensor) -> List[Tuple[str, bytes]]:
        """
        为 API 调用准备图像数据
        
        Args:
            image: 输入图像张量
            
        Returns:
            图像名称和字节数据的列表
        """
        try:
            images = []
            
            if len(image.shape) == 4:  # 批量图像
                batch_size = image.shape[0]
                logger.info(f"Processing batch of {batch_size} images")
                
                for i in range(batch_size):
                    img_tensor = image[i]
                    img_bytes = cls.tensor_to_bytes(img_tensor)
                    images.append((f"image_{i}.png", img_bytes))
                    
            elif len(image.shape) == 3:  # 单张图像
                logger.info("Processing single image")
                img_bytes = cls.tensor_to_bytes(image)
                images.append(("image_0.png", img_bytes))
                
            else:
                raise ValueError(f"Unsupported image tensor shape: {image.shape}")
            
            logger.info(f"Successfully prepared {len(images)} images for API")
            return images
            
        except Exception as e:
            logger.error(f"Error preparing images for API: {e}")
            raise ValueError(f"Error preparing images for API: {e}")
    
    @classmethod
    def validate_image_size(cls, image: Image.Image) -> None:
        """
        验证图像尺寸
        
        Args:
            image: PIL 图像对象
            
        Raises:
            ValueError: 当图像尺寸不符合要求时
        """
        width, height = image.size
        max_width, max_height = cls.DEFAULT_CONFIG["max_image_size"]
        min_width, min_height = cls.DEFAULT_CONFIG["min_image_size"]
        
        if width > max_width or height > max_height:
            raise ValueError(f"Image size {width}x{height} exceeds maximum size {max_width}x{max_height}")
        
        if width < min_width or height < min_height:
            raise ValueError(f"Image size {width}x{height} is smaller than minimum size {min_width}x{min_height}")
        
        logger.debug(f"Image size validation passed: {width}x{height}")
    
    @classmethod
    def resize_image_if_needed(cls, image: Image.Image, target_size: Optional[Tuple[int, int]] = None) -> Image.Image:
        """
        如果需要，调整图像大小
        
        Args:
            image: PIL 图像对象
            target_size: 目标尺寸 (width, height)
            
        Returns:
            调整大小后的图像
        """
        try:
            if target_size is None:
                return image
            
            current_size = image.size
            if current_size == target_size:
                return image
            
            # 使用高质量重采样
            resized_image = image.resize(target_size, Image.Resampling.LANCZOS)
            
            logger.info(f"Resized image from {current_size} to {target_size}")
            return resized_image
            
        except Exception as e:
            logger.error(f"Error resizing image: {e}")
            raise ValueError(f"Error resizing image: {e}")
