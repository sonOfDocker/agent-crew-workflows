import sys
import argparse
from crews.story_readiness.inputs import load_workflow_inputs

def run():
    """
    Validate and load workflow inputs.
    """
    parser = argparse.ArgumentParser(description="Load and validate workflow inputs.")
    parser.add_argument("--context-file", required=True, help="Path to the project context bundle.")
    parser.add_argument("--story-file", required=True, help="Path to the story markdown file.")

    args = parser.parse_args()

    try:
        inputs = load_workflow_inputs(args.story_file, args.context_file)
        
        print("Workflow inputs loaded successfully.\n")
        print(f"Context file: {inputs.context_path}")
        print(f"Context characters: {inputs.context_size}\n")
        print(f"Story file: {inputs.story_path}")
        print(f"Story characters: {inputs.story_size}")
        
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    run()
