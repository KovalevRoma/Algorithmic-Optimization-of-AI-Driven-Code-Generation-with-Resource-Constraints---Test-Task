```latex
\documentclass[a4paper,12pt]{article}

% Encoding and Language Support
\usepackage[utf8]{inputenc}
\usepackage[T2A]{fontenc}
\usepackage[russian,english]{babel}

% Math and Symbols
\usepackage{amsmath}
\usepackage{amssymb}

% Graphics and Plots
\usepackage{graphicx}
\usepackage{pgfplots}

% Page Layout
\usepackage{geometry}
\geometry{margin=1in}

% Fancy Headers and Footers
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{ECON101 Assignment}
\fancyhead[R]{Absolute and Comparative Advantage}
\fancyfoot[C]{\thepage}

% Section Formatting
\usepackage{titlesec}
\titleformat{\section}{\large\bfseries}{\thesection}{1em}{}
\titleformat{\subsection}{\normalsize\bfseries}{\thesubsection}{1em}{}

% Hyperlinks
\usepackage{hyperref}

% Caption Formatting
\usepackage{caption}

% Title and Author Information
\title{
    \vspace{-2cm}
    \textbf{Algorithmic Optimization of AI Driven Code Generation with Resource Constraints\\[0.5em] Test Task}}
\author{Roman Kovalev}
\date{December 2025}

\begin{document}

\maketitle

\vspace{-1cm}
\section*{Repository Contents:}
\begin{itemize}
    \item The file `$calc\_possibilities.py$` demonstrates the distribution of probabilities after $S \cdot \log(S)$ steps during a random walk on a plane. Run the file in the terminal with the command `python3 calc_possibilities.py`, then input the field dimensions separated by a space. The output will be a matrix of the specified size containing probabilities for each cell after $S \cdot \log(S)$ steps.
    \item The file `$random\_walk.py$` contains a random walk generator and visualizes it. Run the file in the terminal with the command `python3 random_walk.py`, then input the field dimensions. The program outputs a sample path between the two most distant points on the field (bottom-left and center).

\end{itemize}

\section*{Solution}
First, note that it does not matter where we start. Due to symmetry (teleports), we can assume that we always start from the bottom-left corner of our area.

The core of the solution is as follows:  
After each step, we randomly choose a direction to move—one of four with equal probability: right/left/up/down.

It turns out that after $S \cdot \log(S)$ steps, for any two cells in the field, the probabilities of being in them will equalize and stop changing (except in cases where the field dimensions are even, in which case the probability is evenly distributed among cells with the same "parity"). After this, on average, within $S$ steps, we should reach the target cell containing the apple.

Thus, the required number of steps for the algorithm is approximately:
$$S \cdot \log(S) + S \approx S \cdot 15 < 35S\text{, since }S \leq 10^6$$

The above is valid provided that the field dimensions are greater than 2. Otherwise, the given number of steps will not suffice. Therefore, for the final solution, it may be necessary to change the strategy: we will choose the direction of movement uniformly, taking into account our previous move. With a probability of $\frac{1}{3}$, we will choose a direction different from the one chosen in the previous step. This will allow us to evenly distribute steps between vertical and horizontal directions, which, by doubling the number of steps, will achieve the desired uniform probability distribution.

\end{document}
```

