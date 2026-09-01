<div align="center">

# 🔬 Lab 2 — Colour Spaces & Image Formats

**BITS F459 · Computer Vision · Week 2**

![Time](https://img.shields.io/badge/⏱%20time-2%20hours%20·%20in%20session-00D9FF?style=for-the-badge)
![Marks](https://img.shields.io/badge/marks-10-FF6B6B?style=for-the-badge)
![Runs](https://img.shields.io/badge/runs%20in-Colab%20·%20no%20install-FFD93D?style=for-the-badge)
![Submit](https://img.shields.io/badge/submit-lab02.ipynb-6BCB77?style=for-the-badge)

### ▶️ **[OPEN THE NOTEBOOK IN COLAB](https://colab.research.google.com/github/Elakkiya16/BITS_F459_Computer_Vision_26_27/blob/main/labs/lab02/lab02.ipynb)**

</div>

---

## 🎯 The point of today

In the demo you will watch three statements hold true, live, on a photo of this room:

| | Statement | What you'll see |
|:--:|:--|:--|
| **1** | Colour detail is cheap, brightness detail is expensive | shrink the two colour channels → invisible; shrink brightness the same way → obvious |
| **2** | JPEG makes smaller files than PNG | same photo, about ten times smaller, looks identical |
| **3** | Lossy formats decay when re-saved, lossless ones don't | open and save twenty times; one of them rots |

**Every one of them is false for some picture.** Anyone can repeat a statement. Knowing *when
it stops being true* means you understand what is going on underneath it, and that is what
today is marked on.

You will also meet one new thing in the demo: **PSNR**, a single number for *how close two
pictures are*, in decibels. Higher means closer. Above about 40 you cannot see a difference,
around 30 it is visibly degraded, below 25 it is obviously broken, and 100 means identical.
Every measurement today is in those units.

---

## ⏱ How the session runs

| | |
|:--|:--|
| **0:00 – 0:15** | Demo — the three rules, and how we measure damage |
| **0:15 – 1:30** | You work through the notebook |
| **1:30 – 1:45** | A few of you put your rule-breakers on the projector |
| **1:45 – 2:00** | Submit, leaderboard, questions |

---

## 📋 What you do

### Part A · Build your tools — 4 marks

**A1 (1 mark)** — convert *your* pixel (the notebook prints it, from your BITS ID) into
greyscale, YCrCb and HSV **on paper**. Show the intermediate values, not just the answers.

**A2 (1 mark)** — write `rgb_to_gray`, `rgb_to_ycrcb`, `ycrcb_to_rgb` and `rgb_to_hsv` in
plain NumPy. These are the tools; everything below runs on them.

**A3 (2 marks) — find what was done to your picture.** The notebook takes your own photo and
puts it through **exactly one** of ten changes, chosen by your BITS ID:

| | | |
|:--|:--|:--|
| `red_and_blue_swapped` | `colour_channels_swapped` | `colour_shrunk` |
| `brightness_shrunk` | `hue_shifted` | `colour_faded` |
| `few_levels` | `colour_removed` | `brightness_curved` |
| `low_quality_jpeg` | | |

Several look almost the same by eye — `colour_shrunk` and `colour_faded` both wash the colour
out; `brightness_shrunk` and `low_quality_jpeg` both go blocky. **Staring at it will not settle
it. Measuring will.** You get a `compare()` tool that checks the two pictures one channel at a
time: a channel that scores about 100 was not touched at all, which rules out most of the list
immediately.

Say which one it was, and give the number that rules out the look-alike. A name with nothing
behind it scores zero.

### Part B · Find the pictures where they stop being true — 4 marks

**Challenge 1 (2 marks) — make colour matter more than brightness.** Shrinking both colour
channels throws away *twice as much data* as shrinking brightness, and normally still looks
better. Find or build a picture where it comes out the other way round.

**Challenge 2 (2 marks) — make PNG smaller than JPEG.** Sizes only mean something at equal
quality, so we fix the quality first: the notebook finds the lowest JPEG quality setting that
still reaches 40 dB on your picture, and compares file sizes at that setting.

In both, **write down what you are aiming for before you look at the result.** That prediction
is half the mark. You may photograph something or build it with `synth(...)` — building one on
purpose is not the easy way out, because you have to know exactly which property matters.

### Part C · The smallest-file challenge — 2 marks + leaderboard

Everyone compresses **the same class photo**, taken during the demo. Smallest file wins, as
long as your rebuilt picture still scores **30 dB** against the original at full size.
Anything you have met today is allowed: converting colour spaces, shrinking channels, using
fewer levels, resizing, any file format. The notebook hands you a plain JPEG as the starting
point — beat it.

---

## 💾 Submitting

**Colab → File → Save a copy in GitHub**

| Field | Value |
|:--|:--|
| Repository | `BITS-F459-Computer-Vision/f459-<your BITS ID, lowercase>` |
| Branch | `main` |
| File path | `lab02.ipynb` |
| Commit message | `Lab 2` |

**Exactly `lab02.ipynb`, at the top level of your repo.** No folder, no other name.

> ⚠️ **Run every cell top to bottom, and run the last cell last.** Colab saves the notebook
> *with its outputs*, and the outputs are what gets read. A notebook saved before it was run
> is empty as far as marking is concerned.

<details>
<summary>Pushing from your laptop instead</summary>

```bash
cp ~/Downloads/lab02.ipynb .        # repo root
git add lab02.ipynb && git commit -m "Lab 2" && git push
```
</details>

---

## ✅ Before you leave

- [ ] A1 says PASS · A2 says PASS
- [ ] Working table filled in, intermediates included
- [ ] `DIAGNOSIS` has the name, the numbers, and a reason
- [ ] `PREDICT_1` written **before** challenge 1 ran; challenge 1 says **BROKEN**
- [ ] `PREDICT_2` written **before** challenge 2 ran; challenge 2 says **BROKEN**
- [ ] The smallest-file challenge says **VALID** and beats the starting point
- [ ] All three `EXPLAIN` answers written
- [ ] Last cell run **last**, its output visible
- [ ] Saved as `lab02.ipynb` in your repo — and you opened GitHub and checked it is there

---

## 🆘 Troubleshooting

| Problem | Fix |
|:--|:--|
| Camera doesn't work | `SOURCE = "upload"` and pick a photo from your phone — better quality anyway |
| Neither works | `SOURCE = "synth"` builds a picture from two colours you choose |
| Hue check fails, the rest pass | You returned OpenCV's units. Yours: `H` from 0 to 360, `S` and `V` from 0 to 1 |
| YCrCb check off by about 100 | You stacked `Cb` before `Cr` |
| Inverse check fails | The constants are `1.403`, `0.714`, `0.344`, `1.773` |
| Divide-by-zero in HSV | Grey pixels have `Δ = 0` — those get `H = 0`, `S = 0` |
| Challenge 1 won't flip | Your picture needs its detail in the *colour* channels, not the brightness one. Two strong colours of **similar brightness**, meeting at sharp edges |
| Challenge 2 won't flip | JPEG struggles with big flat areas and hard edges — think screenshot, slide, whiteboard, poster |
| Smallest-file says INVALID | You are below 30 dB. Undo one step — usually the resize |
| Can't fetch the class photo | It gets pushed during the break; re-run that cell afterwards |
| Last cell errors | Run it after everything else; it collects variables the earlier cells define |

---

<div align="center">

### ⏭️ Next week: **Feature extraction — edges, corners, descriptors**

</div>
