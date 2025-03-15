# Test-Time-Compute Routing Agent

## Project name and one-line description

Run extented thinking (test-time-compute) on difficult problems outperforming o3-mini-high, o1, and r1 using just llama-3.3-70b, while running quick thinking on simple problems; and use web3 tools (agentkit).

## Problem statement and solution approach

## Agents

### ttc-kirill-picker

The main routing agents that decides if it is a simple question, blockchain interaction (cdp-agentkit) question, or reasoning and thinking question. Then it routs the questio to the appropriate agents

[https://app.near.ai/agents/8c5f182867abaeb61756c63da5f4fd30cc84ddfc907bb158d45773e1f7c8662d/ttc-kirill-picker/latest](https://app.near.ai/agents/8c5f182867abaeb61756c63da5f4fd30cc84ddfc907bb158d45773e1f7c8662d/ttc-kirill-picker/latest)

### ttc-kirill-wait-8

This is the inovative test-time-compute agent based on the ideas of s1 paper. After getting an answer it querries `wait, check the reasoning` 8 times and gets better result than o3-mini-high using just llama-3.3-70b

[https://app.near.ai/agents/8c5f182867abaeb61756c63da5f4fd30cc84ddfc907bb158d45773e1f7c8662d/ttc-kirill-wait-8/latest](https://app.near.ai/agents/8c5f182867abaeb61756c63da5f4fd30cc84ddfc907bb158d45773e1f7c8662d/ttc-kirill-wait-8/latest)

### agentkit-kirill

This agent is based on cdp-agentkit and interacts with blockchain

[https://app.near.ai/agents/8c5f182867abaeb61756c63da5f4fd30cc84ddfc907bb158d45773e1f7c8662d/agentkit-kirill/latest](https://app.near.ai/agents/8c5f182867abaeb61756c63da5f4fd30cc84ddfc907bb158d45773e1f7c8662d/agentkit-kirill/latest)

## Technical architecture overview

## Quantative benchmarks and agent performance

Our

### Benchmark suite and evaluation metrics

​Defined success metrics for each task the agent performs
​Quantitative performance measurements
​Reproducible testing environment
​Comparison against baseline approaches
​Error rate analysis
​Task completion time metrics
​Resource utilization measurements

## Setup and installation instructions

## Future development roadmap
