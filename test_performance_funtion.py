# Testing with timeit()

import timeit
import datetime

# Paste inside the triple quotes the funtion to measure it performance

funtion_to_test = '''

def join_numbers(limit_number=1):
    "-".join(str(n) for n in range(100000))
    pass

'''


def test_your_funtion(funtion_to_test):
    
    execution_time = timeit.timeit(funtion_to_test, number=1000)
    time_to_string = str(datetime.timedelta(seconds=execution_time))
    
    print("Execution Time: {} Hours, {} Minutes and {} Seconds".format(time_to_string.split(":")[0], time_to_string.split(":")[1],time_to_string.split(":")[2]))
    

    
#Test the funtion [join_numbers()] in the test_your_funtion() 

test_your_funtion(join_numbers)