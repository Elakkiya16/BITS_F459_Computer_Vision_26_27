<div align="center">

# 🛣️ Lab 7 · k-NN on a Street Photograph

**BITS F459 · Computer Vision · Week 7**

![Time](https://img.shields.io/badge/⏱%20work-two%20hours-00D9FF?style=for-the-badge)
![Marks](https://img.shields.io/badge/marks-10-FF6B6B?style=for-the-badge)
![Runs](https://img.shields.io/badge/runs%20in-Colab%20·%20no%20install-FFD93D?style=for-the-badge)
![Submit](https://img.shields.io/badge/submit-lab07a%20+%20lab07b-6BCB77?style=for-the-badge)

### ▶️ **[NOTEBOOK A IN COLAB](https://colab.research.google.com/github/Elakkiya16/BITS_F459_Computer_Vision_26_27/blob/main/labs/lab07/lab07a.ipynb)** &nbsp;·&nbsp; **[NOTEBOOK B IN COLAB](https://colab.research.google.com/github/Elakkiya16/BITS_F459_Computer_Vision_26_27/blob/main/labs/lab07/lab07b.ipynb)**

</div>

---

## 🎯 The point of today

This week's lectures built k-NN on a handful of points and made three choices: which distance,
whether to scale the features, and which k. Today you make all three on a **real photograph**.

**Notebook A.** The walkthrough's steps on a new street photograph, then on four more. The code
for every step is given and works. You choose the patches that are clearly sky, road and tree,
follow one patch through the vote, see what each of the three choices does to the map, and find
out what happens when the classifier meets a photograph from a darker, cloudy day. **Explore**
boxes after each step tell you what to change and what to record.

**Notebook B.** Twelve points generated from your BITS ID, so nobody else has your data. Each
question tells you a property, and you build a point or a choice that has it. Every question has
a worked example on a separate dataset first.

**Ten marks: three in A, seven in B.** One of the ten, E7, is a stretch question.

---

## ⏱ How the session runs

| | |
|:--|:--|
| **0:00 – 0:10** | The photograph, the three choices, and what a construction question is |
| **0:10 – 0:50** | Notebook A — explore k-NN on five street photographs |
| **0:50 – 1:50** | Notebook B — E1 to E7 on your own data |
| **1:50 – 2:00** | Pack, download, submit both notebooks |

While you work on Notebook B, I will come round and ask you about your map and one of your
answers.

If you run short, Sections 1 to 8 of A and E1 to E3 of B are the ones to have finished.

---

## 📋 What you do

### Notebook A · explore — 3 marks

| | | |
|:--|:--|:--|
| **1–3** | The photograph, its edges, and x₁, x₂ for every patch; the 400 numbers inside patches you choose | explore |
| **4** | Label 8 training and 4 validation patches per class | your turn |
| **5–6** | Feature space, and one patch you choose followed through the k-NN vote | your turn |
| **7–8** | Choose k, colour the photograph, and see what each of the three choices does | explore |
| **9** | Four more photographs: find where it fails, add 12 patches, and score again | your turn |
| **10** | The same work with scikit-learn | explore |

### Notebook B · k-NN by construction — 7 marks

| | | |
|:--|:--|:--|
| **E1** | Label your Q for k = 1, 3 and 5 | compute |
| **E2** | A point where 1-NN and 3-NN disagree | construct |
| **E3** | A point where L1 and L2 disagree | construct |
| **E4** | One added point, at least 2 from Q, that changes Q's label | construct |
| **E5** | The smallest stretch of x₁ that changes Q's label | search |
| **E6** | The fewest removals that change Q's label | search |
| **E7** | Stretch: find the hidden k and distance by testing points | probe it |

---

## 🧠 How to approach a construction question

1. **Read the worked example first.** It answers the same question on a different dataset,
   step by step.
2. **Write the test.** Turn the property into a function that returns True or False, using
   your own `knn_predict`.
3. **Then search.** Try the points of a grid, every half unit from 0 to 10, and keep the first
   that passes. That is 441 points and takes under a second.
4. **Check the constraints, not just the goal.** Not Q, not a training point, at least 2 from Q,
   at most one decimal place.

---

## 🤝 Working with others, and with AI

You may talk to anyone and use any tool. A tool can write you a search loop, and the loop still
has to run on your data. Nobody else's answer to E1, E5 or E6 is yours, because nobody else
has your twelve points.

What you cannot do is submit an answer you have not run. The checker recomputes everything.

---

## ✅ Before you submit

- [ ] Notebook A: `THRESH` back at 20, your 36 patches clearly their class, Explore 4, 6 and 7 recorded
- [ ] You can point to one wrong patch on your map and explain it from its two numbers
- [ ] The same BITS ID in both notebooks
- [ ] The last cell of each notebook run **last**: A prints the `LAB07A` line, B says `format OK`
- [ ] Both files downloaded and renamed to exactly `lab07a.ipynb` and `lab07b.ipynb`
- [ ] Both uploaded to your repo, `f459-<your BITS ID, lowercase>`
- [ ] You clicked each file on GitHub and saw your outputs in it

---

<div align="center">

**BITS F459 · Computer Vision · Dr Elakkiya R**

</div>
