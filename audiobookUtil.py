from PyPDF2 import PdfFileReader
from pyttsx3 import init


def getTextFromAllPages():
    txt = ""
    with open('PythonQuestions.pdf', 'rb') as f:
        pdfReaderObj = PdfFileReader(f)
        numPages = pdfReaderObj.getNumPages()
        for pageN in range(numPages):
            page = pdfReaderObj.getPage(pageN)
            pageContent = page.extractText()
            txt += pageContent
    return txt

txt = getTextFromAllPages()
engine = init()
engine.save_to_file(txt, 'test.mp3')
engine.runAndWait()

# pip install PyPDF2
# pip install pyttsx3