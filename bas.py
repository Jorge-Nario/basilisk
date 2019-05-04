import numpy as np
import scipy as sc
import pandas as pd
import glob
import heapq

class search():
    def __init__(self):
        pass


    def __my_metric__(self, dist_type, a, b):

        if dist_type == 'jaccard'
            return jaccard_similarity_score(a, b, normalize=True)
        else:
            #assume cosine similarity
            return 1 - spatial.distance.cosine(dataSetI, dataSetII)

    def find_nearest(self, files, target):


        H = []
        heapq.heapify(H)

        push = heapq.heappush
        pop = heapq.heappop

        for f in files:
            df = pd.read_csv(f)

            for row in df.values:

                distance = self.__my_metric__(target, row)


                neighbor = (distance, row[1:])
                if len(H) < 10:
                    push(H, neighbor)
                else:
                    furthest_saved_neighbor = pop(H)

                    closest_neighbor = max(furthest_saved_neighbor, neighbor)

                    push(H, closest_neighbor)

        return H
