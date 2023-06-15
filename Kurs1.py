'''def str_counter(s):   # O (N*M) S = 30
    for sym in set(s):
        count = 0
        for sub_sym in s:
            if sym == sub_sym:
                count+=1
        print(sym, count)

str_counter('abcnra')

def str_counter(s):   # O (N**2) S = 36
    for sym in s:
        count = 0
        for sub_sym in s:
            if sym == sub_sym:
                count+=1
        print(sym, count)

str_counter('abcnra')'''
def str_counter(s): #O (N)
    syms_counter = {}
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym, 0) + 1
    for syms, count in syms_counter.items():
        print(syms, count)
str_counter('abcnra')

