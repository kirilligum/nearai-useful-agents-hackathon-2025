from nearai.agents.environment import Environment


def run(env: Environment):
    # Your agent code here
    prompt = {
        "role": "system",
        "content": """
            You will receive a problem and descriptions of two LLM agents. Your task is to select the appropriate agent to solve the given problem. Respond only with the agent's number—nothing else.

            Agents:

            1: A fast, plain Llama LLM. Good for quick factual answers without complex reasoning. Not suitable for counting, math, puzzles, or multi-step thinking.

            2: A multi-step reasoning LLM with reflection capabilities. Ideal for precise counting, math, solving puzzles, complex problems, and step-by-step thinking. Also select this agent whenever the user explicitly asks to "think" or "think hard."

            Remember: Only output the number of the chosen agent.
            """,
    }

    result = env.completion([prompt] + env.list_messages())
    if "1" in result and "2" not in result:
        result = env.run_agent(
            "travel.primitives.near/trip-organizer/latest",
            query="Plan a two-day trip to Buenos Aires",
        )
    env.add_reply(result)
    print("result:", result)
    print(env.list_messages())

    env.request_user_input()


run(env)
