# Figures for White Paper: Reinforcement Learning Environment for Agentic AI

This document describes the illustrative figures generated for the white paper.
All figures are saved in the `/Users/fei/.openclaw/workspace/rl-paper/figures/` directory.

---

## Figure 1: From LLM-RL to Agentic RL - The MDP to POMDP Transition
**File**: `fig1_mdp_to_pomdp_transition.png`

**Description**: 
A side-by-side comparison illustrating the fundamental paradigm shift from conventional LLM-RL to Agentic RL.

**Left Panel - Conventional LLM-RL (MDP)**:
- Static text prompt as input
- Vocabulary tokens as action space
- Single-step horizon (H=1)
- Immediate reward based on preference
- Open-loop generation

**Right Panel - Agentic RL (POMDP)**:
- Dynamic environment state
- Observation history as memory
- Expanded action space (language + tools)
- Multi-turn horizon (H ≫ 1)
- Cumulative discounted reward
- Closed-loop interaction

**Usage**: Section 1 (Introduction) and Section 2 (Theoretical Framework)

---

## Figure 2: Expanded Action Space (ExpA) Concept
**File**: `fig2_expanded_action_space.png`

**Description**:
A flowchart illustrating the three-component action space that decouples reasoning from execution.

**Components**:
1. **Language Actions (𝒜_lang)**: Internal reasoning, chain-of-thought, natural language processing
2. **Routing Actions (𝒜_route)**: Environment selection and context switching
3. **Environment Actions (𝒜_env)**: Tool execution, API calls, code execution

**Connected Environments**:
- Web Browser (navigate, click, type, scroll)
- Code Interpreter (write_file, execute, debug)
- Calculator (compute, store, recall)
- Database (query, insert, update)

**Usage**: Section 2.2 (Expanded Action Spaces)

---

## Figure 3: Taxonomy of Agentic Capabilities
**File**: `fig3_agentic_capabilities_taxonomy.png`

**Description**:
A radial diagram showing the five core agentic capabilities and their sub-components.

**Capabilities**:
1. **Planning**: Task decomposition, goal setting, replanning
2. **Tool Use**: API calling, code execution, environment manipulation
3. **Memory**: Short-term (context window), long-term (vector DB), episodic (experience replay)
4. **Self-Improvement**: Learning from feedback, error recognition, iterative refinement
5. **Reasoning**: Chain-of-thought, verification, logical deduction

**Usage**: Section 3 (Taxonomy of Agentic Capabilities)

---

## Figure 4: Agentic RL Ecosystem Stack
**File**: `fig4_agentic_rl_ecosystem_stack.png`

**Description**:
A layered architecture diagram showing the complete technology stack for Agentic RL.

**Layer 1 - Infrastructure**:
- Docker containers
- Compute resources (GPU/TPU)
- Cloud platforms

**Layer 2 - Environment Frameworks**:
- OpenEnv (Meta/HuggingFace)
- GEM (General Experience Maker)
- MCP (Model Context Protocol)
- BrowserGym, CodeEnv

**Layer 3 - Training Libraries**:
- Agent-Lightning (Microsoft)
- NVIDIA NeMo RL
- OpenAI Agents SDK
- RLlib, Tianshou

**Layer 4 - Agent Models**:
- Kimi K2.5 (Agent Swarm)
- OpenClaw (OS of Agents)
- Claude Code
- OpenAI Operator

**Usage**: Section 4 (Open-Source Packages)

---

## Figure 5: Synthetic Environment Generation Pipeline
**File**: `fig5_synthetic_environment_pipeline.png`

**Description**:
A process flow diagram showing the 5-step pipeline for generating synthetic training environments.

**Steps**:
1. **Schema Generation**: Define database schemas and data structures
2. **Synthetic Data Population**: Generate realistic sample data
3. **Tool Interface Definition**: Create API schemas and tool specifications
4. **Task Generation**: Create verifiable goals and evaluation criteria
5. **Environment Packaging**: Bundle into deployable environment

**Examples**: Agent World Model (AWM), Reasoning Gym (RG)

**Usage**: Section 7 (Synthetic Environment Generation)

---

## Figure 6: Credit Assignment Algorithms Comparison
**File**: `fig6_credit_assignment_algorithms.png`

**Description**:
A comparison diagram of four key algorithms for long-horizon credit assignment.

**Algorithms**:
1. **GRPO** (Group Relative Policy Optimization)
   - Critic-free design
   - Group-based advantage estimation
   - Reduces memory footprint

2. **HGPO** (Hierarchical Group Policy Optimization)
   - Hierarchical grouping
   - Context consistency preservation
   - Multi-level abstraction

3. **HCAPO** (Hindsight Credit Assignment)
   - LLM-as-post-hoc-critic
   - Dense supervision signals
   - Hindsight reasoning

4. **SHADOW** (Dynamics-Aware State Grouping)
   - State similarity grouping
   - Prevents misleading comparisons
   - Dynamics-aware weighting

**Usage**: Section 8 (Algorithmic Advancements)

---

## Figure 7: The Sim-to-Real Gap
**File**: `fig7_sim_to_real_gap.png`

**Description**:
A visual representation of the reality gap between simulated training and real-world deployment.

**Left Side - Simulated Environment**:
- Cooperative AI assistant
- Complete information provided
- Uniformly positive feedback
- USI Score: ~76

**Right Side - Real World**:
- Confused human users
- Partial information
- Adversarial conditions
- USI Score: ~93

**Gap Analysis**:
- Behavioral Gap: Excessive cooperativeness, information front-loading
- Evaluative Gap: Simplified scoring vs. nuanced judgment

**Usage**: Section 9 (Sim-to-Real Gap)

---

## Figure 8: Evolution Timeline of Agentic AI (2022-2027)
**File**: `fig8_agentic_ai_timeline.png`

**Description**:
A timeline showing the progression of Agentic AI from early LLM-RL to future production deployment.

**Milestones**:
- **2022**: LLM-RL (RLHF) - Preference-based fine-tuning
- **2023**: Tool Use Emergence - ChatGPT plugins, function calling
- **2024**: Agent Frameworks - OpenClaw, LangChain, AutoGPT
- **2025**: Synthetic Environments - AWM, Reasoning Gym
- **2026**: Agent Swarms - Kimi K2.5 PARL, multi-agent coordination
- **2027**: Production Deployment - Enterprise-ready agents

**Trend**: Upward trajectory toward ASI

**Usage**: Section 1 (Introduction) or Section 11 (Conclusion)

---

## LaTeX Integration

To include these figures in your LaTeX document for arXiv submission:

```latex
\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.9\textwidth]{figures/fig1_mdp_to_pomdp_transition.png}
    \caption{The transition from conventional LLM-RL (single-step MDP) to Agentic RL (multi-turn POMDP).}
    \label{fig:mdp-to-pomdp}
\end{figure}
```

For two-column layout:
```latex
\begin{figure*}[htbp]
    \centering
    \includegraphics[width=0.8\textwidth]{figures/fig4_agentic_rl_ecosystem_stack.png}
    \caption{The Agentic RL ecosystem stack showing the four-layer architecture.}
    \label{fig:ecosystem-stack}
\end{figure*}
```

---

## Figure Placement Recommendations

| Figure | Recommended Section | Page Position |
|--------|---------------------|---------------|
| fig1_mdp_to_pomdp_transition.png | Section 1-2 | Top of page |
| fig2_expanded_action_space.png | Section 2.2 | Full width |
| fig3_agentic_capabilities_taxonomy.png | Section 3 | Column width |
| fig4_agentic_rl_ecosystem_stack.png | Section 4 | Full width |
| fig5_synthetic_environment_pipeline.png | Section 7 | Full width |
| fig6_credit_assignment_algorithms.png | Section 8 | Full width |
| fig7_sim_to_real_gap.png | Section 9 | Column width |
| fig8_agentic_ai_timeline.png | Section 1 or 11 | Full width |

---

## Image Specifications

- **Format**: PNG
- **Resolution**: 1024x1024, 1024x1536, or 1536x1024 (OpenAI generated)
- **Color Scheme**: Professional academic colors (blue, gray, white backgrounds)
- **Style**: Clean, minimal, technical illustration
- **Font**: Sans-serif, readable at print resolution

---

*Generated for: "Reinforcement Learning Environment for Agentic AI: From Theory to Practice"*
*Date: March 24, 2026*
