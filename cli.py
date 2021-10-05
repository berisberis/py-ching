#!/usr/bin/env python3

from iching.hex_generator import PyChing

experiment = PyChing(iterations=4096, sets=2)
results = experiment.run()
results_data = results[0]
hex_keys = results_data[0][0].keys()

all_sets_hex_values = []

for one_set in results_data:
    hex_values = one_set[0].values()
    all_sets_hex_values.append(hex_values)
meanings = results[1]

bin_values = []
for one_set in results_data:
    bin_values.append(one_set[2])


print(results[1], bin_values)
