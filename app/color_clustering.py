from sklearn.cluster import KMeans
import numpy as np

def extract_dominant_colors(pixels: np.ndarray, top_n: int = 5):
    kmeans = KMeans(n_clusters=top_n, random_state=42, n_init='auto')
    kmeans.fit(pixels)
    return kmeans.cluster_centers_.astype(int)
