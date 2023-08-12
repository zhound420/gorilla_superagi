from superagi.tools.base_tool import BaseToolkit, BaseTool
from typing import Type, List

# Defining the Gorilla LLM Toolkit
class GorillaToolkit(BaseToolkit):
    name: str = "Gorilla LLM Toolkit"
    description: str = "Toolkit for Gorilla LLM"
    
    def get_tools(self) -> List[BaseTool]:
        return [GorillaTool()]
    
    def get_env_keys(self) -> List[str]:
        return ['GORILLA_LLM_API_ENDPOINT']
