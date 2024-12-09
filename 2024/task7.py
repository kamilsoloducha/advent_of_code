def part1(lines):

    counter = 0

    for line in lines:
        [exp, args] = line.strip('\n').split(':')
        exp = int(exp)
        args = list(map(int, args.strip(' ').split(' ')))
        
        if try_add(exp, args[0], args[1:]) or try_multipy(exp, args[0], args[1:]) or try_concat(exp, args[0], args[1:]):
            counter += exp

    print(counter)



def try_multipy(exp, num, args):
    if len(args) == 0:
        return exp == num

    num = num * args[0]

    if try_multipy(exp, num, args[1:]):
        return True
    
    if try_add(exp, num, args[1:]):
        return True
    
    if(try_concat(exp, num, args[1:])):
        return True
    
    return False
    

def try_add(exp, num, args):
    if len(args) == 0:
        return exp == num

    num = num + args[0]

    if try_multipy(exp, num, args[1:]):
        return True
    
    if try_add(exp, num, args[1:]):
        return True
    
    if(try_concat(exp, num, args[1:])):
        return True

    return False

def try_concat(exp, num, args):
    if len(args) == 0:
        return exp == num
    
    num = int(str(num)+str(args[0]))

    if try_multipy(exp, num, args[1:]):
        return True
    
    if try_add(exp, num, args[1:]):
        return True
    
    if(try_concat(exp, num, args[1:])):
        return True
    
    return False