import os
from dataclasses import dataclass

@dataclass(frozen=True)
class WorkflowInputs:
    """Model representing validated workflow inputs."""
    story_path: str
    story_content: str
    context_path: str
    context_content: str
    story_size: int
    context_size: int

def load_workflow_inputs(story_path: str, context_path: str) -> WorkflowInputs:
    """
    Loads and validates workflow inputs from the given file paths.
    
    Raises:
        FileNotFoundError: If a file does not exist.
        ValueError: If a path is a directory, or a file is empty or unreadable.
    """
    def validate_and_read(path: str, label: str) -> tuple[str, int]:
        if not os.path.exists(path):
            raise FileNotFoundError(f"{label} file not found: {path}")
        
        if os.path.isdir(path):
            raise ValueError(f"{label} path is a directory, expected a file: {path}")
            
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
        except (UnicodeDecodeError, IOError) as e:
            raise ValueError(f"Could not read {label} file at {path}: {str(e)}")

        if not content.strip():
            raise ValueError(f"{label} file is empty: {path}")
            
        return content, len(content)

    story_content, story_size = validate_and_read(story_path, "Story")
    context_content, context_size = validate_and_read(context_path, "Context")

    return WorkflowInputs(
        story_path=os.path.abspath(story_path),
        story_content=story_content,
        context_path=os.path.abspath(context_path),
        context_content=context_content,
        story_size=story_size,
        context_size=context_size
    )
