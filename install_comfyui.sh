#!/bin/bash

# ComfyUI OpenAI Image API Azure 节点安装脚本
# 自动安装脚本

echo "🚀 ComfyUI OpenAI Image API Azure 节点安装脚本"
echo "=================================================="
echo ""

# 检查是否提供了 ComfyUI 路径
if [ -z "$1" ]; then
    echo "❌ 请提供 ComfyUI 安装路径"
    echo "用法: $0 /path/to/ComfyUI"
    echo ""
    echo "示例:"
    echo "  $0 /Users/username/ComfyUI"
    echo "  $0 ~/ComfyUI"
    exit 1
fi

COMFYUI_PATH="$1"
CUSTOM_NODES_PATH="$COMFYUI_PATH/custom_nodes"
TARGET_PATH="$CUSTOM_NODES_PATH/comfy_openai_image_api_azure"

echo "📍 ComfyUI 路径: $COMFYUI_PATH"
echo "📁 Custom Nodes 路径: $CUSTOM_NODES_PATH"
echo ""

# 检查 ComfyUI 目录是否存在
if [ ! -d "$COMFYUI_PATH" ]; then
    echo "❌ ComfyUI 目录不存在: $COMFYUI_PATH"
    exit 1
fi

# 检查 custom_nodes 目录是否存在
if [ ! -d "$CUSTOM_NODES_PATH" ]; then
    echo "❌ custom_nodes 目录不存在: $CUSTOM_NODES_PATH"
    exit 1
fi

echo "✅ ComfyUI 目录验证通过"
echo ""

# 检查是否已经安装
if [ -d "$TARGET_PATH" ]; then
    echo "⚠️  节点已存在，正在更新..."
    cd "$TARGET_PATH"
    git pull origin main
    echo "✅ 节点已更新"
else
    echo "📦 正在克隆项目..."
    cd "$CUSTOM_NODES_PATH"
    git clone https://github.com/cjj198909/comfy_openai_image_api_azure.git
    echo "✅ 项目克隆完成"
fi

echo ""
echo "📋 安装依赖项..."
cd "$TARGET_PATH"

# 尝试找到 ComfyUI 的 Python 环境
PYTHON_CMD="python"
if [ -f "$COMFYUI_PATH/venv/bin/python" ]; then
    PYTHON_CMD="$COMFYUI_PATH/venv/bin/python"
    echo "🐍 使用 ComfyUI 虚拟环境: $PYTHON_CMD"
elif [ -f "$COMFYUI_PATH/venv/Scripts/python.exe" ]; then
    PYTHON_CMD="$COMFYUI_PATH/venv/Scripts/python.exe"
    echo "🐍 使用 ComfyUI 虚拟环境: $PYTHON_CMD"
else
    echo "🐍 使用系统 Python: $PYTHON_CMD"
fi

# 安装依赖项
"$PYTHON_CMD" -m pip install -r requirements.txt

echo ""
echo "✅ 安装完成！"
echo ""
echo "📝 接下来的步骤："
echo "1. 重启 ComfyUI"
echo "2. 在节点列表中查找 'OpenAI Image API'"
echo "3. 配置 API 密钥和端点"
echo ""
echo "📖 更多信息请查看:"
echo "   - README.md"
echo "   - COMFYUI_INSTALLATION_GUIDE.md"
echo ""
echo "🔗 项目地址: https://github.com/cjj198909/comfy_openai_image_api_azure"
echo "🙏 基于原项目: https://github.com/unicough/comfy_openai_image_api"
echo ""
echo "🎉 安装完成！祝您使用愉快！"
