import dotenv

dotenv.load_dotenv()

from crewai import Agent, Crew, Task
from crewai.project import CrewBase, agent, task, crew

@CrewBase
class TranslatorCrew:
    @agent
    def translator_agent(self):
        return Agent(
            config=self.agents_config["translator_agent"], #type: ignore[index]
        )
    
    @task
    def translate_task(self):
        return Task(
            config=self.tasks_config["translate_task"], # type: ignore[index]
        )

    @task
    def retranslate_task(self):
        return Task(
            config=self.tasks_config["retranslate_task"], # type: ignore[index]
        )

    @crew
    def assemble_crew(self):
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            verbose=True,
        )

TranslatorCrew().assemble_crew().kickoff(
    inputs={
        "sentence": "I'm Min and I like to ride my bicicle in Napoli",
    }
)