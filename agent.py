from nearai.agents.environment import Environment


def run(env: Environment):
    # Fetch the current conversation (original query and context)
    conversation = env.list_messages()
    
    # --- Step 1: Run the initial completion ---
    initial_result = env.completion(conversation)
    env.add_reply(initial_result)
    
    # --- Step 2: n-step (n=4) chain-of-thought reasoning ---
    for _ in range(4):
        # Simulate user input: "wait, check your reasoning"
        env.add_message({"role": "user", "content": "wait, check your reasoning"})
        
        # Retrieve the updated conversation (with the new user prompt)
        updated_convo = env.list_messages()
        intermediate_result = env.completion(updated_convo)
        env.add_reply(intermediate_result)
    
    # --- Step 3: Ask for the final answer ---
    env.add_message({"role": "user", "content": "final answer:"})
    final_convo = env.list_messages()
    final_result = env.completion(final_convo)
    env.add_reply(final_result)
    
    # Allow further user input if needed
    env.request_user_input()

run(env)

