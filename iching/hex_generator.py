from collections import Counter
from iching.dictionaries import finder
import secrets


class PyChing:

    def __init__(self, iterations, sets):
        self.iterations = iterations
        self.sets = sets

    def run(self):
        all_the_sets = []
        meanings = []

        for r in range(self.sets):
            one_set = self.create_set()
            all_the_sets.append(one_set[0])
            meanings.append(one_set[1])
        return all_the_sets, meanings

    def create_set(self):
        iteration = IteratedSet(self.iterations)
        counted_iteration = iteration.create_counted_set()
        meaning = Meaning(counted_iteration).hex_meaning()
        sorter = Sorter(counted_iteration)
        sorted_sets = sorter.sort_the_sets_by_key()
        return sorted_sets, meaning


class Sorter:

    def __init__(self, the_sets):
        self.the_sets = the_sets

    def sort_the_sets_by_key(self):
        the_hex_set, the_tri_set, the_bin_set = self.the_sets
        k_sorted_hex_set = self.k_sort(the_hex_set)
        k_sorted_tri_set = self.k_sort(the_tri_set)
        k_sorted_bin_set = self.k_sort(the_bin_set)
        return k_sorted_hex_set, k_sorted_tri_set, k_sorted_bin_set

    @staticmethod
    def k_sort(d):
        return {k: d[k] for k in sorted(d.keys())}


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

    fu_xi_table = [(low, high) for low in range(8) for high in range(8)]

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


class Meaning:
    def __init__(self, counted_sets):
        self.counted_sets = counted_sets

    def hex_meaning(self):
        counted_hex = self.counted_sets[0]
        (hex_first_place) = counted_hex.most_common(1)
        king_wen_first_place = finder.transform_king_wen(hex_first_place[0][0])
        king_wen_meaning = finder.find_king_wen_meaning(king_wen_first_place)
        message = finder.secondary_meaning(king_wen_first_place)
        return king_wen_first_place, king_wen_meaning, message
