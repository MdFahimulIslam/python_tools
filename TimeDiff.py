from datetime import datetime

while True:

    input_command = input('Input your time calculation (eg. 11:15:49 - 10:33:26)\n')
    stripped_command = input_command.replace(' ', '')
    input_times = stripped_command.split('-')

    FMT = '%H:%M:%S'
    t_delta = datetime.strptime(input_times[0], FMT) - datetime.strptime(input_times[1], FMT)

    print(t_delta)
