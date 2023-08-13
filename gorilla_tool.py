import os
import requests

from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Type

# Defining the Input Model
class GorillaToolInput(BaseModel):
    message: str = Field(..., description="Message to be processed by Gorilla LLM")

# Defining the Gorilla LLM Tool
class GorillaTool(BaseTool):
    name: str = "Gorilla LLM Tool"
    args_schema: Type[BaseModel] = GorillaToolInput
    description: str = "Tool to interact with Gorilla LLM"
    
    def _execute(self, message: str = None):
        try:
            response = self.interact_with_gorilla_llm(message)
            processed_response = self.process_gorilla_response(response)
            return processed_response
        except Exception as e:
            return f"Error: {str(e)}"

    def interact_with_gorilla_llm(self, input_message):
        api_url = os.environ.get('GORILLA_LLM_API_ENDPOINT', 'https://default-gorilla-llm-api-endpoint.com/interact')
        payload = {'message': input_message}
        try:
            response = requests.post(api_url, json=payload)
            response.raise_for_status()  # Raise an exception for HTTP errors
            return response.json()
        except requests.RequestException as e:
            raise Exception(f"API Request Error: {str(e)}")

    def process_gorilla_response(self, response):
        if not response or 'result' not in response:
            raise Exception("Invalid API response format")
        return response.get('result', 'No result found')
