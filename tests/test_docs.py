import os

raw_docs_path = os.path.abspath("app/documents/raw")
processed_docs_path = os.path.abspath("app/documents/processed")
categories = os.listdir(raw_docs_path)

def test_categories():
    assert len(categories) > 0, "No categories found in the documents directory."


def test_pdf_documents_in_categories():
    for cats in categories:
        cat_path = os.path.join(raw_docs_path, cats)
        docs = os.listdir(cat_path)
        pdf_docs = [doc for doc in docs if doc.endswith('.pdf')]
        assert len(pdf_docs) > 0, f"No PDF documents found in category: {cats}"

def test_processed_documents():
    for cats in categories:
        processed_cat_path = os.path.join(processed_docs_path, cats)
        assert os.path.exists(processed_cat_path), f"Processed category directory does not exist: {processed_cat_path}"
        processed_docs = os.listdir(processed_cat_path)
        assert len(processed_docs) > 0, f"No processed documents found in category: {cats}"