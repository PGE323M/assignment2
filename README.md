# Assignment 2

[![Assignment 2 tests](https://github.com/PGE323M/assignment2/actions/workflows/main.yml/badge.svg)](https://github.com/PGE323M/assignment2/actions/workflows/main.yml)

## Learning objectives

In this assignment you will:

- implement and test three small Python functions;
- use a default function argument;
- keep track of physical units and apply a conversion factor; and
- learn how a repository-level `AGENTS.md` file gives an AI agent persistent instructions.

Complete the functions in [`assignment2.py`](assignment2.py). Do not change function names or argument order.

## Problem 1: Squaring a value

Complete `square(a)` so that it returns the square of `a`.

## Problem 2: Forward finite difference

Given

$$
x(t) = 5t,
$$

complete `finite_diff(t, delta_t)` so that it estimates the first derivative using

$$
\frac{\partial x}{\partial t}
\approx
\frac{x(t + \Delta t) - x(t)}{\Delta t}.
$$

The value of $\Delta t$ is supplied through the `delta_t` argument.

## Problem 3: Initial well rate

Complete `well(J, Pi, Pwf=2000)` so that it returns the initial production rate in BBL/day.

- `J` is the productivity index in ft³/(psi-day).
- `Pi` is the initial reservoir pressure in psi.
- `Pwf` is the flowing bottom-hole pressure in psi.
- If `Pwf` is omitted, it must default to 2000 psi.

Use

$$
q_w = J(P_i-P_{wf})
$$

and the conversion $1\ \text{ft}^3 = 0.1781\ \text{BBL}$.

## Working with the agent

This repository includes [`AGENTS.md`](AGENTS.md). That file contains standing instructions that an agent loads whenever it works in this repository. It turns the longer submission prompt from Assignment 1 into a short, repeatable command.

Before writing code:

1. Open and read `AGENTS.md`.
2. Start a fresh Copilot chat and ask: `What repository instructions apply to this assignment?`
3. Confirm that the response describes the guarded `submit assignment` workflow.

For implementation, begin with a bounded planning request:

> Read README.md and test.py. Explain the contract, units, and useful edge cases for each function in assignment2.py. Do not edit any files yet.

After reviewing the plan, you may authorize the agent to edit only `assignment2.py`. Inspect its diff and reasoning before accepting the work.

## Testing

Run the public tests from the repository root:

```bash
python -m unittest -v test.py
```

Passing public tests are necessary but not sufficient evidence. Check the function contracts, the default argument, and the units yourself.

## Submission

When `assignment2.py` is complete and the tests pass, start a fresh agent chat and say:

> submit assignment

The agent must follow `AGENTS.md`: it checks the repository state, runs the tests, stages only `assignment2.py`, commits, pushes, and verifies the result. Independently confirm the new commit and the GitHub Actions result.
