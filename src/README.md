# Gym Agents

## General Steps
- Import
- Parameters (inherent from namedtuple)
- Create env
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

## Design
- Params in .yml file
- Read .yml file to a dict
- make an env (rgb_array), with special params
- Write general QLearner and Explorer in a separate class
- Create general learner
- 

main.py
    # read params
    # create env
    # create Qlearner, explorer
    # create Experiment
        # Print training summary
        # Plot training curve, rewards, eps
        # Rerun and print stats
        # Save training stats to file
    # Save model (qtable, dnn)
    # Load model and rerun