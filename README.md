# My-LLM

Personal learning lab: (1) build a tiny GPT from scratch to understand LLM
fundamentals, (2) build and evaluate real AI systems (RAG, tools, evals, APIs).

## Setup
Python 3.11. Note: Intel Mac -> torch pinned to 2.2.2 (last release with x86 macOS wheels), numpy<2.

    python3 -m venv .venv && source .venv/bin/activate
    pip install -r requirements.txt
    pytest

## Layout
src/fundamentals (Project 1), notebooks/, tests/, reports/, docs/ (experiment log).
