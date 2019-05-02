#!/usr/bin/env python3


from collections import Counter
from dictionaries import finder
from helpers import arrays, create_csv, terminal
from generators import hexagrams, fuxi_bin_table


def iterate(iterations):
    table = fuxi_bin_table.generate_table()
    i = 1
    all_hex = []
    all_tri = []
    all_bin = []
    while i <= iterations:
        new_hex = hexagrams.hexagram()
        low_bins, up_bins = new_hex
        for low_bin in low_bins:
            all_bin.append(low_bin)
        for up_bin in up_bins:
            all_bin.append(up_bin)
        low_tri_num = finder.find_trigram_number(arrays.array_to_string(low_bins))
        up_tri_num = finder.find_trigram_number(arrays.array_to_string(up_bins))
        all_tri.append(low_tri_num)
        all_tri.append(up_tri_num)
        cords = arrays.make_cord_array(low_tri_num, up_tri_num)
        fu_xi_num = fuxi_bin_table.lookup_table(table, cords)
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
        terminal.print_results(the_hex_set, the_tri_set, the_bin_set)
        k_sorted_hex_set = arrays.k_sort(the_hex_set)
        k_sorted_tri_set = arrays.k_sort(the_tri_set)
        k_sorted_bin_set = arrays.k_sort(the_bin_set)
        return k_sorted_hex_set, k_sorted_tri_set, k_sorted_bin_set

    def sets_to_csv(mode):
        hex_sorted_set, tri_sorted_set, bin_sorted_set = iterate_and_sort()
        create_csv.to_csv(hex_sorted_set, 'hexagrams', mode)
        create_csv.to_csv(tri_sorted_set, 'trigrams', mode)
        create_csv.to_csv(bin_sorted_set, 'binaries', mode)

    sets_to_csv('w')
    r = 1
    while r < sets:
        sets_to_csv('a')
        r += 1


run(iterations=32768, sets=8)
