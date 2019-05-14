#!/usr/bin/env python3

from generator.iching import PyChing

experiment = PyChing(iterations=4096, sets=8)
experiment.run()
