# List of Figures for White Paper

## Figure 1: From LLM-RL to Agentic RL - The MDP to POMDP Transition
**Placement**: Section 1 (Introduction) or Section 2 (Theoretical Framework)

**Caption**: 
"The fundamental paradigm shift from conventional LLM-RL to Agentic RL. (Left) Conventional LLM-RL operates as a single-step MDP with static prompts, vocabulary-only actions, and immediate rewards. (Right) Agentic RL formalizes interaction as a multi-turn POMDP with dynamic states, expanded action spaces including tool use, and cumulative rewards over extended horizons."

---

## Figure 2: Expanded Action Space (ExpA) Architecture
**Placement**: Section 2.2 (Expanded Action Spaces)

**Caption**:
"The Expanded Action Space (ExpA) framework decouples reasoning from execution through three action types. Language actions ($\mathcal{A}_{lang}$) support internal reasoning; routing actions ($\mathcal{A}_{route}$) select environments; environment actions ($\mathcal{A}_{env}$) execute tools and APIs. This architecture enables modular, composable agent systems."

---

## Figure 3: Taxonomy of Agentic Capabilities
**Placement**: Section 3 (Taxonomy of Agentic Capabilities and Task Domains)

**Caption**:
"A taxonomy of the five core agentic capabilities required for autonomous operation: Planning (decomposition, goal setting, replanning), Tool Use (API calling, code execution), Memory (short-term, long-term, episodic), Self-Improvement (learning from feedback, error recognition), and Reasoning (chain-of-thought, verification)."

---

## Figure 4: Agentic RL Ecosystem Stack
**Placement**: Section 4 (Open-Source Packages and Development Frameworks)

**Caption**:
"The four-layer architecture of the Agentic RL ecosystem. Infrastructure Layer provides containerized compute; Environment Layer (OpenEnv, GEM, MCP) standardizes agent-environment interfaces; Training Layer (Agent-Lightning, NeMo RL, OpenAI SDK) orchestrates learning; Agent Layer deploys production systems (Kimi K2.5, OpenClaw, Claude Code)."

---

## Figure 5: Synthetic Environment Generation Pipeline
**Placement**: Section 7 (Synthetic Environment Generation)

**Caption**:
"The five-step pipeline for generating synthetic training environments. Starting from schema definition, the pipeline progresses through data population, tool interface creation, task generation with verifiable goals, and final environment packaging. Examples include Agent World Model (AWM) and Reasoning Gym (RG)."

---

## Figure 6: Credit Assignment Algorithms for Long-Horizon RL
**Placement**: Section 8 (Algorithmic Advancements and Credit Assignment)

**Caption**:
"Comparison of four key algorithms addressing the credit assignment problem in long-horizon Agentic RL. GRPO eliminates the critic through group-relative advantage; HGPO maintains context consistency via hierarchical grouping; HCAPO leverages LLM-as-critic for hindsight reasoning; SHADOW uses dynamics-aware state grouping to prevent misleading comparisons."

---

## Figure 7: The Sim-to-Real Gap in User Simulation
**Placement**: Section 9 (The Sim-to-Real Gap and User Simulation)

**Caption**:
"The reality gap between simulated training environments and real-world deployment. Simulated environments (USI ~76) exhibit excessive cooperativeness and uniformly positive feedback, while real-world interactions (USI ~93) involve partial information and nuanced judgment. This gap comprises behavioral differences (information front-loading) and evaluative differences (scoring simplification)."

---

## Figure 8: Evolution Timeline of Agentic AI (2022-2027)
**Placement**: Section 1 (Introduction) or Section 11 (Conclusion)

**Caption**:
"The evolution of Agentic AI from 2022 to 2027, showing key milestones: LLM-RL with RLHF (2022), emergence of tool use capabilities (2023), development of agent frameworks like OpenClaw (2024), synthetic environment generation with AWM and RG (2025), agent swarm architectures like Kimi K2.5 (2026), and production deployment readiness (2027)."

---

## LaTeX Figure Environment Templates

### Single Column Figure
```latex
\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.48\textwidth]{figures/fig3_agentic_capabilities_taxonomy.png}
    \caption{Taxonomy of the five core agentic capabilities required for autonomous operation.}
    \label{fig:capabilities}
\end{figure}
```

### Full Width Figure (Two-Column Layout)
```latex
\begin{figure*}[htbp]
    \centering
    \includegraphics[width=0.9\textwidth]{figures/fig4_agentic_rl_ecosystem_stack.png}
    \caption{The four-layer architecture of the Agentic RL ecosystem.}
    \label{fig:ecosystem}
\end{figure*}
```

### Side-by-Side Figures
```latex
\begin{figure}[htbp]
    \centering
    \begin{subfigure}[b]{0.48\textwidth}
        \includegraphics[width=\textwidth]{figures/fig1_mdp_to_pomdp_transition.png}
        \caption{MDP to POMDP transition}
        \label{fig:mdp-pomdp}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.48\textwidth}
        \includegraphics[width=\textwidth]{figures/fig2_expanded_action_space.png}
        \caption{Expanded Action Space}
        \label{fig:expa}
    \end{subfigure}
    \caption{Theoretical foundations of Agentic RL.}
    \label{fig:theory}
\end{figure}
```

---

## Figure Placement Guidelines

| Figure | Section | Position | Width |
|--------|---------|----------|-------|
| fig1_mdp_to_pomdp_transition.png | Sec 1-2 | Top of page | 0.9\textwidth |
| fig2_expanded_action_space.png | Sec 2.2 | Full width | 0.9\textwidth |
| fig3_agentic_capabilities_taxonomy.png | Sec 3 | Column | 0.48\textwidth |
| fig4_agentic_rl_ecosystem_stack.png | Sec 4 | Full width (span) | 0.9\textwidth |
| fig5_synthetic_environment_pipeline.png | Sec 7 | Full width | 0.9\textwidth |
| fig6_credit_assignment_algorithms.png | Sec 8 | Full width | 0.9\textwidth |
| fig7_sim_to_real_gap.png | Sec 9 | Column | 0.48\textwidth |
| fig8_agentic_ai_timeline.png | Sec 1/11 | Full width | 0.9\textwidth |

---

## Required LaTeX Packages

Add to your preamble:
```latex
\usepackage{graphicx}
\usepackage{subcaption}  % For subfigures
\usepackage{stfloats}    % For spanning figures in two-column layout
```

---

*Generated for: "Reinforcement Learning Environment for Agentic AI: From Theory to Practice"*
