import numpy as np

S = raw_input("input string S ")
T = raw_input("input string T ")



S_len = len(S)
T_len = len(T)

number_count = 0

for i in range(S_len-T_len):
    S_str = S[0+i:T_len-1+i]
    S_temp = S_str
    list_s = list(set(list(S_str)))
    list_s.sort(key=list(S_str).index)
    for j in range(len(list_s)):
        S_temp = S_temp.replace(list_s[j],T[j])
    if(S_temp==T[0:T_len-1]):
        number_count += 1
print(number_count)