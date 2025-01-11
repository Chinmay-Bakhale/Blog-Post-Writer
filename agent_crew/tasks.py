from crewai import Task
from agents import news_researcher_agent, news_writer
from tools import tool

research_task = Task(
    description=("Identify the nest big trend in {topic}. "
                 "Focus on finding pros and cons and the overall narrative. "
                 "Your final report should clearly articulate the key points, "
                 "it's market opportunities, and potential risks."),
                 expected_output = "A comprehensive 4 paragraph report on the latest {topic} trends.",
                 tools=[tool],
                 agent = news_researcher_agent
)

write_task = Task(
    description=("Write a compelling article about the latest {topic} trend."
                 "Your article should be engaging, informative, and well-researched."
                 "Make sure to include a catchy headline and a strong conclusion."
                 "The article should be engaging and easy to understand."),
                 expected_output = "An engaging article about the latest {topic} trend with 4 paragraphs.",
                 tools=[tool],
                 agent = news_writer,
                 async_execution = False,
                 output_file = "new-blog-post.md"
)

