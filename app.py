#!/usr/bin/env python3

from generators.iching import IteratedSet
from helpers.terminal import Results
from helpers.files import CsvMake


class PyChing:

    def __init__(self, iterations, sets):
        self.iterations = iterations
        self.sets = sets

    all_the_sets = []

    def run(self):
        one_set = self.create_set('w')
        self.all_the_sets.append(one_set)
        for r in range(self.sets-1):
            one_set = self.create_set('a')
            self.all_the_sets.append(one_set)
        return self.all_the_sets

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


experiment = PyChing(iterations=4096, sets=8)
experiment.run()
