from langgraph.graph import StateGraph
from agent_nodes import agent_response
from judge_node import judge_node
from datetime import datetime

# Topic input + logging
def get_topic():
    topic = input("🎤 Enter the debate topic: ")
    with open("debate_log.txt", "a") as f:
        f.write(f"[{datetime.now()}] Topic: {topic}\n")
    return topic

# LangGraph Build
def build_graph():
    schema = (("topic", str), ("arguments", list))
    g = StateGraph(state_schema=schema)

    # Input Node
    g.add_node("UserInput", lambda state: {
        "topic": get_topic(),
        "arguments": []
    })
    g.set_entry_point("UserInput")

    # 8 Rounds Alternate: A, B, A, B...
    prev = "UserInput"
    for i in range(8):
        agent = "AgentA" if i % 2 == 0 else "AgentB"
        node_name = f"{agent}_Round_{(i // 2) + 1}"
        g.add_node(node_name, agent_response(agent))
        g.add_edge(prev, node_name)
        prev = node_name

    # Judge
    g.add_node("Judge", judge_node)
    g.add_edge(prev, "Judge")

    return g.compile()

# Execute DAG
if __name__ == "__main__":
    print("\n🚀 Starting Multi-Agent Debate...\n")
    graph = build_graph()
    runnable = graph.with_config({})
    runnable.invoke({})
