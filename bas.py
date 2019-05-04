import numpy as np
import scipy as sc
import pandas as pd
import glob
import heapq


class search():
    def __init__(self):
        pass

    def __hey__(self):
        print('yo')


    def my_metric(self, a, b):
        a = np.array(a)
        b = np.array(b)
        return a @ b

    def find_nearest(self, files, target):
        H = []
        heapq.heapify(H)

        push = heapq.heappush
        pop = heapq.heappop

        for f in files:
            df = pd.read_csv(f)

            for row in df.values:

                distance = self.my_metric(target, row)
                neighbor = (distance, row[1:])
                if len(H) < 10:
                    push(H, neighbor)
                else:
                    furthest_saved_neighbor = pop(H)

                    closest_neighbor = max(furthest_saved_neighbor, neighbor)

                    push(H, closest_neighbor)

        return H
