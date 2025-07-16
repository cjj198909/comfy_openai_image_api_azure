# Release Notes - v0.1.0: Azure OpenAI Image Editing Enhancement

## 🚀 Major Release: Enterprise-Grade Azure OpenAI Integration

**发布日期**: 2025年7月16日  
**版本**: v0.1.0  
**兼容性**: ComfyUI, Azure OpenAI API 2025-04-01-preview

---

## 🎯 发布概述

这是一个重大更新，将项目从基础的 HTTP 请求实现升级为使用官方 Azure OpenAI SDK 的企业级解决方案。新版本提供了更强大的功能、更好的错误处理和更简单的使用体验。

## ✨ 新功能特性

### 🔧 核心技术升级
- **最新 Azure OpenAI SDK**: 使用官方 OpenAI Python SDK 1.0+
- **API 版本更新**: 支持 2025-04-01-preview 版本
- **模块化架构**: 分离配置管理、图像处理和错误处理
- **类型安全**: 完整的 TypeScript 风格类型提示
- **企业级日志**: 结构化日志记录和错误追踪

### 🛠️ 用户体验改进
- **智能配置**: 自动检测和验证环境变量
- **批量处理**: 支持同时处理多张图像
- **错误恢复**: 自动重试和智能错误处理
- **安全管理**: 凭证隐藏和安全存储
- **丰富文档**: 详细的使用指南和示例

### 🎨 图像处理增强
- **高效转换**: 优化的张量和 PIL 图像转换
- **格式支持**: 支持多种图像格式 (PNG, JPEG, WEBP)
- **尺寸验证**: 自动图像尺寸检查和调整
- **内存优化**: 更好的内存使用和垃圾回收

## 📁 新增文件

### 核心模块
- `src/openai_image_api/azure_config.py` - Azure 配置管理器
- `src/openai_image_api/image_utils.py` - 图像处理工具库

### 示例和测试
- `examples/azure_image_edit_example.py` - 完整使用示例
- `test_integration.py` - 集成测试套件

### 文档和配置
- `QUICK_START.md` - 快速开始指南
- `config.env.example` - 环境变量配置模板
- `TROUBLESHOOTING.md` - 故障排除指南
- `COMFYUI_INSTALLATION_GUIDE.md` - ComfyUI 安装指南

### 工具脚本
- `install_comfyui.sh` - ComfyUI 自动安装脚本
- `image_edit.py` - 独立图像编辑脚本

## 🔄 更新的文件

### 核心代码
- `src/openai_image_api/nodes.py` - 完全重构的主节点代码
- `pyproject.toml` - 更新依赖项和项目信息
- `README.md` - 全面更新的文档

### 配置
- `.gitignore` - 添加项目特定的忽略规则

## 💡 使用示例

### 基本用法
```python
from src.openai_image_api.nodes import OpenAIImageAPI

node = OpenAIImageAPI()
result = node.generate_image(
    prompt="make it in the style of Studio Ghibli",
    model="gpt-image-1",
    size="1024x1024",
    quality="high",
    provider="azure",
    image=your_image_tensor
)
```

### 环境变量配置
```bash
export AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
export AZURE_OPENAI_API_KEY=your-api-key
export AZURE_OPENAI_API_VERSION=2025-04-01-preview
export AZURE_OPENAI_DEPLOYMENT=gpt-image-1
```

## 🔧 安装和升级

### 从 GitHub 安装
```bash
git clone https://github.com/cjj198909/comfy_openai_image_api_azure.git
cd comfy_openai_image_api_azure
pip install -e .
```

### 更新现有安装
```bash
git pull origin main
pip install -e .
```

### 测试安装
```bash
python test_integration.py
```

## 📋 环境要求

### 必需依赖
- Python 3.8+
- openai >= 1.0.0
- python-dotenv >= 1.0.0
- pillow >= 10.0.0
- numpy >= 1.21.0

### 可选依赖
- torch (ComfyUI 环境中自动提供)
- requests >= 2.25.0

## 🚨 重要变更

### 配置变更
- 新增多种环境变量格式支持
- 推荐使用 `AZURE_OPENAI_*` 前缀的环境变量
- 配置验证和错误提示改进

### API 变更
- 从手动 HTTP 请求改为官方 SDK
- 改进的错误处理和重试机制
- 更好的类型安全和代码补全

### 向后兼容性
- 保持与现有 ComfyUI 工作流的兼容性
- 现有的环境变量仍然支持
- 节点接口保持不变

## 🔍 故障排除

### 常见问题
1. **环境变量未设置**: 参考 `config.env.example` 配置
2. **API 密钥错误**: 检查 Azure 门户中的密钥状态
3. **端点格式错误**: 确保使用正确的 Azure OpenAI 端点格式

### 获取帮助
- 查看 `TROUBLESHOOTING.md` 详细故障排除指南
- 检查 `QUICK_START.md` 快速开始指南
- 运行 `python test_integration.py` 验证配置

## 🎯 下一步计划

- 添加更多图像编辑功能
- 支持其他 Azure 认知服务
- 性能优化和缓存机制
- 更多示例和教程

## 🙏 致谢

感谢所有贡献者和用户的支持！这个版本的改进基于社区反馈和 Azure OpenAI 的最新功能。

---

## 📞 支持和反馈

如有问题或建议，请：
- 创建 GitHub Issue
- 查看项目文档
- 参考示例代码

**🎉 享受全新的 Azure OpenAI 图像编辑体验！**
