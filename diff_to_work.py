from sys import getsizeof
from math import ceil
exp1 = 0x1B
sigd1 = 0x308a93
s9 = (13*10**12)*600 #work done by an s9 in 10min
phs2 = (2*10**15)*600 # work done by 2phs

def target_from_nbits(exp, sigd):
    return sigd*256**(exp-3)

def int_to_bytes(x: int) -> bytes:
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')

def compact(target):
    size = len(int_to_bytes(target))
    exp = size-3
    sigd = target // 256**exp
    if( sigd & 0x00800000):
        sigd //= 256
        exp+=1
    print("Exp: %x"% (exp+3), "Sigd: %x"% sigd)

def work(target):
    return 2**256//(target-1)

def target(work):
    return (work/2**256)+1

def reward(work, height):
    for div in range(height//144):
        work*= 99826;
        work //= 100000;
    return work/14200000000000


#if __name__ == __main__:
#    print(target_from_nbits(exp1, sigd1))
#    t = target_from_nbits(exp1, sigd1)
#    w = work(t)
#    w2 = w*60*2*11*2
#    t2 = work(w2)
#    print(compact(t2))
#    r = reward(work(t2))
#    print("reward", r)
#    print("work", w2)
#    print("s9s", w2/s9)
#    print("2phs ", reward(phs2))















