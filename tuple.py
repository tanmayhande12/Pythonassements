s1=(10,20,30,40,50)
s2=(30,40,50,60,70,80)
s1=sorted(s2,reverse=True)
print('length',len(s1))
print('max',max(s1))
print('min',min(s2))
print('sum',sum(s1))
print(s2)
print(s1)
s4=(1,2)
x,y=s4
print(x)
print(y)

def sort_tuple_list_by_sum(tuple_list):
  return sorted(tuple_list, key=lambda x: sum(x))
input_list = [(4, 5), (2, 3), (6, 7), (2, 8)]
sorted_list = sort_tuple_list_by_sum(input_list)
print(sorted_list)  