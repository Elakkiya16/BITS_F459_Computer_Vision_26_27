<div align="center">

# 🦓 Lab 11 · Object Detection

**BITS F459 · Computer Vision · Object Detection**

![Time](https://img.shields.io/badge/⏱%20work-90%20minutes-00D9FF?style=for-the-badge)
![Marks](https://img.shields.io/badge/marks-10%20+%20bonus-FF6B6B?style=for-the-badge)
![Runs](https://img.shields.io/badge/runs%20in-Colab%20CPU-FFD93D?style=for-the-badge)
![Submit](https://img.shields.io/badge/submit-lab11.ipynb-6BCB77?style=for-the-badge)

### ▶️ **[OPEN THE NOTEBOOK](https://colab.research.google.com/github/Elakkiya16/BITS_F459_Computer_Vision_26_27/blob/main/labs/lab11/lab11.ipynb)** &nbsp;·&nbsp; **[LIVE BOARD](https://docs.google.com/spreadsheets/d/1VKc20jU8JoLgjBTQsVtdUxXnnlwGk5vmrAaHqCfSv7M/edit)**

</div>

---

## 🎯 Today

The demo on the screen takes every idea from the detection lecture and runs it on real photographs: box formats,
IoU, the raw output of YOLO, NMS, Faster R-CNN against YOLO against RT-DETR, average precision, thresholds and
open-vocabulary detection. You do the same on **your own settings** from your BITS ID, on **African Wildlife**:
photographs of buffalo, elephants, rhinos and zebras with a box around every animal. You write IoU, NMS and AP
yourself and check them against torchvision, and you find out what a COCO detector does with two animals it has
never been taught.

- Open the notebook, type your BITS ID in the **Setup** cell and run it. Keep its output visible.
- The notebook has **headings and empty cells only**. The headings match the demo sections.
- When the demo finishes a section, the task for that section appears on the clock screen. Do it in the empty
  cell under the same heading, print the line the heading asks for, and write **one line of inference** in the cell below it.
- Everything runs on the **free Colab CPU**. Section 1 installs `ultralytics` (about 30 seconds). Each model
  downloads its weights the first time you use it.
- **Live board:** [open the sheet](https://docs.google.com/spreadsheets/d/1VKc20jU8JoLgjBTQsVtdUxXnnlwGk5vmrAaHqCfSv7M/edit) while signed in
  with your **BITS Google account** (fXXXXXXXX@dubai.bits-pilani.ac.in). Only your own row is editable.
- When the screen says **Live board first**, work the number out by hand and type it in **your row**
  of the live board **before** you run the cell that checks it.

---

## 📥 Load your data

**African Wildlife** (4 classes, about 100 MB, under a minute):

```python
import os, glob, urllib.request, zipfile, yaml
URL = "https://github.com/ultralytics/assets/releases/download/v0.0.0/african-wildlife.zip"
ROOT = "african-wildlife"
if not os.path.isdir(os.path.join(ROOT, "images")):
    urllib.request.urlretrieve(URL, "african-wildlife.zip")
    zipfile.ZipFile("african-wildlife.zip").extractall(ROOT)
VAL = sorted(glob.glob(os.path.join(ROOT, "images", "val", "*.jpg")))
```

`ROOT` holds `images/{train,val,test}`, `labels/{train,val,test}` and `african-wildlife.yaml`. Every image has a
label file with the same name: one line per animal, `class cx cy w h`, with the four numbers divided by the image
width or height.

**Your images.** Always draw them from `VAL` in this sorted order with Python's `random`, exactly as the clock
screen says, so that your answers can be checked: `sorted(random.Random(SEED).sample(VAL, 50))` for Sections 8 to 10,
`sorted(random.Random(SEED + 1).sample(VAL, 100))` for the open round, `sorted(random.Random(SEED + 2).sample(VAL, 10))`
for Section 7.

**Fine-tuning in the open round** needs a dataset file with full paths. Keep the val images out of training:

```python
open("aw.yaml", "w").write(f"path: {os.path.abspath(ROOT)}\ntrain: images/train\nval: images/test\n"
                           "names:\n  0: buffalo\n  1: elephant\n  2: rhino\n  3: zebra\n")
```

---

## ⏱ How the session runs

| | |
|:--|:--|
| **1:50 – 1:55 PM** | Open the notebook and the live board, run Setup and Section 1 |
| **1:55 – 3:05 PM** | Demo and tasks, Sections 2 to 10, released on the clock |
| **3:05 – 3:30 PM** | Section 11 open round: best mAP on your 100 images, live leaderboard |
| **3:30 – 3:40 PM** | Run the Hand in cell, download, upload |

---

## 🏁 Marks

- **Six marks from the notebook.** Every printed answer is recomputed from your own BITS ID and the dataset labels:
  S2 + S3 · S4 + S5 · S6 · S7 · S8 + S9 · S10.
- **Four marks from the live board:** B3, B4, B5 and B8, typed before you run the cell.
- **Open round bonus (Section 11).** Your mAP is recomputed from the `pred` you hand in (11-point AP at IoU 0.5,
  mean of the four classes, at most 20 boxes per image). +1 if it is 0.75 or more, and +1 to the three best in the
  class (ties go to the faster method). The bonus makes up lost marks; the total stays at most 10.
- A notebook run with someone else's BITS ID scores nothing.

---

## ✅ Before you submit

- [ ] The Setup cell shows **your** BITS ID
- [ ] Every section prints its line and has its one-line inference
- [ ] Your best open-round result is in column B11 of the live board
- [ ] The Hand in cell prints one line starting with `LAB11`
- [ ] Downloaded, kept the name `lab11.ipynb`, uploaded to `f459-<your BITS ID, lowercase>`
- [ ] You opened it on GitHub and saw the `LAB11` line

---

<div align="center">

**BITS F459 · Computer Vision · Prof Elakkiya R**

</div>
