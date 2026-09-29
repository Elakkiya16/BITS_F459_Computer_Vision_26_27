<div align="center">

# 🧩 Lab 6 · Describing and Grouping

**BITS F459 · Computer Vision · Week 6**

![Time](https://img.shields.io/badge/⏱%20work-two%20hours-00D9FF?style=for-the-badge)
![Marks](https://img.shields.io/badge/marks-10-FF6B6B?style=for-the-badge)
![Runs](https://img.shields.io/badge/runs%20in-Colab%20·%20no%20install-FFD93D?style=for-the-badge)
![Submit](https://img.shields.io/badge/submit-lab06.ipynb-6BCB77?style=for-the-badge)

### ▶️ **[OPEN THE NOTEBOOK IN COLAB](https://colab.research.google.com/github/Elakkiya16/BITS_F459_Computer_Vision_26_27/blob/main/labs/lab06/lab06.ipynb)**

</div>

---

## 🎯 The point of today

Every lab so far has asked you to compute something from an input you were given. Today
eight of the ten questions ask the opposite. **You are told a property, and you build an
input that has it.**

There is no single right answer to those questions. There are infinitely many, and yours
will not be anyone else's. A checker runs whatever you hand in and decides whether it
really has the property. An answer that looks right but does not work is worth nothing,
and an answer that works is worth full marks however you found it.

Two more questions give you a piece of code whose behaviour is hidden and ask you to work
out what it does by experimenting on it. Yours is not the same as the person next to you.

**Ten questions, one mark each.** No image to bring, no upload, nothing to install.

---

## ⏱ How the session runs

| | |
|:--|:--|
| **0:00 – 0:10** | What a construction question is, and how the checker works |
| **0:10 – 1:00** | Part A — the descriptor, questions 1 to 5 |
| **1:00 – 1:50** | Part B — segmentation, questions 6 to 10 |
| **1:50 – 2:00** | Pack, download, submit |

If you run short, questions 1, 2, 6 and 7 are the four to have finished.

---

## 📋 What you do

### Part A · the descriptor — 5 marks

| | | |
|:--|:--|:--|
| **1** | Work out what the hidden `mystery_descriptor` does, and reimplement it | probe it |
| **2** | Build a patch whose descriptor hits your own target within 0.03 | construct |
| **3** | Build a patch with at most four non-zero pixels and exactly two non-zero bins | construct |
| **4** | Build two patches that look nothing alike but describe almost identically | construct |
| **5** | Find the smallest brightening of your own patch that moves the descriptor | measure |

Question 5 has an obvious answer that is wrong. Work out why before you trust it.

### Part B · segmentation — 5 marks

| | | |
|:--|:--|:--|
| **6** | Work out what the hidden `mystery_kmeans` does, and reimplement it | probe it |
| **7** | Build a dataset that takes at least four iterations to converge | construct |
| **8** | Find the smallest number of points for which that is possible | search |
| **9** | Build a dataset where k-means gives the wrong answer **and scores better for it** | construct |
| **10** | Show whether any starting point would have saved it | search |

Question 9 is the one to understand. The lecture said k-means cannot handle non-spherical
clusters. Question 9 asks you to prove it, and question 10 asks you to say where the fault
actually lies: in the algorithm, or in what the algorithm is trying to minimise.

---

## 🧠 How to approach a construction question

1. **Write the test first.** Turn the stated property into a function that returns True or
   False. You cannot search for something you cannot recognise.
2. **Then search.** Random guessing, or start anywhere and keep any change that reduces the
   error. Both are legitimate and both are fast.
3. **Check the constraints, not just the goal.** Most lost marks will be patches with the
   wrong shape or values outside 0 to 255, not wrong ideas.

For the two hidden functions: design the smallest input that would tell one possible rule
apart from another, and compare against `lecture_descriptor` or `lecture_kmeans` every time.
A patch that is all one value, a single bright pixel, a clean vertical edge, the same patch
at twice the contrast. Points in a line, points exactly between the two centres, a cluster
with one outlier in it.

---

## 🤝 Working with others, and with AI

You may talk to anyone and use any tool you like. That is not a concession, it is the point:
none of it produces an answer on its own. A tool can write you a search loop, and the loop
still has to run on your data, against your target, with your hidden function. Nobody can
hand you question 5's number or question 8's N, because neither is written down anywhere.

What you cannot do is submit an answer you have not run. The checker re-runs everything.

---

## ✅ Before you submit

- [ ] Questions 1 and 6 print `match` on every hidden case
- [ ] Questions 2, 3 and 4 print numbers inside the stated limits
- [ ] Questions 7, 8 and 9 print the iteration counts and SSEs you expect
- [ ] Question 10 has both counts and a one-word verdict
- [ ] The packing cell was run **last** and its output is visible
- [ ] File downloaded, renamed to exactly `lab06.ipynb`, uploaded to your repo
- [ ] You clicked the file on GitHub and saw your outputs in it

---

<div align="center">

**BITS F459 · Computer Vision · Dr Elakkiya R**

</div>
