import PyPDF2


class PDFTool:

    def __init__(self, path):
        self.text = self._load_pdf(path)

    def _load_pdf(self, path):
        reader = PyPDF2.PdfReader(path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text

    def search(self, keyword):
        if keyword.lower() in self.text.lower():
            return self.text[:2000]  
        return "No relevant section found"