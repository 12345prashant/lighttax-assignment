import pdfplumber


class PDFNavigator:

    def __init__(self, path):
        self.text = ""

        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                self.text += page.extract_text() + "\n"

    def search(self, keyword):
        chunks = self.text.split("\n")

        matches = [c for c in chunks if keyword.lower() in c.lower()]

        return "\n".join(matches[:20])