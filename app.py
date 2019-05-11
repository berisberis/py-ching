#!/usr/bin/env python3

from generators.iterator import Iteration
from helpers.terminal import Results
from helpers.files import CsvMake


class IChing:

    def run(self, iterations, sets):
        all_the_sets = []
        one_set = self.create_set(iterations, 'w')
        all_the_sets.append(one_set)
        for r in range(sets-1):
            one_set = self.create_set(iterations, 'a')
            all_the_sets.append(one_set)
        return all_the_sets

    def create_set(self, iterations, mode):
        make_csv = CsvMake()
        iteration = Iteration()
        counted_iteration = iteration.iterate(iterations)
        this_set = make_csv.sets_to_csv(mode, self.sort_the_sets(Results.print_results(counted_iteration)))
        return this_set

    @staticmethod
    def k_sort(d):
        return {k: d[k] for k in sorted(d.keys())}

    def sort_the_sets(self, the_sets):
        the_hex_set, the_tri_set, the_bin_set = the_sets
        k_sorted_hex_set = self.k_sort(the_hex_set)
        k_sorted_tri_set = self.k_sort(the_tri_set)
        k_sorted_bin_set = self.k_sort(the_bin_set)
        return k_sorted_hex_set, k_sorted_tri_set, k_sorted_bin_set


iching = IChing()
iching.run(iterations=4096, sets=8)
