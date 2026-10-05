#Surabya Satyal Multiplication table
import time

for row in range(1,13):
    for collum in range(1,13):
        answer = (row*collum)
        print(f"{answer:>4}",end = '')
    print('\n')       
    time.sleep(0.25)