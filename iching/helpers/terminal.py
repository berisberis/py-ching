from iching.dictionaries import finder


class Results:

    def __init__(self, counted_sets):
        self.counted_sets = counted_sets

    def print_results(self):
        counted_hex, counted_tri, counted_bin = self.counted_sets
        (hex_first_place, hex_first_count), (hex_second_place, hex_second_count) = counted_hex.most_common(2)
        (tri_first_place, tri_first_count), (tri_second_place, tri_second_count) = counted_tri.most_common(2)
        (bin_first_place, bin_first_count), (bin_second_place, bin_second_count) = counted_bin.most_common(2)

        print('-'*30)
        king_wen_first_place = finder.transform_king_wen(hex_first_place)
        king_wen_second_place = finder.transform_king_wen(hex_second_place)
        print(f'\nHexagram {king_wen_first_place} was found {hex_first_count} times')
        print(finder.find_king_wen_meaning(king_wen_first_place))
        print(f'\nHexagram {king_wen_second_place} was found {hex_second_count} times')
        print(finder.find_king_wen_meaning(king_wen_second_place))

        print(f'\nTrigram {tri_first_place} was found {tri_first_count} times')
        print(finder.find_trigram_meaning(tri_first_place))
        print(f'\nTrigram {tri_second_place} was found {tri_second_count} times')
        print(finder.find_trigram_meaning(tri_second_place))

        print(f'\nBinary {bin_first_place} was found {bin_first_count} times')
        print(f'Binary {bin_second_place} was found {bin_second_count} times')
        print('-'*30)

