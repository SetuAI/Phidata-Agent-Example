from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from phi.storage.agent.sqlite import SqlAgentStorage
from fastapi import FastAPI
from phi.playground import Playground, serve_playground_app
import uvicorn

from dotenv import load_dotenv

load_dotenv()

web_search_agent = Agent(
    name = "Web Agent Sherlock",
    description = "Sherlock Web agent searches content from the web.",
    model = Groq(id="llama-3.3-70b-versatile"),
    tools  = [DuckDuckGo()],
    instructions = ["Make sure to include the sources without fail."],
    show_tool_calls = True,
    markdown = True,
    debug_mode=True
)

#web_search_agent.print_response("What is the capital of Nepal?", stream=True)

finance_agent = Agent(
    name="Kaizen Finance Agent",
    description = "Kaizen is a finance agent that provides accurate and double-checked information related to financial queries",
    model = Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, 
                         analyst_recommendations=True, 
                         company_info=True, 
                         company_news=True)],
    instructions=["Use tables to display data about the stocks. Make sure you give the most recent stock price. "],
    show_tool_calls=True,
    markdown=True,
    debug_mode = True
)
#finance_agent.print_response("Give us the most recent stock price and your anaysis on the NVDA stock. Also which one should I  buy ? NVDA or TSLA ? ", stream=True)

#app = Playground(agents=[finance_agent, web_search_agent]).get_app()

#if __name__ == "__main__":
    #serve_playground_app("playground:app", reload=True)


agent_team = Agent(
    team=[web_search_agent, finance_agent],
    model = Groq(id="llama-3.3-70b-versatile"),
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
    debug_mode =True
)

agent_team.print_response("Summarize analyst recommendations and share the latest news and stock price for last 10 trading days for NVDA", stream=True)