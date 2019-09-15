import unittest
from iching.hex_generator import Hexagram
from iching.hex_generator import IteratedSet
from iching.hex_generator import Sorter


class TestTrigram(unittest.TestCase):
    def test_trigram_elements_are_binary(self):
        hexagram = Hexagram.trigram()
        first, second, third = hexagram
        self.assertLessEqual(first, 1, "Must be less than 2")
        self.assertLessEqual(second, 1, "Must be less than 2")
        self.assertLessEqual(third, 1, "Must be less than 2")

    def test_trigram_is_not_null(self):
        hexagram = Hexagram.trigram()
        self.assertIsNotNone(hexagram)

    def test_trigram_is_tuple(self):
        hexagram = Hexagram.trigram()
        assert tuple(hexagram)


class TestHexagram(unittest.TestCase):
    def test_hexagram_has_tuples(self):
        hexagram = Hexagram.create_hexagram()
        hex1, hex2 = hexagram
        assert tuple(hex1)
        assert tuple(hex2)

    def test_hexagram_is_tuple(self):
        hexagram = Hexagram.create_hexagram()
        assert tuple(hexagram)


class TestIteratedSet(unittest.TestCase):
    def test_create_counted_sets_are_lists(self):
        iterated_set = IteratedSet(4096)
        counted_set = iterated_set.create_counted_set()
        counted_hex, counted_tri, counted_bin = counted_set
        # self.isinstance(type(counted_hex), Counter)
        assert tuple(counted_hex)
        assert list(counted_tri)
        assert list(counted_bin)


class TestSorter(unittest.TestCase):
    def test_sort_the_sets_by_key_is_tuple(self):
        iterated_set = IteratedSet(4096)
        counted_iteration = iterated_set.create_counted_set()
        sorter = Sorter(counted_iteration)
        sorted_sets = sorter.sort_the_sets_by_key()
        assert tuple(sorted_sets)

    def test_sort_the_sets_by_key_dict_inside_tuple(self):
        iterated_set = IteratedSet(4096)
        counted_iteration = iterated_set.create_counted_set()
        sorter = Sorter(counted_iteration)
        sorted_hex, sorted_tri, sorted_bin = sorter.sort_the_sets_by_key()
        assert dict(sorted_hex)
        assert dict(sorted_tri)
        assert dict(sorted_bin)

