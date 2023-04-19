# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
# SPHINXBUILD   ?= sphinx-multiversion
SOURCEDIR     = source
BUILDDIR      = ../rlang/docs

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

multiversion:
	@sphinx-multiversion $(SOURCEDIR) $(BUILDDIR)
	@cp themes/sphinx_rtd_theme_versioned/index.html $(BUILDDIR)/index.html


# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
# 	echo '<meta http-equiv="Refresh" content="0; url=\'/master\'" />' > $(BUILDDIR)/index.html
