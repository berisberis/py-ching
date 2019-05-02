class FuXiSequence:

    @staticmethod
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

    @staticmethod
    def lookup_table(table, cords):
        glyph_num = table.index(cords)
        return glyph_num
