# Algorithmic Optimization of AI-Driven Code Generation with Resource Constraints

**Author:** Roman Kovalev  
**Date:** December 2025  

---

## Repository Contents

- **`calc_possibilities.py`**  
  This file demonstrates the distribution of probabilities after S * log(S) steps during a random walk on a plane.  
  **How to use:**
  1. Run the file in the terminal with the command:  
     ```bash
     python3 calc_possibilities.py
     ```
  2. Enter the field dimensions separated by a space.  
  **Output:**  
  A matrix of the specified size, containing the probabilities of being in each cell after S*log(S) steps.

- **`random_walk.py`**  
  This file contains a random walk generator and visualizes it.  
  **How to use:**
  1. Run the file in the terminal with the command:  
     ```bash
     python3 random_walk.py
     ```
  2. Enter the field dimensions.  
  **Output:**  
  A sample path between the two most distant points on the field (bottom-left and center).

---

## Solution

To begin with, the starting point does not matter. Due to symmetry (teleports), we can always assume that the starting point is the bottom-left corner of the field.

### Key Idea

At each step, we randomly choose a direction—one of four (right/left/up/down)—with equal probability.  

After S*log(S) steps:
- The probabilities of being in any two cells of the field will equalize and stop changing.  
- **Exception:** If the field dimensions are even, the probabilities will distribute evenly among cells with the same parity.

On average, within S additional steps, the target cell containing the apple will be reached.

### Required Steps

The total number of steps required by the algorithm can be approximated as:  

$$S *\log(S) + S \approx S*15 < 35S$$, since $$S \leqslant 10^6 $$


### Special Case: Small Fields

If the field dimensions are <= 2, the above number of steps will not suffice.  
**Alternative Strategy:**
1. At each step, select a direction uniformly, considering the previous move.
2. With a probability of 1/3, choose a direction different from the one in the previous step.

This adjustment ensures a balanced distribution of steps between vertical and horizontal movements, achieving the desired uniform probability distribution by doubling the number of steps.

---

