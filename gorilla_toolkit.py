from abc import ABC
from superagi.tools.base_tool import BaseToolkit, BaseTool
from typing import Type, List
#from superagi.tools.external_tools.gorilla_superagi.gorilla_tool import GorillaTool

# Defining the Gorilla LLM Toolkit
class GorillaToolkit(BaseToolkit, ABC):
    name: str = "Gorilla LLM Toolkit"
    description: str = "Toolkit for Gorilla LLM"
    
    def get_tools(self) -> List[BaseTool]:
        return [GorillaTool()]
    
    def get_env_keys(self) -> List[str]:
        return ['GORILLA_LLM_API_ENDPOINT']
