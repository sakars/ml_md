m=[1,2,'a',4,5,'6']
i_list=[]
s_list=[]
for i in m:
    if isinstance(i,int):
        i_list.append(i)
    elif isinstance(i,str):
        s_list.append(i)
print(i_list)
print(s_list)