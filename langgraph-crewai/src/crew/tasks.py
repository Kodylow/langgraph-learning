from crewai import Task
from textwrap import dedent


class EmailFilterTasks:
    def filter_emails_task(self, agent, emails):
        return Task(agent.email_filter_agent, emails)

    def action_required_emails_task(self, agent):
        return Task(agent.email_action_agent)

    def draft_responses_task(self, agent):
        return Task(agent.email_response_writer)
