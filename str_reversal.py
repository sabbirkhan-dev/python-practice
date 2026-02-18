# str[start:stop:step]
"""
srt_rev = "reversal"
print(srt_rev[::-1])
"""

# test = "sabbir"
# print(test[1:]+ test[0])
# print(test[1:]) 

def str_rever(str):
    if len(str) == 0:
        return str
    else:
        return str_rever(str[1:]) + str[0]
    
print(str_rever("sabbir")) 

