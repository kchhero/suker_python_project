import time

lkLogFileName = "lk_log.txt"
kernelLogFileName = "kernel_log.txt"

def logAbstraction() :
    check_lk_log_start_mark = "[0] welcome to lk"
    check_lk_log_end_mark = "lge_bootlog_init: token   (null)"
    check_kernel_log_start_mark = "Initializing cgroup subsys cpu"
    check_kernel_log_end_mark = "" #not used
    kernel_log_max_size = 1024*1024  #1MB
    
    lk_log = file(lkLogFileName, 'w')
    kernel_log = file(kernelLogFileName, 'w')
    
    kernel_logging_start = False
    lk_logging_start = False
    
    kernel_size_sum = 0
    
    print "Start logging !!"
    timess = time.time()
    
    ddrcs0_bin = open('DDRCS0.bin','rb')
    for line in ddrcs0_bin.xreadlines() :
        if check_kernel_log_start_mark in line :
            kernel_logging_start = True
    
        if kernel_logging_start==False :
            pass
        else :
            if check_lk_log_start_mark in line :            
                lk_logging_start = True
    
            if lk_logging_start==True :
                if check_lk_log_end_mark in line :
                    lk_log.write(line.strip())
                    lk_log.write("\n")
                    lk_logging_start = False
                    lk_log.close()
                else :
                    lk_log.write(line.strip())
                    lk_log.write("\n")
            
            kernel_log.write(line.strip())
            kernel_log.write("\n")
            kernel_size_sum += len(line)
            if kernel_size_sum >= kernel_log_max_size :
                print "last size : ",kernel_size_sum - len(line)
                print "last len size : ",len(line)
                kernel_logging_start = False
                kernel_log.close()
                break
    
    print "Done !!"
    print "Time : ", time.time()-timess

"""
def detailInfoAbstractionForLk() :
    ss
    
def detailInfoAbstractionForKernel() :
    aa
    """

logAbstraction()