# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# This function returns the largest number in a given array.

def find_max(l):
    # # Write code here
    # # num = l.pop()
    # max = l[len(l) -1]
    # if (len(l)==0):
    #     return max
    # l.pop()
    if len(l) == 1:
        return l[0]
    else:
        return max(l[0],find_max(l[1:]))
    



print(find_max([1, 4, 45, 6, -50, 10, 2]))
# => 45