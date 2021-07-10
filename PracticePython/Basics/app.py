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

#dynamic programming

def fibonacci_dynamic_programming(n):
    a = []
    a.append(0)
    a.append(1)
    for i in range(2, n+1):
        print(i, i-1, i-2)
        a.append(a[i-1] + a[i-2])
        print(a[i])
    print(a)

#call the function

fibonacci_dynamic_programming(5)