from PyPDF2 import PdfMerger
pdfs=[]
merger= PdfMerger()
n=int(input("Enter the number of pdfs you wants to merge : "))
for i in range(0,n):
    name=input(f"Enter the pdf {i +1} name : ")
    pdfs.append(name)

for pdf in pdfs:
    merger.append(pdf)

merger.write("conbined.pdf")
merger.close()