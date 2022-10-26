debug_data = ['Number of previous msg sent to server',
              'Total bytes of previous msg sent to server',
              'Number of stored light sensor data',
              'Light sensor marker',
              'Number of error occurred',
              'Error marker',
              'Stored temperature point number',
              'Temperature marker',
              'Number of temperature data sent to server',
              'Unknown']

input_string = r"01/01/1970 00:01:04,External Battery,576,576.00 %|01/01/2066 00:03:37,External Battery,0," \
               r"0.00 %|01/01/2066 00:03:37,External Battery,0,0.00 %|01/01/2066 00:03:37,External Battery,0," \
               r"0.00 %|01/01/2066 00:03:37,External Battery,7786,7786.00 %|01/01/2066 00:03:37,External Battery,75," \
               r"75.00 %|01/01/2066 00:03:37,External Battery,17,17.00 %|01/01/2066 00:03:37,External Battery,6," \
               r"6.00 %|01/01/2066 00:03:37,External Battery,8,8.00 %|01/01/2066 00:03:37,External Battery,8,8.00 %| "

# input_string = input('Input your External Battery Info: \n')
stripped_string = input_string.strip()
pipe_sep_strings = stripped_string.split('|')

# Delete all empty strings
pipe_sep_strings = list(filter(None, pipe_sep_strings))

# Iterate through all strings separated by pipe character (|)
for pss in pipe_sep_strings:
    comma_sep_strings = pss.split(',')
    time = comma_sep_strings[0]
    int_value = int(str(comma_sep_strings[2]))

    index = pipe_sep_strings.index(pss)

    print('{:<50} Time = {} and value = {}'.format(debug_data[index], time, int_value))

'''
01/01/1970 00:01:04,External Battery,576,576.00 %|01/01/2066 00:03:37,External Battery,0,0.00 %|01/01/2066 00:03:37,External Battery,0,0.00 %|01/01/2066 00:03:37,External Battery,0,0.00 %|01/01/2066 00:03:37,External Battery,7786,7786.00 %|01/01/2066 00:03:37,External Battery,75,75.00 %|01/01/2066 00:03:37,External Battery,17,17.00 %|01/01/2066 00:03:37,External Battery,6,6.00 %|01/01/2066 00:03:37,External Battery,8,8.00 %|01/01/2066 00:03:37,External Battery,8,8.00 %|
'''