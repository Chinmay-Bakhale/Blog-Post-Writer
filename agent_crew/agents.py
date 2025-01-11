from crewai import Agent, LLM
from tools import tool
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import os

load_dotenv()

#llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro",
#                             verbose=True,
#                             temperature=0.5,
#                             api_key=os.getenv("GOOGLE_API_KEY"))

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
llm2 = LLM(model="gemini/gemini-1.5-pro",
           temperature=0.5,
           verbose=True)
#ai_response = llm.invoke("What is the latest trend in anime?")
#print(ai_response)

news_researcher_agent = Agent(name="researcher_agent",
                         role="Senior Researcher",
                         goal="Uncover groundbreaking research in the field of {topic}",
                         verbose=True,
                         memory=True,
                         backstory=("Driven to curiosity, you are at the forefront"
                         "of innovation and discovery in the field of {topic}."
                         "eager to explore knowledge that could change the world."),
                         toos=[tool],
                         llm=llm2,
                         allow_delegation=True
                         )

news_writer = Agent(name="writer_agent",
                    role="Senior Writer",
                    goal="Give compelling stories about {topic}",
                    verbose=True,
                    memory=True,
                    backstory=("With a passion for storytelling, you are dedicated"),
                    tools=[tool],
                    llm=llm2,
                    allow_delegation=False
                    )