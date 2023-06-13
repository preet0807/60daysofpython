def print_formatted(number):
    # your code goes 
    width= len(bin(number)[2:])

    for i in range (1,number+1):
        # print(i, end="")
        dec_num=i
        dec_str=str(dec_num)
        oct_num= oct(i)
        oct_str= str(oct_num)
        oct_strf=oct_str.lstrip("0o")
        # print("\t", end ="")
        # print(oct_strf, end="")
        hex_num=hex(i)
        hex_str=str(hex_num)
        hex_strf= hex_str.upper()
        hex_strf=hex_strf.lstrip("0X")
        # print("\t", end ="")
        # print (hex_strf, end="")
        bin_num=bin(i)
        bin_str=str(bin_num)
        bin_strf= bin_str.lstrip("0b")
        # print("\t",end="")
        print((dec_str).rjust(width),(oct_strf).rjust(width),(hex_strf).rjust(width),(bin_strf).rjust(width))

    return
    





if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

