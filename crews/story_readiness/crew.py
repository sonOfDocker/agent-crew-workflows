from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class StoryReadinessCrew():
    """StoryReadiness crew for refining and validating stories"""
    agents_config = 'agents.yaml'
    tasks_config = 'tasks.yaml'

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
    def test_strategy_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['test_strategy_agent'],
            verbose=True
        )

    @task
    def refine_story_task(self) -> Task:
        return Task(
            config=self.tasks_config['refine_story_task'],
        )

    @task
    def technical_review_task(self) -> Task:
        return Task(
            config=self.tasks_config['technical_review_task'],
        )

    @task
    def define_test_strategy_task(self) -> Task:
        return Task(
            config=self.tasks_config['define_test_strategy_task'],
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
    def implement_story_task(self) -> Task:
        return Task(
            config=self.tasks_config['implement_story_task'],
        )

    @task
    def review_story_task(self) -> Task:
        return Task(
            config=self.tasks_config['review_story_task'],
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
