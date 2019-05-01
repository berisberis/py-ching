#!/usr/bin/env python3


import secrets
import csv
from collections import Counter


def hexagram():

    def trigram():
        t = 1
        trigram_array = []
        while t <= 3:
            int_rand = secrets.randbelow(1000)
            if int_rand > 500:
                trigram_array.append(1)
            else:
                trigram_array.append(0)
            t += 1
        return trigram_array

    h = 1
    hexagram_array = []
    while h <= 2:
        hexagram_array.append(trigram())
        h += 1
    return hexagram_array


def array_to_string(array):
    string = ''
    for item in array:
        string += ''.join(str(item))
    return string


def find_trigram_number(trigram_bin):
    trigrams = {
        "000": 8, "001": 7,
        "010": 6, "011": 5,
        "100": 4, "101": 3,
        "110": 2, "111": 1,
    }
    trigram_number = trigrams[trigram_bin]
    return trigram_number


def generate_table():
    table = []
    low = 9
    while low > 1:
        low -= 1
        up = 9
        while up > 1:
            up -= 1
            table.append([low, up])
    return table


def lookup_table(table, cords):
    glyph_num = table.index(cords)
    return glyph_num


def transform_king_wen(number):
    king_wen_dir = {
        0:   2,  1: 23,  2:  8,  3: 20,  4: 16,  5: 35,  6: 45,  7: 12,
        8:  15,  9: 52, 10: 39, 11: 53, 12: 62, 13: 56, 14: 31, 15: 33,
        16:  7, 17:  4, 18: 29, 19: 59, 20: 40, 21: 64, 22: 47, 23:  6,
        24: 46, 25: 18, 26: 48, 27: 57, 28: 32, 29: 50, 30: 28, 31: 44,
        32: 24, 33: 27, 34:  3, 35: 42, 36: 51, 37: 21, 38: 17, 39: 25,
        40: 36, 41: 22, 42: 63, 43: 37, 44: 55, 45: 30, 46: 49, 47: 13,
        48: 19, 49: 41, 50: 60, 51: 61, 52: 54, 53: 38, 54: 58, 55: 10,
        56: 11, 57: 26, 58:  5, 59:  9, 60: 34, 61: 14, 62: 43, 63: 1
    }
    king_wen = king_wen_dir[number]
    return king_wen


def find_trigram_meaning(number):
    meanings = {
        1: "☰ Heaven",
        2: "☱ Lake",
        3: "☲ Fire",
        4: "☳ Thunder",
        5: "☴ Wind",
        6: "☵ Water",
        7: "☶ Mountain",
        8: "☷ Earth",
    }
    trigram_meaning = meanings[number]
    return trigram_meaning


def make_cord_array(low_tri_num, up_tri_num):
    this_array = [low_tri_num, up_tri_num]
    return this_array


def find_king_wen_meaning(glyph_number):
    meanings = {
        1: "䷀ Creative Heaven", 2: "䷁ Receptive Earth",
        3: "䷂ Difficulty at the Beginning", 4: "䷃ Youthful Folly",
        5: "䷄ Waiting", 6: "䷅ Conflict",
        7: "䷆ Army", 8: "䷇ Holding Together",
        9: "䷈ Small Taming", 10: "䷉ Treading",
        11: "䷊ Peace", 12: "䷋ Standstill",
        13: "䷌ Fellowship", 14: "䷍ Great Possesion",
        15: "䷎ Modesty", 16: "䷏ Enthusiasm",
        17: "䷐ Following", 18: "䷑ Work on the Decayed",
        19: "䷒ Approach", 20: "䷓ Contemplation",
        21: "䷔ Biting Through", 22: "䷕ Grace",
        23: "䷖ Splitting Apart", 24: "䷗ Return",
        25: "䷘ Innocence", 26: "䷙ Great Taming",
        27: "䷚ Mouth Corners", 28: "䷛ Great Preponderance",
        29: "䷜ Abysmal Water", 30: "䷝ Clinging Fire",
        31: "䷞ Influence", 32: "䷟ Duration",
        33: "䷠ Retreat", 34: "䷡ Great Power",
        35: "䷢ Progress", 36: "䷣ Darkening of the Light",
        37: "䷤ Family", 38: "䷥ Opposition",
        39: "䷦ Obstruction", 40: "䷧ Deliverance",
        41: "䷨ Decrease", 42: "䷩ Increase",
        43: "䷪ Breakthrough", 44: "䷫ Coming to Meet",
        45: "䷬ Gathering Together", 46: "䷭ Pushing Upward",
        47: "䷮ Oppression", 48: "䷯ The Well",
        49: "䷰ Revolution", 50: "䷱ The Cauldron",
        51: "䷲ The Arousing Thunder", 52: "䷳ The Keeping Still Mountain",
        53: "䷴ Development", 54: "䷵ The Marrying Maiden",
        55: "䷶ Abundance", 56: "䷷ The Wanderer",
        57: "䷸ The Gentle Wind", 58: "䷹ The Joyous Lake",
        59: "䷺ Dispersion", 60: "䷻ Limitation",
        61: "䷼ Inner Truth", 62: "䷽ Small Preponderance",
        63: "䷾ After Completion", 64: "䷿ Before Completion",
    }
    return meanings[glyph_number]


def iterate(iterations):
    table = generate_table()
    i = 1
    all_hex = []
    all_tri = []
    all_bin = []
    while i <= iterations:
        new_hex = hexagram()
        low_bins, up_bins = new_hex
        for low_bin in low_bins:
            all_bin.append(low_bin)
        for up_bin in up_bins:
            all_bin.append(up_bin)
        low_tri_num = find_trigram_number(array_to_string(low_bins))
        up_tri_num = find_trigram_number(array_to_string(up_bins))
        all_tri.append(low_tri_num)
        all_tri.append(up_tri_num)
        cords = make_cord_array(low_tri_num, up_tri_num)
        fu_xi_num = lookup_table(table, cords)
        all_hex.append(fu_xi_num)
        i += 1
    counted_hex = Counter(all_hex)
    counted_tri = Counter(all_tri)
    counted_bin = Counter(all_bin)
    return counted_hex, counted_tri, counted_bin


def k_sort(d):
    return {k: d[k] for k in sorted(d.keys())}


def print_results(counted_hex, counted_tri, counted_bin):
    most_common_hex = counted_hex.most_common(2)
    most_common_tri = counted_tri.most_common(2)
    most_common_bin = counted_bin.most_common(2)

    (hex_first_place, hex_first_times), (hex_second_place, hex_second_times) = most_common_hex
    (tri_first_place, tri_first_times), (tri_second_place, tri_second_times) = most_common_tri
    (bin_first_place, bin_first_times), (bin_second_place, bin_second_times) = most_common_bin

    print(f'\nHexagram {transform_king_wen(hex_first_place)} was found {hex_first_times} times')
    print(find_king_wen_meaning(hex_first_place))
    print(f'\nHexagram {transform_king_wen(hex_second_place)} was found {hex_second_times} times')
    print(find_king_wen_meaning(hex_second_place))

    print(f'\nTrigram {tri_first_place} was found {tri_first_times} times')
    print(find_trigram_meaning(tri_first_place))
    print(f'\nTrigram {tri_second_place} was found {tri_second_times} times')
    print(find_trigram_meaning(tri_second_place))

    print(f'\nBinary {bin_first_place} was found {bin_first_times} times')
    print(f'Binary {bin_second_place} was found {bin_second_times} times')


def run(iterations, sets):

    def iterate_and_sort():
        the_set = iterate(iterations)
        the_hex_set, the_tri_set, the_bin_set = the_set
        print_results(the_hex_set, the_tri_set, the_bin_set)
        k_sorted_hex_set = k_sort(the_hex_set)
        k_sorted_tri_set = k_sort(the_tri_set)
        k_sorted_bin_set = k_sort(the_bin_set)
        return k_sorted_hex_set, k_sorted_tri_set, k_sorted_bin_set

    def sets_to_csv(mode):
        hex_sorted_set, tri_sorted_set, bin_sorted_set = iterate_and_sort()
        to_csv(hex_sorted_set, 'hexagrams', mode)
        to_csv(tri_sorted_set, 'trigrams', mode)
        to_csv(bin_sorted_set, 'binaries', mode)

    sets_to_csv('w')
    r = 1
    while r < sets:
        sets_to_csv('a')
        r += 1


def to_csv(k_sorted_set, filename, mode):
    with open(f'{filename}.csv', mode=mode) as csv_file:
        fieldnames = list(k_sorted_set.keys())
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader() if mode == 'w' else None
        writer.writerow(k_sorted_set)


run(32768, 8)
