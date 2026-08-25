<div align="center">

# 🧰 Lab 0 — Get Your Machine Ready

**BITS F459 · Computer Vision · 2026-27**

![Time](https://img.shields.io/badge/⏱%20time-30%20minutes-00D9FF?style=for-the-badge)
![When](https://img.shields.io/badge/when-Week%201%20session-FFD93D?style=for-the-badge)
![Marks](https://img.shields.io/badge/marks-0%20·%20but%20mandatory-FF6B6B?style=for-the-badge)
![Track](https://img.shields.io/badge/tracks-Local%20%7C%20Colab-6BCB77?style=for-the-badge)

**Nothing here is graded. Everything here decides whether Week 1 is fun or miserable.**

</div>

---

## ⚡ The 30-second version

You need five things working, in this order:

```
1️⃣ GitHub account  →  2️⃣ Classroom repo  →  3️⃣ Python  →  4️⃣ Packages  →  5️⃣ ALL OK + commit
```

If all five work, you're done. The rest of this page is how to get there and what to do when one of them fights you.

> 🎯 **Come to Week 1 with steps 1–4 already done.** We do this together in the first 30 minutes of the session, but 30 minutes is enough to *check* your setup, not enough to download Python on campus wifi with 39 other people. Do what you can at home.

---

## 🛤️ Two tracks — pick one, know both

<table>
<tr>
<th width="50%">💻 Track A — Local <br/><sub><b>recommended</b></sub></th>
<th width="50%">☁️ Track B — Google Colab <br/><sub><b>your safety net</b></sub></th>
</tr>
<tr valign="top">
<td>

Python + VS Code on your own laptop.

✅ Real developer workflow<br/>
✅ Fast for Weeks 1–5 (all CPU)<br/>
✅ Works offline, files are yours<br/>
⚠️ ~15 min to set up once

**Use this if your laptop is yours to install on.**

</td>
<td>

Runs in the browser. Nothing to install.

✅ Working in 5 minutes, guaranteed<br/>
✅ Free GPU — you'll need it from Week 6<br/>
✅ Identical for everyone, so I can help fast<br/>
⚠️ Needs internet; sessions time out

**Use this if Track A fights you.**

</td>
</tr>
</table>

> 🔑 **The golden rule of Lab 0:** if the local install has beaten you for **10 minutes**, stop and switch to Colab. You are here to do computer vision, not to fix `PATH`. Come back to Track A later in the week — I'll help in chamber hour.
>
> You will end up using **both** anyway: local for the NumPy weeks, Colab for the GPU weeks. Setting up both today is time well spent.

---

## 1️⃣ GitHub account + your leaderboard alias

<details open>
<summary><b>Do this first — everything else hangs off it</b></summary>

<br/>

1. Create an account at **[github.com/signup](https://github.com/signup)** if you don't have one.
   - Use an email you'll keep after graduating, not only your BITS one.
   - Your **username is public and permanent-ish**. Pick something you'd put on a CV. `elakkiya-r` ✅ · `xX_cvking_Xx` ❌
2. Get the **student pack** (free, worth doing): **[education.github.com/pack](https://education.github.com/pack)** — Copilot, free private repos and more, verified with your BITS ID.
3. **Choose your leaderboard alias.** This is the name the whole class sees on the weekly leaderboard. It is *not* your GitHub username and *not* your real name — that's the point. Keep it clean and keep it for the semester.

   > 🏷️ Write your alias down now. You'll enter it in step 5.

</details>

## 2️⃣ Join the GitHub Classroom

<details open>
<summary><b>This creates your personal repo for the semester</b></summary>

<br/>

1. Open the **Classroom invite link** shared in the session (and on the LMS).
2. Pick your name from the roster so your repo is linked to you. ⚠️ If you skip this, your submissions land nowhere.
3. Accept the assignment. GitHub creates a private repo just for you, named something like `bits-f459-labs-<your-username>`.
4. Clone it:

   ```bash
   git clone https://github.com/<classroom-org>/bits-f459-labs-<your-username>.git
   cd bits-f459-labs-<your-username>
   ```

   The exact URL is on your repo's green **Code** button.

5. Tell git who you are (once per machine):

   ```bash
   git config --global user.name  "Your Name"
   git config --global user.email "your@email.com"
   ```

   Use the **same email as your GitHub account**, or your commits won't be credited to you.

</details>

## 3️⃣ Python

<details open>
<summary><b>Track A · install Python 3.10 or newer</b></summary>

<br/>

Check what you already have — a lot of you have Python and don't know it:

```bash
python --version      # Windows
python3 --version     # macOS / Linux
```

If it says **3.10, 3.11, 3.12 or 3.13**, skip ahead. If it errors or says 3.9 or lower, install:

| OS | How |
|----|-----|
| 🪟 **Windows** | [python.org/downloads](https://www.python.org/downloads/) → **tick "Add python.exe to PATH"** on the first screen. Miss that box and nothing below works. |
| 🍎 **macOS** | [python.org/downloads](https://www.python.org/downloads/), or `brew install python@3.12` |
| 🐧 **Linux** | `sudo apt install python3 python3-pip python3-venv` |

Then install **VS Code**: [code.visualstudio.com](https://code.visualstudio.com/) → open it → Extensions (`Ctrl/Cmd+Shift+X`) → install **Python** and **Jupyter** (both by Microsoft).

</details>

<details>
<summary><b>Track B · Colab</b> — click if you're going the browser route</summary>

<br/>

1. Go to **[colab.research.google.com](https://colab.research.google.com)** and sign in with any Google account.
2. `File → New notebook`. In the first cell type `import numpy, cv2; print("hello vision")` and press `Shift+Enter`.
3. It printed? You're done — numpy, OpenCV, matplotlib and PyTorch are already there.
4. For the GPU weeks: `Runtime → Change runtime type → T4 GPU`. Do it now so you know where it lives.
5. To open a lab notebook: `File → Open notebook → GitHub tab` → paste this repo's URL.

⚠️ **Colab forgets everything when the session ends.** Anything you want to keep, download it or push it to your repo before you close the tab.

</details>

## 4️⃣ Create a virtual environment and install the packages

<details open>
<summary><b>Track A only — keeps this course's packages out of the rest of your laptop</b></summary>

<br/>

From inside your cloned repo folder:

```bash
# create it (once)
python -m venv .venv          # Windows
python3 -m venv .venv         # macOS / Linux

# activate it (every time you open a new terminal)
.venv\Scripts\activate        # Windows PowerShell
source .venv/bin/activate     # macOS / Linux
```

Your prompt should now start with `(.venv)`. That's how you know it worked.

```bash
pip install --upgrade pip
pip install -r setup/requirements.txt
```

☕ Takes 2–4 minutes. In VS Code, press `Ctrl/Cmd+Shift+P` → **Python: Select Interpreter** → choose the one with `.venv` in the path.

> 🪶 **This is the light install** — NumPy, OpenCV, Matplotlib, Jupyter and Gradio, enough for Weeks 1–3. **PyTorch is not included**; it's a multi-GB download you don't need yet. We install it together in **Week 4** with `setup/requirements-dl.txt`.

</details>

## 5️⃣ Verify — and prove it

<details open>
<summary><b>The one command that checks everything</b></summary>

<br/>

```bash
python setup/verify_setup.py --id 2023A7PS1234U --alias your-alias
```

Use **your** BITS ID and **your** leaderboard alias. Your ID seeds the numbers in every lab's verification questions — nobody else gets your numbers, so it has to be right.

You want to see:

```
============================================
  ALL OK  —  you are ready for Week 1.
============================================
  wrote setup_report.txt
```

Then commit it:

```bash
git add setup_report.txt
git commit -m "Lab 0 setup complete"
git push
```

✅ **When that push succeeds, Lab 0 is done.** That one file proves Python runs, the packages import, OpenCV actually computes, git works, and your Classroom repo is live — the whole chain, in one shot.

<sub>On Colab: run the same script in a cell with `!python verify_setup.py --id ... --alias ...` after cloning this repo, then download `setup_report.txt` and add it to your repo through the GitHub web UI.</sub>

</details>

---

## ✅ Walk-in checklist

Print this, tick it, bring it:

- [ ] GitHub account exists and I know my username
- [ ] Leaderboard alias chosen
- [ ] Classroom assignment accepted, repo cloned
- [ ] `git config` done with my GitHub email
- [ ] Python 3.10+ responds to `python --version`
- [ ] VS Code with Python + Jupyter extensions
- [ ] `.venv` created and activated
- [ ] `pip install -r setup/requirements.txt` finished clean
- [ ] `verify_setup.py` printed **ALL OK**
- [ ] `setup_report.txt` committed and pushed
- [ ] Colab opened once and a cell run — my fallback is ready

---

## 🚑 When it breaks

<details>
<summary><b>Common failures and the actual fix</b></summary>

<br/>

| 😖 What you see | 💡 What it means | 🔧 Fix |
|---|---|---|
| `python: command not found` | Not installed, or not on PATH | Windows: reinstall and **tick "Add to PATH"**. macOS/Linux: use `python3` |
| `'pip' is not recognized` | Same PATH problem | `python -m pip install ...` instead of `pip install ...` |
| `.venv\Scripts\activate` → *running scripts is disabled* | PowerShell execution policy | Run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`, answer `Y` |
| `ModuleNotFoundError: cv2` after installing | Wrong interpreter — you installed into one Python, VS Code is using another | Check `(.venv)` is in your prompt; re-run **Python: Select Interpreter** |
| `error: externally-managed-environment` | System Python is protected (Mac/Linux) | You forgot to activate the venv. Activate it, don't use `--break-system-packages` |
| Install stuck at *Building wheel* | Compiling from source on an old pip | `pip install --upgrade pip` then retry |
| `Permission denied (publickey)` on push | SSH key not set up | Clone with the **HTTPS** URL instead |
| Push asks for a password and rejects it | GitHub killed password auth | Use a **Personal Access Token** as the password: GitHub → Settings → Developer settings → Tokens (classic) → `repo` scope |
| Everything is slow / disk full | OpenCV + friends need ~1.5 GB | Free up space, or go Track B |

Still stuck after **10 minutes**? Switch to Colab, finish the lab, and bring the laptop to chamber hour. Don't lose the session to an install.

</details>

<details>
<summary><b>Why a virtual environment at all?</b></summary>

<br/>

Because in Week 4 you'll install PyTorch, in Week 9 something that wants a different NumPy, and in Week 11 a diffusion library with strong opinions. Without a venv, each install quietly breaks the last one and by Week 10 nothing runs. With a venv, the damage is contained in one folder you can delete and rebuild in three minutes.

Deleting `.venv` and redoing step 4 is a completely legitimate repair. It is not failure.

</details>

<details>
<summary><b>What am I actually installing?</b></summary>

<br/>

| Package | What it's for |
|---------|---------------|
| **numpy** | Arrays. An image *is* a NumPy array — this is the whole course |
| **opencv-python** | Reference implementations we check your code against |
| **matplotlib** | Showing images and plots |
| **pillow** | Reading and writing image files |
| **scikit-image** | Classical vision utilities (Weeks 2–3) |
| **scikit-learn** | Classifiers and clustering (Weeks 3–4) |
| **jupyter** | Running the lab notebooks |
| **gradio** | Turning your code into a live app with sliders — Week 1's finale |

Added in Week 4: **torch**, **torchvision**.

</details>

---

<div align="center">

### ⏭️ Next: [Lab 1 — Filter Studio](../lab01)

*You'll build your own Instagram from scratch. No filter libraries. Just arithmetic on a grid of numbers.*

**Come with ALL OK on your screen.** 🩵

</div>
