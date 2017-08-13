def max(**dict):
    max=0
    for i in dict.keys():
        if dict[i]>max:
            max_valued_key=i;
    return max_valued_key;

def delete_key(max,**dict):
    del dict[max]
    return dict


list=[]
count_list={}
count=0
size=int(input("enter size"))
for i in range(size):
    list.append(int(input()))
for i in range(size):
   for j in range(size):
       print("list[i]",list[i])
       print("list[j]",list[j])
       if list[i]==list[j]:
           count+=1
           print("count is",count)
           count_list[list[i]]=count;
           print (count_list)
c=0
result=[]
for i in count_list.keys():
    if c>3:
        break
    else:
        maximum=max(count_list)
        result.append(maximum)
        count_list=delete_key(count_list,maximum)
        print("count list after deleting max",count_list)
        c+=1




