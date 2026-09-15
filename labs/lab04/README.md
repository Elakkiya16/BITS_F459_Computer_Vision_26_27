<div align="center">

# 🔍 Lab 4 — Finding Edges in a Noisy Picture

**BITS F459 · Computer Vision · Week 4**

![Time](https://img.shields.io/badge/⏱%20work-about%20one%20hour-00D9FF?style=for-the-badge)
![Marks](https://img.shields.io/badge/marks-10-FF6B6B?style=for-the-badge)
![Runs](https://img.shields.io/badge/runs%20in-Colab%20·%20no%20install-FFD93D?style=for-the-badge)
![Submit](https://img.shields.io/badge/submit-lab04.ipynb-6BCB77?style=for-the-badge)

### ▶️ **[OPEN THE NOTEBOOK IN COLAB](https://colab.research.google.com/github/Elakkiya16/BITS_F459_Computer_Vision_26_27/blob/main/labs/lab04/lab04.ipynb)**

</div>

---

## 🎯 The point of today

In the lecture the five steps of Canny were worked out on a grid where you could see every
pixel. Today you do it twice: once by hand on a 7 × 7 of your own, then on a real
photograph that has had sensor noise added to it.

**Nothing to bring.** No photograph, no upload. Everything comes from your BITS ID.

The picture only looks slightly grainy. Run the edge finder on it with no smoothing and it
returns **eight times as many edge pixels as there really are**. Almost all of them are the
noise being differentiated. Getting from that back to a clean outline is the whole lab.

---

## ⏱ How the session runs

| | |
|:--|:--|
| **0:00 – 0:10** | The five steps worked through on the projector |
| **0:10 – 0:40** | Part A — by hand, on your own 7 × 7 |
| **0:40 – 0:55** | Part B — noise and smoothing |
| **0:55 – 1:20** | Part C — the two thresholds, and the leaderboard |
| **1:20 – 1:30** | Submit, questions |

Part C is the one to leave if you run short. A and B are what the lecture covered.

---

## 📋 What you do

### Part A · All five steps, on your own 7 × 7 — 5 marks

Your image is **two bright blocks with a dark channel between them**, and one faint speck
in the background. Two blocks rather than one, because a single block only ever produces
gradients pointing one way; with the channel, all four directions appear in your picture.
The brightness values, the sizes and the speck all come from your BITS ID.

**A1 (1 mark)** — one value of **S** is missing. Work it out with the Gaussian from the
lecture. Then take the 3 × 3 window of S around the missing gradient and give `Gx`, `Gy`,
the `length`, the `angle` between 0 and 180, and the `direction`.

> If your missing value sits on an edge of the image, the row or column outside it is a
> **copy of the nearest one**. The notebook explains this where you need it.

**A2 (2 marks)** — step 3, four times over. The notebook names one pixel for each of the
four directions: 0°, 45°, 90° and 135°. For each, read the two neighbours **across its own
edge** and say whether the pixel is kept or set to zero. The pair is left and right at 0°,
above and below at 90°, and a diagonal at 45° and 135°.

**A3 (1 mark)** — step 4. The notebook prints the largest value left after thinning. Work
out your own two thresholds from it, using the proportions from the lecture:
`t_high = 0.70 × that value` and `t_low = 0.35 × it`, both rounded.

**A4 (1 mark)** — step 5. Using your thresholds, count the strong, the weak and the ones
discarded outright, then find **the one weak pixel that step 5 throws away** and say why it
goes when the others stay.

### Part B · The same five steps on a photograph — 2 marks

The course banner, in grey, with noise added from your BITS ID. The **reference** is the
edge map of the clean picture: that is what you are trying to get back.

**B1 (1 mark)** — the notebook runs all six smoothing sizes with the thresholds held at 10
and 20. Copy the six scores across, give the pixel count with no smoothing, work out how
many **more** that is than the reference has, and say in one sentence why heavy smoothing
is just as bad as none.

**B2 (1 mark)** — choose the smoothing. The mark is a score of **0.683** or better. Only
one of the six sizes reaches it.

### Part C · The two gradient thresholds — 3 marks + leaderboard

Now all three settings are yours. These are thresholds on |∇f|, the same kind of number you
worked out in A3. They are not pixel counts.

**C1 (1 mark)** — the **highest score** you can reach. Holding the thresholds at 10 and 20
in Part B was a restriction, and lifting it buys more. Beat your own Part B score by
**0.010** or more.

**C2 (1 mark)** — the **smallest edge map**. Two maps can score the same while one is a
clean outline and the other is that outline plus a scattering of fragments. Hold the score
at **0.60** or better and get under **13,000** edge pixels. Different settings from C1.

**C3 (1 mark)** — set `t_low` equal to your `t_high`. That leaves no weak class at all, so
step 5 has nothing to rescue. Report the score and the pixel count, and one sentence on
what happened to the contours.

**Leaderboard:** C2, the fewest edge pixels with the score still at 0.60 or above. Everyone
has the same picture, so the counts compare directly.

---

## 💾 Submitting

1. **Run every cell from top to bottom, and run the last cell last.**
2. In Colab: **File → Download → Download .ipynb**
3. **Rename the downloaded file to exactly `lab04.ipynb`.** Colab usually calls it
   `Copy of lab04.ipynb`, and that name will not be accepted.
4. Open your own repository:
   `github.com/BITS-F459-Computer-Vision/f459-<your BITS ID, lowercase>`
5. **Add file → Upload files**, drag `lab04.ipynb` in, then **Commit changes**.
6. **Click the file on GitHub and look at it before you leave.** You should see your own
   outputs in it.

> ⚠️ **The last cell is what gets marked.** It recomputes every measurement from the
> settings you have chosen at the moment you run it. If you change anything above it
> afterwards, come back down and run it again before you download.

Uploading again later replaces the file, so you can submit more than once. The last one counts.

## ✅ Before you leave

- [ ] A1 shows `correct` on all six lines
- [ ] `A2` filled in for all four directions, both neighbours and the verdict each time
- [ ] `A3` matches the rule the notebook checks
- [ ] `A4` filled in, including which weak pixel is thrown away and why
- [ ] `B1` has all six scores and the subtraction against the reference
- [ ] `SMOOTH` reaches 0.683
- [ ] `BEST` gains at least 0.010 over your Part B score
- [ ] `FEWEST` holds 0.60 and gets under 13,000
- [ ] `HYSTERESIS` filled in with the numbers you actually got
- [ ] Last cell run **last**, its output visible
- [ ] Downloaded, renamed to exactly `lab04.ipynb`, uploaded to your repo
- [ ] You opened GitHub, clicked the file, and saw your outputs

---

## 🆘 Troubleshooting

| Problem | Fix |
|:--|:--|
| A1 says my `Gx` is too high | Check the sign. Work out which side of your window is brighter; the gradient is negative when brightness falls in that direction |
| My angle is negative | `arctan` gives you something between −90 and 90. Add 180 to a negative angle: the answer wanted is between 0 and 180 |
| My angle is huge | Your calculator is in radians |
| My angle is above 157.5 | That still rounds to 0°. The band wraps around |
| A2 verdict looks wrong | You compared the wrong pair. Check the direction first, then read the two neighbours on that line |
| A2: my two neighbours are equal | That happens. If your pixel loses to both, it is zero either way |
| A3 says check the arithmetic | Use the largest value the cell printed, multiply, then round to a whole number |
| A4: I cannot find the weak pixels | They are the values between your two thresholds. There are usually two or three, and exactly one of them is thrown away |
| I cannot get past 0.683 | Look again at which row of your own table is highest. Only one size reaches it |
| C1 and C2 give me the same settings | They should not. The highest score and the smallest map are different places |
| C2: fewer pixels but the score collapsed | The score has to stay at 0.60. Raising both thresholds together throws away the outline as well as the litter |
| The last cell errors | Run it after everything else. It uses variables the earlier cells define |

---

<div align="center">

### ⏭️ Next: **corners, and how to describe them**

</div>
