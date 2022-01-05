import PyPDF2
from googlesearch import search


search = search("fb")

pdfObj = open('PythonQuestions.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfObj)

pageObj = pdfReader.getPage(0)
t = pageObj.extractText()

"""
Libraries:

pip install PyPDF2

pip install google

"""