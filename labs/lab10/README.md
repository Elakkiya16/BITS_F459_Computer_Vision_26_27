<div align="center">

# 🧠 Lab 10 · Pretrained CNN Architectures

**BITS F459 · Computer Vision · CNN Architectures**

![Time](https://img.shields.io/badge/⏱%20work-90%20minutes-00D9FF?style=for-the-badge)
![Marks](https://img.shields.io/badge/marks-10%20+%20bonus-FF6B6B?style=for-the-badge)
![Runs](https://img.shields.io/badge/runs%20in-Colab%20CPU%20·%20no%20install-FFD93D?style=for-the-badge)
![Submit](https://img.shields.io/badge/submit-lab10.ipynb-6BCB77?style=for-the-badge)

### ▶️ **[OPEN THE NOTEBOOK](https://colab.research.google.com/github/Elakkiya16/BITS_F459_Computer_Vision_26_27/blob/main/labs/lab10/lab10.ipynb)** &nbsp;·&nbsp; **[LIVE BOARD](https://docs.google.com/spreadsheets/d/1Jx8WM8JlOBO_e3xuVIIQvbDizc6N_zlsRUCU3Keyo2I/edit)**

</div>

---

## 🎯 Today

The demo on the screen opens every network from Week 7 in Keras: LeNet-5, AlexNet, VGG-16, ResNet-50,
Inception-v3, MobileNet-v2, EfficientNet and ConvNeXt. You do the same on **your own settings** from your BITS ID,
check every size against the formulas from the lecture, run a pretrained ResNet-50 on **your three classes of
flower photographs**, and measure what each network costs on the Colab CPU.

- Open the notebook, type your BITS ID in the **Setup** cell and run it. Keep its output visible.
- The notebook has **headings and empty cells only**. The headings match the demo sections.
- When the demo finishes a section, the task for that section appears on the clock screen. Do it in the empty
  cell under the same heading, print the line the heading asks for, and write **one line of inference** in the cell below it.
- Everything runs on the **free Colab CPU**. Use `weights=None` whenever you only need the architecture: it builds
  in seconds and downloads nothing. Only Sections 6, 7 and 13 need `weights="imagenet"`.
- **Live board:** [open the sheet](https://docs.google.com/spreadsheets/d/1Jx8WM8JlOBO_e3xuVIIQvbDizc6N_zlsRUCU3Keyo2I/edit) while signed in
  with your **BITS Google account** (fXXXXXXXX@dubai.bits-pilani.ac.in). Only your own row is editable.
- When the screen says **Live board first**, work the number out from the formula and type it in **your row**
  of the live board **before** you run the cell that checks it.

---

## 📥 Load your data

**Section 2: flower photographs** (5 classes, about 220 MB, one minute):

```python
p = keras.utils.get_file(origin="https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz", extract=True)
ROOT = os.path.dirname(glob.glob(os.path.join(p if os.path.isdir(p) else os.path.dirname(p), "**", "daisy"), recursive=True)[0])
```

`ROOT` then holds five folders: `daisy`, `dandelion`, `roses`, `sunflowers`, `tulips`.

**Section 13: Imagenette** (10 ImageNet classes, 160-pixel version, about 95 MB):

```python
q = keras.utils.get_file(origin="https://s3.amazonaws.com/fast-ai-imageclas/imagenette2-160.tgz", extract=True)
VAL = glob.glob(os.path.join(q if os.path.isdir(q) else os.path.dirname(q), "**", "val"), recursive=True)[0]
WNID = {"n01440764": 0, "n02102040": 217, "n02979186": 482, "n03000684": 491, "n03028079": 497,
        "n03394916": 566, "n03417042": 569, "n03425413": 571, "n03445777": 574, "n03888257": 701}
```

`VAL` holds one folder per class, named by WordNet ID; `WNID` gives the ImageNet output index of each folder, in
the order tench, English springer, cassette player, chain saw, church, French horn, garbage truck, gas pump,
golf ball, parachute.

---

## ⏱ How the session runs

| | |
|:--|:--|
| **1:50 – 1:55 PM** | Open the notebook and the live board, run Setup |
| **1:55 – 3:10 PM** | Demo and tasks, Sections 1 to 12, released on the clock |
| **3:10 – 3:30 PM** | Section 13 open round: fastest accurate model on Imagenette, live leaderboard |
| **3:30 – 3:40 PM** | Run the Hand in cell, download, upload |

---

## 🏁 Marks

- **Six marks from the notebook.** Every printed answer is recomputed from your own BITS ID:
  S2 + S3 · S4 + S5 · S6 + S7 · S8 + S9 · S10 + S11 · S12.
- **Four marks from the live board:** B3, B4, B8 and B10, typed before you run the cell.
- **Open round bonus (Section 13).** +1 if your top-1 accuracy on your 100 Imagenette images is 0.90 or more, and
  +1 to the three best in the class (ties go to the faster model). The bonus makes up lost marks; the total stays at most 10.
- A notebook run with someone else's BITS ID scores nothing.

---

## ✅ Before you submit

- [ ] The Setup cell shows **your** BITS ID
- [ ] Every section prints its line and has its one-line inference
- [ ] Your best open-round result is in column B13 of the live board
- [ ] The Hand in cell prints one line starting with `LAB10`
- [ ] Downloaded, kept the name `lab10.ipynb`, uploaded to `f459-<your BITS ID, lowercase>`
- [ ] You opened it on GitHub and saw the `LAB10` line

---

<div align="center">

**BITS F459 · Computer Vision · Prof Elakkiya R**

</div>
