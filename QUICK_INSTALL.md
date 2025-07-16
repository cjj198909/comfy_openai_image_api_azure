# 🚀 ComfyUI 节点快速安装指南

## 最简单的安装方式

### 1. 进入 ComfyUI 的 custom_nodes 目录

```bash
cd /path/to/your/ComfyUI/custom_nodes
```

### 2. 克隆项目

```bash
git clone https://github.com/cjj198909/comfy_openai_image_api_azure.git
```

### 3. 安装依赖项

```bash
cd comfy_openai_image_api_azure
pip install -r requirements.txt
```

### 4. 重启 ComfyUI

重新启动 ComfyUI，节点就会自动加载！

## 🎯 使用方法

安装完成后，您可以在 ComfyUI 中找到：
- **节点名称**: "OpenAI Image API"
- **分类**: "image/OpenAI"

### OpenAI 配置示例
- `provider`: 选择 "openai"
- `api_key`: 输入您的 OpenAI API 密钥
- `prompt`: "A beautiful landscape"
- `model`: "gpt-image-1"
- `size`: "1024x1024"
- `quality`: "high"

### Azure OpenAI 配置示例
- `provider`: 选择 "azure"
- `azure_endpoint`: "https://your-resource.openai.azure.com/"
- `api_key`: 输入您的 Azure OpenAI API 密钥
- `azure_deployment`: "gpt-image-1"
- `prompt`: "A futuristic city"
- `model`: "gpt-image-1"
- `size`: "1024x1024"
- `quality`: "high"

## 🔧 故障排除

- **节点未显示**：确保已重启 ComfyUI
- **依赖项错误**：确保在正确的 Python 环境中安装依赖项
- **API 错误**：检查 API 密钥和端点配置

## 📖 更多信息

- 详细文档：[COMFYUI_INSTALLATION_GUIDE.md](COMFYUI_INSTALLATION_GUIDE.md)
- 项目地址：https://github.com/cjj198909/comfy_openai_image_api_azure
- 原始项目：https://github.com/unicough/comfy_openai_image_api

就这么简单！🎉
