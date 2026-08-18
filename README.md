# Awesome RSI (Recursive Self-Improvement) [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

Recursive Self-Improvement (RSI) refers to processes in which AI systems improve their own capabilities and can also improve the mechanisms that generate subsequent improvements.

Recent progress in self-training, agent memory, harness optimization, automated AI research, self-modifying coding agents, and evolutionary search has made RSI increasingly relevant as an empirical research direction rather than only a theoretical idea.

Awesome RSI collects and organizes important work across these areas, including model-level self-improvement, context and memory evolution, harness and scaffold evolution, multi-agent systems, automated AI research, benchmarks, and safety.

Not every work listed here demonstrates RSI in the strict sense. Some represent bounded self-improvement or enabling techniques that may contribute to more complete recursive systems.

If you are new to the topic, start with Fundamentals & Getting Started. If you already know the basics, explore the sections most relevant to your interests.

This is a community-maintained and evolving list. Contributions, missing papers, new benchmarks, frameworks, and suggestions for improving the taxonomy are very welcome.

The taxonomy is organizational rather than mutually exclusive; many systems span multiple layers and mechanisms.

## Contents

- [Scope & Terminology](#scope--terminology)
- [Fundamentals & Getting Started](#fundamentals--getting-started)
- [Model-level RSI](#model-level-rsi)
  - [Self-Training & Self-Reward](#self-training--self-reward)
  - [Synthetic Data & Self-Distillation](#synthetic-data--self-distillation)
  - [Self-Play & Iterative Fine-tuning](#self-play--iterative-fine-tuning)
  - [Self-Taught Reasoning](#self-taught-reasoning)
- [Harness-level RSI](#harness-level-rsi)
  - [Prompt & Program Optimization](#prompt--program-optimization)
  - [Context & Memory Evolution](#context--memory-evolution)
  - [Harness & Scaffold Evolution](#harness--scaffold-evolution)
  - [Extensible Harness Substrates](#extensible-harness-substrates)
  - [Self-Verification & Self-Correction — Enabling Foundations](#self-verification--self-correction--enabling-foundations)
  - [Self-Evolving Agent Frameworks](#self-evolving-agent-frameworks)
- [Multi-Agent Self-Improvement](#multi-agent-self-improvement)
  - [Co-Evolution](#co-evolution)
  - [Inference-time Debate](#inference-time-debate)
- [Coding / Software-Engineering Self-Improvement](#coding--software-engineering-self-improvement)
  - [Self-Modifying Coding Agents](#self-modifying-coding-agents)
  - [Iterative Repair & Training](#iterative-repair--training)
- [Automated AI R&D](#automated-ai-rd)
- [Evolutionary & Open-Ended RSI](#evolutionary--open-ended-rsi)
- [Safety, Alignment & Theory](#safety-alignment--theory)
  - [Supporting Safety Foundations](#supporting-safety-foundations)
- [Introspection & Self-Modeling](#introspection--self-modeling)
- [Benchmarks & Evaluations](#benchmarks--evaluations)
  - [Direct RSI & Self-Improvement Evaluations](#direct-rsi--self-improvement-evaluations)
  - [Automated AI R&D Evaluations](#automated-ai-rd-evaluations)
  - [Long-Horizon & Agent Capability Evaluations](#long-horizon--agent-capability-evaluations)
- [Frameworks & Tools](#frameworks--tools)
  - [Self-Modifying / Self-Evolving Systems](#self-modifying--self-evolving-systems)
  - [Harness / Memory / Skill Evolution](#harness--memory--skill-evolution)
  - [Automated Search / AI R&D](#automated-search--ai-rd)
- [Blog Posts & Discussions](#blog-posts--discussions)
- [Talks & Videos](#talks--videos)
- [Related Awesome Lists](#related-awesome-lists)

## Scope & Terminology

For this list, we use the following operational distinctions:

**Self-refinement** — improves the current output without a persistent change to the system.

**Persistent self-improvement** — changes to weights, memory, skills, prompts, harness, or code that carry into the next round.

**Recursive self-improvement** — the mechanism that produces improvements is itself the object of improvement.

**RSI substrate** — exposes an agent's own structure as a modifiable object, but does not necessarily form an automatic self-improvement loop by default.

## Fundamentals & Getting Started

Foundational papers, formal treatments, and surveys that establish the vocabulary and core questions of RSI.

- [A Survey of Self-Evolving Agents: On Path to Artificial Super Intelligence](https://arxiv.org/abs/2507.21046) - Surveys what, when, and how foundation-model agents can evolve across models, memory, tools, and architectures. (TMLR 2026)
- [Recursive Self-Improvement in AI: From Bounded Self-Refinement to Autonomous Research Loops](https://arxiv.org/abs/2607.07663) - Surveys recent self-improvement work by update target and loop closure while separating bounded refinement from open-ended RSI. (arXiv 2026)
- [A Comprehensive Survey of Self-Evolving AI Agents: A New Paradigm Bridging Foundation Models and Lifelong Agentic Systems](https://arxiv.org/abs/2508.07407) - Organizes agent evolution around feedback loops, update targets, domain applications, evaluation, and safety. (arXiv 2025)
- [A Survey on Self-Evolution of Large Language Models](https://arxiv.org/abs/2404.14387) - Presents a four-stage taxonomy of experience acquisition, refinement, updating, and evaluation for self-evolving LLMs. (arXiv 2024)
- [A Formulation of Recursive Self-Improvement and Its Possible Efficiency](https://arxiv.org/abs/1805.06610) - Gives a formal definition of a restricted RSI system and analyzes when efficient recursive improvement is computable. (arXiv 2018)
- [From Seed AI to Technological Singularity via Recursively Self-Improving Software](https://arxiv.org/abs/1502.06512) - Defines RSI software, surveys prior approaches, and proposes convergence concepts and computational limits. (arXiv 2015)
- [The Singularity: A Philosophical Analysis](https://consc.net/papers/singularity.pdf) - Develops a rigorous philosophical case for an intelligence explosion and examines its assumptions and consequences. (Journal of Consciousness Studies 2010)
- [Gödel Machines: Self-Referential Universal Problem Solvers Making Provably Optimal Self-Improvements](https://arxiv.org/abs/cs/0309048) - Defines a fully self-referential machine that rewrites itself after proving a modification improves expected utility. (Artificial General Intelligence book 2006)
- [Optimal Ordered Problem Solver](https://arxiv.org/abs/cs/0207097) - Introduces an asymptotically optimal program-search system that reuses solutions to accelerate later problem solving. (Machine Learning 2004)
- [Evolutionary Principles in Self-Referential Learning, or on Learning How to Learn: The Meta-Meta-... Hook](https://people.idsia.ch/~juergen/diploma1987ocr.pdf) - Describes early meta-evolution and self-referential learning mechanisms that recursively improve learning methods. (Diploma thesis 1987)
- [Speculations Concerning the First Ultraintelligent Machine](https://www.sciencedirect.com/science/article/pii/S0065245808604180) - Introduces the intelligence-explosion argument in which a machine capable of improving machine design triggers accelerating capability gains. (Advances in Computers 1965)

## Model-level RSI

Methods that improve model weights or training behavior through self-generated feedback, data, or reasoning, including canonical enabling methods later reused in persistent self-improvement loops.

### Self-Training & Self-Reward

- [EvoLM: Self-Evolving Language Models through Co-Evolved Discriminative Rubrics](https://arxiv.org/abs/2605.03871) - Alternately trains one model to generate discriminative rubrics and improve its policy from rubric-conditioned rewards without human annotations or external reward models. (arXiv 2026)
- [RLAIF vs. RLHF: Scaling Reinforcement Learning from Human Feedback with AI Feedback](https://arxiv.org/abs/2309.00267) - Studies reinforcement learning from AI-generated preferences as a scalable alternative to direct human feedback. (ICML 2024)
- [Self-Play Fine-Tuning Converts Weak Language Models to Strong Language Models](https://arxiv.org/abs/2401.01335) - Iteratively improves one language model through self-play preference learning without additional human annotations. (ICML 2024)
- [Self-Rewarding Language Models](https://arxiv.org/abs/2401.10020) - Trains language models to generate and judge their own instruction-following data over repeated alignment rounds. (ICML 2024)

### Synthetic Data & Self-Distillation

- [Recursive Synthesis for Long-Horizon Terminal Tasks](https://arxiv.org/abs/2608.05466) - Treats accepted tasks as seeds for the next round, generating increasingly difficult terminal tasks used for SFT and PPO as enabling work rather than strict RSI. (arXiv 2026)
- [Beyond Human Data: Scaling Self-Training for Problem-Solving with Language Models](https://arxiv.org/abs/2312.06585) - Iteratively samples, filters, and retrains on model-generated solutions to scale self-training beyond human demonstrations. (TMLR 2024)
- [Self-Alignment with Instruction Backtranslation](https://arxiv.org/abs/2308.06259) - Generates instructions for unlabeled model-written documents and fine-tunes on the resulting synthetic instruction-response pairs. (ICLR 2024)
- [Large Language Models Can Self-Improve](https://arxiv.org/abs/2210.11610) - Uses high-confidence model-generated answers as pseudo-labels for iterative fine-tuning on reasoning tasks. (EMNLP 2023)
- [Self-Instruct: Aligning Language Models with Self-Generated Instructions](https://arxiv.org/abs/2212.10560) - Bootstraps instruction-following data from a model's own generations and filters it before fine-tuning. (ACL 2023)

### Self-Play & Iterative Fine-tuning

- [Learning to Self-Evolve](https://arxiv.org/abs/2603.18620) - Uses reinforcement learning to teach models how to edit their own contexts for stronger performance on future tasks. (arXiv 2026)
- [SERPO: Self-Evolving Rubric Policy Optimization for Open-Ended Test-Time Reinforcement Learning](https://arxiv.org/abs/2607.26873) - Co-evolves response evidence, query-specific rubrics, and policy parameters in a closed test-time reinforcement-learning loop. (arXiv 2026)
- [Teaching LLMs to Self-Evolve: Cultivating Core Meta-Skills with Reinforcement Learning](https://arxiv.org/abs/2607.21971) - Trains MetaEvolve's reflection and feedback-driven refinement skills before applying inference-time evolutionary search to open-ended optimization. (arXiv 2026)
- [TEMPO: Scaling Test-time Training for Large Reasoning Models](https://arxiv.org/abs/2604.19295) - Interleaves model-parameter updates on unlabeled test questions with periodic critic recalibration on labeled data to sustain test-time improvement. (arXiv 2026)
- [Meta-Rewarding Language Models: Self-Improving Alignment with LLM-as-a-Meta-Judge](https://arxiv.org/abs/2407.19594) - Lets a language model judge its own judgments and iteratively improve both evaluation and instruction-following ability. (EMNLP 2025)
- [Self-Adapting Language Models](https://arxiv.org/abs/2506.10943) - Introduces SEAL, which generates its own update data and fine-tuning directives to adapt model weights to new tasks. (NeurIPS 2025)
- [Self-Improvement in Language Models: The Sharpening Mechanism](https://arxiv.org/abs/2412.01951) - Formalizes self-improvement as amortizing a model's verifier-guided search into a sharper post-trained policy. (ICLR 2025)
- [Self-Play Preference Optimization for Language Model Alignment](https://arxiv.org/abs/2405.00675) - Frames alignment as a two-player game and iteratively updates a policy toward a preference-model Nash equilibrium. (ICLR 2025)
- [SELF: Self-Evolution with Language Feedback](https://arxiv.org/abs/2310.00533) - Repeats self-feedback, response refinement, filtering, and fine-tuning so an LLM progressively improves on unlabeled instructions. (arXiv 2023)

### Self-Taught Reasoning

- [rStar-Math: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking](https://arxiv.org/abs/2501.04519) - Couples Monte Carlo tree search with self-evolved training data and a process preference model to improve mathematical reasoning. (ICML 2025)
- [Quiet-STaR: Language Models Can Teach Themselves to Think Before Speaking](https://arxiv.org/abs/2403.09629) - Trains language models to generate useful internal rationales throughout arbitrary text rather than only on question-answer tasks. (COLM 2024)
- [STaR: Bootstrapping Reasoning With Reasoning](https://arxiv.org/abs/2203.14465) - Alternates rationale generation, answer filtering, rationalization, and fine-tuning to bootstrap reasoning ability. (NeurIPS 2022)

## Harness-level RSI

Methods that improve prompts, memory, verification, tools, or agent policies around a model.

### Prompt & Program Optimization

- [Automated Design of Agentic Systems](https://arxiv.org/abs/2408.08435) - Uses a meta-agent to invent and iteratively improve agent architectures represented as executable code. (ICLR 2025)
- [TextGrad: Automatic "Differentiation" via Text](https://arxiv.org/abs/2406.07496) - Backpropagates textual feedback through compound AI systems to optimize prompts, code, and other textual variables. (Nature 2025)
- [Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models](https://arxiv.org/abs/2310.04406) - Combines Monte Carlo tree search, model-based value estimates, environment feedback, and self-reflection without updating base weights. (ICML 2024)
- [Large Language Models as Optimizers](https://arxiv.org/abs/2309.03409) - Introduces OPRO, which iteratively proposes and evaluates natural-language solutions and prompts from a history of scored attempts. (ICLR 2024)
- [Promptbreeder: Self-Referential Self-Improvement Via Prompt Evolution](https://arxiv.org/abs/2309.16797) - Evolves both task prompts and the mutation prompts that generate future prompt improvements. (ICML 2024)
- [Self-Taught Optimizer (STOP): Recursively Self-Improving Code Generation](https://arxiv.org/abs/2310.02304) - Demonstrates an LLM-written scaffolding program that improves the program responsible for making further improvements. (COLM 2024)
- [DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines](https://arxiv.org/abs/2310.03714) - Compiles declarative LM programs by optimizing prompts and demonstrations against a user-defined metric. (NeurIPS 2023 R0-FoMo Workshop)

### Context & Memory Evolution

- [Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models](https://arxiv.org/abs/2510.04618) - Evolves context as a structured playbook through generation, reflection, and curation while avoiding destructive context collapse. (ICLR 2026)
- [EvolveR: Self-Evolving LLM Agents through an Experience-Driven Lifecycle](https://arxiv.org/abs/2510.16079) - Distills interaction trajectories into reusable strategic principles, retrieves them during future tasks, and reinforces the agent policy in a closed experience loop. (ICML 2026)
- [Learning to Continually Learn via Meta-learning Agentic Memory Designs](https://arxiv.org/abs/2602.07755) - Uses a meta-agent to discover executable memory schemas and retrieval and update mechanisms that continually improve from experience. (arXiv 2026)
- [A-MEM: Agentic Memory for LLM Agents](https://arxiv.org/abs/2502.12110) - Builds a dynamically linked note network whose organization evolves as an agent accumulates new experiences. (NeurIPS 2025)
- [ExpeL: LLM Agents Are Experiential Learners](https://arxiv.org/abs/2308.10144) - Extracts reusable insights from successful and failed trajectories and transfers them to future tasks without weight updates. (AAAI 2024)
- [MemoryBank: Enhancing Large Language Models with Long-Term Memory](https://arxiv.org/abs/2305.10250) - Maintains and selectively forgets long-term interaction memories so an agent can adapt its responses over time. (AAAI 2024)
- [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) - Improves agents across trials by storing natural-language reflections derived from task feedback. (NeurIPS 2023)

### Harness & Scaffold Evolution

- [Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses](https://arxiv.org/abs/2604.25850) - Autonomously evolves tools, middleware, memory, and prompts through observable edits whose predictions are verified on later tasks. (arXiv 2026)
- [AI4AI at Test-Time: Strong-to-Weak Capability Transfer via Harnesses](https://arxiv.org/abs/2608.12307) - Uses stronger builder models to iteratively construct inference-time harnesses that transfer capability to weaker target models without parameter updates. (arXiv 2026)
- [AutoHarness: Improving LLM Agents by Automatically Synthesizing a Code Harness](https://arxiv.org/abs/2603.03329) - Synthesizes and iteratively refines executable harnesses from environment feedback, eliminating illegal actions across 145 TextArena games. (arXiv 2026)
- [Continual Harness: Online Adaptation for Self-Improving Foundation Agents](https://arxiv.org/abs/2605.09998) - Refines prompts, sub-agents, skills, and memory online within a single continuous trajectory and extends the loop to model-weight co-learning. (arXiv 2026)
- [EvoHarness-RL: Learning Self-Evolving Runtime Harness for Long-Horizon LLM Agents](https://arxiv.org/abs/2608.05446) - Trains agents to construct and coordinate evolving Belief, Progress, and Experience state during long-horizon execution. (arXiv 2026)
- [MemoHarness: Agent Harnesses That Learn from Experience](https://arxiv.org/abs/2607.14159) - Learns case-adaptive configurations across six harness control dimensions from execution diagnoses and a reusable experience bank. (arXiv 2026)
- [MetaSkill-Evolve: Recursive Self-Improvement of LLM Agents via Two-Timescale Meta-Skill Evolution](https://arxiv.org/abs/2607.05297) - Evolves task skills in a fast loop and the meta-skills governing its Analyzer, Retriever, Allocator, Proposer, and Evolver in a slower recursive loop. (arXiv 2026)

### Extensible Harness Substrates

Extensible agent runtimes that expose prompts, tools, skills, memory, plugins, or control flow as modifiable surfaces. These systems do not necessarily implement self-improvement by default, but can serve as substrates for RSI experiments.

General extensibility alone is insufficient. An RSI substrate should expose agent-relevant runtime components such as prompts, memory, skills, tools, or control flow as programmatically modifiable surfaces suitable for persistent self-modification experiments.

- [Agent Zero](https://github.com/agent0ai/agent-zero) - Open agentic framework whose prompts, tools, skills, plugins, and multi-agent profiles can be inspected, replaced, and extended.
- [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) - Open-source agent harness from DeepSeek AI built around an everything-is-a-plugin architecture.
- [OpenClaw](https://github.com/openclaw/openclaw) - Persistent agent runtime with workspace-scoped skills and a Skill Workshop where agents can draft reusable skill changes for review and application.
- [Pi](https://github.com/earendil-works/pi) - Self-extensible coding-agent harness with a reusable agent runtime, terminal UI, and unified multi-provider LLM API.

### Self-Verification & Self-Correction — Enabling Foundations

Primarily bounded self-refinement and verification methods that serve as building blocks for persistent self-improving systems.

- [Chain-of-Verification Reduces Hallucination in Large Language Models](https://arxiv.org/abs/2309.11495) - Plans and answers independent verification questions before producing a revised response. (Findings of ACL 2024)
- [CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://arxiv.org/abs/2305.11738) - Uses external tools to validate an output and converts the resulting evidence into iterative corrections. (ICLR 2024)
- [Large Language Models Cannot Self-Correct Reasoning Yet](https://arxiv.org/abs/2310.01798) - Shows that intrinsic self-correction can degrade reasoning without reliable external feedback and defines an important negative baseline. (ICLR 2024)
- [Let's Verify Step by Step](https://arxiv.org/abs/2305.20050) - Trains process reward models to score intermediate reasoning steps and guide more reliable solution selection. (ICLR 2024)
- [Self-Consistency Improves Chain of Thought Reasoning in Language Models](https://arxiv.org/abs/2203.11171) - Samples diverse reasoning paths and selects their most consistent answer to improve inference-time reliability. (ICLR 2023)
- [Self-Refine: Iterative Refinement with Self-Feedback](https://arxiv.org/abs/2303.17651) - Reuses one language model as generator, critic, and refiner to improve outputs over multiple iterations. (NeurIPS 2023)

### Self-Evolving Agent Frameworks

- [AgentFactory: A Self-Evolving Framework Through Executable Subagent Accumulation and Reuse](https://arxiv.org/abs/2603.18000) - Preserves successful solutions as executable subagents and continually refines them from execution feedback for reuse on future tasks. (ACL 2026 System Demonstrations)
- [EvoAgent: An Evolvable Agent Framework with Skill Learning and Multi-Agent Delegation](https://arxiv.org/abs/2604.20133) - Accumulates structured skills through a feedback loop and delegates complex tasks through a hierarchy of sub-agents. (arXiv 2026)
- [Hyperagents](https://arxiv.org/abs/2603.19461) - Combines a task agent with an editable meta-agent whose self-modification procedure can itself evolve and transfer improvements across domains. (arXiv 2026)
- [SIA: Self Improving AI with Harness & Weight Updates](https://arxiv.org/abs/2605.27276) - Uses task feedback to update both an agent's harness and its model weights within one self-improving loop. (arXiv 2026)
- [SkillRise: Agentic Reinforcement Learning for Cross-Task Skill Evolution](https://arxiv.org/abs/2607.26784) - Alternates a single policy between solving tasks and curating a persistent, evolving skill document that later tasks inherit. (arXiv 2026)
- [Alita-G: Self-Evolving Generative Agent for Agent Generation](https://arxiv.org/abs/2510.23601) - Generates, abstracts, and curates reusable MCP tools from successful trajectories to turn a generalist agent into a domain specialist. (arXiv 2025)
- [EvoAgentX: An Automated Framework for Evolving Agentic Workflows](https://arxiv.org/abs/2507.03616) - Unifies workflow generation, execution, evaluation, and evolutionary optimization across agent prompts, tools, and topologies. (arXiv 2025)
- [Gödel Agent: A Self-Referential Agent Framework for Recursive Self-Improvement](https://arxiv.org/abs/2410.04444) - Lets an agent inspect and rewrite its own logic without relying on a fixed hand-designed optimization routine. (ACL 2025)
- [MemEvolve: Meta-Evolution of Agent Memory Systems](https://arxiv.org/abs/2512.18746) - Jointly evolves experiential knowledge and the architecture that encodes, stores, retrieves, and manages agent memory. (arXiv 2025)
- [Self-evolving Agents with Reflective and Memory-Augmented Abilities](https://arxiv.org/abs/2409.00872) - Combines iterative feedback, reflection, and forgetting-aware memory optimization for continual agent adaptation. (Neurocomputing 2025)
- [Agent-Pro: Learning to Evolve via Policy-Level Reflection and Optimization](https://arxiv.org/abs/2402.17574) - Refines an agent's beliefs and behavioral policy from interactive experience using reflection and search. (ACL 2024)
- [Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291) - Builds an expanding skill library and uses environmental feedback for lifelong autonomous learning in Minecraft. (TMLR 2024)

## Multi-Agent Self-Improvement

Systems that use interaction among multiple agents to improve reasoning, policies, or agent populations.

### Co-Evolution

- [Agent0: Unleashing Self-Evolving Agents from Zero Data via Tool-Integrated Reasoning](https://arxiv.org/abs/2511.16043) - Co-evolves curriculum and executor agents initialized from the same base model to improve tool-using reasoning without human-curated data. (arXiv 2025)
- [DEBATE, TRAIN, EVOLVE: Self Evolution of Language Model Reasoning](https://arxiv.org/abs/2505.15734) - Fine-tunes a model on its own multi-agent debate traces and repeats the debate-training loop without ground-truth labels. (EMNLP 2025)
- [EvoAgent: Towards Automatic Multi-Agent Generation via Evolutionary Algorithms](https://arxiv.org/abs/2406.14228) - Applies mutation, crossover, and selection to expand a specialized agent into a diverse multi-agent system. (NAACL 2025)
- [SOTOPIA-π: Interactive Learning of Socially Intelligent Language Agents](https://arxiv.org/abs/2403.08715) - Improves an agent policy through behavior cloning and self-reinforcement on filtered multi-agent social interactions. (ACL 2024)

### Inference-time Debate

Primarily current-run improvement via multi-agent debate, without persistent system change.

- [Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate](https://arxiv.org/abs/2305.19118) - Uses adversarial debate and a judge to counter degeneration of thought during iterative reflection. (EMNLP 2024)
- [Improving Factuality and Reasoning in Language Models through Multiagent Debate](https://arxiv.org/abs/2305.14325) - Iterates proposals and peer critiques among model instances to converge on more factual and accurate answers. (ICML 2024)

## Coding / Software-Engineering Self-Improvement

Agents and training loops that improve code, software-engineering performance, or their own implementations.

### Self-Modifying Coding Agents

- [Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents](https://arxiv.org/abs/2505.22954) - Evolves a coding agent by modifying its own code and retaining empirically validated improvements in an open-ended archive. (ICLR 2026)
- [A Self-Improving Coding Agent](https://arxiv.org/abs/2504.15228) - Demonstrates a coding agent that edits its own implementation and empirically improves on SWE-bench Verified. (ICLR 2025 SSI-FM Workshop)

### Iterative Repair & Training

Mixes current-run repair loops with methods whose learned improvements persist into later iterations.

- [Training Software Engineering Agents and Verifiers with SWE-Gym](https://arxiv.org/abs/2412.21139) - Supplies executable repository tasks and trajectories for training both SWE agents and inference-time verifiers. (ICML 2025)
- [Teaching Large Language Models to Self-Debug](https://arxiv.org/abs/2304.05128) - Teaches models to inspect execution results, explain their code, and repair failures through iterative prompting. (ICLR 2024)
- [AgentCoder: Multi-Agent-based Code Generation with Iterative Testing and Optimisation](https://arxiv.org/abs/2312.13010) - Coordinates programmer, test-designer, and test-executor agents in a feedback loop that iteratively repairs generated code. (arXiv 2023)

## Automated AI R&D

Systems that automate parts of AI research and development, including experimentation, post-training, algorithm discovery, and the improvement of other AI systems.

- [Frontis-MA1: Training an AI4AI Model towards Recursive Self-Improvement in Machine Learning Engineering](https://arxiv.org/abs/2607.28568) - Connects execution-grounded operator training with long-horizon evolution in the open OpenMLE stack, using machine-learning engineering as an AI4AI testbed for RSI. (arXiv 2026)
- [FT-Dojo: Towards Autonomous LLM Fine-Tuning with Language Agents](https://arxiv.org/abs/2603.01712) - Turns data collection, training, evaluation, diagnosis, and strategy revision into an executable environment for autonomous fine-tuning agents. (arXiv 2026)
- [MLEvolve: A Self-Evolving Framework for Automated Machine Learning Algorithm Discovery](https://arxiv.org/abs/2606.06473) - Combines progressive graph search, retrospective memory, and hierarchical code generation for long-horizon end-to-end machine-learning algorithm discovery. (arXiv 2026)
- [Towards End-to-End Automation of AI Research (The AI Scientist-v2)](https://doi.org/10.1038/s41586-026-10265-5) - Uses template-free agentic tree search to propose hypotheses, run experiments, analyze results, and write complete research papers. (Nature 2026)
- [Towards Execution-Grounded Automated AI Research](https://arxiv.org/abs/2601.14525) - Converts LLM pre-training and post-training into executable research environments where evolutionary search learns from experimental outcomes. (arXiv 2026)
- [The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery](https://arxiv.org/abs/2408.06292) - Automates idea generation, experimentation, paper writing, and review to create a reusable loop for machine-learning research. (arXiv 2024)

## Evolutionary & Open-Ended RSI

Evolutionary, quality-diversity, and open-ended processes that continually discover stronger solutions or learning systems.

- [PACEvolve: Enabling Long-Horizon Progress-Aware Consistent Evolution](https://arxiv.org/abs/2601.10657) - Combines hierarchical context management, backtracking, and adaptive sampling to sustain collaborative long-horizon evolutionary search. (arXiv 2026)
- [AlphaEvolve: A Coding Agent for Scientific and Algorithmic Discovery](https://arxiv.org/abs/2506.13131) - Combines language-model code generation, automated evaluation, and evolutionary search to improve algorithms, including components used in AI training. (arXiv 2025)
- [Higher Order and Self-Referential Evolution for Population-based Methods](https://openreview.net/forum?id=3tk6AES1Aj) - Evolves mutation rates and higher-order meta-mutation rates, including a self-referential top-level parameter that modifies itself. (ICML 2024 AutoRL Workshop)
- [Mathematical Discoveries from Program Search with Large Language Models](https://www.nature.com/articles/s41586-023-06924-6) - Introduces FunSearch, an evolutionary loop that pairs a frozen code model with evaluators to discover new programs and mathematical results. (Nature 2024)
- [AutoML-Zero: Evolving Machine Learning Algorithms From Scratch](https://arxiv.org/abs/2003.03384) - Evolves complete learning algorithms from elementary mathematical operations with minimal human design bias. (ICML 2020)
- [AI-GAs: AI-Generating Algorithms, an Alternate Paradigm for Producing General Artificial Intelligence](https://arxiv.org/abs/1905.10985) - Proposes open-ended systems that automatically generate environments, architectures, and learning algorithms. (arXiv 2019)
- [Paired Open-Ended Trailblazer (POET): Endlessly Generating Increasingly Complex and Diverse Learning Environments and Their Solutions](https://arxiv.org/abs/1901.01753) - Co-evolves environments and agents while transferring solutions between emerging challenges. (GECCO 2019)
- [Learning to Learn by Gradient Descent by Gradient Descent](https://arxiv.org/abs/1606.04474) - Meta-learns an optimizer whose recurrent update rule can replace a hand-designed optimization algorithm. (NeurIPS 2016)
- [Quality Diversity: A New Frontier for Evolutionary Computation](https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2016.00040/full) - Formalizes search for collections that are simultaneously diverse and high-performing within their niches. (Frontiers in Robotics and AI 2016)
- [Illuminating Search Spaces by Mapping Elites](https://arxiv.org/abs/1504.04909) - Introduces MAP-Elites for discovering a diverse archive of locally high-quality solutions. (arXiv 2015)
- [POWERPLAY: Training an Increasingly General Problem Solver by Continually Searching for the Simplest Still Unsolvable Problem](https://arxiv.org/abs/1112.5309) - Alternates between inventing new tasks and modifying a solver so its verified skill set continually expands. (Frontiers in Psychology 2013)

## Safety, Alignment & Theory

Safety, stability, goal preservation, corrigibility, and oversight mechanisms for systems that modify or improve themselves over time.

- [The Economics of Recursive Self-Improvement](https://elasticity.institute/rsi-paper.pdf) - Models the AI capability to AI R&D to stronger capability feedback path as an elasticity network and derives conditions for self-sustaining acceleration. (Elasticity Institute 2026)
- [SAHOO: Safeguarded Alignment for High-Order Optimization Objectives in Recursive Self-Improvement](https://arxiv.org/abs/2603.06333) - Monitors alignment drift during recursive self-improvement through goal-drift detection, constraint-preservation checks, and regression-risk analysis. (ICLR 2026 RSI Workshop)
- [TamperBench: Systematically Stress-Testing LLM Safety Under Fine-Tuning and Tampering](https://arxiv.org/abs/2602.06911) - Systematically stress-tests whether safety alignment is preserved under fine-tuning, weight-space modification, and representation tampering. (arXiv 2026)
- [Your Agent May Misevolve: Emergent Risks in Self-evolving LLM Agents](https://arxiv.org/abs/2509.26354) - Studies harmful drift across model, memory, tool, and workflow evolution pathways and proposes the concept of misevolution. (ICLR 2026)
- [Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence](https://arxiv.org/abs/2510.16657) - Studies when iterative training on self-generated data collapses and shows how external verification can stabilize self-improvement while exposing long-run limits. (arXiv 2025)
- [Evaluating Goal Drift in Language Model Agents](https://arxiv.org/abs/2505.02709) - Measures whether long-horizon agents gradually deviate from their assigned objectives under competing environmental pressures. (arXiv 2025)
- [Performance of Bounded-Rational Agents With the Ability to Self-Modify](https://arxiv.org/abs/2011.06275) - Shows that self-modification can amplify errors and gradually misalign bounded-rational agents even when ideal rational agents would preserve their objectives. (AAAI 2021 SafeAI Workshop)
- [AGI Agent Safety by Iteratively Improving the Utility Function](https://arxiv.org/abs/2007.05411) - Designs a safety mechanism that allows an agent's utility function to be iteratively updated while reducing incentives to manipulate the improvement process. (AGI 2020)
- [Scalable Agent Alignment via Reward Modeling: A Research Direction](https://arxiv.org/abs/1811.07871) - Outlines recursive reward modeling for supervising agents on tasks too complex for direct human evaluation. (arXiv 2018)
- [Self-Modification of Policy and Utility Function in Rational Agents](https://arxiv.org/abs/1605.03142) - Formalizes when rational agents preserve or modify their policies and utility functions and derives conditions under which self-modification remains goal-preserving. (AGI 2016)
- [Intelligence Explosion Microeconomics](https://intelligence.org/files/IEM.pdf) - Models the returns and bottlenecks that determine whether recursive improvement accelerates, plateaus, or becomes explosive. (MIRI technical report 2013)

### Supporting Safety Foundations

- [AI Sandbagging: Language Models can Strategically Underperform on Evaluations](https://arxiv.org/abs/2406.07358) - Shows that models can selectively hide capabilities or target lower scores, undermining evaluation-based governance of self-improvement. (ICML 2025)
- [Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training](https://arxiv.org/abs/2401.05566) - Demonstrates deceptive policies that remain hidden through standard safety training and can become more robust to detection. (arXiv 2024)
- [Model Evaluation for Extreme Risks](https://arxiv.org/abs/2305.15324) - Proposes capability and alignment evaluations for dangerous emergent abilities, including autonomous replication and adaptation. (arXiv 2023)
- [Constitutional AI: Harmlessness from AI Feedback](https://arxiv.org/abs/2212.08073) - Uses written principles and model-generated critiques to scale supervision while retaining explicit behavioral constraints. (arXiv 2022)
- [Optimal Policies Tend to Seek Power](https://arxiv.org/abs/1912.01683) - Proves conditions under which optimal agents are incentivized to preserve options and seek control of their environment. (NeurIPS 2021)
- [Reward Tampering Problems and Solutions in Reinforcement Learning: A Causal Influence Diagram Perspective](https://arxiv.org/abs/1908.04734) - Characterizes incentives to corrupt reward processes and gives design principles that remove them. (Synthese 2021)
- [Risks from Learned Optimization in Advanced Machine Learning Systems](https://arxiv.org/abs/1906.01820) - Analyzes mesa-optimizers whose learned objectives may diverge from the objectives used to train them. (arXiv 2019)
- [Concrete Problems in AI Safety](https://arxiv.org/abs/1606.06565) - Frames practical research problems such as reward hacking, scalable oversight, safe exploration, and robustness to distribution shift. (arXiv 2016)
- [Safely Interruptible Agents](https://auai.org/~w-auai/uai2016/proceedings/papers/68.pdf) - Shows how reinforcement-learning agents can be designed without incentives to resist human interruption. (UAI 2016)

## Introspection & Self-Modeling

Research on whether AI systems can model, diagnose, predict, and reason about their own behavior and internal states, capabilities that may support effective self-improvement.

- [Emergent Introspective Awareness in Large Language Models](https://arxiv.org/abs/2601.01828) - Probes whether language models can detect, report, and deliberately influence their own internal representations rather than merely infer properties of themselves from text. (arXiv 2026)
- [Self-Reference in Large Language Models: The Introspection Threshold for Recursive Self-Improvement](https://arxiv.org/abs/2607.04277) - Argues that sustainable recursive self-improvement requires systems to model their own operations and identifies introspective self-reference as a potential threshold for recursive improvement. (arXiv 2026)
- [Structure Enables Effective Self-Localization of Errors in LLMs](https://arxiv.org/abs/2602.02416) - Shows that structured reasoning enables models to identify where their own reasoning first goes wrong and use that localization for autonomous correction. (ICLR 2026)
- [Looking Inward: Language Models Can Learn About Themselves by Introspection](https://arxiv.org/abs/2410.13787) - Tests privileged self-prediction by comparing a model's forecasts of its own behavior with those of other models. (ICLR 2025)
- [Tell me about yourself: LLMs are aware of their learned behaviors](https://arxiv.org/abs/2501.11120) - Finds that fine-tuned models can articulate learned behavioral tendencies without explicit descriptions of those behaviors in training data. (arXiv 2025)
- [Recursive Introspection: Teaching Language Model Agents How to Self-Improve](https://arxiv.org/abs/2407.18219) - Trains language models to inspect unsuccessful prior attempts and recursively improve their responses across subsequent interaction turns. (NeurIPS 2024)
- [Self-Recognition in Language Models](https://arxiv.org/abs/2407.06946) - Tests whether models can identify their own outputs using model-generated security questions and finds no general self-recognition. (EMNLP 2024)
- [Do Large Language Models Know What They Don't Know?](https://arxiv.org/abs/2305.18153) - Evaluates model self-knowledge by testing recognition of unanswerable and unknowable questions. (Findings of ACL 2023)
- [Language Models (Mostly) Know What They Know](https://arxiv.org/abs/2207.05221) - Measures whether models can evaluate their own claims and predict which questions they know how to answer. (arXiv 2022)
- [Bounded Recursive Self-Improvement](https://arxiv.org/abs/1312.6764) - Studies an implemented goal-directed system that improves its behavior through an explicitly bounded self-modeling loop. (arXiv 2013)

## Benchmarks & Evaluations

Benchmarks grouped by how directly they provide evidence about recursive self-improvement, from explicit improvement loops to enabling research and long-horizon agent capabilities.

### Direct RSI & Self-Improvement Evaluations

- [OpenAI RSI Index](https://openai.com/index/gpt-5-6/) - Reports OpenAI's aggregate internal evaluations for debugging research systems, optimizing kernels and training recipes, running machine-learning experiments, and improving another model, but is not externally reproducible. (OpenAI internal 2026)
- [PostTrainBench: Can LLM Agents Automate LLM Post-Training?](https://arxiv.org/abs/2603.08640) - Gives autonomous agents one base model, one H100 GPU, and ten hours to research and execute the strongest post-training strategy they can find. (ICML 2026)
- [RSI-Bench](https://github.com/sunghunkwag/rsi-bench) - Provides an open-source six-axis framework for measuring self-modification depth, improvement trajectories, operator discovery, adaptation, safety, and goal generation. (community framework 2026)
- [RSIBench-Data](https://arxiv.org/abs/2607.25886) - Isolates data-centric RSI by asking agents to iteratively improve training-data strategies against checkpoint feedback under a fixed post-training stack. (arXiv 2026)

### Automated AI R&D Evaluations

- [MLE-bench](https://github.com/openai/mle-bench) - Measures end-to-end machine-learning engineering performance across 75 Kaggle competitions and is used to track model self-improvement capability. (ICLR 2025)
- [PaperBench](https://github.com/openai/frontier-evals/tree/main/project/paperbench) - Evaluates agents on replicating state-of-the-art AI research from paper descriptions. (ICML 2025)
- [RE-Bench](https://github.com/METR/RE-Bench) - Compares AI agents with human experts on open-ended machine-learning research-engineering tasks under fixed time budgets. (ICML 2025)
- [MLAgentBench](https://github.com/snap-stanford/MLAgentBench) - Tests whether language agents can autonomously execute and improve machine-learning experiments from research instructions. (ICML 2024)

### Long-Horizon & Agent Capability Evaluations

- [Long-Horizon-Terminal-Bench](https://arxiv.org/abs/2607.08964) - Evaluates agents on 46 terminal tasks requiring sustained execution across hundreds of episodes with dense intermediate rewards. (arXiv 2026)
- [OSWorld 2.0](https://arxiv.org/abs/2606.29537) - Measures computer-use agents on 108 realistic end-to-end workflows whose median human completion time is about 1.6 hours. (arXiv 2026)
- [MCPMark](https://arxiv.org/abs/2509.24002) - Stress-tests realistic stateful MCP workflows across SaaS, development, browser, filesystem, and database environments with programmatic grading. (arXiv 2025)
- [METR Task-Completion Time Horizon](https://arxiv.org/abs/2503.14499) - Estimates the human-equivalent task duration at which an agent succeeds with a given probability on non-trivially parallelizable software tasks. (NeurIPS 2025)
- [SWE-Bench Pro](https://arxiv.org/abs/2509.16941) - Tests coding agents on 1,865 contamination-resistant enterprise tasks designed to require hours or days of professional software engineering. (arXiv 2025)
- [TheAgentCompany](https://arxiv.org/abs/2412.14161) - Evaluates agents on 175 cross-application workplace tasks inside a simulated software company with result and checkpoint grading. (NeurIPS 2025)
- [SWE-bench](https://github.com/SWE-bench/SWE-bench) - Provides reproducible real-world software issues used to evaluate coding agents and empirical self-modification systems such as DGM. (ICLR 2024)
- [SWE-bench Verified](https://openai.com/index/introducing-swe-bench-verified/) - Supplies a human-validated subset that reduces broken or underspecified tasks when measuring iterative coding-agent improvements. (OpenAI benchmark 2024)

## Frameworks & Tools

### Self-Modifying / Self-Evolving Systems

- [AgentFactory](https://github.com/zzatpku/AgentFactory) - Self-evolving framework that accumulates and reuses executable subagents to improve future task solving.
- [Darwin Gödel Machine](https://github.com/jennyzzt/dgm) - Official self-modifying coding-agent implementation with open-ended archive-based evolution.
- [Gödel Agent](https://github.com/Arvid-pku/Godel_Agent) - Official implementation of Gödel Agent: A Self-Referential Agent Framework for Recursive Self-Improvement.
- [Hermes Agent](https://github.com/NousResearch/hermes-agent) - Self-improving personal agent with a built-in learning loop that creates and refines skills from experience.
- [HyperAgents](https://github.com/facebookresearch/HyperAgents) - Self-referential agent framework in which an editable meta-agent improves itself and the task agent for computable objectives.
- [SEAL](https://github.com/Continual-Intelligence/SEAL) - Official code for language models that generate their own adaptation data and update instructions.
- [SIA](https://github.com/hexo-ai/sia) - Self-improving AI framework that iteratively updates an agent harness and, when configured, the target model's weights.

### Harness / Memory / Skill Evolution

- [ACE](https://github.com/ace-agent/ace) - Official implementation of Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models.
- [ALMA](https://github.com/zksha/alma) - Official implementation of Learning to Continually Learn via Meta-learning Agentic Memory Designs.
- [Continual Harness](https://github.com/sethkarten/continual-harness) - Self-improving agent harness that adapts online from experience while maintaining a continuous environment trajectory.
- [EvoAgentX](https://github.com/EvoAgentX/EvoAgentX) - Self-evolving agent framework for automatically building, evaluating, and optimizing agentic workflows.
- [EvolveR](https://github.com/KnowledgeXLab/EvolveR) - Self-evolving LLM-agent framework that improves through a closed-loop, experience-driven lifecycle.
- [Letta Code](https://github.com/letta-ai/letta-code) - Memory-first coding-agent harness whose long-lived agents rewrite context and learn skills from experience.
- [Memento-Skills](https://github.com/Memento-Teams/Memento-Skills) - Self-evolving agent framework that retrieves, evaluates, repairs, and rewrites persistent skills through reflective learning.
- [Voyager](https://github.com/MineDojo/Voyager) - Embodied lifelong-learning agent with automatic curriculum, iterative prompting, and a reusable skill library.

### Automated Search / AI R&D

- [ADAS](https://github.com/ShengranHu/ADAS) - Official implementation of a meta-agent that searches over executable agent designs.
- [AI Scientist](https://github.com/SakanaAI/AI-Scientist) - End-to-end system for generating machine-learning ideas, running experiments, and writing research papers.
- [autoresearch](https://github.com/karpathy/autoresearch) - Runs an autonomous loop that edits an LLM training program, trains for five minutes, and keeps only changes that improve validation bits per byte.
- [Evolutionary Model Merge](https://github.com/SakanaAI/evolutionary-model-merge) - Evolves combinations of open models in parameter and data-flow space.
- [FunSearch](https://github.com/google-deepmind/funsearch) - Reference implementation of LLM-guided evolutionary program search with executable evaluators.
- [MLEvolve](https://github.com/InternScience/MLEvolve) - Self-evolving multi-agent framework for end-to-end machine-learning algorithm discovery using progressive search and experience-driven memory.
- [OpenEvolve](https://github.com/algorithmicsuperintelligence/openevolve) - Open-source evolutionary coding agent inspired by AlphaEvolve-style program optimization.
- [POET](https://github.com/uber-research/poet) - Reference implementation for co-evolving environments and their paired agents.

## Blog Posts & Discussions

- [A Taxonomy of Self-Evolving Agents](https://lsl.zone/blog/2026/a-taxonomy-of-self-evolving-agents/) - Distinguishes Model, Harness, and Artifact evolution, complementing this list's own taxonomy. (2026)
- [AlphaEvolve: A Gemini-Powered Coding Agent for Designing Advanced Algorithms](https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/) - Google DeepMind explains AlphaEvolve's evaluator-guided evolution loop and its applications to computing and AI training. (2025)
- [The Darwin Gödel Machine: AI That Improves Itself by Rewriting Its Own Code](https://sakana.ai/dgm/) - Sakana AI explains DGM's empirical alternative to proof-based Gödel Machine self-modification. (2025)
- [When AI Builds Itself](https://www.anthropic.com/institute/recursive-self-improvement) - Anthropic analyzes early evidence, possible paths, and governance challenges for AI-driven AI development. (2025)
- [The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery](https://sakana.ai/ai-scientist/) - Sakana AI presents its automated research pipeline, results, limitations, and open implementation. (2024)
- [Evidence on Recursive Self-Improvement from Current ML](https://www.lesswrong.com/posts/byKF3mnaNRrbkDPWv/evidence-on-recursive-self-improvement-from-current-ml) - Reviews empirical evidence for and against strong returns from AI-assisted AI research. (2023)
- [FunSearch: Making New Discoveries in Mathematical Sciences Using Large Language Models](https://deepmind.google/blog/funsearch-making-new-discoveries-in-mathematical-sciences-using-large-language-models/) - Google DeepMind describes how evolutionary program search produced verifiable mathematical and algorithmic discoveries. (2023)
- [Metalearning Machines Learn to Learn](https://people.idsia.ch/~juergen/metalearning.html) - Jürgen Schmidhuber traces self-referential meta-learning from 1987 through Gödel Machines and modern learned optimizers. (2020)
- [Recursive Self-Improvement](https://www.alignmentforum.org/w/recursive-self-improvement) - The Alignment Forum overview connects self-improving AI to takeoff dynamics, seed AI, and control concerns. (2016)

## Talks & Videos

- [Escape Velocity: The Inflection Point for Recursive Self Improvement](https://slideslive.com/39064188/escape-velocity-the-inflection-point-for-recursive-self-improvement) - Louis Kirsch discusses automated AI research and the conditions required for sustained recursive improvement at the ICLR 2026 RSI workshop. (2026)
- [ICLR 2026 Workshop on AI with Recursive Self-Improvement](https://iclr.cc/virtual/2026/workshop/10000796) - Official video archive for invited talks, contributed work, and panels focused specifically on RSI. (2026)
- [Self-Improving Foundation Models Without Human Supervision](https://iclr.cc/virtual/2025/workshop/23971) - Official ICLR 2025 workshop recordings on synthetic data, weak-to-strong learning, and autonomous adaptation. (2025)
- [Gödel Machine](https://www.youtube.com/watch?v=voczu4I3_xQ) - Jürgen Schmidhuber gives a concise explanation of self-referential, proof-guided code rewriting and its computability limits. (2015)

## Related Awesome Lists

- [Awesome AI Agents](https://github.com/e2b-dev/awesome-ai-agents) - Broad directory of autonomous-agent projects and infrastructure that can serve as components or baselines for self-improving systems. (2023)
- [Awesome AutoML Papers](https://github.com/hibayesian/awesome-automl-papers) - Curated literature on automated model selection, architecture search, hyperparameter optimization, and related techniques. (2018)
- [Awesome Self-Improving Agents](https://github.com/selfimproving-agent/awesome-Self-Improving-Agents) - Focused bibliography of foundation-model agents that update their models, memory, tools, prompts, or workflows. (2024)

## Contributing

Contributions are welcome. Please read the [contribution guidelines](CONTRIBUTING.md) before submitting a pull request.
