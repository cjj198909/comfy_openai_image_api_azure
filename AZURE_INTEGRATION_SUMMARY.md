# Azure OpenAI gpt-image-1 支持集成完成

## 项目概述

已成功为 ComfyUI OpenAI Image API 项目添加了 Azure OpenAI gpt-image-1 的支持。该项目现在支持两个提供商：

1. **OpenAI** - 原生 OpenAI API
2. **Azure OpenAI** - 微软 Azure OpenAI 服务

## 主要功能

### 1. 双提供商支持
- 支持 OpenAI 和 Azure OpenAI 两种提供商
- 通过 `provider` 参数选择使用哪个提供商
- 自动处理不同提供商的配置差异

### 2. 灵活的配置选项
- 支持环境变量配置（推荐）
- 支持节点参数直接配置
- 支持 `.env` 文件配置

### 3. 完整的 Azure OpenAI 参数支持
根据要求，节点中增加了三个 Azure OpenAI 参数：
- `azure_endpoint` - Azure OpenAI 端点 URL
- `api_key` - API 密钥（Azure OpenAI 使用）
- `azure_deployment` - 模型部署名称（对应 Azure 中的 model 参数）

### 4. 环境变量支持
```env
# OpenAI 配置
OPENAI_API_KEY=your_openai_api_key

# Azure OpenAI 配置
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_KEY=your_azure_api_key
AZURE_OPENAI_API_VERSION=2024-12-01-preview
AZURE_OPENAI_DEPLOYMENT=gpt-image-1
```

## 代码更改总结

### 1. 主要节点文件 (`src/openai_image_api/nodes.py`)
- 添加了 `AzureOpenAI` 导入
- 更新了 `INPUT_TYPES` 方法，添加了 `provider` 必需参数
- 添加了 Azure OpenAI 的可选参数：`azure_endpoint`, `azure_api_version`, `azure_deployment`
- 重构了 `generate_image` 方法以支持两种提供商
- 实现了基于提供商的客户端初始化逻辑
- 添加了环境变量加载支持

### 2. 配置文件 (`src/openai_image_api/config.py`)
- 创建了 `AzureOpenAIConfig` 和 `OpenAIConfig` 配置助手类
- 提供了配置验证和客户端参数生成方法
- 支持缺失配置检测

### 3. 依赖项更新
- 更新了 `pyproject.toml` 添加 `python-dotenv` 依赖
- 创建了 `requirements.txt` 文件
- 更新了项目描述和显示名称

### 4. 文档和示例
- 全面更新了 `README.md` 文档
- 创建了 `.env.example` 配置模板
- 添加了 `examples.py` 使用示例文件
- 更新了测试文件以反映新的功能

## 使用方法

### Azure OpenAI 配置
1. 在 Azure 中创建 OpenAI 资源
2. 部署 gpt-image-1 模型
3. 配置环境变量或节点参数：
   - `provider`: 选择 "azure"
   - `azure_endpoint`: 您的 Azure OpenAI 端点
   - `api_key`: Azure OpenAI API 密钥
   - `azure_deployment`: 模型部署名称

### OpenAI 配置
1. 获取 OpenAI API 密钥
2. 配置环境变量或节点参数：
   - `provider`: 选择 "openai"
   - `api_key`: OpenAI API 密钥

## 安全最佳实践

1. 使用环境变量存储 API 密钥
2. 不要在代码中硬编码凭据
3. 定期轮换 API 密钥
4. 监控 API 使用情况和成本
5. 考虑使用 Azure 托管身份（适用时）

## 错误处理

项目包含了全面的错误处理：
- 缺失或无效的 API 密钥检测
- 网络连接问题处理
- 无效图像格式检测
- API 速率限制处理
- 服务不可用处理

## 测试

创建了更新的测试文件，包括：
- 输入类型验证
- 节点元数据测试
- 配置助手测试
- 节点映射验证

## 结论

该项目现在完全支持 Azure OpenAI gpt-image-1 模型，具有：
- 完整的 Azure OpenAI 集成
- 灵活的配置选项
- 强大的错误处理
- 全面的文档和示例
- 安全的凭据管理

用户可以轻松地在 OpenAI 和 Azure OpenAI 之间切换，同时享受一致的用户体验。
