import sys
from crews.story_readiness.crew import StoryReadinessCrew

def run():
    """
    Run the crew.
    """
    inputs = {
        'story_input': 'Provide a brief story description or title here.',
        'project_context': 'Provide project context or path to context bundle here.'
    }
    StoryReadinessCrew().crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    run()
