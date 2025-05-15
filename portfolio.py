import csv
import uuid
import chromadb
from langchain.embeddings import HuggingFaceEmbeddings

class Portfolio:
    def __init__(self, file_path):
        self.file_path = file_path
        self.embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        self.chroma_client = chromadb.PersistentClient(path="vectorstore")
        self.collection = self.chroma_client.get_or_create_collection(name="portfolio")
        self.load_portfolio()

    def load_portfolio(self):
        if not self.collection.count():
            with open(self.file_path, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    title = row["title"]
                    url = row["url"]
                    embedding = self.embeddings.embed_query(title)
                    self.collection.add(
                        documents=[title],
                        metadatas=[{"url": url}],
                        embeddings=[embedding],
                        ids=[str(uuid.uuid4())]
                    )

    def query_links(self, text, top_k=3):
        embedding = self.embeddings.embed_query(text)
        results = self.collection.query(query_embeddings=[embedding], n_results=top_k)
        metadatas = results.get("metadatas", [[]])[0]
        return [m["url"] for m in metadatas if "url" in m]
