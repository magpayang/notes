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
	

