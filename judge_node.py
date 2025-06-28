from agent_nodes import debate_memory, log_message
import random

AGENT_NAME_MAP = {
    "AgentA": "Scientist",
    "AgentB": "Philosopher"
}

def judge_node(state):
    transcript = debate_memory.get_transcript()

    # Count how many arguments each agent made
    scientist_score = sum(1 for round in state["arguments"] if "Scientist" in round)
    philosopher_score = sum(1 for round in state["arguments"] if "Philosopher" in round)

    # Determine winner
    if scientist_score == philosopher_score:
        winner_key = random.choice(["AgentA", "AgentB"])
        winner = AGENT_NAME_MAP[winner_key]
        reason = "Both agents presented balanced arguments. Judge selected randomly."
    elif scientist_score > philosopher_score:
        winner = "Scientist"
        reason = "Scientist presented more consistent arguments throughout the debate."
    else:
        winner = "Philosopher"
        reason = "Philosopher presented more consistent arguments throughout the debate."

    # Log the final summary
    log_message("\n===== 🧾 Debate Summary =====\n" + transcript)
    log_message(f"\n🏁 Final Verdict: {winner} Wins!\n📌 Reason: {reason}\n")

    # Print final results to console
    print("\n📜 Full Debate Transcript:\n")
    print(transcript)
    print(f"\n🏆 Winner: {winner}")
    print(f"📌 Reason: {reason}")

    return state
