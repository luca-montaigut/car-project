import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)


def generate_image(model: str, color: str) -> str:
    prompt = f"A {color} {model} car, highly detailed, sleek design, on a clean background. The car must fit entirely in the image, it's important"
    response = client.images.generate(prompt=prompt, n=1, size="1024x1024")
    return response.data[0].url
