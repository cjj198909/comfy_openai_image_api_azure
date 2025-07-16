# GitHub 上传指南

## 第一步：在 GitHub 上创建新仓库

1. 访问 https://github.com/new
2. 仓库名称：`comfy_openai_image_api_azure`
3. 描述：`ComfyUI OpenAI Image API with Azure OpenAI support - Enhanced version with gpt-image-1`
4. 设置为 Public
5. 不要勾选 "Initialize this repository with a README"
6. 点击 "Create repository"

## 第二步：推送到新仓库

在您创建了新仓库后，运行以下命令：

```bash
# 添加新的远程仓库
git remote add new-origin https://github.com/cjj198909/comfy_openai_image_api_azure.git

# 推送到新仓库
git push -u new-origin main

# 如果您想要删除原来的远程仓库引用
git remote remove origin
git remote rename new-origin origin
```

## 第三步：更新项目链接

在 pyproject.toml 中更新以下内容：

```toml
[project.urls]
bugs = "https://github.com/cjj198909/comfy_openai_image_api_azure/issues"
homepage = "https://github.com/cjj198909/comfy_openai_image_api_azure"
Repository = "https://github.com/cjj198909/comfy_openai_image_api_azure.git"
```

## 项目特色

✅ **Azure OpenAI 支持** - 完整的 Azure OpenAI 集成
✅ **双提供商支持** - 同时支持 OpenAI 和 Azure OpenAI
✅ **灵活配置** - 环境变量和节点参数双重配置
✅ **安全增强** - 遵循 Azure 安全最佳实践
✅ **完整文档** - 详细的使用指南和示例
✅ **错误处理** - 全面的错误处理和重试逻辑

## 原始项目致谢

本项目基于 [unicough/comfy_openai_image_api](https://github.com/unicough/comfy_openai_image_api) 开发，在原有功能基础上增加了 Azure OpenAI 支持和多项增强功能。
