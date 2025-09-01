# main.py

from youtubetool.crew import Youtubetool
import warnings
warnings.filterwarnings("ignore", category=SyntaxWarning)

def run():
    inputs = {
        "url": "https://www.youtube.com/watch?v=zOxaUlRkFG0&ab_channel=TheOrganicChemistryTutor",  # replace with your test video
        "topic": "leetcode"  # optional, used for summarization context
    }
    try:
        Youtubetool().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"❌ Crew run failed: {e}")

if __name__ == "__main__":
    run()
