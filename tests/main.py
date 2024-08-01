from src.read.base_doc import BaseDoc
    
def main():
    PATH = "docs/test2.pdf"
    doc = BaseDoc.generate(PATH)
    doc.read()
    print("\n")
    for i in range(len(doc.get_pages())):
        BaseDoc.pretty_print(f"------- page {i} -------")
        print(doc.get_page(i))
        print("\n\n")

if __name__ == "__main__":
    main()