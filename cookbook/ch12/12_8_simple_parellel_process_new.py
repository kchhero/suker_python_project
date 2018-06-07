import gzip
import io
import glob
from concurrent import futures

def find_robots(filename) :
    robots = set()
    with gzip.open(filename) as f :
        for line in io.TextIOWrapper(f) :
            fields = line.split()
            if len(fields) >= 6 :
                if fields[5] == 'idVendor:' :
                    robots.add(fields[5])
                    robots.add(fields[6])
                    
    return robots

def find_all_robots(logdir) :
    files = glob.glob(logdir+'/*.gz')
    all_robots = set()
    with futures.ProcessPoolExecutor() as pool :
        for robots in pool.map(find_robots, files) :
            all_robots.update(robots)

    return all_robots


if __name__ == '__main__' :
    robots = find_all_robots('logs')
    for ipaddr in robots :
        print(ipaddr)


