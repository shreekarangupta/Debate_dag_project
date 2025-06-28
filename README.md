 🧠 Task 3 - Multi-Agent Debate DAG

**ATG Machine Learning Internship (Task 3 Submission)**
Created by **Karan Gupta**



 📌 Objective

To build a Multi-Agent Debate System using **LangGraph**, where two AI agents debate a given topic in 8 rounds, and a Judge node decides the winner. The debate process uses memory and structured graph logic to ensure flow, turn-taking, and result analysis.
### 🔧 Tech Stack & Tools

* 🧠 **LangGraph** – For building the DAG flow
* 🤖 **HuggingFace Transformers** – For AI agent responses (`flan-t5-base` model)
* 🐍 **Python** – Core logic
* 📝 **Memory & Logging** – Custom memory class + file-based logging
* 🎥 **Demo Tools** – Terminal + Video Recording


 📂 Project Structure

debate_dag_project/
│
├── debate_dag.py         # Main file to run the debate DAG
├── agent_nodes.py        # Agent logic using Flan-T5
├── judge_node.py         # Judge logic to summarize & decide winner
├── memory.py             # Memory class to track agent arguments
├── debate_log.txt        # Logs all arguments and winner (generated during run)
├── dag_diagram.png       # DAG flow diagram image (attached in submission)
└── README.md             # This file


 🚀 How It Works

1. **User Input**

   * Enter a debate topic (e.g., *"Should AI be regulated like medicine?"*)

2. **Debate Starts**

   * Two agents – **Scientist** and **Philosopher** – take alternate turns
   * Each provides 1–2 sentence logical arguments
   * Memory of previous arguments is passed between rounds

3. **8 Rounds**

   * Debate continues for 8 turns (4 rounds each agent)

4. **Judge Node**

   * Collects full transcript
   * Randomly declares a winner if logic is balanced
   * Else selects based on better argument history

5. **Output**

   * Transcript and winner shown in terminal
   * Also saved in `debate_log.txt`

 ▶️ How to Run

1. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the script**

   ```bash
   python debate_dag.py
   ```

3. **Enter a topic when asked**

   * Example: `Can AI replace human teachers?`

4. **View the output**

   * Terminal will show transcript and winner
   * Log also saved in `debate_log.txt`

### 📊 DAG Diagram

![DAG Flow](dag_diagram.png)



### 🎥 Demo

A demo video is provided showing:

* Topic entry
* 8-round debate with turn-taking
* Judge output
* Explanation of flow and logic

### ✅ Features

* 🔁 8 Turn Alternating Debate
* 🧠 Memory-based argument generation
* 🗣️ Flan-T5 for natural language debate
* 📄 Judge node with reasoning
* 📝 Transcript logging

 🙋 About Me

**Karan Gupta**
B.Tech IT | Pre-Final Year Student
Email: karanguptaagra60@gmail.com
GitHub: https://github.com/shreekarangupta
Passionate about AI, NLP, and intelligent systems.


