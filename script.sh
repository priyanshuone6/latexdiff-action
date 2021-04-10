curl -o latexdiff.zip http://ctan.imsc.res.in/support/latexdiff.zip
unzip latexdiff.zip
cd latexdiff
sudo make install
cd ..
sudo apt install texlive-latex-base
git log -n 1 --skip 1 --pretty=format:"%H" ${{ inputs.file-paths }} | xargs -I{} git show {}:${{ inputs.file-paths }} > old_commit.tex
yes "" | latexdiff-vc --pdf old_commit.tex ${{ inputs.file-paths }}
git config user.name ${{ inputs.git-username }}
git config user.email ${{ inputs.git-email }}
git add \*.pdf
git reset latexdiff/*
git commit -m "${{ inputs.commit-msg }}"
git pull
git push