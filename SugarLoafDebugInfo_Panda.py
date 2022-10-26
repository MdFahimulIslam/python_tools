from pandas.core import frame as fr

description = ['Number of previous msg sent to server',
               'Total bytes of previous msg sent to server',
               'Number of stored light sensor data',
               'Light sensor marker',
               'Number of error occurred',
               'Error marker',
               'Stored temperature point number',
               'Temperature marker',
               'Number of temperature data sent to server',
               'Unknown']

'''
Test string :
01/01/1970 00:01:04,External Battery,576,576.00 %|01/01/2066 00:03:37,External Battery,0,0.00 %|01/01/2066 00:03:37,External Battery,0,0.00 %|01/01/2066 00:03:37,External Battery,0,0.00 %|01/01/2066 00:03:37,External Battery,7786,7786.00 %|01/01/2066 00:03:37,External Battery,75,75.00 %|01/01/2066 00:03:37,External Battery,17,17.00 %|01/01/2066 00:03:37,External Battery,6,6.00 %|01/01/2066 00:03:37,External Battery,8,8.00 %|01/01/2066 00:03:37,External Battery,8,8.00 %|
'''
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
data = []
for i in range(len(pipe_sep_strings)):
    pipe_sep_string = pipe_sep_strings[i]
    comma_sep_strings = pipe_sep_string.split(',')
    time = comma_sep_strings[0]
    value = int(str(comma_sep_strings[2]))
    data.append([description[i], time, value])

headers = ["Description", "Time", "Value"]
print(fr.DataFrame(data, None, headers))
