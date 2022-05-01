from fpdf import FPDF
from docx2pdf import convert

file = input("Enter the file name: ")   

filePrefix = file.split(".")[0]
fileSuffix = file.split(".")[1]

if(fileSuffix == 'txt'):
   print("Converting txt to pdf")      
   pdf = FPDF()   
   pdf.add_page()
   pdf.set_font("Arial", size = 15)
   fileOutput = filePrefix + ".pdf"
   f = open(file, "r")
   for x in f:
      pdf.cell(200, 10, txt = x, ln = 1, align = 'C')
   pdf.output(fileOutput)
   print("Done")
   
elif(fileSuffix == "docx" or fileSuffix == "doc"):
   print("Converting docx to pdf")
   convert(file)
   print("Done")
else:
   print("Wrong File")