from crewai import Crew, Process
from tasks import research_task, write_task
from agents import news_researcher_agent, news_writer

crew = Crew(
    agents=[news_researcher_agent, news_writer],
    tasks=[research_task, write_task],
    process= Process.sequential

)

result = crew.kickoff(inputs={'topic': 'AI and quantum computing'})

print(result)