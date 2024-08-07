import numpy as np
from collections import deque

class portfolio:
  def __init__(self, initial_position = 0, initial_price=None):
    self.profit = 0
    self.ptf = initial_position
    self.prices = deque(maxlen=2)
    if initial_price is not None:
      self.prices.append(initial_price)

  def update(self, arm, next_price):
    self.ptf += arm
    self.prices.append(next_price)
    if len(self.prices)==1:
      r = 0
    else:
      r = arm*(self.prices[-1]-self.prices[0])
    self.profit += r
    return r

class stream:
    def __init__(self, dt = 1/252, seed = 0):
      np.random.seed(seed)
      self.mu = np.random.uniform(-0.5, 0.5, 1)
      self.sigma = np.random.uniform(0.001, 0.5, 1)
      self.dt = dt

      self.ret = self.mu*self.dt + self.sigma*np.sqrt(self.dt)*np.random.normal(0, 1, 1)

    def update(self):
      self.ret = self.ret + self.mu*self.dt + self.sigma*np.sqrt(self.dt)*np.random.normal(0, 1, 1)
      return 100*np.exp(self.ret).item()
