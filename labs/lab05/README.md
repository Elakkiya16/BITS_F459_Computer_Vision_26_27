<div align="center">

# 🔍 Lab 5 · Finding Corners

**BITS F459 · Computer Vision · Week 5**

![Time](https://img.shields.io/badge/⏱%20work-about%20one%20hour-00D9FF?style=for-the-badge)
![Marks](https://img.shields.io/badge/marks-10-FF6B6B?style=for-the-badge)
![Runs](https://img.shields.io/badge/runs%20in-Colab%20·%20no%20install-FFD93D?style=for-the-badge)
![Submit](https://img.shields.io/badge/submit-lab05.ipynb-6BCB77?style=for-the-badge)

### ▶️ **[OPEN THE NOTEBOOK IN COLAB](https://colab.research.google.com/github/Elakkiya16/BITS_F459_Computer_Vision_26_27/blob/main/labs/lab05/lab05.ipynb)**

</div>

---

## 🎯 The point of today

Last week you found edges. An edge tells you a boundary is there, but it will not tell you
**where along it** you are: slide a window along an edge and the view does not change. That
is why an edge cannot be used to match two photographs of the same building.

A corner is a point where the window cannot slide in **any** direction without the view
changing. Today you work Harris out by hand, on a board generated from your own BITS ID,
and then watch what happens to it when the picture changes.

**Nothing to bring.** No photograph, no upload. Every number comes from your BITS ID, and
in Part A every one of them is a whole number, so there is no rounding anywhere.

---

## ⏱ How the session runs

| | |
|:--|:--|
| **0:00 – 0:10** | The five steps of Harris on the projector |
| **0:10 – 0:55** | Part A — by hand, on your own board |
| **0:55 – 1:20** | Part B — what survives a change of picture |
| **1:20 – 1:30** | Submit, questions |

Part A is the lecture, worked by hand. If you run short, B1 and B2 are the two to keep.

---

## 📋 What you do

### Part A · Harris by hand, on your own board — 6 marks

The five steps, in the order the lecture gave them:

1. **Differentiate.** Sobel divided by 8, on the board itself. No Gaussian first.
   Canny smooths and then differentiates; Harris differentiates and then smooths, and that
   order is the whole difference between them.
2. **Multiply.** Form `Ix²`, `Iy²` and `IxIy` at every pixel.
3. **Sum over a window.** Add each of the three over the 3 × 3 window. Those three sums
   are the matrix `M`.
4. **Score.** `R = det(M) − k·trace(M)²`, with `k = 0.04`.
5. **Thin.** Non-maximum suppression, so one corner gives one answer and not a blob.

> At the edge of the board, the row or column outside it is a **copy of the nearest one
> inside**. Same replicate rule as Lab 4.

**A1 (1 mark)** — `Ix` and `Iy` at your **corner** pixel, by hand. Lay the Sobel kernel
over the 3 × 3 window centred on that pixel, multiply entry by entry, add, divide by 8.
Both answers are whole numbers.

**A2 (2 marks)** — build `M` at all three marked pixels: the corner, the edge and the flat
one. `M` has four entries but only three different numbers, because it is symmetric. Each
sum runs over the 3 × 3 window, so for each place you need nine values of `Ix` and nine of
`Iy`. *Both marks need all three places right; one mark for two of the three.*

**A3 (2 marks)** — at your corner, `M` has the same number on both diagonal entries. For
that shape the eigenvalues are just `a − b` and `a + b`, with no quadratic to solve. Then
`R`, rounded to the nearest whole number. *One mark for the eigenvalues, one for `R`.*

**A4 (1 mark)** — classify all three pixels from the **sign of `R` alone**: clearly
positive is a corner, clearly negative an edge, zero flat. You can read the edge and the
flat verdict straight off the shape of `M` without computing `R` in full. Then report how
many pixels survive thinning and whether your corner is one of them.

### Part B · What survives a change of picture — 4 marks

Harris scores every pixel. To turn scores into a list of corners you have to decide which
scores count, and the obvious way is to pick a number and keep everything above it. This
part asks whether that number travels.

The same board is shown three ways: as it is, turned by 90 degrees, and at **half the
contrast**, which looks washed out while every shape stays in exactly the same place.

**B1 (1 mark)** — `R` at your corner on the original and on the half-contrast board, and
the ratio between them. **The ratio is not 2.** Say in one sentence why it is what it is,
in terms of how many gradients get multiplied together to make `R`.

**B2 (1 mark)** — choose a threshold `T` that keeps every corner of the **original** board
and nothing else. Then apply that same `T`, unchanged, to the turned picture and to the
half-contrast one, and report what each keeps. The notebook checks your `T` against the
original; the other two counts are the point of the question.

**B3 (2 marks)** — drop the threshold and keep the **strongest N** instead. Report how
many of the original's corners come back on each picture, then say in one sentence which
of the two rules you would use on photographs taken in different light, and why. *One mark
for the counts, one for the sentence.*

---

## 💾 Submitting

1. **Run every cell from top to bottom, and run the packing cell last.**
2. In Colab: **File → Download → Download .ipynb**
3. **Rename the downloaded file to exactly `lab05.ipynb`.** Colab usually calls it
   `Copy of lab05.ipynb`, and that name will not be accepted.
4. Open your own repository:
   `github.com/BITS-F459-Computer-Vision/f459-<your BITS ID, lowercase>`
5. **Add file → Upload files**, drag `lab05.ipynb` in, then **Commit changes**.
6. **Click the file on GitHub and look at it before you leave.** You should see your own
   outputs in it.

> ⚠️ **The packed block is what gets marked.** If you change an answer above and do not run
> the packing cell again, the block still holds the old one. This was set out in the Lab 3
> feedback and it is not accepted from Lab 4 onwards.

Uploading again later replaces the file, so you can submit more than once. The last one counts.

## ✅ Before you leave

- [ ] `A1` filled in, both whole numbers
- [ ] `A2` filled in for all three places, three sums each
- [ ] `A3` has both eigenvalues and `R` rounded to a whole number
- [ ] `A4` has all three verdicts, the survivor count, and the sentence on thinning
- [ ] `B1` has both values of `R`, the ratio, and the reason written out
- [ ] `B2`'s threshold keeps the right number of corners on the original
- [ ] `B3` has both counts and the sentence on which rule to use
- [ ] Packing cell run **last**, its output visible
- [ ] Downloaded, renamed to exactly `lab05.ipynb`, uploaded to your repo
- [ ] You opened GitHub, clicked the file, and saw your outputs

---

## 🆘 Troubleshooting

| Problem | Fix |
|:--|:--|
| My `Ix` has the wrong sign | Work out which side of your window is brighter. The gradient is negative when brightness falls in the direction the kernel points |
| My `Ix` is not a whole number | You divided by something other than 8, or you smoothed the board first. Harris does not smooth before differentiating |
| My window runs off the board | The row or column outside is a copy of the nearest one inside. Same rule as Lab 4 |
| A2: my `Ixy` is zero at the corner | Then you have not got a corner. `Ixy` is only non-zero where `Ix` and `Iy` are both non-zero at the **same** pixel |
| A2: `M` looks different from the lecture | Check you summed over all nine pixels of the window, not just the centre one |
| A3: the eigenvalue shortcut does not work | It only applies when the two diagonal entries are equal. That is true at your corner, not at the edge |
| A3: my `R` is enormous | That is normal. `R` is built from products of four gradients, so it runs into the millions |
| A3: check your `R` | `det(M) = a² − b²` and `trace(M) = 2a`, so `R = (a² − b²) − 0.04 × (2a)²` |
| A4: I cannot get the edge verdict without `R` | Ask what `det(M)` is when one diagonal entry is zero. That settles the sign of `R` immediately |
| A4: my corner does not survive thinning | Re-check the pixel you marked. Thinning keeps only pixels that beat everything around them |
| B1: I expected the ratio to be 2 | Halving the contrast halves every gradient. Count how many gradients are multiplied together to make `R`, and raise 2 to that power |
| B2: no threshold seems to work | It has to keep every corner and nothing else. Start from the **weakest** corner's score and go just below it |
| B2: the half-contrast count is zero | That is the answer, not an error. That is the whole point of the question |
| "Write a proper sentence" | The written answers are checked for length. One clause is not enough |
| The packing cell errors | Run it after everything else. It uses variables the earlier cells define |

---

<div align="center">

### ⏭️ Next: **describing a corner, so it can be matched**

</div>
