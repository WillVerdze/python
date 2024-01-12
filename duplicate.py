def get_list():
    the_list = []
    number_of_elements=int(input("Enter number of elements"))
    for i in range(number_of_elements):
        element=input("Enter element{i+1}: ")
        the_list.append(element)
    return the_list
