## Using brute force approach
def server(lists):
  for i in range(len(lists)-1):  
    for j in range(i+1,len(lists)-1):
        if lists[i][0] > lists[j][0]:
            lists[i],lists[j] = lists[j],lists[i]

        elif lists[i][0] == lists[j][0] and lists[j][1] > lists[i][1]:
            lists[i],lists[j] = lists[j],lists[i]  
  return lists

## Using python based approach
def website(lists):
  sorted_list = sorted(lists,lambda : x[0],-x[1])
  return(sorted_list)
