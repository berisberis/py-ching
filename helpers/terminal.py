from dictionaries import finder


class Results:

    @staticmethod
    def print_results(counted_sets):
        counted_hex, counted_tri, counted_bin = counted_sets
        (hex_first_place, hex_first_times), (hex_second_place, hex_second_times) = counted_hex.most_common(2)
        (tri_first_place, tri_first_times), (tri_second_place, tri_second_times) = counted_tri.most_common(2)
        (bin_first_place, bin_first_times), (bin_second_place, bin_second_times) = counted_bin.most_common(2)

        print(f'\nHexagram {finder.transform_king_wen(hex_first_place)} was found {hex_first_times} times')
        print(finder.find_king_wen_meaning(finder.transform_king_wen(hex_first_place)))
        print(f'\nHexagram {finder.transform_king_wen(hex_second_place)} was found {hex_second_times} times')
        print(finder.find_king_wen_meaning(finder.transform_king_wen(hex_second_place)))

        print(f'\nTrigram {tri_first_place} was found {tri_first_times} times')
        print(finder.find_trigram_meaning(tri_first_place))
        print(f'\nTrigram {tri_second_place} was found {tri_second_times} times')
        print(finder.find_trigram_meaning(tri_second_place))

        print(f'\nBinary {bin_first_place} was found {bin_first_times} times')
        print(f'Binary {bin_second_place} was found {bin_second_times} times')

        return counted_hex, counted_tri, counted_bin
