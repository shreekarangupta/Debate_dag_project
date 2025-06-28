
AGENT_NAME_MAP = {
    "AgentA": "Scientist",
    "AgentB": "Philosopher"
}

class DebateMemory:
    def __init__(self):
        self.memory = {"AgentA": [], "AgentB": []}
        self.current_round = 1

    def add(self, agent, text):
        # Add the text with the round number
        self.memory[agent].append((self.current_round, text))
        # Increment round only after both agents have spoken in current round
        if len(self.memory["AgentA"]) == len(self.memory["AgentB"]):
            self.current_round += 1

    def get_transcript(self):
        transcript = []
        for r in range(1, 9):  # 8 total rounds
            for agent in ["AgentA", "AgentB"]:
                for round_num, msg in self.memory[agent]:
                    if round_num == r:
                        readable_name = AGENT_NAME_MAP[agent]
                        transcript.append(f"[Round {r}] {readable_name}: {msg}")
        return "\n".join(transcript)

    def summary(self):
        return self.get_transcript()
