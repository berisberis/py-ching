import secrets


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
