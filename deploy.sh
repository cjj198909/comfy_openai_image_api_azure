#!/bin/bash

# ComfyUI OpenAI Image API Azure - GitHub 部署脚本
# 基于原项目：https://github.com/unicough/comfy_openai_image_api

echo "🚀 ComfyUI OpenAI Image API Azure - GitHub 部署脚本"
echo "=================================================="
echo ""

# 检查是否在正确的目录
if [ ! -f "pyproject.toml" ]; then
    echo "❌ 错误: 请在项目根目录运行此脚本"
    exit 1
fi

echo "📋 当前项目状态："
echo "- 项目名称: comfy_openai_image_api_azure"
echo "- 作者: Jiajun Chen (基于 Xin 的原始工作)"
echo "- 原始项目: https://github.com/unicough/comfy_openai_image_api"
echo "- 增强功能: Azure OpenAI 支持"
echo ""

# 显示当前 Git 状态
echo "📊 Git 状态："
git status --short
echo ""

# 显示最近的提交
echo "📝 最近的提交："
git log --oneline -5
echo ""

echo "🔧 部署步骤："
echo "1. 请先在 GitHub 上创建新仓库："
echo "   - 仓库名: comfy_openai_image_api_azure"
echo "   - 描述: ComfyUI OpenAI Image API with Azure OpenAI support"
echo "   - 设置为 Public"
echo "   - 不要初始化 README"
echo ""

echo "2. 创建仓库后，运行以下命令："
echo ""
echo "# 添加新的远程仓库"
echo "git remote add new-origin https://github.com/cjj198909/comfy_openai_image_api_azure.git"
echo ""
echo "# 推送到新仓库"
echo "git push -u new-origin main"
echo ""
echo "# 可选：删除原来的远程仓库引用"
echo "git remote remove origin"
echo "git remote rename new-origin origin"
echo ""

echo "✅ 项目已准备就绪！"
echo "📁 包含以下增强功能："
echo "   - ✅ Azure OpenAI 支持"
echo "   - ✅ 双提供商支持 (OpenAI + Azure)"
echo "   - ✅ 灵活配置选项"
echo "   - ✅ 环境变量支持"
echo "   - ✅ 完整的错误处理"
echo "   - ✅ 安全最佳实践"
echo "   - ✅ 详细文档和示例"
echo ""

echo "🙏 致谢原始项目作者 Xin (unicough)"
echo "📖 更多信息请查看 README.md 和 GITHUB_UPLOAD_GUIDE.md"
echo ""

read -p "按 Enter 键继续..."
