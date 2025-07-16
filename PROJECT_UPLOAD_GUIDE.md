# 🚀 项目上传到 GitHub 的完整指南

## 📋 项目概述

这是一个基于 [unicough/comfy_openai_image_api](https://github.com/unicough/comfy_openai_image_api) 的增强版本，添加了 Azure OpenAI 支持和多项改进功能。

## 🎯 主要增强功能

### 1. Azure OpenAI 完整支持
- ✅ 支持 Azure OpenAI gpt-image-1 模型
- ✅ 可配置的 endpoint、key、deployment 参数
- ✅ 与原生 OpenAI API 完全兼容

### 2. 灵活的配置选项
- ✅ 环境变量配置支持
- ✅ 节点参数直接配置
- ✅ 优先级：节点参数 > 环境变量

### 3. 安全增强
- ✅ 环境变量管理敏感信息
- ✅ 完整的错误处理和重试逻辑
- ✅ 遵循 Azure 安全最佳实践

### 4. 开发者友好
- ✅ 详细的文档和示例
- ✅ 单元测试支持
- ✅ 配置助手类

## 🔧 上传步骤

### 第一步：在 GitHub 创建新仓库

1. 访问 https://github.com/new
2. 填写仓库信息：
   - **Repository name**: `comfy_openai_image_api_azure`
   - **Description**: `ComfyUI OpenAI Image API with Azure OpenAI support - Enhanced version with gpt-image-1`
   - **Visibility**: Public
   - **Initialize**: 不要勾选任何初始化选项
3. 点击 "Create repository"

### 第二步：推送代码到新仓库

在终端中运行以下命令：

```bash
# 确保在项目目录中
cd /Users/jiajunchen/Code/comfy_openai_image_api

# 添加新的远程仓库
git remote add new-origin https://github.com/cjj198909/comfy_openai_image_api_azure.git

# 推送到新仓库
git push -u new-origin main

# 可选：更新远程仓库引用
git remote remove origin
git remote rename new-origin origin
```

### 第三步：验证上传

访问您的新仓库：https://github.com/cjj198909/comfy_openai_image_api_azure

确认以下文件已正确上传：
- ✅ README.md (包含 Azure OpenAI 支持说明)
- ✅ src/openai_image_api/nodes.py (增强的节点代码)
- ✅ src/openai_image_api/config.py (配置助手)
- ✅ .env.example (环境变量模板)
- ✅ requirements.txt (依赖项)
- ✅ examples.py (使用示例)

## 📚 使用指南

### Azure OpenAI 配置

```python
# 在 ComfyUI 节点中配置
{
    "provider": "azure",
    "azure_endpoint": "https://your-resource.openai.azure.com/",
    "api_key": "your-azure-api-key",
    "azure_deployment": "gpt-image-1",
    "prompt": "A beautiful landscape",
    "size": "1024x1024",
    "quality": "high"
}
```

### 环境变量配置

```env
# 复制 .env.example 到 .env 并填写
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_KEY=your-azure-api-key
AZURE_OPENAI_DEPLOYMENT=gpt-image-1
```

## 🙏 致谢

本项目基于 [unicough/comfy_openai_image_api](https://github.com/unicough/comfy_openai_image_api) 开发，感谢原作者 Xin 的优秀工作！

## 📄 许可证

MIT License - 与原项目保持一致

## 🆘 支持

- 🐛 Bug 报告: https://github.com/cjj198909/comfy_openai_image_api_azure/issues
- 💡 功能建议: https://github.com/cjj198909/comfy_openai_image_api_azure/issues
- 📖 文档: README.md
