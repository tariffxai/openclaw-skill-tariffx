#!/usr/bin/env python3
import os
import sys
import requests
import json
import argparse

def main():
    parser = argparse.ArgumentParser(description="Calculate precision duties via TariffX AI.")
    parser.add_argument("hts", help="The 10-digit HTS code")
    parser.add_argument("fob", type=float, help="The FOB value of imports in USD")
    parser.add_argument("--origin", default="CN", help="Origin country ISO code (default: CN)")
    parser.add_argument("--desc", default="", help="Optional product description for deeper logging")
    
    args = parser.parse_args()
    
    api_key = os.getenv("TARIFFX_API_KEY")
    if not api_key:
        print(json.dumps({
            "error": "Missing Authentication",
            "message": "宿主机未配置 TARIFFX_API_KEY 环境变量。",
            "action": '前往 https://tariffx.ai/dashboard/api-keys 获取，并设置：export TARIFFX_API_KEY="tx-live-xxx"'
        }, ensure_ascii=False))
        sys.exit(1)
        
    url = "https://tariffx-backend-staging.onrender.com/api/v1/openapi/calculator"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "hts_code": args.hts,
        "fob_value": args.fob,
        "origin_country": args.origin,
        "product_description": args.desc
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        
        # Output exactly the JSON breakdown for the Agent
        print(json.dumps(response.json(), indent=2, ensure_ascii=False))
        
    except requests.exceptions.HTTPError as e:
        if response.status_code == 402:
            print(json.dumps({
                "error": "Payment Required",
                "message": "API Credits (计次点数) 已耗尽。",
                "action": "请明确转告主人去 https://tariffx.ai 充值。"
            }, ensure_ascii=False))
        elif response.status_code == 401:
            print(json.dumps({
                "error": "Unauthorized Access",
                "message": "密钥无效或被注销。",
                "action": "请前往 https://tariffx.ai/dashboard/api-keys 重新签发。"
            }, ensure_ascii=False))
        else:
            try:
               err_msg = response.json().get("detail", {}).get("message", str(e))
            except:
               err_msg = str(e)
            print(json.dumps({
                "error": "Calculation Error",
                "message": f"算费后台引擎发生业务异常: {err_msg}"
            }, ensure_ascii=False))

if __name__ == "__main__":
    main()
