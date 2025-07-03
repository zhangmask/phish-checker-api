# Vercel 会自动将这个函数作为 API 入口

import requests
from flask import Request, jsonify
from flask_cors import cross_origin

API_KEY = "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"
API_URL = "https://integrate.api.nvidia.com/v1/completions"
MODEL_ID = "nvidia/llama-3.1-nemotron-ultra-253b-v1"

@cross_origin()
def handler(request: Request):
    try:
        data = request.get_json()
        url = data.get("url", "")
        prompt = f"请判断以下网址是否为官方网站或其旗下页面，并指出是否存在钓鱼或广告风险：{url}"

        payload = {
            "model": MODEL_ID,
            "messages": [{"role": "user", "content": prompt}]
        }

        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }

        r = requests.post(API_URL, json=payload, headers=headers)
        return jsonify(r.json())

    except Exception as e:
        return jsonify({"error": str(e)}), 500
