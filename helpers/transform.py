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

    @staticmethod
    def sort_the_sets(the_sets):
        the_hex_set, the_tri_set, the_bin_set = the_sets
        k_sorted_hex_set = Arrays.k_sort(the_hex_set)
        k_sorted_tri_set = Arrays.k_sort(the_tri_set)
        k_sorted_bin_set = Arrays.k_sort(the_bin_set)
        return k_sorted_hex_set, k_sorted_tri_set, k_sorted_bin_set
