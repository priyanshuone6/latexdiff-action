# GitHub Action for latexdiff

This repository contains a GitHub action which automatically runs [latexdiff](https://ctan.org/pkg/latexdiff?lang=en) whenever a tex file is updated, 
and pushes the resulting pdf back into the repository.
For example, this is useful if [version-controlling an Overleaf project with GitHub](https://www.overleaf.com/learn/how-to/How_do_I_connect_an_Overleaf_project_with_a_repo_on_GitHub,_GitLab_or_BitBucket%3F).

To use the action, simply copy the [latexdiff.yml](https://github.com/priyanshuone6/latexdiff-test/tree/main/.github/workflows) file over into your GitHub repository
under the folder `.github/workflows/`.

You can then update the configuration in two ways:
- change the tex file(s) that are tracked. The Action will be triggered for files in [line 19](https://github.com/priyanshuone6/latexdiff-test/blob/1b0d9ccfc5221c5998bdb647fbe151353919ce18/.github/workflows/latexdiff.yml#L19) whenever changes are made to files in [lines 11-12](https://github.com/priyanshuone6/latexdiff-test/blob/1b0d9ccfc5221c5998bdb647fbe151353919ce18/.github/workflows/latexdiff.yml#L11-L12)
- change the latexdiff options in [line 45]( 
https://github.com/priyanshuone6/latexdiff-test/blob/1b0d9ccfc5221c5998bdb647fbe151353919ce18/.github/workflows/latexdiff.yml#L45
), see [manual](https://mirror.las.iastate.edu/tex-archive/support/latexdiff/doc/latexdiff-man.pdf)
