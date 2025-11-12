from langgraph.graph import StateGraph, START, END
from src.langgraph.state.state import State
from src.langgraph.nodes.basic_chatbot_node import BasicChatbotNode
from src.langgraph.tools.search_tool import get_tools, create_search_tool_node
from langgraph.prebuilt import tools_condition
from src.langgraph.nodes.chatbot_with_Tool_node import ChatbotWithToolNode


class GraphBuilder:
    def __init__(self, model):
        self.llm = model

    def basic_chatbot_build_graph(self):
        graph = StateGraph(State)

        chatbot_node = BasicChatbotNode(self.llm)

        graph.add_node("chatbot", chatbot_node.process)
        graph.add_edge(START, "chatbot")
        graph.add_edge("chatbot", END)

        return graph.compile()

    def chatbot_with_tools_build_graph(self):
        tools = get_tools()
        tool_node = create_search_tool_node(tools)

        graph = StateGraph(State)

        chatbot_with_tools_obj = ChatbotWithToolNode(self.llm)
        chatbot_node = chatbot_with_tools_obj.create_chatbot(tools)

        graph.add_node("chatbot", chatbot_node)
        graph.add_node("tools", tool_node)

        graph.add_edge(START, "chatbot")
        graph.add_conditional_edges("chatbot", tools_condition)
        graph.add_edge("tools", "chatbot")
        graph.add_edge("chatbot", END)

        return graph.compile()

    def setup_graph(self, usecase: str):
        if usecase == "Basic Chatbot":
            return self.basic_chatbot_build_graph()

        if usecase == "Chatbot With Web":
            return self.chatbot_with_tools_build_graph()

        raise ValueError(f"Unsupported usecase: {usecase}")
