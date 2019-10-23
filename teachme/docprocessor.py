"""Process Documents
This module houses the document processing functions and classes for
cleaning and processing input text to be used by the teachme app.
"""

import re
from teachme import constants

class DocProcessor:
    """Class for Processing Documents
    """

    def __init__(self):
        self.nlp = constants.NLP
        self.processed = False
        self.doc_type = None
        self.text = None
        self.proc_text = None

    def read_txt(self, path: str) -> None:
        """Read a Text File
        Read a text file (txt) as a DocProcessor object.
        """
        file = open(path, mode='r')
        all_text = file.read()
        file.close()
        self.text = all_text
        self.processed = False

    def read_docx(self, path: str) -> None:
        """Read a doc/docx file
        Read a Word Document (doc/docx) as a DocProcessor object.
        """
        import textract
        self.text = textract.process(filename=path).decode('utf-8')
        self.processed = False

    def process_text(self):
        """Process Text
        """
        assert self.text is not None, "DocProcessor().text is None"
        doc = re.sub('[ \t\r\f\v]{2,}', ' ', self.text).strip()
        doc = re.sub('\n{2,}', '\n', doc)
        doc = self.nlp(doc)
        self.proc_text = [sent for sent in doc.sents if len(sent) > 1]
        self.processed = True
