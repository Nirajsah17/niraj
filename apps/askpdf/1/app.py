from utils import generate_embeddings, split_into_chunk, find_cosine_similarity
import tqdm
import json
from datetime import datetime

chunks = split_into_chunk(text, chunk_size=500)
embeddings = []
for chunk in tqdm.tqdm(chunks, desc="proccessing chunks") :
  embedding = generate_embeddings(chunk)
  print(embedding)
  print(chunk)
  embeddings.append(embedding)

data = None
with open('embeddings.json', 'r') as file:
  data = json.load(file)



fileId = timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
data["files"][fileId] = {
  "filename": "ancient_indian.history.pdf",
  "page_count": 20,
  "total_tokens": 4569,
  "chunks": chunks,
  "embeddings": embeddings
}

json.dump(data, open('embeddings.json', 'w'))
  
query = "The earliest discovered instance ?"
QUERY_EMBEDDINGS = generate_embeddings(query)
res = find_cosine_similarity(QUERY_EMBEDDINGS, data["files"][fileId]["embeddings"])
print(res)