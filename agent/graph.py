
from langgraph.graph import StateGraph, START, MessagesState
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.messages import SystemMessage

from services.openai_service import llm
from tools.cv_tools import extract_cv_text
from tools.job_tools import job_posting_tool


# Available tools
tools = [extract_cv_text, job_posting_tool]

# Connect tools to the language model
llm_with_tools = llm.bind_tools(tools)


# Instructions for the assistant
system_prompt = """
You are a professional CV and career assistant.

Your role is to help users analyze their CVs, understand job
requirements, and improve their chances of finding a suitable job.

You have access to two tools:

1. extract_cv_text:
Use this tool when the user provides a CV file path and asks
you to read or analyze their CV.

2. job_posting_tool:
Use this tool when the user provides a job posting URL and
asks you to analyze the position.

You should be able to:
- Extract and understand CV information.
- Analyze job posting requirements.
- Compare a CV with a job posting.
- Identify matching skills and missing qualifications.
- Suggest improvements to the CV.

Always use information from the CV and job posting as evidence.
Never invent qualifications, skills, or experience.
Give clear, structured, and useful answers.
Use a professional and supportive tone.
"""


# Assistant node
def assistant(state: MessagesState):

    messages = [
        SystemMessage(content=system_prompt)
    ] + state["messages"]

    response = llm_with_tools.invoke(messages)

    return {"messages": [response]}


# Create the graph
builder = StateGraph(MessagesState)

builder.add_node("assistant", assistant)
builder.add_node("tools", ToolNode(tools))

builder.add_edge(START, "assistant")

builder.add_conditional_edges(
    "assistant",
    tools_condition
)

builder.add_edge("tools", "assistant")


# Add conversation memory
memory = MemorySaver()

# Compile the graph
graph = builder.compile(checkpointer=memory)
