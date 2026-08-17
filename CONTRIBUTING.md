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

Canonical enabling works may be included when they establish a mechanism that is directly reused by later self-improving systems.

Resources about the financial Relative Strength Index are out of scope.

## Entry Format

Use this format:

```markdown
- [Resource Name](https://example.com) - One sentence explaining what the resource covers and why it is relevant.
```

- Include a working direct link.
- Write exactly one concise, neutral description sentence.
- End every description with a period.
- Use the resource's official title and preserve model or system version names exactly.
- Avoid promotional language and tracking parameters.
- Avoid duplicate resources or identical links. A paper and its official implementation may be listed separately when they serve different purposes.

Every submission or pull request must also provide:

1. **What is being improved?** Identify the model, agent policy, prompt, memory, harness, codebase, optimizer, or other target.
2. **Does the improvement persist across iterations?** State what artifact or behavior carries forward, or explicitly state that it does not.
3. **Is the improvement mechanism itself subject to improvement?** Explain whether and how the process producing improvements can itself change.
4. **Why is this specifically relevant to RSI?** Connect the work directly to recursive self-improvement, persistent self-improvement, or evaluation or safety evidence for those systems.
5. **Publication status:** Identify the status and include the venue and year where applicable, for example `arXiv preprint (2026)`, `workshop: AutoRL@ICML (2024)`, `conference: ICML (2025)`, or `journal: Nature (2026)`.

## Ordering

- Sort research resources by publication year from newest to oldest; within the same year, sort alphabetically by title.
- Sort non-research resources, such as Related Awesome Lists and Tools, alphabetically by title.

## Pull Requests

- Search the list and open pull requests for duplicates before submitting.
- Prefer one resource per pull request.
- Include complete answers to the four required questions and the Publication status field above.
- Place the entry in the most specific applicable subsection.
- Keep formatting consistent with surrounding entries and update the Contents section if you add or rename a heading.
- Verify that `npx --yes awesome-lint@2.3.0` passes before requesting review.

By contributing, you agree that your contribution is released under the repository's [CC0 1.0 Universal license](LICENSE).
