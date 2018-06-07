import gzip
import io
import glob

# [suker@suker-machine] ~/sukerGitHub/suker_python_project/cookbook/ch12
# $ ll logs
# total 148K
# drwxrwxr-x 2 suker suker  4K  4월 24 14:56 ./
# drwxrwxr-x 3 suker suker  4K  4월 24 14:56 ../
# -rw-r----- 1 suker suker 40K  4월 24 14:46 syslog.3.gz
# -rw-r----- 1 suker suker  3K  4월 24 14:46 syslog.4.gz
# -rw-r----- 1 suker suker 39K  4월 24 14:46 syslog.5.gz
# -rw-r----- 1 suker suker 13K  4월 24 14:46 syslog.6.gz
# -rw-r----- 1 suker suker 39K  4월 24 14:46 syslog.7.gz

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
    for robots in map(find_robots, files) :
        all_robots.update(robots)
    return all_robots


if __name__ == '__main__' :
    robots = find_all_robots('logs')
    for ipaddr in robots :
        print(ipaddr)


