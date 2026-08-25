# BITS F459 — Computer Vision

**BITS Pilani, Dubai Campus · First Semester 2026-27**
Instructor-in-charge: Prof. Elakkiya R

This is the course repository. Everything you need for the labs, the mini-project and the leaderboard lives here. Star it, clone it, and check it before every session.

---

## How this course works

Vision is learned by building. Every week has a two-hour lab session in which you write the algorithm of the week yourself — from raw NumPy in the first weeks to fine-tuned deep models by the end — and verify it against a reference before you leave the room. Lectures give you the ideas; the lab is where they become yours.

The arc runs from pixels to language: first classical image processing and features, then machine learning and neural networks, then the modern deep-learning stack for recognition, detection, segmentation, motion, depth, generation and vision–language models.

## Weekly schedule

| Wk | Topic | Lab | Reading |
|----|-------|-----|---------|
| 1 | Images & preprocessing | `labs/lab01` — Filter Studio | T2 Ch.3, R1 Ch.1 |
| 2 | Feature extraction: edges, corners, descriptors | `labs/lab02` | T2 Ch.7 |
| 3 | Segmentation: thresholding, clustering, morphology | `labs/lab03` | T2 Ch.3, 7 |
| 4 | Machine learning for vision | `labs/lab04` | T1 Ch.2, 5–6 |
| 5 | Neural networks | `labs/lab05` | T1 Ch.3–4, 7 |
| 6 | Convolutional neural networks | `labs/lab06` | T1 Ch.10, R1 Ch.3–5 |
|   | **Mid-semester examination — 22 Oct 2026 (AN), closed book, Weeks 1–6** | | |
| 7 | Transfer learning | `labs/lab07` | R1 Ch.6, T1 Ch.9 |
| 8 | Object detection | `labs/lab08` | R1 Ch.7, T2 Ch.6 |
| 9 | Deep segmentation & foundation models | `labs/lab09` | T2 Ch.6, R2 |
| 10 | Motion, video & depth | `labs/lab10` | T2 Ch.9, 12 |
| 11 | Generative models | `labs/lab11` | T1 Ch.15, 17–18 |
| 12 | Vision–language models & synthesis | `labs/lab12` | T1 Ch.12, R2 |
|   | **Comprehensive examination — 18 Dec 2026 (AN), closed book** | | |

Lab folders are published the morning of each session.

## Evaluation

| Component | Weight | Notes |
|-----------|--------|-------|
| EC1 Lab assignments | 20% | Weekly, individual, assessed in-session (see below) |
| EC2 Mini project Term-I | 10% | Problem formulation + literature review, before mid-sem |
| EC3 Mid-semester exam | 20% | 22.10.2026 AN · closed book · Weeks 1–6 |
| EC4 Mini project Term-II | 20% | Implementation + demo + full paper in ICCV/ECCV format |
| EC5 Comprehensive exam | 30% | 18.12.2026 AN · closed book |

### Lab assignments (EC1)

Each lab is a hackathon-style session, marked out of 10: **4 verification** questions (numerical answers seeded from your student ID — nobody has the same numbers), **4 task** marks for the implementation, and **2 stretch** marks for going beyond. Marks are awarded during the session; a session you miss is a session you score zero on that week. Your running standing appears on the class leaderboard under the alias you choose in Week 1.

### Mini project (EC2 + EC4)

Teams of two. Topics come from the second half of the course only — detection, segmentation, motion & depth, generative models, or vision–language — and are released in `mini-project/`. Term-I delivers a problem statement and literature review; Term-II delivers working code, a live demo, and a paper in conference format.

## Textbooks

- **T1** Prince, *Understanding Deep Learning* — free at [udlbook.github.io/udlbook](https://udlbook.github.io/udlbook/)
- **T2** Szeliski, *Computer Vision: Algorithms and Applications*, 2nd ed. — free at [szeliski.org/Book](https://szeliski.org/Book/)
- **R1** Elgendy, *Deep Learning for Vision Systems*
- **R2** Stanford CS231n course notes
- **R3** Recent CVPR / ICCV / ECCV papers, linked per week

## Getting set up

```bash
git clone https://github.com/Elakkiya16/BITS_F459_Computer_Vision_26_27.git
cd BITS_F459_Computer_Vision_26_27
pip install -r setup/requirements.txt
python setup/verify_setup.py
```

`verify_setup.py` should print **ALL OK**. Do this before Week 1 — there is no time in the session to fix an environment.

## Repository layout

```
setup/          requirements + environment check
labs/labXX/     weekly notebook + TASKS.md (published on the day)
mini-project/   topic list, milestones, paper template
leaderboard/    how the class leaderboard works
docs/           browser demos (hosted via GitHub Pages)
```

## Submitting lab work

Labs are distributed and collected through GitHub Classroom; the join link is shared in the Week 1 session. Commit your notebook to your classroom repo before the session ends — the timestamp of your last commit is what counts.

## Live demos

Browser demos for the labs are hosted at **https://elakkiya16.github.io/BITS_F459_Computer_Vision_26_27/** — no install, works on a phone.

---

*Questions: raise an Issue in this repository or bring them to the chamber consultation hour.*
