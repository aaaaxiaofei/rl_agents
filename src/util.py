import logging

def try_env(env, steps=10, render=True):
    observation, info = env.reset(seed=42)
    logging.info(f"{env.observation_space=}, {env.action_space=}")
    logging.info(f"Initial {observation=}, {info=}")
    for _ in range(steps):
        action = env.action_space.sample()  # this is where you would insert your policy
        observation, reward, terminated, truncated, info = env.step(action)
        if render:
            env.render()
        if terminated or truncated:
            observation, info = env.reset()
    