
# Day 1 Lab Analysis

## 1. Observation Table

| Criterion | Chatbot | Workflow | Agent |
|---|---|---|---|
| Q1 correct? | No | Yes | Yes |
| Q2 correct? | No | Yes | Yes |
| Q3 correct? | No | No | Yes |
| Q4 handled well? | Yes | No | Yes |
| Challenge question handled? | No | No | Yes |
| Same output on repeat run? | | | |
| Approximate response time | | | |
| Number of LLM calls per question | | | |
| One strength | | | |
| One weakness | | | |
| Best suited for | | | |

## 2. Agent Trace

For Question 2, the agent used:

1. `get_course_fee(CS101)` → ₹12,000
2. `get_course_fee(AI202)` → ₹18,000
3. `calculator(30000*0.9)` → ₹27,000

Final answer: ₹27,000.

## 3. Challenge Observation

The workflow returned:

> Sorry, I can only answer questions about course fees.

The agent retrieved the course fees and identified these valid combinations within the ₹30,000 budget:

- CS101 + AI202 = ₹30,000
- CS101 + DS303 = ₹27,000

## 4. Discussion Questions

### 1. Why is a confident wrong fee more dangerous than “I don't know”?

A confident wrong fee can cause a user to make an incorrect financial decision. Saying “I don't know” is safer because it does not provide false information.

### 2. Why might a finance office prefer a workflow?

A fixed workflow gives predictable and controlled results for common financial questions. The rules can be checked and verified.

### 3. What problems could happen if agent steps change between runs?

The agent may produce different tool calls or answers on different runs. This can make the system less predictable and harder to test.

### 4. How could you design a system with a workflow for common questions and an agent for the rest?

Common and well-defined questions could first be handled by fixed workflow rules. Questions outside those rules could then be sent to the agent for more flexible reasoning and tool use.

### 5. Which parts of `agent.py` are the LLM, tools, and loop?

- **LLM:** `client.chat.completions.create(...)`
- **Tools:** `get_course_fee` and `calculator`
- **Loop:** `for step in range(1, max_steps + 1)`
- **Tool execution:** `TOOL_FUNCTIONS.get(name)` and the following function call

## 5. Result

The three systems demonstrate different approaches. The plain chatbot can generate natural-language responses but does not have access to private fee data. The rule-based workflow gives controlled results for the questions covered by its rules. The AI agent can use tools and repeatedly reason through a problem, allowing it to handle questions that are not covered by the fixed workflow rules. The agent also demonstrated that tool calling can fail with some models, which is an important reliability consideration.