import os
import pytest
from unittest.mock import MagicMock, patch
from crews.story_readiness.inputs import WorkflowInputs
from crews.story_readiness.crew import StoryReadinessCrew

class TestWorkflow:
    def test_crew_initialization(self):
        """Test that the crew initializes with the correct output directory."""
        output_dir = "test_outputs"
        crew = StoryReadinessCrew(output_dir=output_dir)
        assert crew.output_dir == output_dir
        assert os.path.exists(output_dir)
        # Cleanup
        os.rmdir(output_dir)

    def test_crew_agents_defined(self):
        """Test that all required agents are defined in the crew."""
        crew = StoryReadinessCrew()
        assert crew.story_refiner() is not None
        assert crew.architect() is not None
        assert crew.test_strategist() is not None
        assert crew.developer() is not None
        assert crew.reviewer() is not None

    def test_crew_tasks_defined(self):
        """Test that all required tasks are defined in the crew."""
        crew = StoryReadinessCrew()
        assert crew.refine_story_task() is not None
        assert crew.produce_architecture_notes_task() is not None
        assert crew.produce_test_plan_task() is not None
        assert crew.produce_implementation_plan_task() is not None
        assert crew.produce_review_notes_task() is not None
        assert crew.produce_final_summary_task() is not None

    @patch('crews.story_readiness.crew.Crew')
    def test_crew_kickoff(self, mock_crew):
        """Test that kickoff calls the underlying Crew.kickoff with correct inputs."""
        mock_instance = MagicMock()
        mock_crew.return_value = mock_instance
        
        crew_runner = StoryReadinessCrew()
        inputs = WorkflowInputs(
            story_path="story.md",
            story_content="Story Content",
            context_path="context.md",
            context_content="Context Content",
            story_size=13,
            context_size=15
        )
        
        crew_runner.kickoff(inputs=inputs)
        
        # Verify kickoff was called
        mock_instance.kickoff.assert_called_once()
        # Verify inputs were passed
        call_args = mock_instance.kickoff.call_args[1]
        assert "inputs" in call_args
        assert call_args["inputs"]["story_input"] == "Story Content"
        assert call_args["inputs"]["project_context"] == "Context Content"
        assert "current_date" in call_args["inputs"]

    def test_invalid_inputs_fail(self):
        """Test that the runner fails with non-existent files."""
        from crews.story_readiness.inputs import load_workflow_inputs
        with pytest.raises(FileNotFoundError):
            load_workflow_inputs("non_existent_story.md", "non_existent_context.md")
