import csv
import os


class CsvMake:

    file_names = ['hexagrams', 'trigrams', 'binaries']

    def sets_to_csv(self, mode, sorted_sets):
        for idx, one_set in enumerate(sorted_sets):
            self.to_csv(one_set, self.file_names[idx], mode)
        return sorted_sets

    @staticmethod
    def to_csv(k_sorted_set, filename, mode):
        if not os.path.exists('csv'):
            os.mkdir('csv')
        with open(f'csv/{filename}.csv', mode=mode) as csv_file:
            fieldnames = list(k_sorted_set.keys())
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader() if mode == 'w' else None
            writer.writerow(k_sorted_set)
