# 2. Theoretical Framework: From LLM-RL to Agentic RL

The transition to Agentic Reinforcement Learning represents a fundamental reconceptualization of how large language models interact with their environment. This section establishes the mathematical formalism underlying this paradigm shift, contrasting the degenerate single-step MDP framework of conventional LLM-RL with the temporally extended POMDP formulation of Agentic RL. We introduce the Expanded Action Space (ExpA) concept as a theoretical mechanism for decoupling reasoning from action execution.

## 2.1 MDP vs. POMDP Formalism

### 2.1.1 Conventional LLM-RL: The Degenerate MDP

Traditional reinforcement learning for large language models, typically instantiated as Preference-Based Reinforcement Fine-Tuning (PBRFT), operates within a constrained mathematical framework that can be characterized as a degenerate, single-step Markov Decision Process. In this formulation, the horizon length $H = 1$, reducing the sequential decision-making problem to an isolated prediction task.

**Definition 2.1 (Conventional LLM-RL MDP).** The standard LLM-RL framework is defined as a tuple $\mathcal{M}_{\text{LLM}} = (\mathcal{S}, \mathcal{A}, \mathcal{T}, \mathcal{R}, \gamma)$ where:

- **State space** $\mathcal{S}$: Consists of static text prompts $s \in \mathcal{S}$, where each prompt represents a fixed context with no temporal evolution.

- **Action space** $\mathcal{A} = \mathcal{V}$: The vocabulary tokens, where $a_t \in \mathcal{V}$ represents the next token prediction.

- **Transition function** $\mathcal{T}(s' | s, a) = \delta(s' - s)$: The environment state remains static; the prompt does not change based on the model's output.

- **Reward function** $\mathcal{R}(s, a)$: Typically derived from human preference models or reward models trained on preference data, providing a scalar signal $r \in \mathbb{R}$.

- **Discount factor** $\gamma$: Usually irrelevant for single-step decisions ($\gamma \in [0, 1]$).

The objective in this framework reduces to maximizing immediate reward:

$$\pi^* = \arg\max_{\pi} \mathbb{E}_{s \sim \mathcal{D}, a \sim \pi(\cdot|s)}[\mathcal{R}(s, a)]$$

This formulation treats the LLM as an open-loop generator, where each response is produced without consideration of future interactions or the consequences of its outputs on subsequent states.

### 2.1.2 Agentic RL: The POMDP Formulation

Agentic RL reframes the interaction between language models and their environment as a temporally extended Partially Observable Markov Decision Process (POMDP), capturing the essential characteristics of autonomous agency: persistent state, partial information, and long-horizon planning.

**Definition 2.2 (Agentic RL POMDP).** The Agentic RL framework is defined as a POMDP $\mathcal{P} = (\mathcal{S}, \mathcal{A}, \mathcal{T}, \mathcal{R}, \Omega, \mathcal{O}, \gamma, H)$ where:

- **State space** $\mathcal{S}$: The environment state $s_t \in \mathcal{S}$ evolves dynamically based on agent actions and external dynamics. Unlike the static prompts of LLM-RL, these states represent the complete configuration of the world.

- **Action space** $\mathcal{A}$: Expanded beyond vocabulary tokens to include tool invocations, API calls, and environment manipulations (detailed in Section 2.2).

- **Transition function** $\mathcal{T}(s_{t+1} | s_t, a_t)$: Governs how the environment state evolves in response to agent actions, capturing the causal structure of the world.

- **Reward function** $\mathcal{R}(s_t, a_t, s_{t+1})$: Provides task-specific feedback, often sparse and delayed, indicating progress toward objectives.

- **Observation space** $\Omega$: The agent does not directly observe the full state $s_t$ but receives observations $o_t \in \Omega$ through the observation function.

- **Observation function** $\mathcal{O}(o_t | s_t, a_{t-1})$: Defines the probability of observing $o_t$ given the current state and previous action, formalizing partial observability.

- **Discount factor** $\gamma \in [0, 1)$: Determines the present value of future rewards.

- **Horizon** $H \gg 1$: The episode length extends over multiple interaction steps.

### 2.1.3 State Space: Environment State and Agent Memory

A critical distinction between LLM-RL and Agentic RL lies in the composition of the agent's effective state. In the POMDP formulation, the agent maintains an internal representation that aggregates information across the interaction history.

**Definition 2.3 (Agent Information State).** At time $t$, the agent's information state $h_t$ encompasses the complete history of prior interactions:

$$h_t = (o_0, a_0, o_1, a_1, \ldots, o_{t-1}, a_{t-1}, o_t) \in \mathcal{H}_t$$

where $\mathcal{H}_t = (\Omega \times \mathcal{A})^t \times \Omega$ represents the space of all possible histories of length $t$.

The agent's policy $\pi(a_t | h_t)$ conditions on this history rather than the current observation alone. In practice, LLM-based agents implement this through:

- **Context window**: The concatenation of prior observations and actions within the model's context window serves as an implicit memory mechanism.
- **External memory**: Structured storage systems (e.g., RAG, vector databases) that the agent can query to retrieve relevant historical information.
- **Learned state representations**: Internal representations maintained by the model that compress historical information into a latent state.

The objective in Agentic RL is to maximize the cumulative discounted reward over the full horizon:

$$\pi^* = \arg\max_{\pi} \mathbb{E}\left[\sum_{t=0}^{H-1} \gamma^t \mathcal{R}(s_t, a_t, s_{t+1}) \right]$$

where the expectation is taken over the initial state distribution, transition dynamics, observation emissions, and policy-induced action distributions.

### 2.1.4 Partial Observability and the Observation Function

The observation function $\mathcal{O}(o_t | s_t, a_{t-1})$ formalizes the limited information available to the agent. In Agentic RL contexts, partial observability arises from several sources:

1. **Information asymmetry**: The environment may contain state variables invisible to the agent (e.g., hidden files in a filesystem, internal database states).

2. **Sensing limitations**: The agent's perception is constrained to what can be captured through available interfaces (e.g., screenshots, API responses, text outputs).

3. **Delayed effects**: Actions may have consequences that are not immediately observable, requiring the agent to infer latent state changes.

The belief state $b_t(s) = P(s_t = s | h_t)$ provides a probabilistic representation of the agent's uncertainty about the true environment state given its history. Optimal behavior in POMDPs often requires maintaining and updating this belief state, though LLM-based agents typically employ heuristic approximations through their context windows and reasoning capabilities.

| Property | Conventional LLM-RL (PBRFT) | Agentic Reinforcement Learning |
|----------|---------------------------|-------------------------------|
| Mathematical Setup | Single-step MDP ($H = 1$) | Multi-turn POMDP ($H \gg 1$) |
| State Representation | Static Text Prompt | Dynamic environment + memory |
| Action Space | Vocabulary tokens ($\mathcal{A} = \mathcal{V}$) | Tokens + Tool/API/Environment actions |
| Reward Signal | Subjective Preference (Alignment) | Objective Task Completion (Utility) |
| Information | Full observability | Partial observability |
| Temporal Structure | Stateless, independent decisions | Stateful, sequential dependencies |

## 2.2 Expanded Action Spaces (ExpA)

### 2.2.1 Decoupling Reasoning from Action

A theoretical advancement in Agentic RL is the formal separation of internal reasoning processes from external environment interactions through the concept of Expanded Action Spaces (ExpA). This decoupling addresses a fundamental limitation of treating language generation and environment manipulation as identical operations.

**Definition 2.4 (Expanded Action Space).** The expanded action space $\mathcal{A}_{\text{ExpA}}$ is defined as the union of three disjoint subspaces:

$$\mathcal{A}_{\text{ExpA}} = \mathcal{A}_{\text{lang}} \cup \mathcal{A}_{\text{route}} \cup \mathcal{A}_{\text{env}}$$

where:

- **Language actions** $\mathcal{A}_{\text{lang}} = \mathcal{V}^*$: Sequences of vocabulary tokens used for internal reasoning, chain-of-thought generation, and natural language processing. These actions affect only the agent's internal state (context window) and produce no external effects.

- **Routing actions** $\mathcal{A}_{\text{route}}$: Discrete selector actions that determine which environment or tool the agent will interact with next. A routing action $a_{\text{route}} \in \mathcal{A}_{\text{route}}$ activates a specific environment interface.

- **Environment actions** $\mathcal{A}_{\text{env}} = \bigcup_{e \in \mathcal{E}} \mathcal{A}_e$: The union of action spaces for all available environments $\mathcal{E}$. When environment $e$ is active, actions $a \in \mathcal{A}_e$ are interpreted according to that environment's semantics.

### 2.2.2 Routing Actions and Environment Selection

Routing actions enable the agent to dynamically switch between different operational modes and external systems. Formally, we define a routing function:

$$\rho: \mathcal{A}_{\text{route}} \rightarrow \mathcal{E}$$

that maps routing actions to environment instances. When the agent executes a routing action $a_{\text{route}}$ at time $t$, the subsequent action $a_{t+1}$ is interpreted within the context of environment $\rho(a_{\text{route}})$.

**Example 2.1 (Multi-Environment Routing).** Consider an agent with access to three environments:
- $\mathcal{E}_{\text{web}}$: Web browser environment with actions $\mathcal{A}_{\text{web}} = \{\text{navigate}, \text{click}, \text{type}, \text{scroll}, \ldots\}$
- $\mathcal{E}_{\text{code}}$: Code execution environment with actions $\mathcal{A}_{\text{code}} = \{\text{write\_file}, \text{execute}, \text{debug}, \ldots\}$
- $\mathcal{E}_{\text{calc}}$: Calculator environment with actions $\mathcal{A}_{\text{calc}} = \{\text{compute}, \text{store}, \text{recall}, \ldots\}$

The routing action space $\mathcal{A}_{\text{route}} = \{a_{\text{web}}, a_{\text{code}}, a_{\text{calc}}\}$ allows the agent to switch contexts:

1. Agent generates reasoning: $a_t \in \mathcal{A}_{\text{lang}}$ ("I need to calculate the sum first...")
2. Agent routes to calculator: $a_{t+1} = a_{\text{calc}} \in \mathcal{A}_{\text{route}}$
3. Agent executes calculation: $a_{t+2} = \text{compute}(x + y) \in \mathcal{A}_{\text{calc}}$
4. Agent routes back to reasoning: $a_{t+3} = a_{\text{lang}} \in \mathcal{A}_{\text{route}}$

### 2.2.3 Theoretical Implications of ExpA

The Expanded Action Space framework provides several theoretical advantages:

**Modularity**: By separating $\mathcal{A}_{\text{lang}}$, $\mathcal{A}_{\text{route}}$, and $\mathcal{A}_{\text{env}}$, the agent's reasoning capabilities can be trained and optimized independently of specific environment implementations. This modularity enables:

$$\pi(a | h) = \pi_{\text{route}}(a_{\text{route}} | h) \cdot \pi_{\text{env}}(a_{\text{env}} | h, a_{\text{route}}) \cdot \pi_{\text{lang}}(a_{\text{lang}} | h)$$

where the policy decomposes into routing, environment-specific, and language components.

**Composability**: New environments can be added to $\mathcal{E}$ without retraining the core reasoning capabilities, provided the routing mechanism can map to the new action space.

**Interpretability**: The explicit separation of reasoning tokens ($\mathcal{A}_{\text{lang}}$) from action tokens ($\mathcal{A}_{\text{env}}$) enables process-level supervision and debugging. The agent's "thought process" becomes observable through its language actions, while its external effects are traceable through environment actions.

**Safety**: Routing actions provide natural intervention points for guardrails and safety checks. Before executing $a_{\text{env}} \in \mathcal{A}_e$, the system can validate the action against environment-specific constraints.

### 2.2.4 Comparison with Traditional LLM-RL

The ExpA framework fundamentally differs from traditional LLM-RL in how it treats the relationship between language and action:

| Aspect | Traditional LLM-RL | ExpA-Based Agentic RL |
|--------|-------------------|----------------------|
| Token Function | All tokens are outputs | Tokens partitioned by function |
| Environment Interface | Implicit through text | Explicit routing mechanism |
| Action Semantics | Uniform (all are text) | Context-dependent (language vs. environment) |
| Extensibility | Requires retraining for new capabilities | Modular addition of environments |
| Observability | Black-box output | Transparent reasoning/action separation |

In traditional LLM-RL, when a model generates the token sequence "CALCULATE 2+2", the system must parse this text to extract the intended action. In the ExpA framework, the model explicitly routes to $\mathcal{E}_{\text{calc}}$ and executes $\text{compute}(2+2)$, eliminating the ambiguity of text-based action specification.

The mathematical formulation of Agentic RL with Expanded Action Spaces provides a rigorous foundation for understanding how large language models can evolve from passive generators into autonomous agents capable of sustained interaction with complex, dynamic environments. This framework enables the development of training methodologies, evaluation protocols, and safety mechanisms appropriate for the agentic paradigm.
