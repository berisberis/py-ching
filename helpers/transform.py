class Arrays:

    @staticmethod
    def array_to_string(array):
        string = ''
        for item in array:
            string += ''.join(str(item))
        return string

    @staticmethod
    def make_cord_array(low_tri_num, up_tri_num):
        this_array = [low_tri_num, up_tri_num]
        return this_array

    @staticmethod
    def k_sort(d):
        return {k: d[k] for k in sorted(d.keys())}
