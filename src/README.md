# Gym Agents

## General Steps
- Import
- Parameters (inherent from namedtuple)
- Creat env
    - gym.make
- QLearning class, EpsilonGreedy class (explorer)
- Create learner, explorer
- run env
    for _ in n_runs: # Run several times account for stochastics
        for episode in episodes: # Each episode run to terminate/done
            while not done:
                env.step()
- Visualization
- Save result
