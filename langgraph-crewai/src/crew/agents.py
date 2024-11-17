from crewai import Agent
from .tools import CreateDraftTool


class EmailFilterAgents:
    def __init__(self):
        self.gmail = GmailToolkit()

    def email_filter_agent(self):
        pass

    def email_action_agent(self):
        pass

    def email_response_writer(self):
        pass
