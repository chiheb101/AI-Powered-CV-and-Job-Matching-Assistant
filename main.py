
from langchain_core.messages import HumanMessage
from agent.graph import graph


# Conversation configuration
config = {
    "configurable": {
        "thread_id": "1"
    }
}


print("\n===== CV AND JOB MATCHING ASSISTANT =====")
print("Ask questions about your CV or job opportunities.")
print("Type 'exit' or 'done' to stop the assistant.\n")


while True:

    user_input = input("You: ")

    if user_input.lower().strip() in ["exit", "done"]:
        print("Goodbye!")
        break

    response = graph.invoke(
        {
            "messages": [HumanMessage(content=user_input)]
        },
        config=config
    )

    print("\nAssistant:", response["messages"][-1].content)
    print()
