from nearai.agents.environment import Environment


def run(env: Environment):
    # Your agent code here
    prompt = {
        "role": "system",
        "content": "When answering complex questions, always break down your thinking into concise but specific steps. Start by understanding what's being asked, identify the key components or variables, and explain your reasoning for each decision. Consider multiple approaches when appropriate, explicitly evaluate tradeoffs, and show your work completely. After reaching a conclusion, verify it against the original question to ensure accuracy and completeness. Think step-by-step, and explain your logic in a way that demonstrates your full reasoning process rather than just providing the final answer.",
    }
    result = env.completion([prompt] + env.list_messages())
    env.add_reply(result)

    for _ in range(4):
        env.add_message("user", "wait, check your reasoning")
        intermediate_result = env.completion(env.list_messages())
        env.add_reply(intermediate_result)

    env.add_message("user", "final answer:")
    final_convo = env.list_messages()
    final_result = env.completion(final_convo)
    env.add_reply(final_result)

    # Allow further user input if needed
    env.request_user_input()


run(env)
