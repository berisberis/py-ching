#!/usr/bin/env python3


import secrets
import csv
from collections import Counter


def hexagram():

    def trigram():
        t = 1
        trigram_string = []
        while t <= 3:
            int_rand = secrets.randbelow(1000)
            if int_rand > 500:
                trigram_string.append(1)
            else:
                trigram_string.append(0)
            t += 1
        return trigram_string

    h = 1
    hexagram_array = []
    while h <= 2:
        hexagram_array.append(trigram())
        h += 1
    return hexagram_array


def array_to_string(hexagram_array):
    hexagram_string = ''
    for trigram in hexagram_array:
        hexagram_string += ''.join(str(trigram))
    return hexagram_string


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
    all_bin = []
    all_tri = []
    all_hex = []
    while i <= iterations:
        new_hex = hexagram()
        low_bins = new_hex[0]
        up_bins = new_hex[1]
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
    counted_bin = Counter(all_bin)
    counted_hex = Counter(all_hex)
    counted_tri = Counter(all_tri)
    return counted_hex, counted_tri, counted_bin


def k_sort(d):
    return {k: d[k] for k in sorted(d.keys())}


def print_results(counted_hex, counted_tri, counted_bin):
    most_common_hex = counted_hex.most_common(2)
    most_common_tri = counted_tri.most_common(2)
    most_common_bin = counted_bin.most_common(2)
    first_place_king_wen_hex = transform_king_wen(most_common_hex[0][0])
    times_first_hex = most_common_hex[0][1]
    second_place_king_wen_hex = transform_king_wen(most_common_hex[1][0])
    times_second_hex = most_common_hex[1][1]
    first_place_tri = most_common_tri[0][0]
    times_first_tri = most_common_tri[0][1]
    second_place_tri = most_common_tri[1][0]
    times_second_tri = most_common_tri[1][1]
    first_place_bin = most_common_bin[0][0]
    times_first_bin = most_common_bin[0][1]
    second_place_bin = most_common_bin[1][0]
    times_second_bin = most_common_bin[1][1]
    print(f'\nHexagram {first_place_king_wen_hex} was found {times_first_hex} times')
    print(find_king_wen_meaning(first_place_king_wen_hex))
    print(f'\nHexagram {second_place_king_wen_hex} was found {times_second_hex} times')
    print(find_king_wen_meaning(second_place_king_wen_hex))
    print(f'\nTrigram {first_place_tri} was found {times_first_tri} times')
    print(find_trigram_meaning(first_place_tri))
    print(f'\nTrigram {second_place_tri} was found {times_second_tri} times')
    print(find_trigram_meaning(second_place_tri))
    print(f'\nBinary {first_place_bin} was found {times_first_bin} times')
    print(f'Binary {second_place_bin} was found {times_second_bin} times')


def run(iterations, sets):

    def iterate_and_sort():
        the_set = iterate(iterations)
        the_hex_set = the_set[0]
        the_tri_set = the_set[1]
        the_bin_set = the_set[2]
        print_results(the_hex_set, the_tri_set, the_bin_set)
        k_sorted_hex_set = k_sort(the_hex_set)
        k_sorted_tri_set = k_sort(the_tri_set)
        k_sorted_bin_set = k_sort(the_bin_set)
        return k_sorted_hex_set, k_sorted_tri_set, k_sorted_bin_set

    def sets_to_csv(mode):
        sorted_sets = iterate_and_sort()
        to_csv(sorted_sets[0], 'hexagrams', mode)
        to_csv(sorted_sets[1], 'trigrams', mode)
        to_csv(sorted_sets[2], 'binaries', mode)

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
