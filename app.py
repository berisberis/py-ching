#!/usr/bin/env python3

from generators.set import Iteration
from helpers.terminal import Results
from helpers.files import CsvMake
from helpers.transform import Arrays


class IChing:

    @staticmethod
    def run(iterations, sets):
        CsvMake.sets_to_csv('w', Arrays.sort_the_sets(Results.print(Iteration.iterate(iterations))))
        r = 1
        while r < sets:
            CsvMake.sets_to_csv('a', Arrays.sort_the_sets(Results.print(Iteration.iterate(iterations))))
            r += 1


IChing.run(iterations=4096, sets=4)
