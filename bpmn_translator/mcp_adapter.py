import tempfile
import os
from typing import Dict, List, Optional, Union
from .translator import BPMNTranslator

class MCPBPMNTranslator:
    @staticmethod
    def translate_bpmn(bpmn_content: str, output_format: str = "both") -> Dict[str, str]:
        """
        Translate BPMN content according to MCP interface
        
        Args:
            bpmn_content: The BPMN XML content as string
            output_format: One of "description", "user_stories", or "both"
            
        Returns:
            Dict containing the translation results
        """
        # Create temporary file for BPMN content
        with tempfile.NamedTemporaryFile(mode='w', suffix='.bpmn', delete=False) as tmp:
            tmp.write(bpmn_content)
            tmp_path = tmp.name
        
        try:
            # Create translator instance
            translator = BPMNTranslator(tmp_path)
            
            # Get process description
            description = translator.generate_description() if output_format in ["description", "both"] else None
            
            # Get user stories
            user_stories = translator.generate_user_stories() if output_format in ["user_stories", "both"] else None
            
            result = {}
            if description:
                result["description"] = description
            if user_stories:
                result["user_stories"] = user_stories
                
            return result
            
        finally:
            # Clean up temporary file
            os.unlink(tmp_path)
    
    @staticmethod
    def generate_user_stories(bpmn_content: str, roles: Optional[List[str]] = None) -> Dict[str, List[str]]:
        """
        Generate user stories from BPMN content
        
        Args:
            bpmn_content: The BPMN XML content as string
            roles: Optional list of specific roles to generate stories for
            
        Returns:
            Dict mapping roles to lists of user stories
        """
        # Create temporary file for BPMN content
        with tempfile.NamedTemporaryFile(mode='w', suffix='.bpmn', delete=False) as tmp:
            tmp.write(bpmn_content)
            tmp_path = tmp.name
        
        try:
            # Create translator instance
            translator = BPMNTranslator(tmp_path)
            
            # Generate user stories
            stories = translator.generate_user_stories(roles)
            
            return {"user_stories": stories}
            
        finally:
            # Clean up temporary file
            os.unlink(tmp_path)