<div align="center">

# 💡 Lab 3 — Colour Under Different Light

**BITS F459 · Computer Vision · Week 3**

![Time](https://img.shields.io/badge/⏱%20time-2%20hours%20·%20in%20session-00D9FF?style=for-the-badge)
![Marks](https://img.shields.io/badge/marks-10-FF6B6B?style=for-the-badge)
![Runs](https://img.shields.io/badge/runs%20in-Colab%20·%20no%20install-FFD93D?style=for-the-badge)
![Submit](https://img.shields.io/badge/submit-lab03.ipynb-6BCB77?style=for-the-badge)

### ▶️ **[OPEN THE NOTEBOOK IN COLAB](https://colab.research.google.com/github/Elakkiya16/BITS_F459_Computer_Vision_26_27/blob/main/labs/lab02_01/lab03.ipynb)**

</div>

---

## 🎯 The point of today

A sheet of white paper by the window and the same sheet under a lamp look white to you both
times. The file says something quite different: every number in it has moved, and the second
one is distinctly yellow.

Your eyes correct for the light without telling you. A program does not, unless you make it.

**You need one photograph today.** The notebook makes the second version for you.

In the demo you will watch one photograph put under a different light, and see:

| | What you'll see |
|:--|:--|
| **1** | R, G and B all move a long way. Hue barely moves at all |
| **2** | The first trick anyone reaches for, assuming the picture averages to grey, makes it **worse** |
| **3** | Knowing what the light actually did makes it possible to put the picture back |

---

## ⏱ How the session runs

| | |
|:--|:--|
| **0:00 – 0:05** | How to submit — watch this before you start |
| **0:05 – 0:20** | Demo — light changes, and what survives it |
| **0:20 – 1:35** | You work through the notebook |
| **1:35 – 1:50** | A few corrections on the projector |
| **1:50 – 2:00** | Submit, leaderboard, questions |

---

## 📋 What you do

### Part A · The conversions, and what survives — 4 marks

**A1 (1 mark)** — two pixels, **the same colour at two brightnesses**, both converted to HSV
**on paper**. Show every intermediate step. Then say which of H, S and V barely changed.

**A2 (1 mark)** — write `rgb_to_hsv` so it works on a whole picture. Checked against OpenCV.
`H` from 0 to 360, `S` and `V` from 0 to 1 — not OpenCV's squeezed units.

**A3 (2 marks)** — your photograph is put under a different light. Measure how far every
channel moves, in RGB, HSV and YCrCb. Name the steadiest channel and give the numbers.

### Part B · Work out what the light did, and undo it — 4 marks

The light did three things: a curve, a brightness change, and a colour cast.

**B1 (2 marks)** — before touching anything, say whether the picture was made brighter or
darker, whether the light was warm or cool, and roughly by how much. One mark for the two
directions, one for a brightness estimate within 0.12.

**B2 (2 marks)** — put the picture back. One mark for gaining 3 dB over the relit picture,
one more for gaining 6 dB.

> Try `grey_world` first and watch it fail. It assumes your picture averages to neutral grey.
> Yours does not, and the assumption costs you.

### Part C · The right format for each picture — 2 marks + leaderboard

Three pictures: **your photograph**, a **screenshot** of text and lines, and a **flat
graphic**. Choose the format and setting for each **separately** to make the total as small
as possible, with every one still reaching **32 dB**.

One format is not the right answer for all three. That is the whole question.

---

## 💾 Submitting

When you have finished:

1. **Run every cell from top to bottom, and run the last cell last.**
2. In Colab: **File → Download → Download .ipynb**
3. **Rename the downloaded file to exactly `lab03.ipynb`.** Colab usually calls it
   `Copy of lab03.ipynb`, and that name will not be accepted.
4. Open your own repository:
   `github.com/BITS-F459-Computer-Vision/f459-<your BITS ID, lowercase>`
5. **Add file → Upload files**, drag `lab03.ipynb` in, then **Commit changes**.
6. **Click the file on GitHub and look at it before you leave.** You should see your own
   outputs in it.

> ⚠️ **The outputs are what gets marked.** The notebook is saved together with everything it
> printed, and the last cell is what collects your answers. If you download before running
> that cell, the file is empty as far as marking is concerned.

Uploading again later replaces the file, so you can submit more than once. The last one counts.

## ✅ Before you leave

- [ ] A1 says PASS · A2 says PASS
- [ ] Working table filled in, both pixels, intermediates included
- [ ] `STABLE` filled in
- [ ] `ESTIMATE` written **before** you started tuning
- [ ] `CORRECTION` gains at least 3 dB, and 6 dB if you can get it
- [ ] Part C says VALID and beats the starting point
- [ ] All three `EXPLAIN` answers written
- [ ] Last cell run **last**, its output visible
- [ ] Downloaded, renamed to exactly `lab03.ipynb`, uploaded to your repo
- [ ] You opened GitHub, clicked the file, and saw your outputs

---

## 🆘 Troubleshooting

| Problem | Fix |
|:--|:--|
| Camera doesn't work | `SOURCE = "upload"` and pick a photo from your phone — better quality anyway |
| Neither works | `SOURCE = "synth"` builds a coloured picture for you |
| A2 hue check fails, the rest pass | You returned OpenCV's units. Yours: `H` 0 to 360, `S` and `V` 0 to 1 |
| Divide-by-zero in A2 | Grey pixels have `Δ = 0` — give those `H = 0`, `S = 0` |
| Everything in A3 reads near zero | Your photo has no strong colour in it. Take one with something vivid |
| Correction stuck below 3 dB | Change one setting at a time. `cast` fixes colour, `gain` fixes brightness, `gamma` fixes the shadows |
| Part C says INVALID | One of the three is under 32 dB. Usually the photograph — raise its quality |
| Last cell errors | Run it after everything else; it collects variables the earlier cells define |

---

<div align="center">

### ⏭️ Next week: **Feature extraction — edges, corners, descriptors**

</div>
