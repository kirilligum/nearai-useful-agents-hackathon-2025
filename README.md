# Test-Time-Compute Routing Agent

Video: [https://youtu.be/lam-6aUwTUE](https://youtu.be/lam-6aUwTUE)

- test-time-compute agent
  - based on s1 paper
  - 'wait, check your reasoning' x8
  - solves "how many 'r's are in 'strawberry'?" and GPQA Diamond where o3 fails
- routing agent: ttc, simple, or web3 (agentKit)
- benchmarks
- deployed, running, ready for customization

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

### Benchmark suite and evaluation metrics

see [https://app.near.ai/evaluations](https://app.near.ai/evaluations) agent `8c5f182867abaeb61756c63da5f4fd30cc84ddfc907bb158d45773e1f7c8662d/ttc-kirill-wait-0/0.0.1` scoring 77% on mmlu100

our thinking model beats o3-mini-high and can solve

```
For multi-Higgs-doublet models, do the Breit-Weigner corrections of the Oblique Parameters provide a better constraint on New Physics than the Original Oblique Parameters?
```

from GPQA Diamond dataset that o3-mini-high can't solve

our models solves using ttc: [https://app.near.ai/agents/8c5f182867abaeb61756c63da5f4fd30cc84ddfc907bb158d45773e1f7c8662d/ttc-kirill-wait-8/latest/run?threadId=thread_129fd4aef4374392ae8522a2](https://app.near.ai/agents/8c5f182867abaeb61756c63da5f4fd30cc84ddfc907bb158d45773e1f7c8662d/ttc-kirill-wait-8/latest/run?threadId=thread_129fd4aef4374392ae8522a2)

o3-mini-high answer:

```
...
Our
Thus, the answer is model-dependent: they provide a better constraint when the new states’ widths and proximity to resonances cannot be ignored, but they are not universally superior.
```

#### Defined success metrics for each task the agent performs

#### Quantitative performance measurements

#### Reproducible testing environment

#### Comparison against baseline approaches

#### Error rate analysis

#### Task completion time metrics

#### Resource utilization measurements

## Setup and installation instructions

Follow NEAR AI docs to install the agents mentionned above
[https://docs.near.ai/agents/quickstart/](https://docs.near.ai/agents/quickstart/)

For CDP integration, use [https://github.com/nearai/nearai_langchain/tree/main/examples/cdp_langchain_chatbot](https://github.com/nearai/nearai_langchain/tree/main/examples/cdp_langchain_chatbot)

## Future development roadmap

- marketplace for TTC that can be used with any model
- more TTC like graph-of-though, tree-of-thougt
