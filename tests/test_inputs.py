import os
import pytest
from crews.story_readiness.inputs import load_workflow_inputs, WorkflowInputs

@pytest.fixture
def temp_files(tmp_path):
    story = tmp_path / "story.md"
    story.write_text("# Test Story", encoding="utf-8")
    context = tmp_path / "context.md"
    context.write_text("# Test Context", encoding="utf-8")
    return story, context

def test_load_workflow_inputs_success(temp_files):
    story_path, context_path = temp_files
    inputs = load_workflow_inputs(str(story_path), str(context_path))
    
    assert isinstance(inputs, WorkflowInputs)
    assert inputs.story_content == "# Test Story"
    assert inputs.context_content == "# Test Context"
    assert inputs.story_size == len("# Test Story")
    assert inputs.context_size == len("# Test Context")
    assert os.path.isabs(inputs.story_path)
    assert os.path.isabs(inputs.context_path)

def test_load_workflow_inputs_missing_story(tmp_path):
    context = tmp_path / "context.md"
    context.write_text("context")
    with pytest.raises(FileNotFoundError, match="Story file not found"):
        load_workflow_inputs("non_existent.md", str(context))

def test_load_workflow_inputs_missing_context(tmp_path):
    story = tmp_path / "story.md"
    story.write_text("story")
    with pytest.raises(FileNotFoundError, match="Context file not found"):
        load_workflow_inputs(str(story), "non_existent.md")

def test_load_workflow_inputs_directory_input(tmp_path):
    dir_path = tmp_path / "some_dir"
    dir_path.mkdir()
    context = tmp_path / "context.md"
    context.write_text("context")
    story = tmp_path / "story.md"
    story.write_text("story")
    
    # Story path is a directory
    with pytest.raises(ValueError, match="Story path is a directory"):
        load_workflow_inputs(str(dir_path), str(context))
        
    # Context path is a directory
    with pytest.raises(ValueError, match="Context path is a directory"):
        load_workflow_inputs(str(story), str(dir_path))

def test_load_workflow_inputs_empty_file(tmp_path):
    story = tmp_path / "story.md"
    story.write_text("   ")
    context = tmp_path / "context.md"
    context.write_text("context")
    
    # Story file is empty
    with pytest.raises(ValueError, match="Story file is empty"):
        load_workflow_inputs(str(story), str(context))
        
    # Context file is empty
    story.write_text("story")
    context.write_text("")
    with pytest.raises(ValueError, match="Context file is empty"):
        load_workflow_inputs(str(story), str(context))

def test_load_workflow_inputs_markdown_preservation(tmp_path):
    story_text = "# Title\n\n- Item 1\n- Item 2"
    story = tmp_path / "story.md"
    story.write_text(story_text, encoding="utf-8")
    context = tmp_path / "context.md"
    context.write_text("context")
    
    inputs = load_workflow_inputs(str(story), str(context))
    assert inputs.story_content == story_text
