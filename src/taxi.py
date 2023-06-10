import gymnasium as gym
import util

env_list = ['Acrobot-v1', 'CartPole-v0', 'CartPole-v1', 'MountainCar-v0', 'MountainCarContinuous-v0', 'Pendulum-v1', 'CartPoleJax-v0', 'CartPoleJax-v1', 'PendulumJax-v0', 'BipedalWalker-v3', 'BipedalWalkerHardcore-v3', 'CarRacing-v2', 'LunarLander-v2', 'LunarLanderContinuous-v2', 'Blackjack-v1', 'CliffWalking-v0', 'FrozenLake-v1', 'FrozenLake8x8-v1', 'Taxi-v3', 'Jax-Blackjack-v0', 'Ant-v2', 'Ant-v3', 'Ant-v4', 'HalfCheetah-v2', 'HalfCheetah-v3', 'HalfCheetah-v4', 'Hopper-v2', 'Hopper-v3', 'Hopper-v4', 'Humanoid-v2', 'Humanoid-v3', 'Humanoid-v4', 'HumanoidStandup-v2', 'HumanoidStandup-v4', 'InvertedDoublePendulum-v2', 'InvertedDoublePendulum-v4', 'InvertedPendulum-v2', 'InvertedPendulum-v4', 'Pusher-v2', 'Pusher-v4', 'Reacher-v2', 'Reacher-v4', 'Swimmer-v2', 'Swimmer-v3', 'Swimmer-v4', 'Walker2d-v2', 'Walker2d-v3', 'Walker2d-v4', 'GymV21Environment-v0', 'GymV26Environment-v0']

def main():
    for env_name in env_list[:10]:
        env = gym.make(env_name, render_mode="human")
        util.try_env(env, 20)

if __name__ == "__main__":
    main()