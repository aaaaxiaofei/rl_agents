import gymnasium as gym
import util

env = gym.make("LunarLander-v2", render_mode="human")
util.try_env(env, 100)
