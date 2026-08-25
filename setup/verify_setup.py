#!/usr/bin/env python3
"""
BITS F459 Computer Vision - Lab 0 environment check.

Usage:
    python setup/verify_setup.py --id 2023A7PS1234U --alias your-alias

Checks that Python, the required packages and OpenCV all actually work,
then writes setup_report.txt. Commit that file to your Classroom repo:

    git add setup_report.txt
    git commit -m "Lab 0 setup complete"
    git push
"""

import argparse
import hashlib
import importlib
import platform
import re
import subprocess
import sys
from datetime import datetime, timezone

MIN_PYTHON = (3, 10)

# import name -> pip name
REQUIRED = [
    ("numpy", "numpy"),
    ("cv2", "opencv-python"),
    ("matplotlib", "matplotlib"),
    ("PIL", "pillow"),
    ("skimage", "scikit-image"),
    ("sklearn", "scikit-learn"),
    ("gradio", "gradio"),
]
OPTIONAL = [("torch", "torch"), ("torchvision", "torchvision")]

GREEN, RED, YELLOW, CYAN, BOLD, OFF = (
    ("\033[32m", "\033[31m", "\033[33m", "\033[36m", "\033[1m", "\033[0m")
    if sys.stdout.isatty() else ("", "", "", "", "", "")
)
TICK, CROSS, DOT = "[ok]", "[XX]", "[--]"

ID_PATTERN = re.compile(r"^\d{4}[A-Za-z]\d[A-Za-z]{2}\d{3,4}[A-Za-z]$")


def rule(char="="):
    print(char * 60)


def check_python():
    v = sys.version_info
    ok = (v.major, v.minor) >= MIN_PYTHON
    mark = f"{GREEN}{TICK}{OFF}" if ok else f"{RED}{CROSS}{OFF}"
    print(f"  {mark} Python {v.major}.{v.minor}.{v.micro}"
          + ("" if ok else f"   -> need {MIN_PYTHON[0]}.{MIN_PYTHON[1]} or newer"))
    return ok, f"{v.major}.{v.minor}.{v.micro}"


def check_packages(packages, required=True):
    ok, found = True, {}
    for module, pip_name in packages:
        try:
            m = importlib.import_module(module)
            ver = getattr(m, "__version__", "?")
            found[pip_name] = ver
            print(f"  {GREEN}{TICK}{OFF} {pip_name:<16} {ver}")
        except Exception:
            found[pip_name] = None
            if required:
                ok = False
                print(f"  {RED}{CROSS}{OFF} {pip_name:<16} MISSING"
                      f"   -> pip install {pip_name}")
            else:
                print(f"  {DOT} {pip_name:<16} not installed (added in Week 4)")
    return ok, found


def check_it_actually_works():
    """Importing is not the same as working. Do real arithmetic on real pixels."""
    try:
        import numpy as np
        import cv2

        rng = np.random.default_rng(0)
        img = (rng.random((64, 64, 3)) * 255).astype(np.uint8)

        grey = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        assert grey.shape == (64, 64), "grayscale shape wrong"

        kernel = np.ones((3, 3), np.float32) / 9.0
        blurred = cv2.filter2D(grey.astype(np.float32), -1, kernel)
        assert blurred.shape == grey.shape, "convolution shape wrong"
        assert abs(float(blurred.mean()) - float(grey.mean())) < 5.0, "blur looks wrong"

        print(f"  {GREEN}{TICK}{OFF} colour conversion, convolution and array maths all run")
        return True
    except Exception as exc:
        print(f"  {RED}{CROSS}{OFF} packages import but do not work: {exc}")
        return False


def check_git():
    try:
        ver = subprocess.run(["git", "--version"], capture_output=True,
                             text=True, timeout=10).stdout.strip()
    except Exception:
        print(f"  {RED}{CROSS}{OFF} git not found   -> install from https://git-scm.com")
        return False, None, None

    def cfg(key):
        try:
            out = subprocess.run(["git", "config", "--get", key],
                                 capture_output=True, text=True, timeout=10).stdout.strip()
            return out or None
        except Exception:
            return None

    name, email = cfg("user.name"), cfg("user.email")
    print(f"  {GREEN}{TICK}{OFF} {ver}")
    if name and email:
        print(f"  {GREEN}{TICK}{OFF} git identity     {name} <{email}>")
        return True, name, email

    print(f"  {RED}{CROSS}{OFF} git identity not set   -> "
          'git config --global user.name "Your Name"')
    print("                                  -> "
          'git config --global user.email "your@email.com"')
    return False, name, email


def main():
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("--id", dest="student_id", help="your BITS ID, e.g. 2023A7PS1234U")
    ap.add_argument("--alias", dest="alias", help="your leaderboard alias")
    args = ap.parse_args()

    student_id = (args.student_id or input("BITS ID (e.g. 2023A7PS1234U): ")).strip().upper()
    alias = (args.alias or input("Leaderboard alias: ")).strip()

    print()
    rule()
    print(f"{BOLD}  BITS F459 Computer Vision - Lab 0 environment check{OFF}")
    rule()

    if not ID_PATTERN.match(student_id):
        print(f"  {YELLOW}!{OFF} '{student_id}' does not look like a BITS ID.")
        print("    Your ID seeds your personal lab numbers - check it is right.")
    if not alias:
        print(f"  {RED}{CROSS}{OFF} You need a leaderboard alias. Re-run with --alias.")
        sys.exit(1)

    seed = hashlib.sha256(student_id.encode()).hexdigest()[:8]
    print(f"\n  student ID  {student_id}")
    print(f"  alias       {alias}")
    print(f"  lab seed    {CYAN}{seed}{OFF}   (your lab numbers come from this)")

    print(f"\n{BOLD}Python{OFF}")
    py_ok, py_ver = check_python()

    print(f"\n{BOLD}Required packages{OFF}")
    pkg_ok, found = check_packages(REQUIRED)

    print(f"\n{BOLD}Deep-learning packages{OFF}")
    _, dl_found = check_packages(OPTIONAL, required=False)

    print(f"\n{BOLD}Does it actually compute?{OFF}")
    works = check_it_actually_works() if pkg_ok else False
    if not pkg_ok:
        print(f"  {DOT} skipped - install the missing packages first")

    print(f"\n{BOLD}Git{OFF}")
    git_ok, git_name, git_email = check_git()

    all_ok = py_ok and pkg_ok and works and git_ok
    stamp = datetime.now(timezone.utc).astimezone().strftime("%Y-%m-%d %H:%M:%S %z")

    print()
    rule()
    if all_ok:
        print(f"{BOLD}{GREEN}  ALL OK  -  you are ready for Week 1.{OFF}")
    else:
        print(f"{BOLD}{RED}  NOT READY  -  fix the {CROSS} lines above and run this again.{OFF}")
        print("  Beaten for 10 minutes? Switch to Colab and finish the lab.")
    rule()

    lines = [
        "BITS F459 Computer Vision - Lab 0 setup report",
        "=" * 46,
        f"status        : {'ALL OK' if all_ok else 'NOT READY'}",
        f"generated     : {stamp}",
        f"student id    : {student_id}",
        f"alias         : {alias}",
        f"lab seed      : {seed}",
        "",
        f"python        : {py_ver}",
        f"platform      : {platform.system()} {platform.release()} ({platform.machine()})",
        f"executable    : {sys.executable}",
        f"venv active   : {'yes' if sys.prefix != sys.base_prefix else 'no'}",
        f"git identity  : {git_name or '?'} <{git_email or '?'}>",
        "",
        "packages",
    ]
    for pip_name, ver in {**found, **dl_found}.items():
        lines.append(f"  {pip_name:<16} {ver or 'not installed'}")
    functional = "passed" if works else ("FAILED" if pkg_ok else "skipped (packages missing)")
    lines += ["", f"functional check : {functional}", ""]

    with open("setup_report.txt", "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
    print(f"  wrote {BOLD}setup_report.txt{OFF}")

    if all_ok:
        print("\n  Commit it to your Classroom repo to finish Lab 0:")
        print(f"    {CYAN}git add setup_report.txt{OFF}")
        print(f"    {CYAN}git commit -m \"Lab 0 setup complete\"{OFF}")
        print(f"    {CYAN}git push{OFF}\n")
    else:
        print()

    sys.exit(0 if all_ok else 1)


if __name__ == "__main__":
    main()
