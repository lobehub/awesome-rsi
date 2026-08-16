<!--lint disable awesome-github-->
<!-- This repository is intentionally local-only until the publication step. -->

# Awesome RSI (Recursive Self-Improvement) [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of resources on recursive self-improvement in artificial intelligence.

Recursive self-improvement (RSI) is the process by which an AI system improves its own capabilities, including the methods it uses to make further improvements. RSI matters because increasingly autonomous improvement could accelerate AI progress while introducing difficult questions about evaluation, control, and alignment; here, **RSI refers to recursive self-improvement, not the financial Relative Strength Index**.

## Contents

- [Papers](#papers)
  - [Surveys](#surveys)
  - [Self-Improving Agents](#self-improving-agents)
  - [Self-Modifying Code & AutoML](#self-modifying-code--automl)
  - [Evolutionary & Open-Ended Methods](#evolutionary--open-ended-methods)
  - [Safety & Alignment](#safety--alignment)
- [Frameworks & Tools](#frameworks--tools)
- [Benchmarks & Evaluations](#benchmarks--evaluations)
- [Blog Posts & Articles](#blog-posts--articles)
- [Talks & Videos](#talks--videos)
- [Related Awesome Lists](#related-awesome-lists)

## Papers

Peer-reviewed papers, preprints, and substantial technical reports that directly study RSI or mechanisms that enable it.

### Surveys

- [A Comprehensive Survey of Self-Evolving AI Agents: A New Paradigm Bridging Foundation Models and Lifelong Agentic Systems](https://arxiv.org/abs/2508.07407) - Organizes agent evolution around feedback loops, update targets, domain applications, evaluation, and safety. (2025)
- [A Survey of Self-Evolving Agents: On Path to Artificial Super Intelligence](https://arxiv.org/abs/2507.21046) - Surveys what, when, and how foundation-model agents can evolve across models, memory, tools, and architectures. (2025)
- [A Survey on Self-Evolution of Large Language Models](https://arxiv.org/abs/2404.14387) - Presents a four-stage taxonomy of experience acquisition, refinement, updating, and evaluation for self-evolving LLMs. (2024)

### Self-Improving Agents

- [Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents](https://arxiv.org/abs/2505.22954) - Evolves a coding agent by modifying its own code and retaining empirically validated improvements in an open-ended archive. (2025)
- [Self-Adapting Language Models](https://arxiv.org/abs/2506.10943) - Introduces SEAL, which generates its own update data and fine-tuning directives to adapt model weights to new tasks. (2025)
- [Automated Design of Agentic Systems](https://arxiv.org/abs/2408.08435) - Uses a meta-agent to invent and iteratively improve agent architectures represented as executable code. (2024)
- [Gödel Agent: A Self-Referential Agent Framework for Recursive Self-Improvement](https://arxiv.org/abs/2410.04444) - Lets an agent inspect and rewrite its own logic without relying on a fixed hand-designed optimization routine. (2024)
- [Self-Play Fine-Tuning Converts Weak Language Models to Strong Language Models](https://arxiv.org/abs/2401.01335) - Iteratively improves one language model through self-play preference learning without additional human annotations. (2024)
- [Self-Rewarding Language Models](https://arxiv.org/abs/2401.10020) - Trains language models to generate and judge their own instruction-following data over repeated alignment rounds. (2024)
- [The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery](https://arxiv.org/abs/2408.06292) - Automates idea generation, experimentation, paper writing, and review to create a reusable loop for machine-learning research. (2024)
- [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) - Improves agents across trials by storing natural-language reflections derived from task feedback. (2023)
- [RLAIF vs. RLHF: Scaling Reinforcement Learning from Human Feedback with AI Feedback](https://arxiv.org/abs/2309.00267) - Studies reinforcement learning from AI-generated preferences as a scalable alternative to direct human feedback. (2023)
- [Self-Refine: Iterative Refinement with Self-Feedback](https://arxiv.org/abs/2303.17651) - Reuses one language model as generator, critic, and refiner to improve outputs over multiple iterations. (2023)
- [Self-Taught Optimizer (STOP): Recursively Self-Improving Code Generation](https://arxiv.org/abs/2310.02304) - Demonstrates an LLM-written scaffolding program that improves the program responsible for making further improvements. (2023)
- [Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291) - Builds an expanding skill library and uses environmental feedback for lifelong autonomous learning in Minecraft. (2023)

### Self-Modifying Code & AutoML

- [AlphaEvolve: A Coding Agent for Scientific and Algorithmic Discovery](https://arxiv.org/abs/2506.13131) - Combines language-model code generation, automated evaluation, and evolutionary search to improve algorithms, including components used in AI training. (2025)
- [AutoML-Zero: Evolving Machine Learning Algorithms From Scratch](https://arxiv.org/abs/2003.03384) - Evolves complete learning algorithms from elementary mathematical operations with minimal human design bias. (2020)
- [Learning to Learn by Gradient Descent by Gradient Descent](https://arxiv.org/abs/1606.04474) - Meta-learns an optimizer whose recurrent update rule can replace a hand-designed optimization algorithm. (2016)
- [Gödel Machines: Self-Referential Universal Problem Solvers Making Provably Optimal Self-Improvements](https://arxiv.org/abs/cs/0309048) - Defines a fully self-referential machine that rewrites itself after proving a modification improves expected utility. (2003)
- [Optimal Ordered Problem Solver](https://arxiv.org/abs/cs/0207097) - Introduces an asymptotically optimal program-search system that reuses solutions to accelerate later problem solving. (2002)
- [Evolutionary Principles in Self-Referential Learning, or on Learning How to Learn: The Meta-Meta-... Hook](https://people.idsia.ch/~juergen/diploma1987ocr.pdf) - Describes early meta-evolution and self-referential learning mechanisms that recursively improve learning methods. (1987)

### Evolutionary & Open-Ended Methods

- [Mathematical Discoveries from Program Search with Large Language Models](https://www.nature.com/articles/s41586-023-06924-6) - Introduces FunSearch, an evolutionary loop that pairs a frozen code model with evaluators to discover new programs and mathematical results. (2024)
- [AI-GAs: AI-Generating Algorithms, an Alternate Paradigm for Producing General Artificial Intelligence](https://arxiv.org/abs/1905.10985) - Proposes open-ended systems that automatically generate environments, architectures, and learning algorithms. (2019)
- [Paired Open-Ended Trailblazer (POET): Endlessly Generating Increasingly Complex and Diverse Learning Environments and Their Solutions](https://arxiv.org/abs/1901.01753) - Co-evolves environments and agents while transferring solutions between emerging challenges. (2019)
- [Quality Diversity: A New Frontier for Evolutionary Computation](https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2016.00040/full) - Formalizes search for collections that are simultaneously diverse and high-performing within their niches. (2016)
- [Illuminating Search Spaces by Mapping Elites](https://arxiv.org/abs/1504.04909) - Introduces MAP-Elites for discovering a diverse archive of locally high-quality solutions. (2015)
- [POWERPLAY: Training an Increasingly General Problem Solver by Continually Searching for the Simplest Still Unsolvable Problem](https://arxiv.org/abs/1112.5309) - Alternates between inventing new tasks and modifying a solver so its verified skill set continually expands. (2011)

### Safety & Alignment

- [Model Evaluation for Extreme Risks](https://arxiv.org/abs/2305.15324) - Proposes capability and alignment evaluations for dangerous emergent abilities, including autonomous replication and adaptation. (2023)
- [Constitutional AI: Harmlessness from AI Feedback](https://arxiv.org/abs/2212.08073) - Uses written principles and model-generated critiques to scale supervision while retaining explicit behavioral constraints. (2022)
- [Optimal Policies Tend to Seek Power](https://arxiv.org/abs/1912.01683) - Proves conditions under which optimal agents are incentivized to preserve options and seek control of their environment. (2021)
- [Reward Tampering Problems and Solutions in Reinforcement Learning: A Causal Influence Diagram Perspective](https://arxiv.org/abs/1908.04734) - Characterizes incentives to corrupt reward processes and gives design principles that remove them. (2019)
- [Risks from Learned Optimization in Advanced Machine Learning Systems](https://arxiv.org/abs/1906.01820) - Analyzes mesa-optimizers whose learned objectives may diverge from the objectives used to train them. (2019)
- [Scalable Agent Alignment via Reward Modeling: A Research Direction](https://arxiv.org/abs/1811.07871) - Outlines recursive reward modeling for supervising agents on tasks too complex for direct human evaluation. (2018)
- [Concrete Problems in AI Safety](https://arxiv.org/abs/1606.06565) - Frames practical research problems such as reward hacking, scalable oversight, safe exploration, and robustness to distribution shift. (2016)
- [Safely Interruptible Agents](https://auai.org/~w-auai/uai2016/proceedings/papers/68.pdf) - Shows how reinforcement-learning agents can be designed without incentives to resist human interruption. (2016)
- [Bounded Recursive Self-Improvement](https://arxiv.org/abs/1312.6764) - Studies an implemented goal-directed system that improves its behavior through an explicitly bounded self-modeling loop. (2013)
- [Intelligence Explosion Microeconomics](https://intelligence.org/files/IEM.pdf) - Models the returns and bottlenecks that determine whether recursive improvement accelerates, plateaus, or becomes explosive. (2013)

## Frameworks & Tools

- [ADAS](https://github.com/ShengranHu/ADAS) - Official implementation of a meta-agent that searches over executable agent designs.
- [AI Scientist](https://github.com/SakanaAI/AI-Scientist) - End-to-end system for generating machine-learning ideas, running experiments, and writing research papers.
- [auto-sklearn](https://github.com/automl/auto-sklearn) - Automated machine-learning toolkit for model selection, hyperparameter optimization, and ensembling.
- [Darwin Gödel Machine](https://github.com/jennyzzt/dgm) - Official self-modifying coding-agent implementation with open-ended archive-based evolution.
- [Evolutionary Model Merge](https://github.com/SakanaAI/evolutionary-model-merge) - Evolves combinations of open models in parameter and data-flow space.
- [FunSearch](https://github.com/google-deepmind/funsearch) - Reference implementation of LLM-guided evolutionary program search with executable evaluators.
- [NNI](https://github.com/microsoft/nni) - Neural architecture search, hyperparameter tuning, pruning, and model-compression toolkit.
- [OpenEvolve](https://github.com/algorithmicsuperintelligence/openevolve) - Open-source evolutionary coding agent inspired by AlphaEvolve-style program optimization.
- [POET](https://github.com/uber-research/poet) - Reference implementation for co-evolving environments and their paired agents.
- [SEAL](https://github.com/Continual-Intelligence/SEAL) - Official code for language models that generate their own adaptation data and update instructions.
- [Voyager](https://github.com/MineDojo/Voyager) - Embodied lifelong-learning agent with automatic curriculum, iterative prompting, and a reusable skill library.

## Benchmarks & Evaluations

- [MLAgentBench](https://github.com/snap-stanford/MLAgentBench) - Tests whether language agents can autonomously execute and improve machine-learning experiments from research instructions.
- [MLE-bench](https://github.com/openai/mle-bench) - Measures end-to-end machine-learning engineering performance across 75 Kaggle competitions and is used to track model self-improvement capability.
- [PaperBench](https://github.com/openai/preparedness/tree/main/project/paperbench) - Evaluates agents on replicating state-of-the-art AI research from paper descriptions.
- [RE-Bench](https://github.com/METR/RE-Bench) - Compares AI agents with human experts on open-ended machine-learning research-engineering tasks under fixed time budgets.
- [SWE-bench](https://github.com/SWE-bench/SWE-bench) - Provides reproducible real-world software issues used to evaluate coding agents and empirical self-modification systems such as DGM.
- [SWE-bench Verified](https://openai.com/index/introducing-swe-bench-verified/) - Supplies a human-validated subset that reduces broken or underspecified tasks when measuring iterative coding-agent improvements.

## Blog Posts & Articles

- [AlphaEvolve: A Gemini-Powered Coding Agent for Designing Advanced Algorithms](https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/) - Google DeepMind explains AlphaEvolve's evaluator-guided evolution loop and its applications to computing and AI training.
- [Evidence on Recursive Self-Improvement from Current ML](https://www.lesswrong.com/posts/byKF3mnaNRrbkDPWv/evidence-on-recursive-self-improvement-from-current-ml) - Reviews empirical evidence for and against strong returns from AI-assisted AI research.
- [FunSearch: Making New Discoveries in Mathematical Sciences Using Large Language Models](https://deepmind.google/blog/funsearch-making-new-discoveries-in-mathematical-sciences-using-large-language-models/) - Google DeepMind describes how evolutionary program search produced verifiable mathematical and algorithmic discoveries.
- [Metalearning Machines Learn to Learn](https://people.idsia.ch/~juergen/metalearning.html) - Jürgen Schmidhuber traces self-referential meta-learning from 1987 through Gödel Machines and modern learned optimizers.
- [Recursive Self-Improvement](https://www.alignmentforum.org/w/recursive-self-improvement) - The Alignment Forum overview connects self-improving AI to takeoff dynamics, seed AI, and control concerns.
- [The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery](https://sakana.ai/ai-scientist/) - Sakana AI presents its automated research pipeline, results, limitations, and open implementation.
- [The Darwin Gödel Machine: AI That Improves Itself by Rewriting Its Own Code](https://sakana.ai/dgm/) - Sakana AI explains DGM's empirical alternative to proof-based Gödel Machine self-modification.
- [When AI Builds Itself](https://www.anthropic.com/institute/recursive-self-improvement) - Anthropic analyzes early evidence, possible paths, and governance challenges for AI-driven AI development.

## Talks & Videos

- [Escape Velocity: The Inflection Point for Recursive Self Improvement](https://slideslive.com/39064188/escape-velocity-the-inflection-point-for-recursive-self-improvement) - Louis Kirsch discusses automated AI research and the conditions required for sustained recursive improvement at the ICLR 2026 RSI workshop.
- [Gödel Machine](https://www.youtube.com/watch?v=voczu4I3_xQ) - Jürgen Schmidhuber gives a concise explanation of self-referential, proof-guided code rewriting and its computability limits.
- [ICLR 2026 Workshop on AI with Recursive Self-Improvement](https://iclr.cc/virtual/2026/workshop/10000796) - Official video archive for invited talks, contributed work, and panels focused specifically on RSI.
- [Self-Improving Foundation Models Without Human Supervision](https://iclr.cc/virtual/2025/workshop/23971) - Official ICLR 2025 workshop recordings on synthetic data, weak-to-strong learning, and autonomous adaptation.

## Related Awesome Lists

- [Awesome AI Agents](https://github.com/e2b-dev/awesome-ai-agents) - Broad directory of autonomous-agent projects and infrastructure that can serve as components or baselines for self-improving systems.
- [Awesome AutoML Papers](https://github.com/hibayesian/awesome-automl-papers) - Curated literature on automated model selection, architecture search, hyperparameter optimization, and related techniques.
- [Awesome Self-Improving Agents](https://github.com/selfimproving-agent/awesome-Self-Improving-Agents) - Focused bibliography of foundation-model agents that update their models, memory, tools, prompts, or workflows.

## Contributing

Contributions are welcome. Please read the [contribution guidelines](CONTRIBUTING.md) before submitting a pull request.
