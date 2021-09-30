INTERPRETER = python
BUILDER = pyinstaller
SPEC_FILE = Serration_magic_page.spec
SOURCE = Serration_magic.py

.PHONY : exe
exe : $(SPEC_FILE) $(SOURCE)
	touch $^
	$(BUILDER) $<