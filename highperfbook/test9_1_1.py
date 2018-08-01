import time
import random

TESTCNT = 100000000


def estimate_nbr_points_in_quarter_circle():
    nbr_trials_in_quarter_unit_circle = 0
    for step in range(int(TESTCNT)):
        xs = random.uniform(0, 1)
        ys = random.uniform(0, 1)
        is_in_unit_circle = (xs * xs + ys * ys) <= 1
        nbr_trials_in_quarter_unit_circle += is_in_unit_circle

    print("shot cnt = %f" % (nbr_trials_in_quarter_unit_circle/TESTCNT))
    print("pi = %f" % (4.0*nbr_trials_in_quarter_unit_circle/TESTCNT))

    return nbr_trials_in_quarter_unit_circle


startTime = time.time()
estimate_nbr_points_in_quarter_circle()
print("running time : " + str(time.time()-startTime))
