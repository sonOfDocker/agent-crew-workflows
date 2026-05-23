import os
from datetime import datetime
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crews.story_readiness.inputs import WorkflowInputs

@CrewBase
class StoryReadinessCrew():
    """StoryReadiness crew for refined planning and review."""
    
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    def __init__(self, output_dir: str = "outputs/story-workflow"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    @agent
    def story_refiner(self) -> Agent:
        return Agent(
            config=self.agents_config['story_refiner'],
            verbose=True
        )

    @agent
    def architect(self) -> Agent:
        return Agent(
            config=self.agents_config['architect'],
            verbose=True
        )

    @agent
    def test_strategist(self) -> Agent:
        return Agent(
            config=self.agents_config['test_strategist'],
            verbose=True
        )

    @agent
    def developer(self) -> Agent:
        return Agent(
            config=self.agents_config['developer'],
            verbose=True
        )

    @agent
    def reviewer(self) -> Agent:
        return Agent(
            config=self.agents_config['reviewer'],
            verbose=True
        )

    @task
    def refine_story_task(self) -> Task:
        return Task(
            config=self.tasks_config['refine_story_task'],
            output_file=os.path.join(self.output_dir, 'story-refinement.md')
        )

    @task
    def produce_architecture_notes_task(self) -> Task:
        return Task(
            config=self.tasks_config['produce_architecture_notes_task'],
            output_file=os.path.join(self.output_dir, 'architecture-notes.md')
        )

    @task
    def produce_test_plan_task(self) -> Task:
        return Task(
            config=self.tasks_config['produce_test_plan_task'],
            output_file=os.path.join(self.output_dir, 'test-plan.md')
        )

    @task
    def produce_implementation_plan_task(self) -> Task:
        return Task(
            config=self.tasks_config['produce_implementation_plan_task'],
            output_file=os.path.join(self.output_dir, 'implementation-plan.md')
        )

    @task
    def produce_review_notes_task(self) -> Task:
        return Task(
            config=self.tasks_config['produce_review_notes_task'],
            output_file=os.path.join(self.output_dir, 'review-notes.md')
        )

    @task
    def produce_final_summary_task(self) -> Task:
        return Task(
            config=self.tasks_config['produce_final_summary_task'],
            output_file=os.path.join(self.output_dir, 'final-summary.md')
        )

    @crew
    def crew(self) -> Crew:
        """Creates the StoryReadiness crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )

    def kickoff(self, inputs: WorkflowInputs):
        """Kickoff the crew with inputs."""
        crew_inputs = {
            "story_input": inputs.story_content,
            "project_context": inputs.context_content,
            "current_date": datetime.now().strftime("%Y-%m-%d")
        }
        return self.crew().kickoff(inputs=crew_inputs)
