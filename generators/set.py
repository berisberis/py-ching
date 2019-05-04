from generators.randomizer import Hexagram
from generators.fuxi_bin_table import FuXiSequence
from collections import Counter
from dictionaries.finder import Finder
from helpers.transform import Arrays


class Iteration:

    @staticmethod
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

