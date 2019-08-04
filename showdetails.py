'''
performances = {'Ventriloquism':       '9:00am',
                'Snake Charmer':       '12:00pm',
                'Amazing Acrobatics':  '2:00pm',
                'Enchanted Elephants': '5:00pm'}
schedule_file = open('schedule.txt', 'w')

for key, val in performances.items():
    schedule_file.write(key + ' - ' + val + '\n')

schedule_file.close()

schedule_file = open('schedule.txt', 'r')
show_time = []
for line in schedule_file:
    line = line.split('-') 
    show_time.append(line) 
    print(line)
schedule_file.close()


schedule_file = open('schedule.txt', 'r')
for line in schedule_file:
    (show, time) = line.split(' - ')
    print(show, time)
schedule_file.close()
'''
raw_file = r'C:\git\mydevops\specs\csaha-test.txt'

readfile = open(raw_file, 'r')

for line in readfile:
    print(line.strip())

readfile.close()