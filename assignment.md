# Laboratory 1 — Training a Topic Model

**Course:** ELESB21501, Text and Natural Language Processing  
**Duration:** 4 academic hours (180 minutes, excluding breaks)  
**Work:** individual; AI assistance allowed as described below  
**Submission:** an early analysis checkpoint, followed by your code, evidence and a short recommendation, then a practical defence. The instructor announces the final deadline.

## The situation

A news editor wants to organise headlines into understandable topics automatically. Build an LDA topic model and decide whether its organisation would be useful to the editor.

The editor wants clear, distinguishable topics that reflect news content rather than merely place names or repeated templates. Some headlines may legitimately belong to several topics. A working program is necessary, but it is not sufficient: your recommendation must be supported by actual headlines, comparisons and examples of failure.

## Materials and boundaries

Download **Lab01_Materials.zip**. It contains `headlines_train.csv`, this assignment and `report-template.md`; no starter code or completed solution is supplied. Each non-empty `text` value is one document. Do not use `label` or `is_clickbait` as model inputs, targets or an answer key.

This teaching collection contains short, repeated, template-like headlines and English/Lithuanian fragments. Discuss the implications rather than assuming it represents real news performance. The repository copy is `Lecture2/data/headlines_train.csv`.

Write your own script or notebook. You may use Python libraries such as pandas, scikit-learn and matplotlib, including library implementations of vectorisation and Latent Dirichlet Allocation. You do not need to implement LDA mathematically from scratch. Use a prepared Python environment; no GPU, paid service or API key is required.

## Work plan

| Stage | Minutes | Evidence |
| --- | ---: | --- |
| Inspect 20 headlines and submit initial analysis | 25 | Initial grouping, ambiguous cases and two predicted problems |
| Prepare data and build the first model | 40 | Runnable workflow and documented choices |
| Compare two topic counts and test one preprocessing decision | 45 | Three controlled runs and concrete comparisons |
| Analyse failures and write the recommendation | 40 | Three failure cases, trade-off and selected model |
| Prepare and conduct the practical defence | 30 | Predictions and explanations for unseen headlines |
| **Total** | **180** | |

The instructor organises short defence slots for the group. Extensive hyperparameter searches and long reports are not expected.

## 1. Make an initial judgement before modelling

Remove empty text entries and exact duplicates after stripping surrounding whitespace. Record the counts. Select at most 1,500 unique documents using a reproducible random seed of your choice and record it. Use the same collection throughout the required comparisons.

Before training a model, select 20 headlines from this collection without cherry-picking only easy examples. Record your selection method and give each headline a stable identifier.

For each headline, propose a topic in your own words. You may assign more than one topic or mark it unclear. Identify at least two ambiguous headlines and explain the ambiguity. Summarise your proposed groups and predict two difficulties a topic model may encounter, pointing to actual examples.

**Checkpoint:** by the end of this first stage, upload `initial-analysis.pdf` or `initial-analysis.md` as an early draft in this Moodle assignment and show it to the instructor before training. Keep that original file unchanged in your final submission. If the Moodle interface prevents a draft update, show the initial file to the instructor at the checkpoint and include it unchanged in the final ZIP. The instructor records the checkpoint; this is not an automatically enforced second Moodle deadline.

Complete this initial interpretation without AI-generated grouping or explanations. Later, compare the model with your initial judgement; you may revise your opinion, but explain why rather than rewriting the initial analysis. Your manual groups are a reference for discussion, not class labels for supervised training.

## 2. Build a working topic-modelling workflow

Prepare the text, build a word-count document–term matrix, train an LDA model, and obtain topic words and document-topic weights. Explain your choices for tokenisation, stop words and vocabulary filtering. Count and handle documents with no retained terms.

Keep the collection small enough to run during class. A vocabulary cap of 3,000 terms and around 15 training iterations are practical starting points, not settings to optimise extensively. Record the actual parameters and random seeds you use.

Choose **two different topic counts** between 2 and 10. Justify why these two are plausible for the editor, using your initial inspection. You are not required to use 3, 5 or 8 topics. Keep all other settings fixed when comparing the two counts.

Show the top ten words per topic (or all retained words if fewer than ten exist) for each run. Use headline examples to assess whether the topics are understandable, overlapping, too broad or unnecessarily fragmented. Select a provisional topic count.

## 3. Test one decision instead of guessing

Choose one data-preparation issue that you observed. For example: should place names be removed, how should recurring template phrases be handled, or how should mixed-language filler words be treated? You may choose another issue if you explain its relevance.

Before the test, write a short prediction: what should improve, what useful information might be lost, and which headlines could reveal the effect?

Compare the provisional model with a version that changes **only this one preprocessing decision**. Keep the topic count, document collection, model seed and training settings fixed. If the change creates empty documents, report this and compare headline examples retained in both runs. The vocabulary may change as a consequence of the decision.

The required minimum is **three runs in total**: two topic counts with the original preprocessing, and one run with the selected count and changed preprocessing. Do not add a separate grid search.

Explain the observed benefit and cost using at least two specific headlines, including one illustrating lost information or an unexpected outcome if found. If your prediction is not supported, say so and show the evidence. A justified decision to keep the original preprocessing is a valid result.

## 4. Recommend a solution and expose its weaknesses

For your final selected model:

- Give every topic a short name or explicitly identify it as unclear/mixed. Include its top words and two representative headlines, selected using their topic weights.
- Revisit at least three of your initial 20 headlines. Explain agreement or disagreement between your own grouping and the model. Neither is automatically correct.
- Find **three concrete cases where the output does not meet the editor's needs**. For each, show the headline, model output, why it is problematic, and a possible remedy or an explanation of why the headline is inherently ambiguous. Use at least two distinct kinds of problem. An empty-vector case is valid if you identify it honestly; do not invent a topic assignment for it.
- Write a concise recommendation: which topic count and preprocessing would you use, what trade-off did you accept, and what would still need a human editor's judgement?

Topic IDs are arbitrary, so match topics across runs by words and meaning, not their numbers. No particular topic count, preprocessing choice or conclusion is the correct answer. It is acceptable to conclude that the model is not ready for the editor, provided you support the judgement.

A chart is optional. Classification accuracy, train/validation splitting, perplexity analysis, seed-stability experiments and extensive tuning are not required. The required comparison is exploratory; do not claim it establishes generalisation to unseen news.

## 5. Practical defence: unseen headlines

The instructor will provide two or three new headlines during the defence, including an ambiguous or unusual example. Before running your model, explain which of your topics might apply, where you expect uncertainty, and why.

Then process the headlines with the **already fitted vocabulary and selected model**. Do not retrain on them. Show their topic weights and explain any difference between your prediction and the output. If no vocabulary terms remain, report that there is insufficient evidence for a meaningful assignment.

Prepare this inference capability in advance, but you do not need a separate new-text experiment in the report. During the defence, answer and operate your program yourself, without AI assistance; library documentation is allowed. Exact numerical predictions are not expected. A prediction that proves wrong can still demonstrate understanding if you explain the discrepancy.

Be ready to explain one preprocessing decision, why you preferred one topic count, and one failure case. The defence assesses your understanding of the actual work you submitted.

## AI use and ownership of the work

AI assistance is permitted after the initial analysis checkpoint, but is not required. You may use it for explanations, implementation, debugging or report editing. You remain responsible for all submitted code, results and conclusions.

State which tools you used, for what purposes, and how you checked their outputs. Include one concrete suggestion you verified, corrected or rejected. If you did not use AI, state that. Cite other sources and reused code. Do not submit invented results or claim to have run code you did not run.

No AI-generated initial interpretation and no AI assistance during the defence are allowed. Using AI for the permitted stages does not itself raise or lower the grade. Decisions supported by evidence and demonstrated understanding determine the assessment.

## Deliverables

For the early checkpoint, submit or show the initial 20-headline analysis as described in Stage 1.

For final submission, upload **Lab01_Name_Surname.zip** containing:

1. The unchanged initial analysis and its selection method.
2. Your runnable code or notebook, short run instructions, parameters, seeds and package versions, including the ability to analyse new headlines without retraining.
3. A short report of approximately 1–2 pages using `report-template.md`; detailed tables may be appendices. Include your preprocessing hypothesis, the three-run comparison, three failure cases and recommendation.
4. Topic-word outputs, supporting headline examples and your sources/AI declaration.

Do not include a virtual environment or another copy of the full dataset. Keep an earlier checkpoint file in the assignment until the final ZIP containing the same file is uploaded. Report length is a guide, not a target to fill with generic explanations.

## Assessment — 10 points

| Criterion | Points | Full-credit evidence |
| --- | ---: | --- |
| Initial analysis | 2 | Timely checkpoint, own grouping of 20 headlines, explained ambiguities and two evidence-based predictions |
| Working solution | 2 | Correct runnable workflow, two chosen topic counts, controlled third run, recorded settings and inference with the fitted model |
| Justified comparison and failure analysis | 4 | Topic-count rationale and comparison (1); preprocessing hypothesis and observed benefit/cost (1); three evidenced failure cases (1); recommendation and comparison with initial judgement (1) |
| Practical defence | 2 | Reasoned predictions for unseen headlines (1); independent demonstration and explanation of outcomes/decisions (1) |
| **Total** | **10** | |

Partial credit reflects demonstrated evidence. Merely showing working AI-generated code does not earn the interpretation or defence points. Unclear topics, a rejected hypothesis or an incorrect initial prediction are not themselves failures: assess how convincingly the student investigates and explains them. Sources and AI disclosure must accompany the submission; AI use itself carries no separate points.

This is one laboratory grade. The four laboratory grades form an average contributing 20% of the final course grade.

## Reference

[scikit-learn: LatentDirichletAllocation API](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html)
