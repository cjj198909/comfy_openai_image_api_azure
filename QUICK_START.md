# Azure OpenAI 图像编辑快速开始指南

## 🚀 概述

您的 ComfyUI OpenAI Image API 项目现已成功整合了增强的 Azure OpenAI 图像编辑功能！

## ✨ 新功能特性

### 🔧 技术改进
- **最新 SDK 支持**: 使用 Azure OpenAI SDK 2025-04-01-preview
- **模块化设计**: 分离的配置管理和图像处理模块
- **企业级错误处理**: 完整的异常处理和重试机制
- **详细日志记录**: 调试和监控支持
- **类型安全**: 全面的类型提示支持

### 🛠️ 使用增强
- **智能配置管理**: 自动环境变量检测和验证
- **图像处理优化**: 高效的张量和 PIL 图像转换
- **批量处理支持**: 同时处理多张图像
- **安全凭证管理**: 环境变量优先，隐藏敏感信息

## 🔧 设置步骤

### 1. 环境配置

创建 `.env` 文件（基于 `config.env.example`）:

```bash
# 复制配置模板
cp config.env.example .env

# 编辑配置文件
nano .env
```

填入您的 Azure OpenAI 配置:

```env
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_API_KEY=your-api-key
AZURE_OPENAI_API_VERSION=2025-04-01-preview
AZURE_OPENAI_DEPLOYMENT=gpt-image-1
```

### 2. 安装依赖

```bash
pip install -e .
```

### 3. 测试配置

```bash
python test_integration.py
```

## 🎯 使用方法

### 方法一：在 ComfyUI 中使用

1. 重启 ComfyUI
2. 在节点菜单中找到 "OpenAI/Azure OpenAI Image API with gpt-image-1"
3. 配置节点参数：
   - **Provider**: 选择 "azure"
   - **Prompt**: 输入编辑提示词
   - **Image**: 连接输入图像（可选）
   - **其他参数**: 根据需要调整

### 方法二：运行独立示例

```bash
# 确保设置了环境变量
export AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
export AZURE_OPENAI_API_KEY=your-api-key

# 运行示例脚本
python examples/azure_image_edit_example.py
```

### 方法三：程序化使用

```python
from src.openai_image_api.nodes import OpenAIImageAPI
from src.openai_image_api.azure_config import AzureConfigManager
from src.openai_image_api.image_utils import ImageProcessor

# 创建节点实例
node = OpenAIImageAPI()

# 使用环境变量配置
result = node.generate_image(
    prompt="make it in the style of Studio Ghibli",
    model="gpt-image-1",
    size="1024x1024",
    quality="high",
    provider="azure",
    image=your_image_tensor  # 可选
)

edited_image = result[0]
```

## 📚 API 参考

### 主要类

- **OpenAIImageAPI**: 主要的 ComfyUI 节点类
- **AzureConfigManager**: Azure 配置管理器
- **ImageProcessor**: 图像处理工具类

### 支持的参数

- **prompt**: 图像编辑提示词
- **model**: 模型名称 (gpt-image-1)
- **size**: 图像尺寸 (1024x1024, 1536x1024, 1024x1536)
- **quality**: 图像质量 (low, medium, high)
- **provider**: 服务提供商 (openai, azure)

## 🔍 故障排除

### 常见问题

1. **环境变量未设置**
   ```bash
   # 检查环境变量
   echo $AZURE_OPENAI_ENDPOINT
   echo $AZURE_OPENAI_API_KEY
   ```

2. **API 密钥无效**
   - 检查 Azure 门户中的 API 密钥
   - 确保资源状态正常

3. **端点格式错误**
   - 确保端点格式为: `https://your-resource.openai.azure.com`

4. **部署名称错误**
   - 在 Azure 门户中检查实际部署名称

### 日志调试

启用详细日志:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

查看日志文件:

```bash
tail -f azure_image_edit.log
```

## 🚀 下一步

1. **尝试不同的编辑提示词**
2. **测试批量图像处理**
3. **集成到您的 ComfyUI 工作流**
4. **探索高级配置选项**

## 📞 支持

如有问题，请查看：
- 项目 README.md
- 示例代码
- 日志文件
- Azure OpenAI 文档

---

**🎉 恭喜！您的 Azure OpenAI 图像编辑功能已成功整合！**
