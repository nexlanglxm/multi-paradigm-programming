import csv
 
with open('example.csv', mode ='r') as file:   
    csvFile = csv.DictReader(file)
    scores = []
    
    for lines in csvFile:
        score = int(lines["Score"])
        scores.append(score)    
    
    total = 0
    for score in scores:
        total += score
        
    average = total / len(scores)
    
    minimum = scores[0]
    for score in scores:
        if minimum < score:
            minimum = score
    
    maximum = scores[0]
    for score in scores:
        if maximum > score:
            maximum = score
    
    list1 = scores.copy()
    for i in range(0,len(list1)-1):  
        for j in range(len(list1)-1):  
            if(list1[j]>list1[j+1]):  
                temp = list1[j]  
                list1[j] = list1[j+1]  
                list1[j+1] = temp  
    
    median = list1[int(len(list1)/2)]
    
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
    
    print(f'Average: {average} Median: {median} Smallest: {minimum} Largest: {maximum} mode: {mode}')
    