from google.adk.agents import Agent
import requests
import os

WORKDAY_URL = os.getenv("WORKDAY_URL")

def create_asor(payload: dict):
    """
    Sample tool that posts ASOR data to Workday.
    Replace URL, auth, and payload structure
    with your organization's implementation.
    """

    response = requests.post(
        WORKDAY_URL,
        json=payload,
        timeout=30
    )

    return {
        "status_code": response.status_code,
        "response": response.json() if response.content else {}
    }


workday_agent = Agent(
    name="workday_agent",
    model="gemini-2.5-flash",
    instruction="""
    You help create ASOR requests in Workday.
    Use the create_asor tool whenever an ASOR
    needs to be submitted.
    """,
    tools=[create_asor]
)
