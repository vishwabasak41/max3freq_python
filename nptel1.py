list=[]
count_list={}
count=0
size=int(input("enter size"))
for i in range(size):
    list.append(int(input()))
for i in range(size):
   for j in range(size):
       if list[i]==list[j]:
           count+=1
           count_list[str(list[i])]=count
   count=0
aranged=[]
for i in count_list.keys():
            newlist_sp=sorted(count_list,key=count_list.get, reverse=True)
print(newlist_sp)
for i in range(3):
    aranged.append(newlist_sp[i])
print(aranged)




