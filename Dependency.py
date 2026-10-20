class Document:
    pass
class Printer:
    def print_document(self, document):
        print("Printing document")
document = Document()
printer = Printer()
printer.print_document(document)