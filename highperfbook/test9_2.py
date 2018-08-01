"""Estimate Pi using Threads and Processes"""
import time
import numpy as np
from multiprocessing import Pool


def estimate_nbr_points_in_quarter_circle(nbr_samples):
    np.random.seed()
    xs = np.random.uniform(0, 1, nbr_samples)
    ys = np.random.uniform(0, 1, nbr_samples)
    estimate_inside_quarter_unit_circle = (xs * xs + ys * ys) <= 1
    nbr_trials_in_quarter_unit_circle = np.sum(
        estimate_inside_quarter_unit_circle)
    return nbr_trials_in_quarter_unit_circle


if __name__ == "__main__":
    nbr_samples_in_total = 100000000
    nbr_parallel_blocks = 8

    pool = Pool()

    nbr_samples_per_worker = int(nbr_samples_in_total / nbr_parallel_blocks)
    print(type(nbr_samples_per_worker))
    print("Making {} samples per worker".format(nbr_samples_per_worker))

    # confirm we have an integer number of jobs to distribute
    assert nbr_samples_per_worker == int(nbr_samples_per_worker)
    nbr_samples_per_worker == int(nbr_samples_per_worker)
    map_inputs = [nbr_samples_per_worker] * nbr_parallel_blocks
    print(type(map_inputs))
    t1 = time.time()
    results = pool.map(estimate_nbr_points_in_quarter_circle, map_inputs)
    pool.close()
    print("Dart throws in unit circle per worker:", results)
    print("Took {}s".format(time.time() - t1))
    nbr_in_circle = sum(results)
    combined_nbr_samples = sum(map_inputs)

    pi_estimate = float(nbr_in_circle) / combined_nbr_samples * 4
    print("Estimated pi", pi_estimate)
    print("Pi", np.pi)
