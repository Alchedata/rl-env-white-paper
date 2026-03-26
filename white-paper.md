# Reinforcement Learning Environment for Agentic AI: From Theory to Practice

---

## Abstract

The convergence of Large Language Models (LLMs) and Reinforcement Learning (RL) has precipitated a fundamental transformation in artificial intelligence, shifting from passive "answering" systems to autonomous "acting" agents capable of sustained reasoning and environmental interaction. This white paper provides a comprehensive survey of the emerging landscape of Reinforcement Learning Environments for Agentic AI, bridging the gap between theoretical RL foundations and practical implementation requirements.

We formalize the transition from conventional LLM-RL—operating within a degenerate single-step Markov Decision Process (MDP)—to Agentic Reinforcement Learning, which reframes interaction as a temporally extended Partially Observable Markov Decision Process (POMDP) with horizon $H \gg 1$. Central to this transformation is the Expanded Action Space (ExpA) framework, which decouples internal language-based reasoning from external environment manipulation through explicit routing mechanisms. This theoretical foundation enables systematic analysis of the five core agentic capabilities—planning, tool use, memory, self-improvement, and reasoning—across diverse task domains including software engineering, mathematical reasoning, and web interaction.

Our survey encompasses the rapidly maturing open-source ecosystem, examining standardized environment frameworks (OpenEnv, GEM, MCP) and training libraries (Agent-Lightning, NeMo RL, OpenAI Agents SDK) that constitute the infrastructure for scalable agent development. We review state-of-the-art agentic reasoning models, from Kimi K2.5's trillion-parameter Agent Swarm paradigm to OpenClaw's operating system abstraction and direct-action interfaces like Claude Code and OpenAI Operator. The analysis extends to embodied AI through NVIDIA's Cosmos 3, Isaac Sim 2, and GR00t, addressing the unique challenges of physical agency.

A critical contribution addresses the "dataset ceiling" constraining AI progress through synthetic environment generation. The Agent World Model (AWM) and Reasoning Gym (RG) frameworks demonstrate how procedurally generated, SQL-backed environments with verifiable rewards can provide infinite training data without dependence on finite human annotation pipelines. We examine algorithmic innovations in credit assignment—including GRPO, HGPO, HCAPO, and SHADOW—that enable efficient learning in long-horizon tasks with sparse rewards.

The paper confronts the sim-to-real gap through the User-Sim Index (USI), quantifying systematic divergences between simulated and real human behavior that threaten production readiness. We introduce the CLASSic and CLEAR evaluation frameworks alongside four reliability dimensions—consistency, robustness, predictability, and safety—derived from safety-critical engineering practices.

This work establishes that Agentic RL represents not merely an engineering evolution but a fundamental reconceptualization of artificial intelligence. As RL Gyms become the "verification layer" for AI agents—much as EDA serves silicon development—the infrastructure, algorithms, and theoretical frameworks surveyed here constitute the scaffolding upon which the next generation of autonomous AI will be built.

---

## 1. Introduction

The rapid convergence of Large Language Models (LLMs) and Reinforcement Learning (RL) has precipitated a fundamental transformation in how AI systems are conceived, moving from "answering" to "acting." Traditionally, LLMs were treated as passive text emitters—conditional generators optimized for single-turn output alignment [1]. However, the emergence of Agentic Reinforcement Learning (Agentic RL) marks a paradigm shift where models are reframed as autonomous decision-makers embedded in complex, dynamic worlds. These systems possess "agency": the capacity to autonomously perceive, plan, reason, and adapt strategies over extended sequences of interactions to achieve cumulative objectives [2].

### 1.1 From Static Models to Agentic Systems

The evolution of LLMs from passive text generators to autonomous agentic entities necessitates a corresponding shift in training paradigms. Conventional LLM-RL, typically instantiated as Preference-Based Reinforcement Fine-Tuning (PBRFT), operates within a degenerate, single-step Markov Decision Process (MDP) with a horizon length $H=1$ [3]. In this "open-loop" setting, the environment state is static (the prompt), and the action space is restricted to vocabulary tokens. The reward signal derives from subjective human preferences, optimizing for alignment rather than task completion.

Agentic RL, by contrast, formalizes the interaction as a temporally extended Partially Observable Markov Decision Process (POMDP), requiring the agent to maintain persistent state and reasoning across multiple turns ($H \gg 1$) [4]. The agent receives an observation at each step, and its internal state encompasses the full history of prior actions and observations. The objective shifts from maximizing immediate preference scores to maximizing cumulative discounted reward over a long-term horizon, fundamentally changing both the mathematical framework and the practical requirements for training.

### 1.2 The Theory-Practice Gap in Agentic RL

While the theoretical foundations of RL have been well-established for decades [5], the application of these principles to LLM-based agents reveals a significant gap between theory and practice. Traditional RL research has focused on environments with low-dimensional state spaces, discrete action spaces, and dense reward signals. Agentic RL, however, must contend with high-dimensional textual observations, hybrid action spaces combining language generation with tool invocation, and sparse rewards that may only materialize after extended interaction sequences [6].

Recent theory suggests decoupling environment interactions from language by internalizing them in an Expanded Action space (ExpA) beyond the standard vocabulary [7]. This architectural innovation allows a clean separation between language-based reasoning and direct environment manipulation. In the default language environment, the model reasons via tokens, but it can trigger "routing actions" to activate specific external environments—such as calculators, browsers, or code interpreters—switching its mode of interaction to environment-specific actions. This expansion of the action space from $\mathcal{V}$ (vocabulary) to $\mathcal{V} \cup \mathcal{T}$ (vocabulary plus tool calls) dramatically increases the expressiveness of agent policies while complicating the credit assignment problem.

### 1.3 The Critical Role of RL Environments

Central to the Agentic RL transformation is the development of Reinforcement Learning Gyms—interactive, simulated environments that serve as essential training grounds where models can experiment, fail safely, and learn through trial and error [8]. Much like Electronic Design Automation (EDA) serves as the infrastructure for silicon development, RL Gyms provide the "verification layer" for AI agents, translating human intent into measurable, executable behavior at scale [9].

These environments must satisfy several critical requirements that distinguish them from traditional RL benchmarks. First, they must support long-horizon interactions, allowing agents to execute sequences of dozens or hundreds of steps to accomplish complex objectives [10]. Second, they must provide verifiable reward signals—objective, automatable evaluation criteria that can determine whether a task has been completed successfully without human judgment [11]. Third, they must expose rich observation spaces, including structured data, visual inputs, and execution feedback that enables grounded reasoning.

The industry shift in 2026 from raw intelligence scores to "agency"—the ability to persist toward a goal using tools—has made these gyms the primary vehicle for instilling the reliability, groundedness, and multi-step planning required for real-world deployment [12]. Without high-fidelity simulation environments, agents cannot develop the robust behavioral patterns necessary for deployment in safety-critical applications.

### 1.4 Key Challenges in Agentic RL Training

Training agents within these environments presents several fundamental challenges that this paper addresses in detail.

**Action Space Complexity.** The expanded action spaces of agentic systems—combining language generation, tool invocation, and environment manipulation—create significant exploration challenges. Agents must learn not only what actions to take but also when to switch between different modes of interaction [13].

**Credit Assignment.** Long-horizon tasks suffer from sparse rewards, making it difficult to attribute success to specific intermediate actions [14]. When an agent executes a 50-step sequence to complete a software engineering task, determining which specific code edits or tool calls contributed to the final outcome remains a fundamental algorithmic challenge. Recent advances such as Group Relative Policy Optimization (GRPO) [15] and Hindsight Credit Assignment (HCAPO) [16] address this challenge by comparing trajectories within sample groups and leveraging post-hoc reasoning, but significant open problems remain.

**The Sim-to-Real Gap.** A critical "reality gap" exists between simulated training environments and real-world deployment [17]. Research using the User-Sim Index (USI) reveals that LLM-based user simulators often create an "easy mode" for agents, exhibiting behavioral gaps (excessive cooperativeness, "front-loading" of information) and evaluative gaps (uniformly positive feedback versus nuanced human judgment) [18]. Bridging this gap requires environments that accurately model the stochasticity, partial observability, and adversarial conditions of real-world deployment.

### 1.5 Contributions and Paper Structure

This paper provides a comprehensive survey of the emerging landscape of RL environments for Agentic AI, bridging the gap between theoretical RL foundations and practical implementation requirements. Our contributions are threefold:

1. **Theoretical Framework.** We formalize the transition from LLM-RL to Agentic RL, establishing the POMDP mathematical framework and analyzing the implications of expanded action spaces for training dynamics.

2. **Taxonomy and Architecture.** We present a systematic taxonomy of agentic capabilities and environment architectures, examining standardized frameworks including OpenEnv, GEM, and the Model Context Protocol (MCP).

3. **Synthesis of Advances.** We review algorithmic innovations in credit assignment, synthetic environment generation (Agent World Model, Reasoning Gym), and sim-to-real transfer, identifying critical open problems and future research directions.

The remainder of this paper is organized as follows. Section 2 establishes the theoretical framework, contrasting MDP and POMDP formalisms and analyzing expanded action spaces. Section 3 presents a taxonomy of agentic capabilities and task domains. Section 4 surveys open-source packages and development frameworks. Section 5 reviews state-of-the-art agentic reasoning models. Sections 6 and 7 address embodied AI and synthetic environment generation. Section 8 examines algorithmic advances in credit assignment. Section 9 discusses the sim-to-real gap. Section 10 covers evaluation and production readiness. Section 11 concludes with perspectives on the path toward Artificial Super Intelligence.

---

## 2. Theoretical Framework: From LLM-RL to Agentic RL

The transition to Agentic Reinforcement Learning represents a fundamental reconceptualization of how large language models interact with their environment. This section establishes the mathematical formalism underlying this paradigm shift, contrasting the degenerate single-step MDP framework of conventional LLM-RL with the temporally extended POMDP formulation of Agentic RL. We introduce the Expanded Action Space (ExpA) concept as a theoretical mechanism for decoupling reasoning from action execution.

### 2.1 MDP vs. POMDP Formalism

#### 2.1.1 Conventional LLM-RL: The Degenerate MDP

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

#### 2.1.2 Agentic RL: The POMDP Formulation

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

#### 2.1.3 State Space: Environment State and Agent Memory

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

#### 2.1.4 Partial Observability and the Observation Function

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

### 2.2 Expanded Action Spaces (ExpA)

#### 2.2.1 Decoupling Reasoning from Action

A theoretical advancement in Agentic RL is the formal separation of internal reasoning processes from external environment interactions through the concept of Expanded Action Spaces (ExpA). This decoupling addresses a fundamental limitation of treating language generation and environment manipulation as identical operations.

**Definition 2.4 (Expanded Action Space).** The expanded action space $\mathcal{A}_{\text{ExpA}}$ is defined as the union of three disjoint subspaces:

$$\mathcal{A}_{\text{ExpA}} = \mathcal{A}_{\text{lang}} \cup \mathcal{A}_{\text{route}} \cup \mathcal{A}_{\text{env}}$$

where:

- **Language actions** $\mathcal{A}_{\text{lang}} = \mathcal{V}^*$: Sequences of vocabulary tokens used for internal reasoning, chain-of-thought generation, and natural language processing. These actions affect only the agent's internal state (context window) and produce no external effects.

- **Routing actions** $\mathcal{A}_{\text{route}}$: Discrete selector actions that determine which environment or tool the agent will interact with next. A routing action $a_{\text{route}} \in \mathcal{A}_{\text{route}}$ activates a specific environment interface.

- **Environment actions** $\mathcal{A}_{\text{env}} = \bigcup_{e \in \mathcal{E}} \mathcal{A}_e$: The union of action spaces for all available environments $\mathcal{E}$. When environment $e$ is active, actions $a \in \mathcal{A}_e$ are interpreted according to that environment's semantics.

#### 2.2.2 Routing Actions and Environment Selection

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

#### 2.2.3 Theoretical Implications of ExpA

The Expanded Action Space framework provides several theoretical advantages:

**Modularity**: By separating $\mathcal{A}_{\text{lang}}$, $\mathcal{A}_{\text{route}}$, and $\mathcal{A}_{\text{env}}$, the agent's reasoning capabilities can be trained and optimized independently of specific environment implementations. This modularity enables:

$$\pi(a | h) = \pi_{\text{route}}(a_{\text{route}} | h) \cdot \pi_{\text{env}}(a_{\text{env}} | h, a_{\text{route}}) \cdot \pi_{\text{lang}}(a_{\text{lang}} | h)$$

where the policy decomposes into routing, environment-specific, and language components.

**Composability**: New environments can be added to $\mathcal{E}$ without retraining the core reasoning capabilities, provided the routing mechanism can map to the new action space.

**Interpretability**: The explicit separation of reasoning tokens ($\mathcal{A}_{\text{lang}}$) from action tokens ($\mathcal{A}_{\text{env}}$) enables process-level supervision and debugging. The agent's "thought process" becomes observable through its language actions, while its external effects are traceable through environment actions.

**Safety**: Routing actions provide natural intervention points for guardrails and safety checks. Before executing $a_{\text{env}} \in \mathcal{A}_e$, the system can validate the action against environment-specific constraints.

#### 2.2.4 Comparison with Traditional LLM-RL

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

---

## 3. Taxonomy of Agentic Capabilities and Task Domains

Progress in Agentic Reinforcement Learning is best understood through a systematic classification of the core capabilities that enable autonomous behavior and the task domains where these capabilities are exercised. This taxonomy provides a structured framework for analyzing agentic systems, identifying gaps in current research, and guiding future development efforts.

### 3.1 Core Agentic Capabilities

The transition from passive language models to autonomous agents requires the development of five interconnected capabilities: planning, tool use, memory, self-improvement, and reasoning. Each capability represents a distinct dimension of agency that must be cultivated through appropriate training environments and reinforcement learning algorithms.

#### 3.1.1 Planning

Planning constitutes the foundational capability that enables agents to decompose complex objectives into manageable sub-goals and coordinate actions across extended time horizons. In the Agentic RL framework, planning operates through several mechanisms:

**Task Decomposition** refers to the agent's ability to break down complex, multi-step objectives into discrete, actionable sub-tasks. For example, when asked to "build a web application," an agent must decompose this into requirements analysis, architecture design, implementation, testing, and deployment phases. RL environments that support planning must provide intermediate reward signals that validate correct decomposition while penalizing redundant or misordered steps.

**Goal Setting** involves the agent's capacity to establish intermediate milestones that guide behavior toward ultimate objectives. Effective goal setting requires the agent to maintain a hierarchical representation of objectives, balancing immediate rewards against long-term utility. Training environments must support variable goal structures, allowing agents to learn adaptive goal-setting strategies across different problem domains.

**Replanning** represents the agent's ability to adjust its strategy when encountering unexpected obstacles or changed circumstances. This requires monitoring execution progress, detecting deviations from expected outcomes, and generating alternative action sequences. Replanning capability is particularly critical in dynamic environments where initial plans may become obsolete due to external changes.

#### 3.1.2 Tool Use

Tool use extends the agent's action space beyond vocabulary tokens to include interactions with external systems, APIs, and computational resources. This capability transforms language models from isolated text generators into systems capable of affecting real-world change.

**API Calling** involves the agent's ability to invoke external services through structured interfaces. This includes understanding API documentation, constructing valid requests, parsing responses, and handling errors. Training for API calling requires environments that simulate realistic API behaviors, including rate limiting, authentication failures, and malformed responses.

**Code Execution** enables agents to write, execute, and debug programs to accomplish computational tasks. This capability is essential for data analysis, algorithmic problem-solving, and system administration. Effective training environments must provide sandboxed execution contexts that capture execution outputs, runtime errors, and resource consumption metrics.

The Expanded Action space (ExpA) framework formalizes tool use by decoupling environment interactions from language generation. Under this approach, the model maintains a clean separation between reasoning tokens and action tokens, with "routing actions" triggering transitions between different interaction modes.

#### 3.1.3 Memory

Memory systems enable agents to persist information across interaction episodes and retrieve relevant context for current decision-making. Without effective memory, agents are limited to purely reactive behaviors, unable to learn from past experiences or maintain consistency across extended sessions.

**Short-term Memory** encompasses the immediate context window that the agent can directly attend to during inference. While modern models support increasingly long contexts, effective short-term memory utilization requires training to identify and retain task-relevant information while filtering distractions.

**Long-term Memory** refers to structured storage systems that persist beyond individual sessions, typically implemented through vector databases or knowledge graphs. Agents must learn to encode experiences into retrievable formats and construct appropriate queries to access stored information.

**Episodic Memory** captures specific interaction sequences that can be referenced for future similar situations. This form of memory is particularly valuable for learning from rare events or capturing successful solution patterns that can be reused across tasks.

#### 3.1.4 Self-Improvement

Self-improvement represents the meta-capability that enables agents to enhance their own performance through experience. This capability distinguishes truly autonomous systems from those that remain static after deployment.

**Learning from Feedback** involves updating behavior based on explicit reward signals, implicit user satisfaction indicators, or self-generated evaluations. Effective self-improvement requires environments that provide dense, informative feedback signals that correlate with true task performance.

**Error Recognition** enables agents to identify when their outputs are incorrect or suboptimal, even in the absence of external feedback. This capability is crucial for initiating self-correction cycles and avoiding the propagation of errors through multi-step reasoning chains.

**Iterative Refinement** refers to the process of progressively improving solutions through multiple attempts, incorporating lessons from previous failures. Training environments that support self-improvement must allow for multi-attempt episodes with rich feedback on the quality of intermediate solutions.

#### 3.1.5 Reasoning

Reasoning capabilities enable agents to perform explicit, verifiable inference steps that lead to correct conclusions. Unlike implicit pattern matching, reasoning produces interpretable chains of thought that can be validated and debugged.

**Chain-of-Thought** reasoning involves generating explicit intermediate steps between problem statement and solution. This approach, often implemented through `<think>` tags or similar mechanisms, makes the reasoning process visible and subject to process-level supervision.

**Verification** capabilities enable agents to check the correctness of their own reasoning steps or final outputs. This includes mathematical verification, logical consistency checking, and cross-referencing against known facts. Training for verification requires environments that provide ground-truth labels or automated checking procedures.

### 3.2 Task Domains

The capabilities described above find application across diverse task domains, each presenting unique challenges and requiring specialized environment designs. Three domains have emerged as particularly important proving grounds for Agentic RL research.

#### 3.2.1 Software Engineering

Software engineering tasks require agents to understand codebases, implement features, fix bugs, and maintain systems over time. This domain is characterized by:

- **Structured Action Spaces**: Code modifications follow syntactic and semantic constraints
- **Objective Verification**: Test suites provide unambiguous success criteria
- **Long Horizons**: Complex tasks may require hundreds of sequential actions
- **Tool Integration**: Effective development requires using version control, build systems, and testing frameworks

Benchmarks like SWE-Bench provide standardized evaluation environments where agents must resolve real GitHub issues in production codebases. Success in this domain requires strong planning capabilities for architecture design, tool use for build and test execution, and reasoning capabilities for understanding complex code relationships.

#### 3.2.2 Mathematical Reasoning

Mathematical reasoning tasks evaluate an agent's ability to solve problems requiring precise, step-by-step logical deduction. Key characteristics include:

- **Verifiable Solutions**: Mathematical claims can be checked for correctness with certainty
- **Symbolic Manipulation**: Solutions often require algebraic or logical transformations
- **Multi-step Inference**: Complex problems require chains of deductions
- **Abstraction**: Solutions may require recognizing patterns or applying general theorems

Benchmarks like AIME (American Invitational Mathematics Examination) and various olympiad problems provide challenging test cases. The Reasoning Gym framework offers procedurally generated mathematical tasks that enable curriculum learning and infinite training data generation.

#### 3.2.3 Web and GUI Interaction

Web and GUI interaction tasks require agents to navigate visual interfaces, understand layout semantics, and perform actions through simulated user inputs. This domain features:

- **Multimodal Perception**: Agents must process visual information alongside text
- **Dynamic Environments**: Web pages and applications change state in response to actions
- **Implicit Constraints**: Interface design conventions must be inferred from context
- **Real-world Relevance**: Success transfers directly to practical automation tasks

Benchmarks like OSWorld and BrowserGym provide simulated environments where agents interact with operating systems and web browsers. Success requires integrating visual perception with planning and tool use capabilities.

### 3.3 Capability-Domain Classification Matrix

The following matrix summarizes how core capabilities map to requirements across task domains:

| Capability | Software Engineering | Mathematical Reasoning | Web/GUI Interaction |
|------------|---------------------|------------------------|---------------------|
| **Planning** | Architecture design, task decomposition | Problem decomposition, proof strategy | Navigation planning, task sequencing |
| **Tool Use** | Compilers, debuggers, version control | Calculators, theorem provers, symbolic systems | Browser APIs, form interactions, click actions |
| **Memory** | Codebase understanding, pattern libraries | Formula retrieval, prior problem solutions | Session state, user preferences, history |
| **Self-Improvement** | Bug fix patterns, refactoring strategies | Proof technique learning, error pattern recognition | Interface adaptation, failure recovery |
| **Reasoning** | Logic verification, type checking | Deductive chains, symbolic manipulation | Visual reasoning, layout inference |

### 3.4 Concrete Examples

To illustrate the taxonomy in practice, consider how an agentic system might approach a representative task from each domain:

**Software Engineering Example**: Given a bug report about a memory leak in a Python web application, the agent must:
1. *Plan*: Decompose the task into reproduction, diagnosis, fix implementation, and verification phases
2. *Use Tools*: Execute the application, attach profilers, search codebase, edit files, run tests
3. *Memory*: Reference similar bugs from knowledge base, recall relevant code patterns
4. *Self-Improve*: Learn from failed diagnosis attempts, refine search strategies
5. *Reason*: Trace object lifecycles, verify fix correctness through logical analysis

**Mathematical Reasoning Example**: Solving a combinatorics problem requires:
1. *Plan*: Identify applicable counting principles, establish solution structure
2. *Use Tools*: Invoke symbolic computation for verification, access formula databases
3. *Memory*: Retrieve similar problems and solution templates
4. *Self-Improve*: Recognize incorrect assumptions, backtrack and retry
5. *Reason*: Generate explicit counting arguments, verify each step

**Web Interaction Example**: Booking a flight involves:
1. *Plan*: Sequence navigation through search, selection, and checkout flows
2. *Use Tools*: Interact with browser APIs, fill forms, click buttons
3. *Memory*: Maintain session state, recall user preferences
4. *Self-Improve*: Adapt to interface changes, learn from failed searches
5. *Reason*: Interpret visual layouts, verify booking constraints

This taxonomy provides a framework for analyzing existing systems, identifying capability gaps, and designing targeted training interventions. As the field progresses, we expect the boundaries between capabilities to blur as agents develop increasingly integrated and fluid competence across all dimensions.

---

## 4. Open-Source Packages and Development Frameworks

The rapid maturation of Agentic Reinforcement Learning has been catalyzed by a robust ecosystem of open-source frameworks and libraries. These tools standardize agent-environment interactions, abstract away infrastructure complexity, and enable researchers and practitioners to focus on algorithmic innovation rather than low-level system integration. This section provides a comprehensive survey of the dominant environment frameworks and RL training libraries that constitute the foundation of modern Agentic RL development.

### 4.1 Environment and Interface Frameworks

Standardized environment frameworks serve as the critical abstraction layer between agent policies and the diverse task domains they must navigate. These frameworks provide Gymnasium-style APIs that ensure consistency across different environments while supporting the complex, multi-turn interactions characteristic of Agentic RL.

#### 4.1.1 OpenEnv (Meta/HuggingFace)

OpenEnv represents a collaborative effort between Meta AI and Hugging Face to establish a unified, end-to-end framework for Agentic RL environments. Drawing inspiration from the widely-adopted Gymnasium (formerly OpenAI Gym) interface, OpenEnv extends the paradigm to support the unique requirements of language model agents operating in extended-horizon POMDPs.

**Core Architecture and Design Principles**

OpenEnv's architecture centers on containerized environment isolation, ensuring that agent actions cannot affect the host system while maintaining realistic interaction dynamics. The framework exposes a familiar API surface through three primary methods:

- `reset()`: Initializes the environment state and returns the initial observation
- `step(action)`: Executes an action and returns the tuple `(observation, reward, terminated, truncated, info)`
- `render()`: Provides human-readable visualization of the current state

This design choice enables seamless migration of existing RL algorithms while accommodating the expanded action spaces (ExpA) required for agentic capabilities. OpenEnv supports diverse domain implementations including BrowserGym for web navigation