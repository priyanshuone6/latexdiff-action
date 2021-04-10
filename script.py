#!/usr/bin/env python

import os
import subprocess


paths = os.getenv("INPUT_FILE-PATHS", "").split(",")
options = os.getenv('INPUT_OPTIONS')
#repo = os.getenv("GITHUB_REPOSITORY")

def run_cmd(command):
    #print(command)
    result = subprocess.run(command.split(' '), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(result.stdout)
    print(result.stderr)
    return result.stdout.decode("utf-8") 


run_cmd("curl -o latexdiff.zip http://ctan.imsc.res.in/support/latexdiff.zip")
run_cmd("unzip latexdiff.zip")
run_cmd("cd latexdiff")
run_cmd("sudo make install")
run_cmd("cd ..")
run_cmd("sudo apt install texlive-latex-base")
run_cmd("git config user.name github-actions[bot]")
run_cmd("git config user.email 41898282+github-actions[bot]@users.noreply.github.com")

for path in paths:
    commit_id = run_cmd(f'git log -n 1 --skip 1 --pretty=format:%H {path}')
    run_cmd(f'git show {commit_id}:{path} > old_commit.yml')
    run_cmd(f'yes "" 2>/dev/null | latexdiff-vc {options} --pdf old_commit.tex {path}')
    run_cmd(r"git add \*.pdf")
    run_cmd("git reset latexdiff/*")
    run_cmd(f'git commit -m "Update the pdf of {path}"')
    run_cmd("git pull")
    run_cmd("git push")
