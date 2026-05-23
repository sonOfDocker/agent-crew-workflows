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
        """Test that kickoff calls the underlying Crew.kickoff with correct inputs and processes artifacts."""
        mock_instance = MagicMock()
        mock_crew.return_value = mock_instance
        
        output_dir = "test_kickoff_outputs"
        crew_runner = StoryReadinessCrew(output_dir=output_dir)
        
        # Create fake artifact to test post-processing
        os.makedirs(output_dir, exist_ok=True)
        fake_artifact = os.path.join(output_dir, "story-refinement.md")
        with open(fake_artifact, "w", encoding="utf-8") as f:
            f.write("Initial Content")

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
        assert "story_path" in call_args["inputs"]
        assert "context_path" in call_args["inputs"]
        assert "output_dir" in call_args["inputs"]
        assert "current_date" in call_args["inputs"]

        # Verify post-processing happened
        with open(fake_artifact, "r", encoding="utf-8") as f:
            content = f.read()
        assert content.startswith("> Note: This artifact is AI-generated planning support.")
        assert "Initial Content" in content

        # Cleanup
        os.remove(fake_artifact)
        os.rmdir(output_dir)

    def test_post_process_artifacts_directly(self):
        """Test the post-processing logic directly."""
        output_dir = "test_direct_processing"
        crew = StoryReadinessCrew(output_dir=output_dir)
        
        test_file = os.path.join(output_dir, "architecture-notes.md")
        original_content = "Architecture content here."
        with open(test_file, "w", encoding="utf-8") as f:
            f.write(original_content)
            
        crew._post_process_artifacts()
        
        with open(test_file, "r", encoding="utf-8") as f:
            new_content = f.read()
            
        assert new_content.startswith("> Note: This artifact is AI-generated planning support.")
        assert original_content in new_content
        
        # Verify it doesn't double-prepend
        crew._post_process_artifacts()
        with open(test_file, "r", encoding="utf-8") as f:
            newer_content = f.read()
        assert newer_content == new_content

        # Cleanup
        os.remove(test_file)
        os.rmdir(output_dir)

    def test_post_process_all_artifacts(self):
        """Test that all six expected artifact filenames are handled by post-processing."""
        output_dir = "test_all_artifacts_processing"
        crew = StoryReadinessCrew(output_dir=output_dir)
        
        expected_files = [
            'story-refinement.md',
            'architecture-notes.md',
            'test-plan.md',
            'implementation-plan.md',
            'review-notes.md',
            'final-summary.md'
        ]
        
        for filename in expected_files:
            file_path = os.path.join(output_dir, filename)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(f"Content for {filename}")
            
        crew._post_process_artifacts()
        
        for filename in expected_files:
            file_path = os.path.join(output_dir, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            assert content.startswith("> Note: This artifact is AI-generated planning support.")
            assert f"Content for {filename}" in content
            os.remove(file_path)
            
        os.rmdir(output_dir)

    def test_invalid_inputs_fail(self):
        """Test that the runner fails with non-existent files."""
        from crews.story_readiness.inputs import load_workflow_inputs
        with pytest.raises(FileNotFoundError):
            load_workflow_inputs("non_existent_story.md", "non_existent_context.md")

    def test_task_definitions_include_guardrail_keywords(self):
        """Verify that task definitions in tasks.yaml include key guardrail language."""
        import yaml
        tasks_config_path = os.path.join("crews", "story_readiness", "config", "tasks.yaml")
        with open(tasks_config_path, "r", encoding="utf-8") as f:
            tasks = yaml.safe_load(f)
            
        for task_name, task_data in tasks.items():
            desc = task_data.get("description", "").lower()
            # All tasks should mention they are advisory
            assert "advisory" in desc
            assert "human review" in desc
            
            # Specific guardrail checks
            if task_name == "refine_story_task":
                assert "assumptions" in desc
                assert "open questions" in desc
            elif task_name == "produce_test_plan_task":
                assert "not claim tests have passed" in desc
            elif task_name == "produce_review_notes_task":
                assert "evidence reviewed" in desc
                assert "cautious statuses" in desc
            elif task_name == "produce_final_summary_task":
                assert "required human actions" in desc

    def test_agent_definitions_include_guardrail_keywords(self):
        """Verify that agent definitions in agents.yaml include key guardrail language."""
        import yaml
        agents_config_path = os.path.join("crews", "story_readiness", "config", "agents.yaml")
        with open(agents_config_path, "r", encoding="utf-8") as f:
            agents = yaml.safe_load(f)
            
        for agent_name, agent_data in agents.items():
            if agent_name == "human_owner":
                continue
            backstory = agent_data.get("backstory", "").lower()
            assert "guardrails" in backstory
            assert "advisory" in backstory
            
            if agent_name == "reviewer":
                assert "cautious" in backstory
                assert "not yet verifiable" in backstory
