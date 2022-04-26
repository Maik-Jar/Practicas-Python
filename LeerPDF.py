from PyPDF2.pdf import PdfFileReader

file_manager = open('Comprobante_620.pdf', 'rb')
pdf_read = PdfFileReader(file_manager)
first_page = pdf_read.getPage(0)

word = first_page.extractText()

words_list = word.split()
print(first_page.extractText())  #first_page.extractText()

