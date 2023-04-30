def remove_dup(data):
    data = data
    n=[]
    for i in data:
        if i not in n:
            n.append(i)
    result = ','.join(n)
    
    print("The unique letters: {}".format(result))

if _name_ == '_main_':
    data = input("Enter any string: ").lower()
    remove_dup(data=data)
