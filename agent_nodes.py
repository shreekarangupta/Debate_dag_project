from datetime import datetime
from transformers import pipeline, set_seed
from memory import DebateMemory

debate_memory = DebateMemory()

# Flan-T5 instruction-tuned pipeline
generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    tokenizer="google/flan-t5-base",
    framework="pt"  # Force PyTorch instead of TensorFlow
)

set_seed(42)  # For reproducibility

# Mapping for friendly names
AGENT_NAME_MAP = {
    "AgentA": "Scientist",
    "AgentB": "Philosopher"
}

def log_message(msg):
    with open("debate_log.txt", "a", encoding='utf-8') as f:
        f.write(f"[{datetime.now()}] {msg}\n")

def clean_text(text):
    return text.split("Quote from")[0].strip()

def agent_response(agent):
    def respond(state):
        topic = state["topic"]
        round_num = len(state.get("arguments", [])) + 1  # count actual message turns

        memory = debate_memory.memory
        last_args = []
        for ag in ["AgentA", "AgentB"]:
            last_two = memory[ag][-2:]
            for _, msg in last_two:
                readable_name = AGENT_NAME_MAP[ag]
                last_args.append(f"{readable_name}: {clean_text(msg)}")

        memory_summary = "\n".join(last_args) if last_args else "No previous arguments."
        readable_name = AGENT_NAME_MAP[agent]

        # ✅ Instruction-style prompt
        prompt = (
            f"Instruction: You are {readable_name}, an AI agent in a formal debate.\n"
            f"Input:\nDebate Topic: {topic}\n"
            f"Round: {round_num}\n"
            f"Previous arguments:\n{memory_summary}\n"
            f"Output: Provide your next clear and logical argument (1-2 sentences):"
        )

        output = generator(prompt, max_new_tokens=80, do_sample=True, temperature=0.9)[0]['generated_text']
        response = clean_text(output)

        # 🧠 Save memory and log
        debate_memory.add(agent, response)
        log_message(f"{readable_name} [Round {round_num}]: {response}")
        print(f"[Round {round_num}] {readable_name}: {response}")

        state.setdefault("arguments", []).append({readable_name: response})
        return state
    return respond
