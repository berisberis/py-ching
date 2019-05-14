from generator.helpers.terminal import Results
from generator.helpers.files import CsvMake
from collections import Counter
from generator.dictionaries import finder
import secrets


class PyChing:

    def __init__(self, iterations, sets):
        self.iterations = iterations
        self.sets = sets

    def run(self):
        all_the_sets = []
        one_set = self.create_set('w')
        all_the_sets.append(one_set)
        for r in range(self.sets-1):
            one_set = self.create_set('a')
            all_the_sets.append(one_set)
        return all_the_sets

    def create_set(self, mode):
        iteration = IteratedSet(self.iterations)
        counted_iteration = iteration.create_counted_set()
        Results(counted_iteration).print_results()
        sorter = Sorter(counted_iteration)
        sorted_sets = sorter.sort_the_sets_by_key()
        make_csv = CsvMake(sorted_sets)
        make_csv.sets_to_csv(mode)
        return sorted_sets


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
