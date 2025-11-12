from typing import Annotated, List
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage

class State(TypedDict):
    """Represents the state of the chatbot graph."""
    messages: Annotated[List, add_messages]
