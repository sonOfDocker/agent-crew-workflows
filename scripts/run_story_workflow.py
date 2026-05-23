import sys
import os

# Add the project root to sys.path to allow importing from crews
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from crews.story_readiness.main import run

if __name__ == "__main__":
    run()
