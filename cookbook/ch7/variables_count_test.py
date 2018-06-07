def arg_test(first, *rest) :
    return (first+sum(rest)), (first + sum(rest)) / (1+len(rest))

test_sum, test_average = arg_test(1,2,3,4,5,6,7,8,9,10)
print(test_sum, test_average)

def anyargs(*args, **kwargs) :
    print(args)
    print(kwargs)

anyargs(1,2,3,{1:'a',2:'b',3:'c'})
