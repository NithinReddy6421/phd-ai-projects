from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_texts(texts):
    embeddings = model.encode(texts, show_progress_bar=True)
    return embeddings

if __name__ == "__main__":
    print("Embedding module loaded.")
