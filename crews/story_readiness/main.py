import sys
import argparse
import os
from crews.story_readiness.inputs import load_workflow_inputs
from crews.story_readiness.crew import StoryReadinessCrew

def run():
    """
    Validate and load workflow inputs, then execute the CrewAI workflow.
    """
    parser = argparse.ArgumentParser(description="Run the Story Readiness MVP workflow.")
    parser.add_argument("--context-file", required=True, help="Path to the project context bundle.")
    parser.add_argument("--story-file", required=True, help="Path to the story markdown file.")
    parser.add_argument("--output-dir", default="./outputs/story-workflow", help="Directory for workflow artifacts.")

    args = parser.parse_args()

    try:
        # 1. Load and validate inputs
        inputs = load_workflow_inputs(args.story_file, args.context_file)
        
        print("--- Story Readiness Workflow ---")
        print(f"Context file: {inputs.context_path}")
        print(f"Story file:   {inputs.story_path}")
        print(f"Output dir:   {os.path.abspath(args.output_dir)}")
        print("--------------------------------\n")

        # 2. Initialize and run the crew
        crew_runner = StoryReadinessCrew(output_dir=args.output_dir)
        result = crew_runner.kickoff(inputs=inputs)
        
        print("\n--------------------------------")
        print("Workflow completed successfully.")
        print(f"Artifacts generated in: {os.path.abspath(args.output_dir)}")
        print("- story-refinement.md")
        print("- architecture-notes.md")
        print("- test-plan.md")
        print("- implementation-plan.md")
        print("- review-notes.md")
        print("- final-summary.md")
        print("--------------------------------")
        
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {str(e)}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    run()
