from phi.agent import Agent
from phi.model.groq import Groq # we will be using groq API keys here
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
load_dotenv()

web_search_agent = Agent(
    name = "Web Agent Sherlock",
    description = "Sherlock Web agent searches content from the web.",
    model = Groq(id="llama-3.3-70b-versatile"),
    tools  = [DuckDuckGo()],
    instructions = "Make sure to include the sources without fail.",
    show_tool_calls = True,
    markdown = True,
    debug_mode=True
)

web_search_agent.print_response("Write end to end code for a web search agent in python .",
                                stream=True)