# 3. Taxonomy of Agentic Capabilities and Task Domains

Progress in Agentic Reinforcement Learning is best understood through a systematic classification of the core capabilities that enable autonomous behavior and the task domains where these capabilities are exercised. This taxonomy provides a structured framework for analyzing agentic systems, identifying gaps in current research, and guiding future development efforts.

## 3.1 Core Agentic Capabilities

The transition from passive language models to autonomous agents requires the development of five interconnected capabilities: planning, tool use, memory, self-improvement, and reasoning. Each capability represents a distinct dimension of agency that must be cultivated through appropriate training environments and reinforcement learning algorithms.

### 3.1.1 Planning

Planning constitutes the foundational capability that enables agents to decompose complex objectives into manageable sub-goals and coordinate actions across extended time horizons. In the Agentic RL framework, planning operates through several mechanisms:

**Task Decomposition** refers to the agent's ability to break down complex, multi-step objectives into discrete, actionable sub-tasks. For example, when asked to "build a web application," an agent must decompose this into requirements analysis, architecture design, implementation, testing, and deployment phases. RL environments that support planning must provide intermediate reward signals that validate correct decomposition while penalizing redundant or misordered steps.

**Goal Setting** involves the agent's capacity to establish intermediate milestones that guide behavior toward ultimate objectives. Effective goal setting requires the agent to maintain a hierarchical representation of objectives, balancing immediate rewards against long-term utility. Training environments must support variable goal structures, allowing agents to learn adaptive goal-setting strategies across different problem domains.

**Replanning** represents the agent's ability to adjust its strategy when encountering unexpected obstacles or changed circumstances. This requires monitoring execution progress, detecting deviations from expected outcomes, and generating alternative action sequences. Replanning capability is particularly critical in dynamic environments where initial plans may become obsolete due to external changes.

### 3.1.2 Tool Use

Tool use extends the agent's action space beyond vocabulary tokens to include interactions with external systems, APIs, and computational resources. This capability transforms language models from isolated text generators into systems capable of affecting real-world change.

**API Calling** involves the agent's ability to invoke external services through structured interfaces. This includes understanding API documentation, constructing valid requests, parsing responses, and handling errors. Training for API calling requires environments that simulate realistic API behaviors, including rate limiting, authentication failures, and malformed responses.

**Code Execution** enables agents to write, execute, and debug programs to accomplish computational tasks. This capability is essential for data analysis, algorithmic problem-solving, and system administration. Effective training environments must provide sandboxed execution contexts that capture execution outputs, runtime errors, and resource consumption metrics.

The Expanded Action space (ExpA) framework formalizes tool use by decoupling environment interactions from language generation. Under this approach, the model maintains a clean separation between reasoning tokens and action tokens, with "routing actions" triggering transitions between different interaction modes.

### 3.1.3 Memory

Memory systems enable agents to persist information across interaction episodes and retrieve relevant context for current decision-making. Without effective memory, agents are limited to purely reactive behaviors, unable to learn from past experiences or maintain consistency across extended sessions.

**Short-term Memory** encompasses the immediate context window that the agent can directly attend to during inference. While modern models support increasingly long contexts, effective short-term memory utilization requires training to identify and retain task-relevant information while filtering distractions.

**Long-term Memory** refers to structured storage systems that persist beyond individual sessions, typically implemented through vector databases or knowledge graphs. Agents must learn to encode experiences into retrievable formats and construct appropriate queries to access stored information.

**Episodic Memory** captures specific interaction sequences that can be referenced for future similar situations. This form of memory is particularly valuable for learning from rare events or capturing successful solution patterns that can be reused across tasks.

### 3.1.4 Self-Improvement

Self-improvement represents the meta-capability that enables agents to enhance their own performance through experience. This capability distinguishes truly autonomous systems from those that remain static after deployment.

**Learning from Feedback** involves updating behavior based on explicit reward signals, implicit user satisfaction indicators, or self-generated evaluations. Effective self-improvement requires environments that provide dense, informative feedback signals that correlate with true task performance.

**Error Recognition** enables agents to identify when their outputs are incorrect or suboptimal, even in the absence of external feedback. This capability is crucial for initiating self-correction cycles and avoiding the propagation of errors through multi-step reasoning chains.

**Iterative Refinement** refers to the process of progressively improving solutions through multiple attempts, incorporating lessons from previous failures. Training environments that support self-improvement must allow for multi-attempt episodes with rich feedback on the quality of intermediate solutions.

### 3.1.5 Reasoning

Reasoning capabilities enable agents to perform explicit, verifiable inference steps that lead to correct conclusions. Unlike implicit pattern matching, reasoning produces interpretable chains of thought that can be validated and debugged.

**Chain-of-Thought** reasoning involves generating explicit intermediate steps between problem statement and solution. This approach, often implemented through `<think>` tags or similar mechanisms, makes the reasoning process visible and subject to process-level supervision.

**Verification** capabilities enable agents to check the correctness of their own reasoning steps or final outputs. This includes mathematical verification, logical consistency checking, and cross-referencing against known facts. Training for verification requires environments that provide ground-truth labels or automated checking procedures.

## 3.2 Task Domains

The capabilities described above find application across diverse task domains, each presenting unique challenges and requiring specialized environment designs. Three domains have emerged as particularly important proving grounds for Agentic RL research.

### 3.2.1 Software Engineering

Software engineering tasks require agents to understand codebases, implement features, fix bugs, and maintain systems over time. This domain is characterized by:

- **Structured Action Spaces**: Code modifications follow syntactic and semantic constraints
- **Objective Verification**: Test suites provide unambiguous success criteria
- **Long Horizons**: Complex tasks may require hundreds of sequential actions
- **Tool Integration**: Effective development requires using version control, build systems, and testing frameworks

Benchmarks like SWE-Bench provide standardized evaluation environments where agents must resolve real GitHub issues in production codebases. Success in this domain requires strong planning capabilities for architecture design, tool use for build and test execution, and reasoning capabilities for understanding complex code relationships.

### 3.2.2 Mathematical Reasoning

Mathematical reasoning tasks evaluate an agent's ability to solve problems requiring precise, step-by-step logical deduction. Key characteristics include:

- **Verifiable Solutions**: Mathematical claims can be checked for correctness with certainty
- **Symbolic Manipulation**: Solutions often require algebraic or logical transformations
- **Multi-step Inference**: Complex problems require chains of deductions
- **Abstraction**: Solutions may require recognizing patterns or applying general theorems

Benchmarks like AIME (American Invitational Mathematics Examination) and various olympiad problems provide challenging test cases. The Reasoning Gym framework offers procedurally generated mathematical tasks that enable curriculum learning and infinite training data generation.

### 3.2.3 Web and GUI Interaction

Web and GUI interaction tasks require agents to navigate visual interfaces, understand layout semantics, and perform actions through simulated user inputs. This domain features:

- **Multimodal Perception**: Agents must process visual information alongside text
- **Dynamic Environments**: Web pages and applications change state in response to actions
- **Implicit Constraints**: Interface design conventions must be inferred from context
- **Real-world Relevance**: Success transfers directly to practical automation tasks

Benchmarks like OSWorld and BrowserGym provide simulated environments where agents interact with operating systems and web browsers. Success requires integrating visual perception with planning and tool use capabilities.

## 3.3 Capability-Domain Classification Matrix

The following matrix summarizes how core capabilities map to requirements across task domains:

| Capability | Software Engineering | Mathematical Reasoning | Web/GUI Interaction |
|------------|---------------------|------------------------|---------------------|
| **Planning** | Architecture design, task decomposition | Problem decomposition, proof strategy | Navigation planning, task sequencing |
| **Tool Use** | Compilers, debuggers, version control | Calculators, theorem provers, symbolic systems | Browser APIs, form interactions, click actions |
| **Memory** | Codebase understanding, pattern libraries | Formula retrieval, prior problem solutions | Session state, user preferences, history |
| **Self-Improvement** | Bug fix patterns, refactoring strategies | Proof technique learning, error pattern recognition | Interface adaptation, failure recovery |
| **Reasoning** | Logic verification, type checking | Deductive chains, symbolic manipulation | Visual reasoning, layout inference |

## 3.4 Concrete Examples

To illustrate the taxonomy in practice, consider how an agentic system might approach a representative task from each domain. These examples are also aligned with benchmark families commonly used to evaluate agentic systems, such as SWE-Bench for software engineering, AIME-style mathematical reasoning tasks, and WebArena or OSWorld-style interactive workflows.

**Software Engineering Example (SWE-Bench-style)**: Given a real GitHub issue in a production repository where a dependency upgrade has broken the CI test suite, the agent must:
1. *Plan*: Break the issue into reproduction, root-cause analysis, patch design, regression testing, and validation against the original bug report
2. *Use Tools*: Search the codebase, inspect git history, run the failing tests, edit source files, and execute the full test suite
3. *Memory*: Retain knowledge of repository structure, prior failed hypotheses, and project-specific conventions discovered during exploration
4. *Self-Improve*: Refine the debugging strategy after unsuccessful patches, using test feedback and stack traces to narrow the search space
5. *Reason*: Infer how the dependency change altered program behavior, identify the minimal corrective patch, and verify that the fix does not introduce regressions

**Mathematical Reasoning Example (AIME-style)**: Solving an AIME-style number theory problem with a single exact answer requires:
1. *Plan*: Identify the relevant invariants, choose a proof strategy, and decompose the problem into intermediate lemmas or subcases
2. *Use Tools*: Invoke symbolic or numerical computation to test conjectures, verify modular arithmetic, and check boundary cases
3. *Memory*: Recall similar olympiad techniques, intermediate deductions, and previously eliminated cases without repeating work
4. *Self-Improve*: Detect when a line of reasoning leads to contradiction, revise assumptions, and switch to a more promising strategy
5. *Reason*: Construct a rigorous derivation that leads to the unique final answer and confirm consistency between the proof and computational checks

**Web Interaction Example (WebArena/OSWorld-style)**: Resolving a customer support request in a browser-based commerce dashboard requires:
1. *Plan*: Sequence the workflow across order lookup, policy verification, refund or replacement processing, and confirmation logging
2. *Use Tools*: Navigate the web UI, search records, fill forms, click controls, and extract relevant information from dynamic pages
3. *Memory*: Track the current session state, the customer's order details, and the actions already taken across multiple pages
4. *Self-Improve*: Recover from failed searches, unexpected pop-ups, or changed layouts by trying alternate navigation paths
5. *Reason*: Interpret interface cues, apply business rules correctly, and verify that the final action satisfies the support request without violating policy

This taxonomy provides a framework for analyzing existing systems, identifying capability gaps, and designing targeted training interventions. As the field progresses, we expect the boundaries between capabilities to blur as agents develop increasingly integrated and fluid competence across all dimensions.
