import csv
from sorting_algo import bubble_sort
import statistics

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
    
    average = statistics.mean(scores)
    minimum = min(scores)   
    maximum = max(scores)
    median = get_median_value(scores)
    mode = statistics.mode(scores)

    print(f'Average: {average} Median: {median} Smallest: {minimum} Largest: {maximum} mode: {mode}')