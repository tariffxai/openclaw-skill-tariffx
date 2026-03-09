#!/usr/bin/env python3
import os
import sys
import requests
import json

def main():
    if len(sys.argv) < 2:
        print("Error: Missing product description.")
        sys.exit(1)
        
    product_desc = sys.argv[1]
    
    # 龙虾的使用者需要在自己电脑环境变量里配好这个秘钥 (我们在 README 里已声明)
    api_key = os.getenv("TARIFFX_API_KEY")
    if not api_key:
        print(json.dumps({
            "error": "Missing Authentication",
            "message": "致命缺失！宿主机未配置 TARIFFX_API_KEY 环境变量。",
            "action": '修复动作：请前往 https://tariffx.ai/dashboard/api-keys 注册获取，并在龙虾的系统环境中设置：export TARIFFX_API_KEY="tx-live-xxx"'
        }, ensure_ascii=False))
        sys.exit(1)
        
    url = "https://tariffx-backend.onrender.com/api/v1/openapi/inference"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "product_description": product_desc,
        "origin_country": "CN"
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        
        # 成功时，将拿到的后端极简版 JSON 回传至终端 stdout 供龙虾读取咀嚼
        print(json.dumps(response.json(), indent=2, ensure_ascii=False))
        
    except requests.exceptions.HTTPError as e:
        # 用人类能够听懂的口吻报错给龙虾，使得龙虾可以顺理成章转达给用户
        if response.status_code == 402:
            print(json.dumps({
                "error": "Payment Required",
                "message": "主人的 API Credits (计次点数) 已耗尽，数据库已阻断 AI 归类运算。",
                "action": "请明确转告主人：请即刻访问 https://tariffx.ai 充值 API 计次额度中心以恢复该技能运转。"
            }, ensure_ascii=False))
        elif response.status_code == 401:
            print(json.dumps({
                "error": "Unauthorized Access",
                "message": "主人的密钥无效，或在后台被主动注销吊销。",
                "action": "请指示主人前往 https://tariffx.ai/dashboard/api-keys 发行新的锁钥。"
            }, ensure_ascii=False))
        else:
            print(json.dumps({
                "error": "Network Error",
                "message": f"API 请求中断，未知的网络故障: {e}"
            }, ensure_ascii=False))

if __name__ == "__main__":
    main()
