import os
import time

from langchain_community.agent_toolkits import GmailToolkit
from langchain_community.tools.gmail.search import GmailSearch


class Nodes:
    def __init__(self):
        self.gmal = GmailToolkit()

    def check_email(self, state):
        print("# checking for new emails")
        search = GmailSearch(api_resource=self.gmal.api_resource)
        emails = search("after:newer_than:1d")
        checked_emails = (
            state["checked_emails_ids"] if state["checked_emails_ids"] else []
        )
        thread = []
        new_emails = []
        print("HERE ARE THE EMAILS", emails)
        for email in emails:
            if (email["id"] not in checked_emails) and (
                email["threadId"] not in thread
            ):
                thread.append(email["threadId"])
                new_emails.append(
                    {
                        "id": email["id"],
                        "threadId": email["threadId"],
                        "subject": email["subject"],
                    }
                )
        return {
            **state,
            "emails": new_emails,
            "checked_emails_ids": [
                *checked_emails,
                *[email["id"] for email in new_emails],
            ],
        }

    def wait_next_run(self, state):
        pass

    def new_emails(self, state):
        pass
