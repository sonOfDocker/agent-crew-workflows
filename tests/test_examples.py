import os
import pytest

def test_example_files_exist():
    """
    Verify that the example files for the golden path demo exist.
    """
    example_dir = os.path.join("examples", "story_workflow")
    files = [
        "context-bundle.example.md",
        "story.example.md",
        "README.md",
        os.path.join("expected-output", "README.md")
    ]
    
    for file in files:
        file_path = os.path.join(example_dir, file)
        assert os.path.exists(file_path), f"Example file missing: {file_path}"
        assert os.path.getsize(file_path) > 0, f"Example file is empty: {file_path}"

def test_example_files_content():
    """
    Verify that the example files contain expected markdown headers.
    """
    example_dir = os.path.join("examples", "story_workflow")
    
    # Check context bundle
    context_path = os.path.join(example_dir, "context-bundle.example.md")
    with open(context_path, "r", encoding="utf-8") as f:
        content = f.read()
        assert "# Example Project Context" in content
        assert "## Project Name" in content
        assert "## MVP Workflow Summary" in content

    # Check story example
    story_path = os.path.join(example_dir, "story.example.md")
    with open(story_path, "r", encoding="utf-8") as f:
        content = f.read()
        assert "# STORY: Add README Usage Notes for Story Workflow" in content
        assert "## Problem Statement" in content
        assert "## Acceptance Criteria" in content

def test_expected_artifact_list_matches_contract():
    """
    Verify that the documented expected artifacts match the standard artifact names.
    """
    readme_path = os.path.join("examples", "story_workflow", "expected-output", "README.md")
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    expected_artifacts = [
        "story-refinement.md",
        "architecture-notes.md",
        "test-plan.md",
        "implementation-plan.md",
        "review-notes.md",
        "final-summary.md"
    ]
    
    for artifact in expected_artifacts:
        assert artifact in content, f"Artifact {artifact} not documented in expected-output README"
