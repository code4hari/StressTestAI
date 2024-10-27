from typing import Dict, Any
import anthropic
import google.generativeai as genai
from openai import OpenAI
import os
from dotenv import load_dotenv

class ModelClient:
    """Base class for model clients"""
    async def generate_response(self, prompt: str) -> str:
        raise NotImplementedError

class AnthropicClient(ModelClient):
    def __init__(self, api_key: str):
        self.client = anthropic.Client(api_key)
        
    async def generate_response(self, prompt: str) -> str:
        response = await self.client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=1024,
            temperature=0.7,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.content

class OpenAIClient(ModelClient):
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)
        
    async def generate_response(self, prompt: str) -> str:
        response = await self.client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1024,
            temperature=0.7
        )
        return response.choices[0].message.content

class GeminiClient(ModelClient):
    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')
        
    async def generate_response(self, prompt: str) -> str:
        response = await self.model.generate_content(prompt)
        return response.text

class MultiModelManager:
    def __init__(self):
        load_dotenv()
        
        self.clients = {
            "claude": AnthropicClient(os.getenv('ANTHROPIC_API_KEY')),
            "gpt4": OpenAIClient(os.getenv('OPENAI_API_KEY')),
            "gemini": GeminiClient(os.getenv('GOOGLE_API_KEY'))
        }
    
    async def generate_responses(self, prompt: str) -> Dict[str, str]:
        responses = {}
        for model_name, client in self.clients.items():
            try:
                responses[model_name] = await client.generate_response(prompt)
            except Exception as e:
                print(f"Error with {model_name}: {str(e)}")
                responses[model_name] = f"ERROR: {str(e)}"
        return responses