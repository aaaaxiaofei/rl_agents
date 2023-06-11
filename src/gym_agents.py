import gymnasium as gym
import util

env_list = ['Acrobot-v1', 'CartPole-v0', 'CartPole-v1', 'MountainCar-v0', 'MountainCarContinuous-v0', 'Pendulum-v1', 'CartPoleJax-v0', 'CartPoleJax-v1', 'PendulumJax-v0', 'BipedalWalker-v3', 'BipedalWalkerHardcore-v3', 'CarRacing-v2', 'LunarLander-v2', 'LunarLanderContinuous-v2', 'Blackjack-v1', 'CliffWalking-v0', 'FrozenLake-v1', 'FrozenLake8x8-v1', 'Taxi-v3', 'Jax-Blackjack-v0', 'Ant-v2', 'Ant-v3', 'Ant-v4', 'HalfCheetah-v2', 'HalfCheetah-v3', 'HalfCheetah-v4', 'Hopper-v2', 'Hopper-v3', 'Hopper-v4', 'Humanoid-v2', 'Humanoid-v3', 'Humanoid-v4', 'HumanoidStandup-v2', 'HumanoidStandup-v4', 'InvertedDoublePendulum-v2', 'InvertedDoublePendulum-v4', 'InvertedPendulum-v2', 'InvertedPendulum-v4', 'Pusher-v2', 'Pusher-v4', 'Reacher-v2', 'Reacher-v4', 'Swimmer-v2', 'Swimmer-v3', 'Swimmer-v4', 'Walker2d-v2', 'Walker2d-v3', 'Walker2d-v4', 'GymV21Environment-v0', 'GymV26Environment-v0']

'''
0 Acrobot-v1 Works
1 CartPole-v0 Works
2 CartPole-v1 Works
3 MountainCar-v0 Works
4 MountainCarContinuous-v0 Works
5 Pendulum-v1 Works
9 BipedalWalker-v3 Works
10 BipedalWalkerHardcore-v3 Works
12 LunarLander-v2 Works
13 LunarLanderContinuous-v2 Works
15 CliffWalking-v0 Works
16 FrozenLake-v1 Works
17 FrozenLake8x8-v1 Works
18 Taxi-v3 Works
'''


print(f"Total {len(env_list)} envs")

def main():
    for i, env_name in enumerate(env_list[16:17]):
        print()
        try:
            env = gym.make("CarRacing-v2", render_mode="human")
            util.try_env(env, 20)
            print(i, env_name, 'Works')
        except Exception as e:
            # print(i, env_name, 'Failed')
            pass

if __name__ == "__main__":
    main()