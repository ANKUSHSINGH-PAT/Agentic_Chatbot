from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode
from langchain_tavily import TavilySearch

def get_tools():
    tools=[TavilySearch(max_results=2)]
    return tools

def create_search_tool_node(tools):
    return ToolNode(tools=tools)