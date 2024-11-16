# Module 1

Many LLM apps use a control flow:

Start -> Step 1 -> LLM -> ... -> Step N -> End

with steps pre/post-LLM calls (tool calls, retrievals, etc.)

This forms a "chain". Same control flow every time so very reliable and easy to reason about.

But we want Agents that can pick their own control flow!

> Agents are systems where the control flow is defined by the LLM.

![alt text](image.png)

Practical Challenge:

- X axis: Agent's level of control low to high
- Y axis: Application's reliability low to high

Basic routers are low control, high reliability. Autonomous agents are high control, low reliability. LangGraph lets you increase reliability for highly autonomous agents. "Bends" the curve upwards.

Intuition: Let developer set parts of control flow (reliable), inject LLM to make it an agent (control), Express the custom control flows as graphs (LangGraph)

LangGraph Pillars: Persistence, Streaming, Human in the Loop, Controllability

LangGraph is application orchestration, LangChain is application components / integrations.
