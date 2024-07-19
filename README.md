# Welcome!
## This repository is intended to:
- provide tools for Online Learning methodologies;
- provide trading applications thanks to a GBM-like synthetic stream of financial data;
- provide Notebooks for immediate visualization of the testing phases.

## This repository is NOT intended to:
- provide brand new methodologies for trading strategies. In fact, the current scope is only related to the implementation of state-of-art methods.

## Current State of the Work:
- In the __Benchmarks__ folder you can find:
  - __agent.py__, which includes the classes "portfolio" and "stream" to properly return RL-like losses/rewards and simulate a financial environment, respectively;
  - __benchmarks.py__, which includes the UCB, TS, and BuyAndHold classes to provide Online Learning models;
  - __Benchmark_Testing.ipynb__, which shows the performance of the above methodologies.
    
  Note that:
  - To put the algorithms to the test, a small time horizon is largely sufficient. Moreover, fast convergence is one of the key aspects for incremental learning purposes. If the aim is to provide operationally decent algorithms, we cannot allow for significant losses during the initial phase of convergence;
  - Many useful extensions for the above-mentioned methods are already implemented here: https://github.com/PaoloBiolghini/OnlineLearningProject. 

__Thank you for your attention__. Feel free to contact me for any issue, doubt or comment.
Michele Sparviero
