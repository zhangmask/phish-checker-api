import json
import requests

API_KEY = "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"
MODEL_ID = "nvidia/llama-3.1-nemotron-ultra-253b-v1"

def handler(event, context):
    try:
        body = json.loads(event["body"])
        url = body.get("url", "")
        prompt = f"请判断以下网址是否为官方网站或其旗下页面，并指出是否存在钓鱼或广告风险：{url}"

        response = requests.post(
            "https://integrate.api.nvidia.com/v1/completions",
            json={
                "model": MODEL_ID,
                "messages": [{"role": "user", "content": prompt}]
            },
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            }
        )

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": response.text
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
