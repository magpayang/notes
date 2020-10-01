import os

def clear():
    return os.system('clear')

def enu(input_array):
    count = 0
    for entry in input_array:
            print(count, entry)
            count += 1

def enuT(input_class, enable_debug = True):
        ''' given a class, list all entries within dir(<class>) then tell me if its a method or attribute '''
        count = 0
        r = input_class
        tempo_array = []
        input_array = dir(input_class)
        for entry in input_array:
                tempo_string = 'type(r.'+entry+')'
                tempo_tup = (count, entry, eval(tempo_string))
                tempo_array.append(tempo_tup)
                if enable_debug: print(tempo_tup)
                count += 1

        return tempo_array
		
def enuD(input_dict, enable_debug=True):
	''' enumerate keys and values for a given dictionary '''
	count = 0
	tempo_array = []
	for key in input_dict.keys():
		tempo_tuple = (count, key, input_dict[key])
		print(tempo_tuple)
		tempo_array.append(tempo_tuple)
		count += 1
	return tempo_array
	
import time
from datetime import datetime

def display_time(time=None):
	''' from corey s. prints time '''
	if time is None:
		time=datetime.now()
	print(time.strftime('%B %d, %Y %H:%M:%S'))
	
def tell_time_loop(delay=6, message="Our time now is", alt_func=None):
	''' '''
	count = 0
	print_message = ' '+message+' '
	while True:
		print(count, print_message, time.asctime())
		count += 1
		time.sleep(delay)
		if alt_func is not None:
			eval(alt_func)
			
	
