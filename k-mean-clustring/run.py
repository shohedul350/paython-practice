import math

def kMeans(data, k):
    centroids = data[:k]
    classes = [-1] * len(data)
    itr = True

    while itr:
        itr = False

        for d, point in enumerate(data):
            distances = [math.hypot(*(point[i] - centroids[c][i] for i in range(len(point)))) for c in range(k)]
            m = distances.index(min(distances))

            if classes[d] != m:
                itr = True
            classes[d] = m

        for c in range(k):
            cluster_points = [data[d] for d, _ in enumerate(data) if classes[d] == c]
            centroids[c] = [round(sum(p[i] for p in cluster_points) / len(cluster_points), 2) for i in range(len(data[0]))]

    return classes

print(kMeans([[0, 0], [0, 1], [1, 3], [2, 0]], 2))