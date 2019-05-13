import csv
import os


class CsvMake:

    def __init__(self, sorted_sets):
        self.sorted_sets = sorted_sets

    file_names = ['hexagrams', 'trigrams', 'binaries']

    def sets_to_csv(self, mode):
        for key, one_set in enumerate(self.sorted_sets):
            self.write_to_csv(one_set, self.file_names[key], mode)

    @staticmethod
    def write_to_csv(one_set, filename, mode):
        if not os.path.exists('csv'):
            os.mkdir('csv')
        with open(f'csv/{filename}.csv', mode=mode) as csv_file:
            fieldnames = list(one_set.keys())
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader() if mode == 'w' else None
            writer.writerow(one_set)
