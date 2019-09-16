def find_trigram_number(trigram_bin):
    trigrams = {
        (0, 0, 0): 0,
        (0, 0, 1): 1,
        (0, 1, 0): 2,
        (0, 1, 1): 3,
        (1, 0, 0): 4,
        (1, 0, 1): 5,
        (1, 1, 0): 6,
        (1, 1, 1): 7
    }
    trigram_number = trigrams[trigram_bin]
    return trigram_number


def find_trigram_meaning(number):
    meanings = {
        0: "☷ Earth",
        1: "☶ Mountain",
        2: "☵ Water",
        3: "☴ Wind",
        4: "☳ Thunder",
        5: "☲ Fire",
        6: "☱ Lake",
        7: "☰ Heaven",
    }
    trigram_meaning = meanings[number]
    return trigram_meaning


def trigram_color(number):
    trigram_colors = {
        0: 'grey',
        1: 'blue',
        2: 'green',
        3: 'cyan',
        4: 'red',
        5: 'magenta',
        6: 'yellow',
        7: 'white',
    }
    color_is = trigram_colors[number]
    return color_is


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
        63: "䷾ After Completion", 64: "䷿ Before Completion"
    }
    return meanings[glyph_number]


def secondary_meaning(number):
    messages = {
        1: "All is going well. You are heading for success.",
        2: "For success, follow the path that has been set for you.",
        3: "Despite a bad start, your venture will be successful.",
        4: "Someone needs your experience and your advice.",
        5: "Take things slowly and gently. Wait for the right time to act.",
        6: "Compromise in an argument and don't be vengeful.",
        7: "Take control of the situation and control of yourself.",
        8: "Teamwork is better than solitary action.",
        9: "Be patient, hold back and adopt a restrained approach.",
        10: "Behave with propriety and proceed with caution.",
        11: "Difficulties are fading away. Your reputation is starting to grow.",
        12: "You're facing a stalemate because others are being petty.",
        13: "Be clear, honest and honourable in your relationships.",
        14: "You will receive abundance on many levels.",
        15: "It is better to be modest and humble than to be pompous.",
        16: "Enlist the help of others by enthusing them with your vision.",
        17: "Your conscience is your best guide as to how to behave.",
        18: "Wait 3 days before repairing the damage caused by previous mistakes.",
        19: "Adopting the correct approach will lead to joy and success.",
        20: "Don't waste time on anything that's beyond your control.",
        21: "You must overcome obstacles before you achieve success.",
        22: "Don't judge people or projects by their superficial appearance.",
        23: "Something must come to an end before you start anything new.",
        24: "Situations are improving and you are back on a winning streak.",
        25: "Act with honesty and integrity if you want success.",
        26: "Increase the number of people you know and work with.",
        27: "Nourish others and yourself in every way, but do so with moderation.",
        28: "A situation is becoming too stressful for you. Ask for help.",
        29: "Life is hard, but you will survive if you're honest and keep your head.",
        30: "There is no point in fighting against the natural order of things.",
        31: "You're attracted to someone, but must let nature take its course.",
        32: "The present situation is the best route to success and prosperity.",
        33: "Retreating at the right time is your best tactic at the moment.",
        34: "Don't confuse might with right. Behave honourably.",
        35: "Act for other people's welfare as well as your own.",
        36: "Be modest and put your ambitions to one side at the moment.",
        37: "If you want success, don't try to be something you're not.",
        38: "Small steps will enable you to overcome your current problems.",
        39: "Retreat from a major obstacle and take a different course.",
        40: "Don't introduce new plans; focus on existing arrangements.",
        41: "Make conscious reductions in various areas of your life.",
        42: "Everything is going well and you will be successful. Be generous.",
        43: "Focus on the truth, and be honest, earnest and sincere.",
        44: "Don't enter into partnerships with people you have only just met.",
        45: "Gather together with others and show them your respect.",
        46: "Success is on the way. You will pass a test with flying colours.",
        47: "Accept the current situation and be optimistic about the future.",
        48: "There is more than enough to go round. Don't be greedy.",
        49: "This is a good time to introduce gradual changes to your life.",
        50: "Instigate change that will nourish everyone, including yourself.",
        51: "What seems like a shock will eventually lead to peace once more.",
        52: "Stay in the here and now. Know when to act and when to rest.",
        53: "Do things in their correct order. Progress will be slow but steady.",
        54: "Abandon a new project if it has too many pitfalls.",
        55: "Share your good fortune with others. Don't worry about losing it.",
        56: "Humility, integrity and perseverance lead to success.",
        57: "Focus on small improvements rather than major changes.",
        58: "Behaving correctly and being firm will lead to joy and success.",
        59: "Success comes from being mindful of what you want to achieve.",
        60: "Limitations will give you a stable framework in which to operate.",
        61: "Follow what you believe and have faith in your convictions.",
        62: "Aiming too high leads to possible peril and disappointment.",
        63: "Tidy up the loose ends in a project that's almost finished.",
        64: "Don't let complacency jeopardize a current project."
    }
    return messages[number]
