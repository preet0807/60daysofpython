def swap_case(s):
    res=""
    for char in s:
        if char.isupper():
            res = res+ char.lower()
        elif char.islower():
            res=res+char.upper()
        elif char==" ":
            res=res+" "
        else:
            res=res+char
        
    return res
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)