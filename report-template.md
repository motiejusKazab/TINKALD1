# Laboratory 1 — Editor's recommendation

Name:  
Date:  
Run instructions, package versions and saved parameters:

Use approximately 1–2 pages of explanation; put detailed tables in appendices.

## Initial analysis — separate checkpoint file

Before modelling, prepare `initial-analysis.md` or `initial-analysis.pdf` with:

- Counts before/after cleaning, sample size, seed and method for selecting 20 headlines.
- A table: headline ID | full text | your proposed group(s) | ambiguity and reason.
- Your proposed topic groups and two predicted modelling problems, with examples.

Do this interpretation without AI. Upload a draft and show it to the instructor at the checkpoint, or show the file directly if draft updates are unavailable. Include that unchanged file in your final ZIP. Do not rewrite it after seeing the model results.

## 1. Decisions and prediction

Why did you choose these two topic counts?

Which single preprocessing issue did you test, why, and what benefit/cost did you predict before testing?

## 2. Three-run comparison

| Run | Topic count | Preprocessing | Fixed settings / seed | Evidence of usefulness or problems |
| --- | --- | --- | --- | --- |
| A | | Original | | |
| B | | Original | | |
| C | Selected A/B count | One change | | |

Concrete headline evidence of the preprocessing effect, including a cost or unexpected outcome if observed:

## 3. Final model and failure analysis

Reference topic names, top words and two representative headlines per topic in an appendix.

Compare at least three of your original 20 headlines with their model outputs.

| Headline ID and text | Actual model output | Why it fails the editor's needs | Possible remedy or inherent ambiguity |
| --- | --- | --- | --- |
| | | | |
| | | | |
| | | | |

Use at least two distinct kinds of problem across these three cases.

## 4. Recommendation

Chosen model and preprocessing, evidence for the choice, accepted trade-off, and what still requires human judgement:

## 5. Sources and AI use

Sources and reused code. AI tools and purposes, how outputs were checked, and one suggestion verified/corrected/rejected; otherwise state that no AI was used. The initial interpretation and defence must be completed without AI assistance.

## Defence preparation

Ensure your program can analyse instructor-provided headlines using the fitted vocabulary and model. Handle inputs with no retained terms. Be prepared to predict, run and explain; no separate new-text experiment or written defence answers are required beforehand.
