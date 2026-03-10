#!/usr/bin/env python3
import os
import sys
import requests
import json
import argparse

def main():
    parser = argparse.ArgumentParser(description="Calculate customs bond requirements via TariffX AI.")
    parser.add_argument("--past", type=float, default=0.0, help="Duties paid in previous 12 months in USD")
    parser.add_argument("--future", type=float, default=0.0, help="Estimated duties for next 12 months in USD")
    parser.add_argument("--adcvd", action="store_true", help="Product is subject to AD/CVD")
    parser.add_argument("--pga", action="store_true", help="Product is subject to PGA (FDA, EPA, etc)")
    
    args = parser.parse_args()
    
    api_key = os.getenv("TARIFFX_API_KEY")
    if not api_key:
        print(json.dumps({
            "error": "Missing Authentication",
            "message": "宿主机未配置 TARIFFX_API_KEY 环境变量。",
            "action": '前往 https://tariffx.ai/dashboard/api-keys 获取，并设置：export TARIFFX_API_KEY="tx-live-xxx"'
        }, ensure_ascii=False))
        sys.exit(1)
        
    if args.past == 0 and args.future == 0:
        print(json.dumps({
            "error": "Invalid Input",
            "message": "过往12个月关税(--past) 或 未来预期关税(--future) 必须至少一个大于0。"
        }, ensure_ascii=False))
        sys.exit(1)
        
    url = "https://tariffx-backend-staging.onrender.com/api/v1/openapi/bond"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "duties_prev_12m": args.past,
        "est_total_duties_next_year": args.future if args.future > 0 else None,
        "has_ad_cvd": args.adcvd,
        "has_pga": args.pga
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
                "message": f"精算后台发生业务异常: {err_msg}"
            }, ensure_ascii=False))

if __name__ == "__main__":
    main()
