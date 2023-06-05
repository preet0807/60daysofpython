if __name__ == '__main__':
    nested_list=[]
    scores=[]
    number_values=[]

    for _ in range(int(input())):
        name = input()
        score = float(input())
        new_item=[name,score]
        nested_list.append(new_item)
    
    # print(sorted(nested_list))
    for sublist in nested_list:
        for item in sublist:
          if isinstance(item, float):
                
            number_values.append(item)
final=[]

# print(number_values)
min=999999999
for i in number_values:
   if i<min:
        min=i
number_values = [x for x in number_values if x != min]

min=999999999
for i in number_values:
       if i<min:
        min=i
print(min)
for sublist in nested_list:
    if sublist[1]==min:
        final.append(sublist[0])
sorted_list= sorted(final)
for i in sorted_list:
    print(i)
        

