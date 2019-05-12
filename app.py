#!/usr/bin/env python3

from generators.iching import Iteration
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
        iteration = Iteration(self.iterations)
        counted_iteration = iteration.iterate()
        results = Results(counted_iteration)
        results.print_results()
        sorted_sets = self.sort_the_sets(counted_iteration)
        make_csv = CsvMake(sorted_sets)
        this_set = make_csv.sets_to_csv(mode)
        return this_set

    @staticmethod
    def k_sort(d):
        return {k: d[k] for k in sorted(d.keys())}

    @classmethod
    def sort_the_sets(cls, the_sets):
        the_hex_set, the_tri_set, the_bin_set = the_sets
        k_sorted_hex_set = cls.k_sort(the_hex_set)
        k_sorted_tri_set = cls.k_sort(the_tri_set)
        k_sorted_bin_set = cls.k_sort(the_bin_set)
        return k_sorted_hex_set, k_sorted_tri_set, k_sorted_bin_set


experiment = PyChing(iterations=4096, sets=8)
experiment.run()
