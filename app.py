import mesop as me
import mesop.labs as mel
from swarm import Swarm, Agent

client = Swarm()

import wikipedia

def wikipedia_lookup(q: str) -> str:
    """Look up a query in Wikipedia and return the result"""
    try: return wikipedia.page(q).summary
    except: return None

def wikipedia_search(q: str) -> str:
    """Search for a topic in Wikipedia and return the result"""
    return wikipedia.search(q)

def transfer_to_pr_agent():
    return pr_agent

agent = Agent(
    name="Agent",
    instructions="""You are a helpful agent that answers user queries by finding and analysing information from Wikipedia.
                    You will be given a city or other location and you must retrieve it's entry on Wikipedia and then hand over to the PR Agent.""",
    functions=[wikipedia_lookup, transfer_to_pr_agent],
)

pr_agent = Agent(
    name="PR Agent",
    instructions="""You are an experienced PR copywriter. 
                    Use only the information retrieved from Wikipedia to write an enthusiastic 100-word summary of the topic 
                    that would be suitable for a promonional campaign.
                    Explain how you used the original material to create the result""",
)

messages = [{"role": "user", "content": "Paris"}]

response = client.run(agent=agent, messages=messages)
print(response.messages[-1]["content"])

@me.page(
  path="/",
  title="Swarm app",
)
def app():
  mel.text_to_text(
    upper_case_stream,
    title="Swarm PR genrator app",
  )


def upper_case_stream(s: str):
  return "Echo: " + s