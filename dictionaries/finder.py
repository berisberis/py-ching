class Finder:

    @staticmethod
    def find_trigram_number(trigram_bin):
        trigrams = {
            "000": 8, "001": 7,
            "010": 6, "011": 5,
            "100": 4, "101": 3,
            "110": 2, "111": 1,
        }
        trigram_number = trigrams[trigram_bin]
        return trigram_number

    @staticmethod
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

    @staticmethod
    def trigram_color(number):
        trigram_colors = {
            1: 'white',
            2: 'yellow',
            3: 'magenta',
            4: 'red',
            5: 'cyan',
            6: 'green',
            7: 'blue',
            8: 'grey'
        }
        color_is = trigram_colors[number]
        return color_is

    @staticmethod
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

    @staticmethod
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
        try:
            return meanings[glyph_number]
        except KeyError:
            print(f'\n\nHexagram 0 does not exist!!!\n\n')

