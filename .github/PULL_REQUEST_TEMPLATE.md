## Summary

<!-- Briefly describe the change and the resource, metadata, or taxonomy affected. -->

## Pre-submission self-check

- [ ] I answered all six required submission items below, including both Public artifacts and Evaluation artifact status. My artifact claim concerns the evaluation supporting this README entry's claim, not an unrelated experiment from the same paper.
- [ ] I used the official title and canonical direct URL, placed the entry in the most specific subsection, and checked the subsection's Year or Alphabetical ordering policy. I did not infer a publication year from the title or URL.
- [ ] The description is one concise, neutral sentence ending in a period before any publication annotation. For sentence counting, read through the first sentence-ending punctuation; the trailing publication annotation is metadata, not another sentence. Where applicable, I use `- [Official title](URL) - Description sentence. (Venue YYYY)` (or `(YYYY)` for dated posts/talks), with the venue/status and year verified against an authoritative source. The entire Markdown line need not end with a period.

For each component below, I recorded whether it is required by the reported evaluation, a specific public locator (URL/DOI/release tag and relevant path/version), or the missing component and why it is unavailable. If not required, I explained why; I did not treat a repository homepage as proof that every component is present.

- [ ] Task set / generative task source: ______
- [ ] Scoring logic: ______
- [ ] Evaluation harness: ______
- [ ] Data / checkpoints: ______
- [ ] Execution environment, including dependencies, versions and required non-public infrastructure: ______

- [ ] Every component I call publicly available is retrievable by anyone through a stable locator, with no access request, email gate, payment, licence negotiation, or institutional affiliation requirement.
- [ ] I applied the decisive test using only public artifacts: can an independent third party rerun or meaningfully check some part of the reported evaluation? Answer: ______; specific checkable part, locators and rerun/check procedure: ______; missing components and limitations: ______.
- [ ] I classified in the CONTRIBUTING order: Not applicable only where no reported evaluation depends on the artifact set (an experiment on public data is not automatically N/A); Open only if every required component is public; Internal if no meaningful part can be independently reproduced from public artifacts, including evaluations dependent on non-public task sets or infrastructure; Partial otherwise only where a meaningful part remains independently checkable. Any ambiguity is explained against the specific evaluation claimed.
- [ ] I defaulted downward: I do not claim Open or Partial without specific public locators and identified missing components. If I cannot substantiate the claimed level, I selected a lower supported level; absence of evidence does not justify Not applicable.
- [ ] I identified any evaluation the resource itself flags as non-reproducible. I put the status in submission metadata, not a README status badge, and stated material reproducibility limits plainly in the description where relevant.

Artifact status is the author's declaration. Maintainers do not rewrite it on the author's behalf; they identify “should be X + missing components” and ask the author to correct the submission.

## Required RSI submission details

### What is being improved?

<!-- Identify the model, agent policy, prompt, memory, harness, codebase, optimizer, or other target. -->

### Does the improvement persist across iterations?

<!-- State what artifact or behavior carries forward, or explicitly state that it does not. -->

### Is the improvement mechanism itself subject to improvement?

<!-- Explain whether and how the process producing improvements can itself change. -->

### Why is this specifically relevant to RSI?

<!-- Connect the work directly to recursive self-improvement, persistent self-improvement, or evaluation or safety evidence for those systems. -->

### Publication status

<!-- Identify the status and include the venue and year where applicable, for example: arXiv preprint (2026), workshop: AutoRL@ICML (2024), conference: ICML (2025), or journal: Nature (2026). -->

### Public artifacts
Official implementation:
Public data / checkpoints:
Public evaluation harness:

### Evaluation artifact status
Open / Partial / Internal / Not applicable

## Checklist

- [ ] I searched the list and open pull requests for duplicates.
- [ ] I used the resource's official title and canonical URL.
- [ ] I placed the entry in the most specific applicable subsection and followed its ordering rules.
- [ ] I verified the publication status against a primary or authoritative source.
- [ ] npx --yes awesome-lint@2.3.0 passes locally.
