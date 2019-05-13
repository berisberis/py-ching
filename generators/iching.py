from collections import Counter
from dictionaries import finder
import secrets


class Hexagram:

    @staticmethod
    def trigram():
        trigram_array = []
        for t in range(3):
            int_rand = secrets.randbelow(2)
            if int_rand == 1:
                trigram_array.append(1)
            else:
                trigram_array.append(0)
        return tuple(trigram_array)

    @classmethod
    def create_hexagram(cls):
        hexagram_array = []
        for h in range(2):
            hexagram_array.append(cls.trigram())
        return tuple(hexagram_array)


class IteratedSet:

    def __init__(self, iterations):
        self.iterations = iterations

    fu_xi_table = sorted([(a, b) for a in range(1, 9) for b in range(1, 9)], reverse=True)

    def create_counted_set(self):
        all_hex = []
        all_tri = []
        all_bin = []
        for i in range(self.iterations):
            new_hex = Hexagram.create_hexagram()
            low_bins, up_bins = new_hex
            for low_bin in low_bins:
                all_bin.append(low_bin)
            for up_bin in up_bins:
                all_bin.append(up_bin)
            low_tri_num = finder.find_trigram_number(low_bins)
            up_tri_num = finder.find_trigram_number(up_bins)
            all_tri.append(low_tri_num)
            all_tri.append(up_tri_num)
            coords = (low_tri_num, up_tri_num)
            fu_xi_num = self.fu_xi_table.index(coords)
            all_hex.append(fu_xi_num)
        counted_hex = Counter(all_hex)
        counted_tri = Counter(all_tri)
        counted_bin = Counter(all_bin)
        return counted_hex, counted_tri, counted_bin
