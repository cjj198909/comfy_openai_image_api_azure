# 🔧 故障排除指南

## 常见错误及解决方案

### 1. "Request URL is missing an 'http://' or 'https://' protocol"

**错误原因：** Azure OpenAI 端点配置不正确

**解决方案：**
1. 确保 `azure_endpoint` 参数包含完整的 URL，包括 `https://`
2. 正确格式：`https://your-resource.openai.azure.com/`
3. 错误格式：`your-resource.openai.azure.com/`

**示例配置：**
```
✅ 正确：https://admin-maejzf5d-westus3.openai.azure.com/
❌ 错误：admin-maejzf5d-westus3.openai.azure.com/
```

### 2. "Connection error"

**可能原因：**
- 网络连接问题
- API 端点配置错误
- API 密钥无效
- 防火墙阻止连接

**解决方案：**
1. 检查网络连接
2. 验证 API 端点 URL 格式正确
3. 确认 API 密钥有效
4. 检查防火墙设置

### 3. "Azure OpenAI endpoint is required"

**错误原因：** 选择了 Azure 提供商但未配置端点

**解决方案：**
1. 在节点参数中填写 `azure_endpoint`
2. 或设置环境变量 `AZURE_OPENAI_ENDPOINT`

### 4. "Azure OpenAI API key is required"

**错误原因：** 缺少 API 密钥

**解决方案：**
1. 在节点参数中填写 `api_key`
2. 或设置环境变量 `AZURE_OPENAI_API_KEY`

### 5. 节点未显示在 ComfyUI 中

**解决方案：**
1. 确保节点已正确安装在 `custom_nodes` 目录
2. 检查依赖项是否已安装：`pip install -r requirements.txt`
3. 重启 ComfyUI
4. 查看 ComfyUI 控制台是否有错误信息

## 📋 配置检查清单

### Azure OpenAI 配置
- [ ] `provider` 设置为 "azure"
- [ ] `azure_endpoint` 以 `https://` 开头
- [ ] `azure_endpoint` 以 `/` 结尾
- [ ] `api_key` 不为空
- [ ] `azure_deployment` 匹配您的部署名称

### OpenAI 配置
- [ ] `provider` 设置为 "openai"
- [ ] `api_key` 不为空

## 🔍 调试步骤

### 1. 检查节点参数
确保所有必需参数都已正确填写：
- `prompt`: 不为空
- `provider`: 选择正确的提供商
- `azure_endpoint`: 完整的 HTTPS URL（Azure 专用）
- `api_key`: 有效的 API 密钥

### 2. 验证 Azure 资源
如果使用 Azure OpenAI：
1. 登录 Azure 门户
2. 确认 OpenAI 资源正在运行
3. 检查部署状态
4. 验证 API 密钥是否有效

### 3. 测试网络连接
```bash
# 测试 Azure OpenAI 连接
curl -X POST "https://your-resource.openai.azure.com/openai/deployments/gpt-image-1/images/generations?api-version=2024-12-01-preview" \
  -H "Content-Type: application/json" \
  -H "api-key: your-api-key" \
  -d '{"prompt": "test", "size": "1024x1024"}'
```

### 4. 查看详细错误信息
启用详细日志记录：
1. 在 ComfyUI 控制台查看完整错误堆栈
2. 检查是否有网络相关错误
3. 确认 API 响应状态

## 🆘 获取帮助

如果问题仍然存在：

1. **GitHub Issues**: https://github.com/cjj198909/comfy_openai_image_api_azure/issues
2. **提供信息**：
   - 错误信息的完整堆栈跟踪
   - 节点配置截图（隐藏 API 密钥）
   - ComfyUI 版本信息
   - 操作系统信息

3. **常见解决方案**：
   - 更新到最新版本
   - 重新安装依赖项
   - 检查网络和防火墙设置
   - 验证 Azure 资源配置

## 📝 快速修复

### 最常见问题的快速修复：

1. **端点格式错误**：
   ```
   将：admin-maejzf5d-westus3.openai.azure.com/
   改为：https://admin-maejzf5d-westus3.openai.azure.com/
   ```

2. **空参数**：
   确保所有必需的参数都已填写，不要留空

3. **网络问题**：
   检查防火墙和代理设置

4. **API 密钥问题**：
   重新生成 API 密钥并更新配置
