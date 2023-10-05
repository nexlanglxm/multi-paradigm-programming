def  bubble_sort(list1):
    '''
        The bubble sort function arranges the values in ascending numerical order (as denoted by the > sign in line 63 )

        :param list1: a copy of the list of numbers given as input
        :return: amends the list so the get_median_value function can find the median value
    '''
    for i in range(0,len(list1)-1):  
        for j in range(len(list1)-1):  
            if(list1[j]>list1[j+1]):  
                temp = list1[j]  
                list1[j] = list1[j+1]  
                list1[j+1] = temp  
    