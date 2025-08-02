# creates function that runs the KMeans clustering algorithm to find dominant colors from the pixeks

from sklearn.cluster import KMeans
import numpy as np

# np.ndarray is a 2d array of RGB pixel values, each row is a pixel of (R,G,B) format
# top_n is the number of dominant colors to extract - 5 is default
def extract_dominant_colors(pixels: np.ndarray, top_n: int = 5):
    kmeans = KMeans(n_clusters=top_n, random_state=42, n_init='auto')
    kmeans.fit(pixels)
    return kmeans.cluster_centers_.astype(int) # returns RGB values of final cluster centers - casts to integers
