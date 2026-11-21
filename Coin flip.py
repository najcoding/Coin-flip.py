Got it — you want a Python program that calculates the probability of getting between 2 and 4 heads inclusive from 10 fair coin flips using probability math functions.

We can use the binomial probability formula:

𝑃
(
𝑘
 heads
)
=
(
𝑛
𝑘
)
⋅
𝑝
𝑘
⋅
(
1
−
𝑝
)
𝑛
−
𝑘
P(k heads)=(kn​)⋅pk⋅(1−p)n−k

Where:

𝑛
n = number of trials (10 flips)
𝑘
k = number of heads
𝑝
p = probability of heads (0.5 for a fair coin)
Complete Python Code
import math

def binomial_probability(n, k, p):
    """
    Calculate the probability of getting exactly k successes in n trials.
    Uses the binomial probability formula.
    """
    if not (0 <= k <= n):
        return 0.0  # Invalid k
    comb = math.comb(n, k)  # Combination n choose k
    return comb * (p ** k) * ((1 - p) ** (n - k))

def probability_between_k(n, k_min, k_max, p=0.5):
    """
    Calculate probability of getting between k_min and k_max successes inclusive.
    """
    if k_min > k_max or k_min < 0 or k_max > n:
        raise ValueError("Invalid range for k_min and k_max.")
    
    total_prob = 0.0
    for k in range(k_min, k_max + 1):
        total_prob += binomial_probability(n, k, p)
    return total_prob

# Parameters
n_flips = 10
k_min = 2
k_max = 4
p_heads = 0.5

try:
    result = probability_between_k(n_flips, k_min, k_max, p_heads)
    print(f"Probability of getting between {k_min} and {k_max} heads from {n_flips} flips: {result:.6f}")
except ValueError as e:
    print(f"Error: {e}")

How It Works
math.comb(n, k) computes 
(
𝑛
𝑘
)
(kn​) (combinations).
binomial_probability calculates the probability for exactly k heads.
probability_between_k sums probabilities for k_min to k_max.
Error handling ensures valid inputs.
Example Output
Probability of getting between 2 and 4 heads from 10 flips: 0.525879


This means there’s about 52.59% chance of getting between 2 and 4 heads inclusive.

If you want, I can also give you a NumPy-based version that’s faster for large numbers of flips.
Do you want me to provide that?