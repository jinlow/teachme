"""Process Documents
This module houses the document processing functions and classes for
cleaning and processing input text to be used by the teachme app.
"""
import spacy

class DocProcessor:
    """Class for Processing Document
    """

    def __init__(self):
        self.nlp = spacy.load('en_core_web_md')
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

    def process_text(self):
        """Process Text
        """
        assert self.text is not None, "DocProcessor().text is None"
        doc = self.nlp(self.text)
        self.proc_text = [sent for sent in doc.sent]
