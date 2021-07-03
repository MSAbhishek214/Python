from scipy.stats import norm


def get_cumulative_expectation(rewards, count):
    pr = [val/sum(count) for val in count]
    n = len(count)
    cex = 0
    for idx in range(n):
        cex = cex + rewards[idx] * pr[idx]
    return cex


# probability computations
rewards = norm.rvs(size=10)
count = norm.rvs(size=10)

cum_rewards = get_cumulative_expectation(rewards, count)
print(cum_rewards)
