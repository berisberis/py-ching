import secrets


class Hexagram:

    @staticmethod
    def create():

        def trigram():
            trigram_array = []
            for t in range(3):
                int_rand = secrets.randbelow(2)
                if int_rand == 1:
                    trigram_array.append(1)
                else:
                    trigram_array.append(0)
            return trigram_array

        hexagram_array = []
        for h in range(2):
            hexagram_array.append(trigram())
        return hexagram_array
