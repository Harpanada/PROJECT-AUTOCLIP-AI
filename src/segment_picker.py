# from sentence_transformers import SentenceTransformer
# from sklearn.cluster import KMeans
# import numpy as np

# N_CLIPS=5

# def Pick_Segment(text):
#     #Embbeders
#     embedder = SentenceTransformer('all-MiniLM-L6-v2')
#     embeddings = embedder.encode(text)

#     #Kmeans Clustering
#     kmeans = KMeans(n_clusters=N_CLIPS, random_state=0)
#     labels = kmeans.fit(embeddings)

#     clips=[]
#     center= kmeans.cluster_centers_
#     for cid in range(N_CLIPS):
#          index_segment = np.where(labels == cid)[0]
#          if len(index_segment) == 0: #Kalau cluster kosong skip
#              continue
         
#          #Cari Segment Paling Dekat dengan Center
#          dist= np.linalg.norm(embeddings[index_segment] - center[cid], axis=1)
#          best_segment= index_segment[np.argmin(dist)]
#          clips.append((best_segment, text[best_segment]))
    
#     return clips

from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans
import numpy as np

N_CLIPS = 5

def Pick_Segment(texts):
    # Pastikan texts list
    if isinstance(texts, str):
        texts = [texts]

    # Embeddings
    embedder = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = embedder.encode(texts)
    
    # Pastikan embeddings 2D
    embeddings = np.atleast_2d(embeddings)

    # KMeans Clustering
    kmeans = KMeans(n_clusters=min(N_CLIPS, len(texts)), random_state=0)
    kmeans.fit(embeddings)
    labels = kmeans.labels_

    clips = []
    centers = kmeans.cluster_centers_

    for cid in range(kmeans.n_clusters):
        index_segment = np.where(labels == cid)[0]
        if len(index_segment) == 0:
            continue

        # Cari segment paling dekat dengan center
        dist = np.linalg.norm(embeddings[index_segment] - centers[cid], axis=1)
        best_segment = index_segment[np.argmin(dist)]
        # clips.append((best_segment, texts[best_segment]))
        clips.append((texts[best_segment]))

    return clips
