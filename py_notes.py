import os

def clear():
    return os.system('clear')

def enu(input_array):
    count = 0
    for entry in input_array:
            print(count, entry)
            count += 1

def enuT(input_array, r_resp, enable_debug = True):
        ''' given input_array=dir(r) and r_resp = r '''
        count = 0
        r = r_resp
        tempo_array = []
        for entry in input_array:
                tempo_string = 'type(r.'+entry+')'
                tempo_tup = (count, entry, eval(tempo_string))
                tempo_array.append(tempo_tup)
                if enable_debug: print(tempo_tup)
                count += 1

        return tempo_array


