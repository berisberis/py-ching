#!/usr/bin/env python3


import secrets
import csv
from collections import Counter


def hexagram():

    def trigram():
        t = 1
        trigram_string = ''
        while t <= 3:
            int_rand = secrets.randbelow(1000)
            if int_rand > 500:
                trigram_string += str(1)
            else:
                trigram_string += str(0)
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


def make_cord_array(low_num, up_num):
    this_array = [low_num, up_num]
    return this_array


def find_glyph(glyph):
    i_ching = {
        "111111": 1, "000000": 2,
        "100010": 3, "010001": 4,
        "111010": 5, "010111": 6,
        "010000": 7, "000010": 8,
        "111011": 9, "110111": 10,
        "111000": 11, "000111": 12,
        "101111": 13, "111101": 14,
        "001000": 15, "000100": 16,
        "100110": 17, "011001": 18,
        "110000": 19, "000011": 20,
        "100101": 21, "101001": 22,
        "000001": 23, "100000": 24,
        "100111": 25, "111001": 26,
        "100001": 27, "011110": 28,
        "010010": 29, "101101": 30,
        "001110": 31, "011100": 32,
        "001111": 33, "111100": 34,
        "000101": 35, "101000": 36,
        "101011": 37, "110101": 38,
        "001010": 39, "010100": 40,
        "110001": 41, "100011": 42,
        "111110": 43, "011111": 44,
        "000110": 45, "011000": 46,
        "010110": 47, "011010": 48,
        "101110": 49, "011101": 50,
        "100100": 51, "001001": 52,
        "001011": 53, "110100": 54,
        "101100": 55, "001101": 56,
        "011011": 57, "110110": 58,
        "010011": 59, "110010": 60,
        "001100": 61, "110011": 62,
        "101010": 63, "010101": 64,
    }
    glyph_number = i_ching[glyph]
    return glyph_number


def find_meaning(glyph_number):
    meanings = {
        1: "䷀ Creative Heaven",
        2: "䷁ Receptive Earth",
        3: "䷂ Difficulty at the Beginning",
        4: "䷃ Youthful Folly",
        5: "䷄ Waiting",
        6: "䷅ Conflict",
        7: "䷆ Army",
        8: "䷇ Holding Together",
        9: "䷈ Small Taming",
        10: "䷉ Treading",
        11: "䷊ Peace",
        12: "䷋ Standstill",
        13: "䷌ Fellowship",
        14: "䷍ Great Possesion",
        15: "䷎ Modesty",
        16: "䷏ Enthusiasm",
        17: "䷐ Following",
        18: "䷑ Work on the Decayed",
        19: "䷒ Approach",
        20: "䷓ Contemplation",
        21: "䷔ Biting Through",
        22: "䷕ Grace",
        23: "䷖ Splitting Apart",
        24: "䷗ Return",
        25: "䷘ Innocence",
        26: "䷙ Great Taming",
        27: "䷚ Mouth Corners",
        28: "䷛ Great Preponderance",
        29: "䷜ Abysmal Water",
        30: "䷝ Clinging Fire",
        31: "䷞ Influence",
        32: "䷟ Duration",
        33: "䷠ Retreat",
        34: "䷡ Great Power",
        35: "䷢ Progress",
        36: "䷣ Darkening of the Light",
        37: "䷤ Family",
        38: "䷥ Opposition",
        39: "䷦ Obstruction",
        40: "䷧ Deliverance",
        41: "䷨ Decrease",
        42: "䷩ Increase",
        43: "䷪ Breakthrough",
        44: "䷫ Coming to Meet",
        45: "䷬ Gathering Together",
        46: "䷭ Pushing Upward",
        47: "䷮ Oppression",
        48: "䷯ The Well",
        49: "䷰ Revolution",
        50: "䷱ The Cauldron",
        51: "䷲ The Arousing Thunder",
        52: "䷳ The Keeping Still Mountain",
        53: "䷴ Development",
        54: "䷵ The Marrying Maiden",
        55: "䷶ Abundance",
        56: "䷷ The Wanderer",
        57: "䷸ The Gentle Wind",
        58: "䷹ The Joyous Lake",
        59: "䷺ Dispersion",
        60: "䷻ Limitation",
        61: "䷼ Inner Truth",
        62: "䷽ Small Preponderance",
        63: "䷾ After Completion",
        64: "䷿ Before Completion",
    }
    return meanings[glyph_number]


def k_sort(d):
    return [(k, d[k]) for k in sorted(d.keys())]


def iterate():
    # table = generate_table()
    i = 1
    all_tri = []
    all_hex = []
    while i <= 262144:
        new_hex = hexagram()
        all_tri.append(find_trigram_number(new_hex[0]))
        all_tri.append(find_trigram_number(new_hex[1]))
        to_string = array_to_string(new_hex)
        all_hex.append(find_glyph(to_string))
        i += 1
    counted_hex = Counter(all_hex)
    counted_tri = Counter(all_tri)
    return counted_hex, counted_tri


def print_results(counted_hex, counted_tri):
    most_common_hex = counted_hex.most_common(3)
    most_common_tri = counted_tri.most_common(3)
    first_place_hex = most_common_hex[0][0]
    times_first_hex = most_common_hex[0][1]
    second_place_hex = most_common_hex[1][0]
    times_second_hex = most_common_hex[1][1]
    first_place_tri = most_common_tri[0][0]
    times_first_tri = most_common_tri[0][1]
    second_place_tri = most_common_tri[1][0]
    times_second_tri = most_common_tri[1][1]
    print(f'\nHexagram {first_place_hex} was found {times_first_hex} times')
    print(find_meaning(first_place_hex))
    print(f'\nHexagram {second_place_hex} was found {times_second_hex} times')
    print(find_meaning(second_place_hex))
    print(f'\nTrigram {first_place_tri} was found {times_first_tri} times')
    print(find_trigram_meaning(first_place_tri))
    print(f'\nTrigram {second_place_tri} was found {times_second_tri} times')
    print(find_trigram_meaning(second_place_tri))


def run():
    the_set = iterate()
    the_hex_set = the_set[0]
    the_tri_set = the_set[1]
    print_results(the_hex_set, the_tri_set)


def create_csv(values):
    # placeholder function
    return values


run()
