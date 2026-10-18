# Contribution Guidelines

Thank you for helping improve Awesome RSI. This list is curated rather than exhaustive, so every proposed resource should be useful, credible, and directly relevant to AI recursive self-improvement.

## Inclusion Criteria

A resource should:

- Study recursive self-improvement itself, demonstrate self-improvement that persists across iterations, or provide evaluation or safety evidence directly bearing on either of those areas.
- Link to a stable primary or authoritative source whenever one is available.
- Offer substantive technical, empirical, historical, or conceptual value.
- Be publicly accessible, or clearly identify any access restrictions.
- Fit an existing category; propose a new category only when several high-quality resources justify it.

Broad enabling methods are not sufficient on their own. A contribution must make a specific, evidence-based case for its relationship to recursive or persistent self-improvement rather than merely sharing techniques such as prompting, synthetic data, memory, search, or multi-agent interaction.

Meta-learning, continual or lifelong learning, online learning, and test-time adaptation are related enabling families, but are not sufficient for inclusion unless the system controls or generates persistent updates from its own experience.

Canonical enabling works may be included when they establish a mechanism that is directly reused by later self-improving systems.

Resources about the financial Relative Strength Index are out of scope.

## Evidence of Self-Improvement

When a resource claims persistent or recursive self-improvement, submissions should explain what evidence supports the claim.

Relevant evidence may include:

- Task-level performance improvements against an appropriate baseline.
- Persistence of modifications across subsequent tasks or iterations.
- Performance on independent or held-out evaluations.
- Comparisons between original and modified improvement procedures.
- Resource-controlled comparisons covering inference cost, compute, tools, data, and external assistance.
- Multi-round results demonstrating whether improvements remain useful or transfer to new tasks.

A self-referential architecture, repeated optimization loop, or increasing task score is insufficient on its own to establish improved update capability.

Claims of improver gain should distinguish improvements to the task-solving system from improvements to the mechanism responsible for producing future system updates.

When evidence is incomplete, the resource may still be included if it satisfies the existing inclusion criteria, but its description must not overstate the demonstrated result.

## Benchmark and Capability Proxy Admission

General capability benchmarks are out of scope unless they measure a bottleneck
that directly constrains persistent or recursive self-improvement.

Relevant bottlenecks may include:
- autonomous AI research and engineering;
- long-horizon autonomous execution;
- adaptive interaction and generalization in novel environments;
- self-modification or improvement of models, agents, harnesses, or code.

Difficulty alone is insufficient for inclusion.
General knowledge and closed-ended reasoning benchmarks are out of scope unless
there is specific evidence connecting them to self-improvement capability.

## Artifact Availability

Every entry that rests on an evaluation must state which artifacts are public. The status classifies the artifacts behind the claim the entry makes, not an arbitrary experiment from the same paper.

The reproducibility artifact set has five components: the task set or generative task source; the scoring logic; the evaluation harness; the data or checkpoints; and the execution environment, including any required non-public infrastructure.

**Publicly available** means retrievable by anyone through a stable locator (URL, DOI, release tag) without an access request, email gate, payment, licence negotiation, or institutional affiliation.

Decide in this order:

1. **Not applicable** — the resource reports no evaluation whose rerun depends on this artifact set. Surveys, position papers, and theory papers that illustrate rather than evaluate qualify. A paper that reports an experiment on a public dataset does not.
2. **Open** — every component the reported evaluation actually requires is publicly available.
3. **Internal** — an independent party cannot reproduce any meaningful part of the reported evaluation using only public artifacts. Evaluations that depend on non-public task sets or non-public infrastructure are always Internal, however much ancillary code is released.
4. **Partial** — everything else: some components are public and a material part is not, but the public part still supports some meaningful, independently checkable part of the evaluation.

The decisive test for Partial vs Internal: using only public artifacts, can an independent party rerun or meaningfully check some part of the reported evaluation? Yes → Partial. No → Internal.

Two guard rails:

- Classify by the strongest claim that can be independently checked, not by intent or by how much code was released. Shipping a training library while withholding the evaluation does not make an entry Partial.
- Defaults run downward. A claim of Open or Partial that cites no specific public locator, and does not name the non-public components, is set to the lower level until evidence is supplied.

A submission must state the status; a locator for each public component; what each missing component is and why it is unavailable; and any evaluation the resource itself flags as non-reproducible.

Artifact status is the author's declaration. Maintainers do not rewrite it on the author's behalf; they identify “should be X + missing components” and ask the author to correct the submission.

Status is recorded in the submission metadata. Entries in this README do not carry status markers; where reproducibility is materially limited, state that plainly in the entry description instead.

## Entry Format

Use this format:

```markdown
- [Research Resource Name](https://example.com/paper) - One concise, neutral description sentence. (Venue 2026)
- [Tool Name](https://example.com/tool) - One concise, neutral description sentence.
```

- Include a working direct link.
- Write exactly one concise, neutral description sentence, read through its first sentence-ending punctuation.
- End that description sentence with a period before any publication annotation. The trailing publication annotation is metadata, so the entire Markdown line need not end with a period.
- Use the resource's official title and preserve model or system version names exactly.
- Avoid promotional language and tracking parameters.
- Avoid duplicate resources or identical links. A paper and its official implementation may be listed separately when they serve different purposes.

Every submission or pull request must also provide:

1. **What is being improved?** Identify the model, agent policy, prompt, memory, harness, codebase, optimizer, or other target.
2. **Does the improvement persist across iterations?** State what artifact or behavior carries forward, or explicitly state that it does not.
3. **Is the improvement mechanism itself subject to improvement?** Explain whether and how the process producing improvements can itself change.
4. **Why is this specifically relevant to RSI?** Connect the work directly to recursive self-improvement, persistent self-improvement, or evaluation or safety evidence for those systems.
5. **Publication status:** Identify the status and include the venue and year where applicable, for example `arXiv preprint (2026)`, `workshop: AutoRL@ICML (2024)`, `conference: ICML (2025)`, or `journal: Nature (2026)`.
6. **Public artifacts and evaluation artifact status**

## Ordering

Sort entries only within the same heading's direct-entry list. Never sort across headings or flatten a parent and its children. Contents, prose, explanatory bullets, images, and fenced code examples are outside this check.

Each resource-bearing heading must have an explicit policy in the table below and in the checker. Unregistered headings or unsupported entry syntax are “unable to determine”, never a silent pass.

**Year policy:** sort by publication year descending, then by title key ascending, then by the exact original title ascending, then by the exact URL ascending. Take the year only from the final parenthesized publication annotation in the description; permit one trailing period after that annotation for compatibility. That annotation must contain exactly one standalone four-digit year in 1900–2099. Do not infer a year from the title, URL, arXiv identifier, access date, or PR metadata. A missing or ambiguous year requires correction before the order can be determined.

**Alphabetical policy:** sort by title key, exact original title, then exact URL, all ascending; any publication year annotation is ignored for ordering.

**Title key:** take the exact plain-text link label; apply Unicode NFKC normalization, then Unicode lowercase (not locale collation). Do not strip leading articles: the original title string is the sorting subject; apply only the mechanical normalization specified here, without changing the displayed title. Split at whitespace, `/`, and Unicode dash punctuation (category Pd, including the ASCII hyphen). Within each token delete all characters other than Unicode letters and numbers (categories L and N); discard empty tokens. Compare the resulting tuple of tokens lexicographically by Unicode code point; a shorter prefix sorts first. Do not remove accents or use natural-number sorting. Thus `2` and `10` are compared as text. Preserve the displayed official title unchanged.

Original-title and URL tie-breakers compare the exact strings from the Markdown link, case-sensitively by Unicode code point, without URL normalization. Identical title and URL keys tie; preserve their relative order and report duplicates separately through the existing duplicate policy. A title with an empty normalized key is invalid.

A heading containing both papers and frameworks still uses its registered policy: resource type is not guessed from the URL. In year-policy headings, frameworks and reports must also have an authoritative publication/release year annotation. Undated tools belong in an appropriate alphabetical heading. A parent may contain children with different policies; its children remain independent lists.

If a genuinely mixed dated/undated direct-entry list is introduced later, it must first be registered as **Mixed**, with an explicit allowlist of canonical URLs permitted to be undated. Sort dated entries first using the Year key, then allowlisted undated entries using the Alphabetical key. An unlisted missing year is invalid. No current heading is registered as Mixed; adding one requires a reviewed policy-table/checker update, not inference from a missing annotation.

| 完整分区路径 | 条数 | 现状 / 拟定策略 |
|---|---:|---|
| Fundamentals & Getting Started | 16 | 全带年份 / Year |
| Model-level RSI / Self-Training & Self-Reward | 6 | 全带年份 / Year |
| Model-level RSI / Synthetic Data & Self-Distillation | 6 | 全带年份 / Year |
| Model-level RSI / Self-Play & Iterative Fine-tuning | 9 | 全带年份 / Year |
| Model-level RSI / Self-Taught Reasoning | 3 | 全带年份 / Year |
| Harness-level RSI / Prompt & Program Optimization | 7 | 全带年份 / Year |
| Harness-level RSI / Context & Memory Evolution | 11 | 全带年份 / Year |
| Harness-level RSI / Harness & Scaffold Evolution | 15 | 全带年份 / Year |
| Harness-level RSI / Extensible Harness Substrates | 4 | 全无年份 / Alphabetical |
| Harness-level RSI / Self-Verification & Self-Correction — Enabling Foundations | 6 | 全带年份 / Year |
| Harness-level RSI / Self-Evolving Agent Frameworks | 13 | 全带年份 / Year |
| Multi-Agent Self-Improvement / Co-Evolution | 11 | 全带年份 / Year |
| Multi-Agent Self-Improvement / Inference-time Debate | 2 | 全带年份 / Year |
| Coding / Software-Engineering Self-Improvement / Self-Modifying Coding Agents | 4 | 全带年份 / Year |
| Coding / Software-Engineering Self-Improvement / Iterative Repair & Training | 3 | 全带年份 / Year |
| Automated AI R&D | 12 | 全带年份 / Year |
| Embodied & Physical Self-Improvement | 6 | 全带年份 / Year |
| Evolutionary & Open-Ended RSI | 13 | 全带年份 / Year |
| Safety, Alignment & Theory（直接条目） | 13 | 全带年份 / Year |
| Safety, Alignment & Theory / Supporting Safety Foundations | 9 | 全带年份 / Year |
| Introspection & Self-Modeling | 10 | 全带年份 / Year |
| Benchmarks & Evaluations / Direct RSI & Self-Improvement Evaluations | 4 | 全带年份，含 community framework / Year |
| Benchmarks & Evaluations / Frontier Lab Self-Improvement & AI R&D Evaluation Frameworks | 3 | 全带年份，含模型报告与博客 / Year |
| Benchmarks & Evaluations / AI R&D Capability Proxies | 7 | 全带年份，含仓库链接 / Year |
| Benchmarks & Evaluations / Agent Capability Proxies | 9 | 全带年份，含官方 benchmark 网页 / Year |
| Frameworks & Tools / Self-Modifying / Self-Evolving Systems | 7 | 全无年份 / Alphabetical |
| Frameworks & Tools / Harness / Memory / Skill Evolution | 15 | 全无年份 / Alphabetical |
| Frameworks & Tools / Automated Search / AI R&D | 8 | 全无年份 / Alphabetical |
| Blog Posts & Discussions | 14 | 全带年份 / Year |
| Talks & Videos | 4 | 全带年份 / Year |
| Related Awesome Lists | 3 | 全带年份，但现规则明确按标题 / Alphabetical |

## Pull Requests

- Search the list and open pull requests for duplicates before submitting.
- Prefer one resource per pull request.
- Include complete answers to all six required submission items above, including Public artifacts and evaluation artifact status, and complete the PR template's pre-submission self-check.
- Place the entry in the most specific applicable subsection.
- Keep formatting consistent with surrounding entries and update the Contents section if you add or rename a heading.
- Verify that `npx --yes awesome-lint@2.3.0` passes before requesting review.

By contributing, you agree that your contribution is released under the repository's [CC0 1.0 Universal license](LICENSE).
