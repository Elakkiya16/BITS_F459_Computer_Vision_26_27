<div align="center">

# 🧠 Lab 9 · Convolutional Neural Networks with Keras

**BITS F459 · Computer Vision · CNNs**

![Time](https://img.shields.io/badge/⏱%20work-90%20minutes-00D9FF?style=for-the-badge)
![Marks](https://img.shields.io/badge/marks-10%20+%20bonus-FF6B6B?style=for-the-badge)
![Runs](https://img.shields.io/badge/runs%20in-Colab%20·%20no%20install-FFD93D?style=for-the-badge)
![Submit](https://img.shields.io/badge/submit-lab09.ipynb-6BCB77?style=for-the-badge)

### ▶️ **[OPEN THE NOTEBOOK](https://colab.research.google.com/github/Elakkiya16/BITS_F459_Computer_Vision_26_27/blob/main/labs/lab09/lab09.ipynb)** &nbsp;·&nbsp; **[LIVE BOARD](https://docs.google.com/spreadsheets/d/1Av5zW3LoIZkISvn4tBXggqMvJKZ9s1eBDP4t4AiGdf4/edit)**

</div>

---

## 🎯 Today

The demo on the screen builds a CNN on EuroSAT satellite photographs, one small step at a time. You build the
same thing, step by step, on **your own three classes of CIFAR-10** colour photographs, with
**your own network settings** from your BITS ID.

- Open the notebook, type your BITS ID in the **Setup** cell and run it. Keep its output visible.
- The notebook has **headings and empty cells only**. The headings match the demo sections.
- When the demo finishes a section, the task for that section appears on the clock screen. Do it in
  the empty cell under the same heading, print the line the heading asks for, and write **one line
  of inference** in the cell below it.
- When the screen says **Live board first**, work the number out from the formula and type it in
  **your row** of the live board **before** you run the cell that checks it.

---

## 📥 Load your data (Section 2)

Paste this in the empty cell under **2. Data Exploration**. It loads CIFAR-10 from Hugging Face in under a minute.

```python
from datasets import load_dataset
import numpy as np
cifar = load_dataset("uoft-cs/cifar10")
Xtr = np.stack(cifar["train"]["img"]);  ytr = np.array(cifar["train"]["label"])
Xte = np.stack(cifar["test"]["img"]);   yte = np.array(cifar["test"]["label"])
print(Xtr.shape, ytr.shape, Xte.shape, yte.shape)
```

It prints `(50000, 32, 32, 3) (50000,) (10000, 32, 32, 3) (10000,)`. Labels 0 to 9 are airplane, automobile, bird,
cat, deer, dog, frog, horse, ship, truck. If Colab says `datasets` is not found, run `!pip install datasets` first.

---

## ⏱ How the session runs

| | |
|:--|:--|
| **1:50 – 1:55 PM** | Open the notebook and the live board, run Setup |
| **1:55 – 3:05 PM** | Demo and tasks, Sections 1 to 12, released on the clock |
| **3:05 – 3:30 PM** | Section 13 open round: beat your own baseline, live leaderboard |
| **3:30 – 3:40 PM** | Run the Hand in cell, download, upload |

---

## 🏁 Marks

- **Six marks from the notebook.** Every printed answer is recomputed from your own BITS ID:
  S2 + S3 · S4 + S5 · S6 + S7 · S8 · S9 + S10 · S11 + S12.
- **Four marks from the live board:** B4, B6, B8 and B10. B10 must match your own confusion matrix.
  B12 is a guess and carries no mark.
- **Open round bonus (Section 13).** +1 if your improved network beats your own Section 10 accuracy by at
  least 2 points within your parameter budget, and +1 to the three best in the class. The bonus makes up
  lost marks; the total stays at most 10.
- A notebook run with someone else's BITS ID scores nothing.

---

## ✅ Before you submit

- [ ] The Setup cell shows **your** BITS ID
- [ ] Every section prints its line and has its one-line inference
- [ ] Your best open-round result is in column B13 of the live board
- [ ] The Hand in cell prints one line starting with `LAB09`
- [ ] Downloaded, kept the name `lab09.ipynb`, uploaded to `f459-<your BITS ID, lowercase>`
- [ ] You opened it on GitHub and saw the `LAB09` line

---

<div align="center">

**BITS F459 · Computer Vision · Prof Elakkiya R**

</div>
