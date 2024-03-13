# Question:
# Given a stochastic matrix representing probabilities of moving from one health state to another in 1 year,
# and an initial distribution of individuals across health states, determine the percentage of individuals
# in each health state after 1 year.

import numpy as np

# Initial state vector
X = np.array([[0.85, 0.10, 0.05, 0]])

# Transition matrix
P = np.array([[0.90, 0.07, 0.02, 0.01],
              [0, 0.93, 0.05, 0.02],
              [0, 0, 0.85, 0.15],
              [0, 0, 0, 1.00]])

# Compute the new state vector after 1 year
# print(P.T)
# print(X.T)
print(X.shape)
print(P.shape)

Y = P.T @ X.T

print("Percentage in each health state after 1 year:")
print("Asymptomatic:", Y[0][0]*100, "%")
print("Symptomatic:", Y[1][0]*100, "%")
print("AIDS:", Y[2][0]*100, "%")
print("Death:", Y[3][0]*100, "%")
