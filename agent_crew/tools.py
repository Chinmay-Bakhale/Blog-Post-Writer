from dotenv import load_dotenv
load_dotenv()
import os

os.environ["SERPERIOR_API_KEY"] = os.getenv("SERPER_API_KEY")

from crewai_tools import SerperDevTool

tool = SerperDevTool()