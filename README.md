# Test-Time-Compute Routing Agent

## Project name and one-line description

Run extented thinking (test-time-compute) on difficult problems outperforming o3-mini-high, o1, and r1 using just llama-3.3-70b, while running quick thinking on simple problems; and use web3 tools (agentkit).

## Problem statement and solution approach

Foundational models haven't improved in the last 2 years (since gpt-4). gpt-4.5 is 10x the parameters (18T) but not much improvement with metrics. The latest improvements (o3,o1,r1,sonnet,s1) were due to additional computational resources during the inference, called test-time-compute (ttc). TTC is highly centralized (o3,o1,sonnet) and r1 has limited performance and demands high resources to be properly decentralize. People and agent should have access to smart competitive models!!

We solve this buy creating and agent that figures out when the extra resources are needed and runs our innovative model based that is using test-time-compute and is beating SOTA.

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

- marketplace for TTC that can be used with any model
- more TTC like graph-of-though, tree-of-thougt
