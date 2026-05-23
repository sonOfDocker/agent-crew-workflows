import sys
import os
from datetime import datetime
from crews.story_readiness.crew import StoryReadinessCrew

def run():
    """
    Run the Story Readiness crew.
    """
    if len(sys.argv) < 3:
        print("Usage: python main.py <story_file_path> <context_bundle_path>")
        sys.exit(1)

    story_path = sys.argv[1]
    context_path = sys.argv[2]

    if not os.path.exists(story_path):
        print(f"Error: Story file not found at {story_path}")
        sys.exit(1)

    if not os.path.exists(context_path):
        print(f"Error: Context bundle not found at {context_path}")
        sys.exit(1)

    with open(story_path, 'r', encoding='utf-8') as f:
        story_input = f.read()

    with open(context_path, 'r', encoding='utf-8') as f:
        project_context = f.read()

    inputs = {
        'story_input': story_input,
        'project_context': project_context,
        'current_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

    print(f"Starting Story Readiness Workflow for: {story_path}")
    result = StoryReadinessCrew().crew().kickoff(inputs=inputs)
    print("\nWorkflow completed successfully.")
    print("Result:", result)

if __name__ == "__main__":
    run()
