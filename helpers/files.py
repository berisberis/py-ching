import csv


class CsvMake:

    @staticmethod
    def to_csv(k_sorted_set, filename, mode):
        with open(f'{filename}.csv', mode=mode) as csv_file:
            fieldnames = list(k_sorted_set.keys())
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader() if mode == 'w' else None
            writer.writerow(k_sorted_set)

