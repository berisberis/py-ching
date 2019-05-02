#!/usr/bin/env python3


from collections import Counter
from dictionaries.finder import Finder
from helpers.terminal import Results
from helpers.files import CsvMake
from helpers.transform import Arrays
from generators.randomizer import Hexagram
from generators.fuxi_bin_table import FuXiSequence


def iterate(iterations):
    table = FuXiSequence.generate_table()
    i = 1
    all_hex = []
    all_tri = []
    all_bin = []
    while i <= iterations:
        new_hex = Hexagram.create()
        low_bins, up_bins = new_hex
        for low_bin in low_bins:
            all_bin.append(low_bin)
        for up_bin in up_bins:
            all_bin.append(up_bin)
        low_tri_num = Finder.find_trigram_number(Arrays.array_to_string(low_bins))
        up_tri_num = Finder.find_trigram_number(Arrays.array_to_string(up_bins))
        all_tri.append(low_tri_num)
        all_tri.append(up_tri_num)
        cords = Arrays.make_cord_array(low_tri_num, up_tri_num)
        fu_xi_num = FuXiSequence.lookup_table(table, cords)
        all_hex.append(fu_xi_num)
        i += 1
    counted_hex = Counter(all_hex)
    counted_tri = Counter(all_tri)
    counted_bin = Counter(all_bin)
    return counted_hex, counted_tri, counted_bin


def run(iterations, sets):

    def iterate_and_sort():
        the_set = iterate(iterations)
        the_hex_set, the_tri_set, the_bin_set = the_set
        Results.print(the_hex_set, the_tri_set, the_bin_set)
        k_sorted_hex_set = Arrays.k_sort(the_hex_set)
        k_sorted_tri_set = Arrays.k_sort(the_tri_set)
        k_sorted_bin_set = Arrays.k_sort(the_bin_set)
        return k_sorted_hex_set, k_sorted_tri_set, k_sorted_bin_set

    def sets_to_csv(mode):
        hex_sorted_set, tri_sorted_set, bin_sorted_set = iterate_and_sort()
        CsvMake.to_csv(hex_sorted_set, 'hexagrams', mode)
        CsvMake.to_csv(tri_sorted_set, 'trigrams', mode)
        CsvMake.to_csv(bin_sorted_set, 'binaries', mode)

    sets_to_csv('w')
    r = 1
    while r < sets:
        sets_to_csv('a')
        r += 1


run(iterations=32768, sets=8)
