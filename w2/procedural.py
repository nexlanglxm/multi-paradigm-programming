import csv
from sorting_algo import bubble_sort

def get_maximum_value(list):
    '''
        Given a list of numbers this function will return the maximum/highest value

        :param list: the list of numbers given as input
        :return: the maximum numerical value
    '''
    maximum = list[0]
    for l in list:
        if maximum > l:
            maximum = l
    return maximum

def get_minimum_value(list):
    '''
        Given a list of numbers this function will return the minimum/lowest value

        :param list: the list of numbers given as an input
        :return: the minimum numerical value
    '''
    minimum = list[0]
    for l in list:
        if minimum < l:
            minimum = l
    return minimum        
    
def get_average(list):
    """ 
        Given a list of numbers as input this function will return the numerical average.
    
        :param list: the list of numbers given as input
        :return: the numerical average of the list
    """
    total = 0
    for l in list:
        total += l
        
    average = total / len(list)
    return average

def get_median_value(list):
    '''
        Given a list of numbers this function will return the numerical median/middle value

        :param list: the list of numbers given as an input
        :return: the median value; half the numerical values are larger, half are smaller
    '''
    list1 = list.copy()
    bubble_sort(list1)
    median = list1[int(len(list1)/2)]
    return median
    
def get_mode(list):
    '''
        Given a list of numerical values this function will return the value which appears most often

        :param list:
        :return: the mode, most often occurence in the list
    '''
    highest_freq = 0
    mode = scores[0]
    for score in scores:
        frequency = 0
        for score2 in scores:
            if score == score2:
                frequency += 1
        if frequency > highest_freq:
            mode = score
            highest_freq = frequency
    return mode

def read_scores_from_csv(filename):
    '''

    '''
    scores = []
    with open(filename, mode ='r') as file:   
        csvFile = csv.DictReader(file)
    
        for lines in csvFile:
            score = int(lines["Score"])
            scores.append(score)    
    return scores
    
if __name__ == "__main__":

    scores = read_scores_from_csv('example.csv')
    
    average = get_average(scores)
    minimum = get_minimum_value(scores)   
    maximum = get_maximum_value(scores)
    median = get_median_value(scores)
    mode = get_mode(scores)

    print(f'Average: {average} Median: {median} Smallest: {minimum} Largest: {maximum} mode: {mode}')
    