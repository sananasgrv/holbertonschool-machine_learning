#!/usr/bin/env python3
"""Monte-Carlo policy gradient training loop (REINFORCE)."""
import numpy as np
policy_gradient = __import__('policy_gradient').policy_gradient


def train(env, nb_episodes, alpha=0.000045, gamma=0.98, show_result=False):
    """Trains a policy with the Monte-Carlo policy gradient.

    env is the environment instance
    nb_episodes is the number of episodes to train over
    alpha is the learning rate
    gamma is the discount factor
    show_result renders the environment every 1000 episodes when True
    Returns: the list of scores (total reward per episode)
    """
    weight = np.random.rand(*env.observation_space.shape,
                            env.action_space.n)
    scores = []

    for episode in range(nb_episodes):
        state, _ = env.reset()
        grads = []
        rewards = []
        score = 0

        while True:
            if show_result and episode % 1000 == 0:
                env.render()
            action, grad = policy_gradient(state, weight)
            state, reward, terminated, truncated, _ = env.step(action)
            grads.append(grad)
            rewards.append(reward)
            score += reward
            if terminated or truncated:
                break

        for i, grad in enumerate(grads):
            future = rewards[i:]
            gt = sum(np.array(future) * gamma ** np.arange(len(future)))
            weight += alpha * grad * gt

        scores.append(score)
        print("Episode: {} Score: {}".format(episode, score))

    return scores
