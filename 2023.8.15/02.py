list1 = ['aaa', 111, (4, 5), 2.01]
list2 = ['bbb', 333, 111, 3.14, (4, 5)]

def check_elements(list1, list2, element):
    if element in list1 and element not in list2:
        return str(element) + " only in List1"
    elif element in list2 and element not in list1:
        return str(element) + " only in List2"
    elif element in list1 and element in list2:
        return str(element) + " in List1 and List2"
    else:
        return str(element) + " doesn't belong to either list"

elements_to_check = list1
for element in elements_to_check:
    result = check_elements(list1, list2, element)
    print(result)

# for data_1 in list1:
#     if data_1 in list1 and data_1 not in list2:
#         print(str(data_1) + " only in List1")
#     elif data_1 in list2 and data_1 not in list1:
#         print(str(data_1) + " only in List2")
#     elif data_1 in list1 and data_1 in list2:
#         print(str(data_1) + " in List1 and List2")
#     else:
#         print(str(data_1) + " doesn't belong to either list")
