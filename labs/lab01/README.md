<div align="center">

# 📸 Lab 1 — Image Operations, Live on Your Face

**BITS F459 · Computer Vision · Week 1**

![Time](https://img.shields.io/badge/⏱%20time-in%20session-00D9FF?style=for-the-badge)
![Marks](https://img.shields.io/badge/marks-none%20·%20demo%20lab-FF6B6B?style=for-the-badge)
![Runs](https://img.shields.io/badge/runs%20in-Colab%20·%20no%20install-FFD93D?style=for-the-badge)
![Save](https://img.shields.io/badge/save%20to-your%20lab%20repo-6BCB77?style=for-the-badge)

### ▶️ **[OPEN THE NOTEBOOK IN COLAB](https://colab.research.google.com/github/Elakkiya16/BITS_F459_Computer_Vision_26_27/blob/main/labs/lab01/lab01_selfie_studio.ipynb)**

*One click. Nothing to install. Works on a phone.*

</div>

---

## 🎯 What you'll do

Take one selfie, then run **every operation from the lecture** on your own face — with sliders, so you see the arithmetic change the picture as you drag.

| | Operation | Formula | Slide |
|:--:|-----------|---------|:-----:|
| **Point operations** — each pixel changed on its own ||||
| 1 | Brightness | $g = f + \beta$ | 40 |
| 2 | Contrast | $g = \alpha \cdot f$ | 41 |
| 3 | Arithmetic & blending | $g = \lambda f_1 + (1-\lambda) f_2$ | 42 |
| 8 | Thresholding | $g = 255$ if $f \ge T$, else $0$ | 47 |
| **Geometric** — values stay, positions move ||||
| 4 | Translation | $(x', y') = (x + t_x,\; y + t_y)$ | 43 |
| 5 | Scaling | $(x', y') = (s_x x,\; s_y y)$ | 44 |
| 6 | Rotation | rotate about the centre | 45 |
| 7 | Flipping | $x' = W - 1 - x$ | 46 |
| **Neighbourhood** — a pixel depends on its neighbours ||||
| 9 | Blurring (mean filter) | average of the 3×3 neighbourhood | 48 |
| 10 | Sharpening (convolution) | $g(x,y) = \sum_i \sum_j K(i,j) f(x+i, y+j)$ | 50–53 |

By the end you'll see why **one number** — a 5 instead of a 4 in the kernel — turns "make this crisper" into "find every boundary in the scene".

---

## 🚀 How to run it

1. Click **[Open the notebook in Colab](https://colab.research.google.com/github/Elakkiya16/BITS_F459_Computer_Vision_26_27/blob/main/labs/lab01/lab01_selfie_studio.ipynb)**
2. Click **Copy to Drive** at the top — otherwise your changes are not saved
3. Run each cell with **Shift + Enter**, top to bottom
4. When the camera appears, click **📸 CLICK TO CAPTURE**

<details>
<summary>🚑 <b>Camera not working?</b></summary>

<br/>

Change one line in the selfie cell:

```python
SOURCE = "upload"      # instead of "camera"
```

You'll be asked to pick a photo instead — on a phone that opens the camera directly. Everything below works exactly the same.

Common causes: you're in Safari (use **Chrome**), you clicked *Block* on the permission popup (reload and click *Allow*), or your laptop is managed by an institution that disables the camera.

</details>

---

## 💾 How to save your work to your repository

Your notebook lives in Google Drive while you work. Getting it into **your GitHub lab repo** is the skill we're practising today.

### In Colab: **File → Save a copy in GitHub**

Then fill the dialog:

| Field | What to put |
|-------|-------------|
| **Repository** | `BITS-F459-Computer-Vision/f459-<your BITS ID>` |
| **Branch** | `main` |
| **File path** | `labs/lab01/lab01_selfie_studio.ipynb` |
| **Commit message** | `Lab 1 complete` |
| ☑️ **Include a link to Colab** | tick it |

Click **OK**.

> 🔐 **First time only:** Colab asks permission to access your GitHub account. Click **Authorize** in the popup. If nothing happens, your browser blocked it — allow popups for `colab.research.google.com` and try again.

> ⚠️ **Run every cell before you save.** Colab saves the notebook *with its outputs*, so your selfie and your results are stored inside the file. Save it early and it lands on GitHub blank.

<details>
<summary>🔁 <b>Alternative: download and push from your laptop</b></summary>

<br/>

If Colab's GitHub save refuses to work:

1. **File → Download → Download .ipynb**
2. Move the file into your cloned repo, under `labs/lab01/`
3. Then:

```bash
git add labs/lab01/
git commit -m "Lab 1 complete"
git push
```

</details>

---

## 📤 Putting it in your repo

This lab is a **warm-up — there are no marks.** It exists so that by the end of the session you have
proved three things work: your Colab, your GitHub repo, and the link between them.

Saving it is the point. From next week the same three steps are how every lab is submitted, so get
them working now while there is nothing at stake.

### ✅ Before you leave

- [ ] Selfie captured (or photo uploaded)
- [ ] All ten operations run — every slider tried
- [ ] The final grid rendered with your face in it
- [ ] Saved to `BITS-F459-Computer-Vision/f459-<your BITS ID>` at `labs/lab01/`
- [ ] Opened the repo on GitHub and **checked the file is actually there**

That last tick is the one that matters. If the notebook is sitting in your repo with your face in it,
everything is wired up correctly and next week will be easy.

---

## 🆘 Troubleshooting

| 😖 Problem | 🔧 Fix |
|-----------|--------|
| "Save a copy in GitHub" doesn't list my repo | Sign in to GitHub in the same browser, then reload Colab. Check you accepted the repo invitation |
| No repositories appear at all | You haven't authorized Colab yet — the popup was blocked. Allow popups and retry |
| I can't find my repo name | It's `f459-` followed by your BITS ID in lowercase, e.g. `f459-2023a7ps1234u` |
| Saved, but GitHub shows an empty notebook | You saved before running the cells. Run all, then save again |
| Runtime disconnected and I lost everything | Colab drops idle sessions. Re-run from the top — it takes two minutes. Save to GitHub as soon as you have results |
| Sliders don't appear | Run the Setup cell first, then the cell with the sliders |

---

<div align="center">

### ⏭️ Next week: **Feature extraction — edges, corners, descriptors**

*We stop calling `filter2D` and write convolution ourselves — then use it to find what matters in an image.*

</div>
