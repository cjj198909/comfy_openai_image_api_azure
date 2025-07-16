#!/usr/bin/env python3
"""
项目整合测试脚本

测试 Azure OpenAI 图像编辑功能的基本集成
"""

import os
import sys
import logging
from pathlib import Path

# 添加项目根目录到 Python 路径
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_azure_config():
    """测试 Azure 配置管理"""
    try:
        from src.openai_image_api.azure_config import AzureConfigManager
        
        print("✅ 测试 Azure 配置管理...")
        
        # 测试环境变量获取
        test_endpoint = "https://test.openai.azure.com"
        test_key = "test-key-123"
        
        # 临时设置环境变量
        os.environ["AZURE_OPENAI_ENDPOINT"] = test_endpoint
        os.environ["AZURE_OPENAI_API_KEY"] = test_key
        
        # 创建配置
        config = AzureConfigManager.create_config()
        assert config.endpoint == test_endpoint
        assert config.api_key == test_key
        
        # 验证配置
        AzureConfigManager.validate_config(config)
        
        # 获取配置摘要
        summary = AzureConfigManager.get_config_summary(config)
        assert "***" in summary["api_key"]
        
        print("✅ Azure 配置管理测试通过")
        return True
        
    except ImportError as e:
        print(f"❌ 导入错误: {e}")
        return False
    except Exception as e:
        print(f"❌ 测试失败: {e}")
        return False

def test_imports():
    """测试模块导入"""
    try:
        print("✅ 测试模块导入...")
        
        # 测试 Azure 配置
        from src.openai_image_api.azure_config import AzureConfigManager, AzureOpenAIConfig
        print("  - Azure 配置模块 ✅")
        
        # 测试 OpenAI 导入
        from openai import AzureOpenAI
        print("  - OpenAI SDK ✅")
        
        # 测试其他依赖
        import base64
        import json
        from PIL import Image
        import numpy as np
        print("  - 基础依赖 ✅")
        
        print("✅ 所有模块导入测试通过")
        return True
        
    except ImportError as e:
        print(f"❌ 导入错误: {e}")
        return False
    except Exception as e:
        print(f"❌ 测试失败: {e}")
        return False

def test_project_structure():
    """测试项目结构"""
    try:
        print("✅ 测试项目结构...")
        
        required_files = [
            "src/openai_image_api/__init__.py",
            "src/openai_image_api/nodes.py",
            "src/openai_image_api/azure_config.py",
            "src/openai_image_api/image_utils.py",
            "examples/azure_image_edit_example.py",
            "config.env.example",
            "pyproject.toml",
            "README.md"
        ]
        
        missing_files = []
        for file_path in required_files:
            if not os.path.exists(file_path):
                missing_files.append(file_path)
        
        if missing_files:
            print(f"❌ 缺少文件: {missing_files}")
            return False
        
        print("✅ 项目结构测试通过")
        return True
        
    except Exception as e:
        print(f"❌ 测试失败: {e}")
        return False

def test_env_example():
    """测试环境变量示例文件"""
    try:
        print("✅ 测试环境变量配置...")
        
        config_file = "config.env.example"
        if not os.path.exists(config_file):
            print(f"❌ 配置文件不存在: {config_file}")
            return False
        
        with open(config_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        required_vars = [
            "AZURE_OPENAI_ENDPOINT",
            "AZURE_OPENAI_API_KEY",
            "AZURE_OPENAI_API_VERSION",
            "AZURE_OPENAI_DEPLOYMENT"
        ]
        
        missing_vars = []
        for var in required_vars:
            if var not in content:
                missing_vars.append(var)
        
        if missing_vars:
            print(f"❌ 配置文件缺少变量: {missing_vars}")
            return False
        
        print("✅ 环境变量配置测试通过")
        return True
        
    except Exception as e:
        print(f"❌ 测试失败: {e}")
        return False

def main():
    """主函数"""
    print("🚀 开始项目整合测试...")
    print("=" * 50)
    
    tests = [
        ("项目结构", test_project_structure),
        ("模块导入", test_imports),
        ("Azure 配置", test_azure_config),
        ("环境变量配置", test_env_example),
    ]
    
    passed = 0
    failed = 0
    
    for test_name, test_func in tests:
        print(f"\n📋 运行测试: {test_name}")
        try:
            if test_func():
                passed += 1
                print(f"✅ {test_name} 测试通过")
            else:
                failed += 1
                print(f"❌ {test_name} 测试失败")
        except Exception as e:
            failed += 1
            print(f"❌ {test_name} 测试异常: {e}")
    
    print("\n" + "=" * 50)
    print(f"📊 测试结果: {passed} 通过, {failed} 失败")
    
    if failed == 0:
        print("🎉 所有测试通过！项目整合成功！")
        print("\n📝 下一步:")
        print("1. 设置您的 Azure OpenAI 环境变量")
        print("2. 运行 python examples/azure_image_edit_example.py")
        print("3. 在 ComfyUI 中使用 OpenAI Image API 节点")
        return True
    else:
        print("❌ 部分测试失败，请检查错误并修复")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
