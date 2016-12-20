getFunction = ["function", "build_uboot", "build_optee"]

def pppp(funcName) :
    lineNum = [0,0]
    with open("build.sh", "r") as f :
        for num, line in enumerate(f, 1) :
            if "function" in line and funcName in line :
                lineNum[0] = num
    	
            elif "function" in line or "parse_args $@" in line :
                if lineNum[0] != 0 :
                    lineNum[1] = num-1
                    return lineNum
    
print pppp("build_uboot")
print pppp("build_optee")
