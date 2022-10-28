import aspose.words as aw
documento = input('Ingrese el nombre del documento con extensión pdf: ')

doc = aw.Document(documento)
doc.save("Output.docx")