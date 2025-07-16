# ComfyUI 节点安装指南

## 📦 安装方法

### 方法一：Git Clone 安装（推荐）

1. **进入 ComfyUI 的 custom_nodes 目录**
   ```bash
   cd /path/to/ComfyUI/custom_nodes
   ```

2. **克隆项目**
   ```bash
   git clone https://github.com/cjj198909/comfy_openai_image_api_azure.git
   ```

3. **进入项目目录**
   ```bash
   cd comfy_openai_image_api_azure
   ```

4. **安装依赖项**
   ```bash
   pip install -r requirements.txt
   ```
   
   或者使用 ComfyUI 的 Python 环境：
   ```bash
   /path/to/ComfyUI/venv/bin/pip install -r requirements.txt
   ```

5. **重启 ComfyUI**
   - 重新启动 ComfyUI 应用程序

### 方法二：下载 ZIP 文件安装

1. **下载项目**
   - 访问 https://github.com/cjj198909/comfy_openai_image_api_azure
   - 点击绿色的 "Code" 按钮
   - 选择 "Download ZIP"

2. **解压文件**
   - 将下载的 ZIP 文件解压到 ComfyUI 的 `custom_nodes` 目录下
   - 确保文件夹名为 `comfy_openai_image_api_azure`

3. **安装依赖项**
   ```bash
   cd /path/to/ComfyUI/custom_nodes/comfy_openai_image_api_azure
   pip install -r requirements.txt
   ```

4. **重启 ComfyUI**

### 方法三：使用 ComfyUI Manager

1. **打开 ComfyUI Manager**
   - 在 ComfyUI 界面中点击 "Manager" 按钮

2. **安装自定义节点**
   - 选择 "Install Custom Nodes"
   - 搜索 "OpenAI Image API" 或 "Azure OpenAI"
   - 找到该节点并点击 "Install"

3. **重启 ComfyUI**

## 🔍 验证安装

安装完成后，您应该能在 ComfyUI 的节点列表中看到：
- **节点名称**: "OpenAI Image API"
- **显示名称**: "OpenAI/Azure OpenAI Image API with gpt-image-1"
- **分类**: "image/OpenAI"

## ⚙️ 配置说明

### 环境变量配置（可选）

在 ComfyUI 根目录创建 `.env` 文件：

```env
# OpenAI 配置
OPENAI_API_KEY=your_openai_api_key

# Azure OpenAI 配置
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_KEY=your_azure_api_key
AZURE_OPENAI_API_VERSION=2024-12-01-preview
AZURE_OPENAI_DEPLOYMENT=gpt-image-1
```

### 节点参数配置

您也可以直接在节点界面中配置：

**必需参数：**
- `prompt`: 图像生成提示
- `model`: 选择 "gpt-image-1"
- `size`: 选择图像尺寸
- `quality`: 选择图像质量
- `provider`: 选择 "openai" 或 "azure"

**可选参数：**
- `api_key`: API 密钥
- `azure_endpoint`: Azure OpenAI 端点
- `azure_deployment`: Azure 部署名称

## 🚀 使用示例

### OpenAI 使用示例
1. `provider`: 选择 "openai"
2. `api_key`: 输入您的 OpenAI API 密钥
3. `prompt`: "A beautiful landscape with mountains"
4. `model`: "gpt-image-1"
5. `size`: "1024x1024"
6. `quality`: "high"

### Azure OpenAI 使用示例
1. `provider`: 选择 "azure"
2. `azure_endpoint`: "https://your-resource.openai.azure.com/"
3. `api_key`: 输入您的 Azure OpenAI API 密钥
4. `azure_deployment`: "gpt-image-1"
5. `prompt`: "A futuristic city scene"
6. `model`: "gpt-image-1"
7. `size`: "1024x1024"
8. `quality`: "high"

## 🛠️ 故障排除

### 常见问题

1. **节点未显示**
   - 确保已重启 ComfyUI
   - 检查 custom_nodes 目录是否正确
   - 查看 ComfyUI 控制台是否有错误信息

2. **依赖项错误**
   - 确保已安装 requirements.txt 中的所有依赖
   - 使用正确的 Python 环境

3. **API 调用失败**
   - 检查 API 密钥是否正确
   - 确认网络连接正常
   - 验证 Azure 端点配置

### 获取帮助

- 🐛 报告问题: https://github.com/cjj198909/comfy_openai_image_api_azure/issues
- 📖 项目文档: https://github.com/cjj198909/comfy_openai_image_api_azure/blob/main/README.md
- 💡 功能建议: https://github.com/cjj198909/comfy_openai_image_api_azure/issues

## 📋 系统要求

- ComfyUI
- Python 3.8+
- 网络连接（用于 API 调用）
- OpenAI API 密钥或 Azure OpenAI 资源

## 🔄 更新节点

要更新到最新版本：

```bash
cd /path/to/ComfyUI/custom_nodes/comfy_openai_image_api_azure
git pull origin main
pip install -r requirements.txt
```

然后重启 ComfyUI。
