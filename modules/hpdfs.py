"""READ A PDF / BUT NEED TO SOLVE BUGS FIRST :)
# from nltk.tokenize import sent_tokenize, word_tokenize
import PyPDF2 # Caso seja PDF a ser lido

# Read a PDF file
pdf_to_read = open('distributedscrumprimer-1.pdf', 'rb')
pdf = PyPDF2.PdfFileReader(pdf_to_read)
pdf_num_pages = pdf.numPages
# page = pdf.getPage(9)
# content = page.extractText()
# print(content)

# Put the content of each page as a single value
# in a list / i.e. one list-value for each page
content_by_pages = []
for page_num in range(pdf_num_pages):
    page = pdf.getPage(page_num)
    page_content = page.extractText()
    content_by_pages.append(page_content)
"""
