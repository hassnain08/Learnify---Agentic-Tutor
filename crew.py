# crew.py

from crewai import Agent, Crew, Task, Process
from crewai.project import CrewBase, agent, task, crew
from crewai.agents.agent_builder.base_agent import BaseAgent
from youtubetool.tools.custom_tool import YoutubeTranscriptTool
from typing import List

@CrewBase
class Youtubetool():
    """YouTube Lecture Summarizer Crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def summarizer(self) -> Agent:
        return Agent(
            config=self.agents_config['summarizer'],
            tools=[YoutubeTranscriptTool()],
            verbose=True
        )

    @agent
    def formatter(self) -> Agent:
        return Agent(
            config=self.agents_config['formatter'],
            verbose=True
        )

    @task
    def summarization_task(self) -> Task:
        return Task(
            config=self.tasks_config['summarization_task'],
            input="{url}"  # this will be dynamically replaced by what's passed in inputs
    )


    @task
    def formatting_task(self) -> Task:
        return Task(
            config=self.tasks_config['formatting_task'],
            output_file="lecture_summary.md"
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
