print("Name:Raushan kumar\nCRN:2221139\nURN:2203751")
def insert_element(lst, index, element):
    # lst.insert(element) -->error
    lst.insert(index, element)
    print(f"Element {element} inserted at index {index}")
    print("updated list:",lst)

def remove_element(lst, element):
        lst.remove(element)
        print(f"Element {element} removed from the list.")
        print("updated list:",lst)
mylist = [1, 2, 3, 4, 5]
insert_element(mylist, 2, 10)
remove_element(mylist, 4)
mylist.pop()#pop() fun delete last element from the list,when we don't give any index but,
mylist.pop(2)  # when we give any index then pop(2) fun will delete that element which are presndt at that index.
mylist.remove(2)# by element
print("after pop and remove:",mylist)

