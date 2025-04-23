"""
title: openlit monitoring pipeline
author: open-webui
date: 2024-05-30
version: 1.0
license: MIT
description: A pipeline for monitoring open-webui with openlit.
requirements: openlit, openai
"""
from typing import List, Union, Generator, Iterator
from schemas import OpenAIChatMessage
from openai import OpenAI
import openlit


class Pipeline:
    def __init__(self):
        self.name = "Monitoring"
        pass

    async def on_startup(self):
        print(f"on_startup:{__name__}")
        
        # Start openlit collecting metrics
        OTEL_ENDPOINT = "http://<my-ip>:4318"
        PRICING_JSON = "/path/to/openlit_pricing.json"
        openlit.init(
            otlp_endpoint=OTEL_ENDPOINT,
            pricing_json=PRICING_JSON,
            collect_gpu_stats=True
            )
        pass

    async def on_shutdown(self):
        print(f"on_shutdown:{__name__}")
        pass

    def pipe(self, user_message: str, model_id: str, messages: List[dict], body: dict) -> Union[str, Generator, Iterator]:
        print(f"pipe:{__name__}")

        client = OpenAI(
            base_url="http://localhost:8000/v1",
            api_key="token-abc123",
            )
        
        completion = client.chat.completions.create(
            model="TinyLlama/TinyLlama_v1.1",
            messages=[
                {"role": "user", "content": user_message}
                ])
        
        print(completion.choices[0].message.content)

        return (completion.choices[0].message.content)
