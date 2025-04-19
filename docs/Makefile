SPHINXBUILD = sphinx-build
SOURCEDIR = .
BUILDDIR = _build

.PHONY: html clean

html:
	$(SPHINXBUILD) -b html $(SOURCEDIR) $(BUILDDIR)/html -W -n -a

clean:
	rm -rf $(BUILDDIR)