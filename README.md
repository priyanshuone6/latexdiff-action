# <img width="24" height="24" src="icon.svg"> latexdiff-action
[![GitHub Marketplace](https://img.shields.io/badge/Marketplace-latexdiff--action-blue.svg?colorA=24292e&colorB=0366d6&style=flat&longCache=true&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAYAAAAfSC3RAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAM6wAADOsB5dZE0gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAERSURBVCiRhZG/SsMxFEZPfsVJ61jbxaF0cRQRcRJ9hlYn30IHN/+9iquDCOIsblIrOjqKgy5aKoJQj4O3EEtbPwhJbr6Te28CmdSKeqzeqr0YbfVIrTBKakvtOl5dtTkK+v4HfA9PEyBFCY9AGVgCBLaBp1jPAyfAJ/AAdIEG0dNAiyP7+K1qIfMdonZic6+WJoBJvQlvuwDqcXadUuqPA1NKAlexbRTAIMvMOCjTbMwl1LtI/6KWJ5Q6rT6Ht1MA58AX8Apcqqt5r2qhrgAXQC3CZ6i1+KMd9TRu3MvA3aH/fFPnBodb6oe6HM8+lYHrGdRXW8M9bMZtPXUji69lmf5Cmamq7quNLFZXD9Rq7v0Bpc1o/tp0fisAAAAASUVORK5CYII=)](https://github.com/marketplace/actions/latexdiff-action)
[![Release](https://img.shields.io/github/v/release/priyanshuone6/latexdiff-action.svg?style=flat&color=success)](https://github.com/priyanshuone6/latexdiff-action/releases/tag/v1)

A GitHub action to automatically runs [latexdiff](https://ctan.org/pkg/latexdiff?lang=en) whenever a tex file is updated, and push the resulting pdf back into the repository.

For example, this is useful if [version-controlling an Overleaf project with GitHub](https://www.overleaf.com/learn/how-to/How_do_I_connect_an_Overleaf_project_with_a_repo_on_GitHub,_GitLab_or_BitBucket%3F).

## Action inputs
**Required inputs**
| Name | Description |
| --- | --- |
| `file-paths` | List of all the file paths to run latexdiff on |

**Optional inputs**
| Name | Description | Default |
| --- | --- | --- |
| `git-username` | The committer username | `github-actions[bot]` |
| `git-email` | The committer email address | `41898282+github-actions[bot]@users.noreply.github.com` |
| `options` | latexdiff options | No options |

## Reference example
```yml
name: Update latexdiff pdf

on:
  push:
    # Add file paths here to trigger the workflow only when these files are modified (optional)
    paths:
    - intro.tex
    - example/test.tex

jobs:
  latexdiff-action:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
        # Required to fetch all the commits for all branches
        with:
          fetch-depth: 0

      - name: latexdiff-action
        uses: priyanshuone6/latexdiff-action@v1
        with:
          file-paths: intro.tex,example/test.tex
```

## Use original workflow
To use the action, simply copy the [latexdiff.yml](https://github.com/priyanshuone6/latexdiff-action/blob/v1/.github/workflows) file over into your GitHub repository
under the folder `.github/workflows/`.

You can then update the configuration in two ways:
- change the tex file(s) that are tracked. The Action will be triggered for files in [line 19](https://github.com/priyanshuone6/latexdiff-action/blob/fbe2f58351efe0bfb3e56db58e1df20154cce6db/.github/workflows/latexdiff.yml#L19) whenever changes are made to files in [lines 11-12](https://github.com/priyanshuone6/latexdiff-action/blob/fbe2f58351efe0bfb3e56db58e1df20154cce6db/.github/workflows/latexdiff.yml#L11-L12)
- change the latexdiff options in [line 45]( 
https://github.com/priyanshuone6/latexdiff-action/blob/fbe2f58351efe0bfb3e56db58e1df20154cce6db/.github/workflows/latexdiff.yml#L45
), see [manual](https://mirror.las.iastate.edu/tex-archive/support/latexdiff/doc/latexdiff-man.pdf)
