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
        response = self.interact_with_gorilla_llm(message)
        processed_response = self.process_gorilla_response(response)
        return processed_response

    def interact_with_gorilla_llm(self, input_message):
        # Fetching the API endpoint from an environment variable
        api_url = os.environ.get('GORILLA_LLM_API_ENDPOINT', 'http://zanino.millennium.berkeley.edu:8000/v1')
        payload = {'message': input_message}
        response = requests.post(api_url, json=payload)
        return response.json()

    def process_gorilla_response(self, response):
        # Extracting relevant information from the Gorilla LLM response
        return response.get('result', 'No result found')
