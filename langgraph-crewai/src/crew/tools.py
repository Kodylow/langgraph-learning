from langchain_community.agent_toolkits import GmailToolkit
from langchain_community.tools.gmail.create_draft import GmailCreateDraft
from langchain.tools import tool


class CreateDraftTool:
    @tool("Create Draft")
    def create_draft(data):
        pass
