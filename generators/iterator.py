from collections import Counter
from dictionaries import finder
import secrets


class Iteration:
    table = sorted([[a, b] for a in range(1, 9) for b in range(1, 9)], reverse=True)

    @staticmethod
    def create_hexagram():

        def trigram():
            trigram_array = []
            for t in range(3):
                int_rand = secrets.randbelow(2)
                if int_rand == 1:
                    trigram_array.append(1)
                else:
                    trigram_array.append(0)
            return tuple(trigram_array)

        hexagram_array = []
        for h in range(2):
            hexagram_array.append(trigram())
        return hexagram_array

    def iterate(self, iterations):
        all_hex = []
        all_tri = []
        all_bin = []
        for i in range(iterations):
            new_hex = self.create_hexagram()
            low_bins, up_bins = new_hex
            for low_bin in low_bins:
                all_bin.append(low_bin)
            for up_bin in up_bins:
                all_bin.append(up_bin)
            low_tri_num = finder.find_trigram_number(low_bins)
            up_tri_num = finder.find_trigram_number(up_bins)
            all_tri.append(low_tri_num)
            all_tri.append(up_tri_num)
            coords = [low_tri_num, up_tri_num]
            fu_xi_num = self.table.index(coords)
            all_hex.append(fu_xi_num)
        counted_hex = Counter(all_hex)
        counted_tri = Counter(all_tri)
        counted_bin = Counter(all_bin)
        return counted_hex, counted_tri, counted_bin
