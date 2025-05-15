import csv
import uuid
import chromadb
from langchain.embeddings import HuggingFaceEmbeddings

class ProposalMemory:
    def __init__(self, file_path):
        self.file_path = file_path
        self.embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        self.chroma_client = chromadb.PersistentClient(path="proposal_memory")
        self.collection = self.chroma_client.get_or_create_collection(name="proposals")
        self.load_previous_proposals()

    def load_previous_proposals(self):
        if not self.collection.count():
            with open(self.file_path, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    full_text = f"Title: {row['title']}\nDescription: {row['description']}\nProposal: {row['proposal']}"
                    embedding = self.embeddings.embed_query(row["description"])
                    self.collection.add(
                        documents=[full_text],
                        metadatas=[{"title": row["title"]}],
                        embeddings=[embedding],
                        ids=[str(uuid.uuid4())]
                    )

    def retrieve_similar_proposals(self, job_description, top_k=2):
        embedding = self.embeddings.embed_query(job_description)
        results = self.collection.query(query_embeddings=[embedding], n_results=top_k)
        return results.get("documents", [[]])[0]
