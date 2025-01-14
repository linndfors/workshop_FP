import csv

def create_file(dict_goals):
    '''
    Create a csv-file with information about goals on day
    >>> print(create_file({'Eat': 3}))
    None
    '''
    data = []
    header = ['Days', 'Numbers', 'Success', 'Failure']
    for goal in dict_goals.keys():
        element = [goal, '0', '', '']
        data.append(element)
    
    with open('tracker.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data)

def write_in_file(d1, d2):
    '''
    Compare how many times you make it and how many you should
    '''
    for key in d1:
        with open('tracker.csv', 'a') as file:
            content=file.readlines()
            if d1[key] == d2[key]:
                for line in content:
                    if line[0] == key:
                        line[2] = '*'
            else:
                for line in file:
                    if line[0] == key:
                        line[3] = '*'

def get_info(get_file):
    '''
    Ask how many times you do your goals today
    '''
    with open(get_file,'r') as track_file:
        plans=track_file.readlines()
        new_dict_goals={}
        new_plans_lst=[]
        for line in plans:
            line=line.replace('\n','')
            new_line=line.split(',')
            new_plans_lst.append(new_line)
    new_plans_lst.pop(0)
    for x in range(len(new_plans_lst)):
        goal=new_plans_lst[x][0]
        answer=int(input(f'{goal}. Do you do this task? If yes print "1" \n'))
        if answer==1:
            if new_dict_goals.get(goal):
                new_dict_goals[goal]+=1
            else:
                new_dict_goals[goal]=1
    return new_dict_goals

def set_goals():
    '''
    Ask for goals for today
    '''
    goals_dict={}
    while True:
        goal=input("Set your goal for today:\n")
        times=int(input("How many time you should do it:\n"))
        goals_dict[goal]=times
        choise=input('Write "end" to quit or "add" to add a new goal:\n')
        if choise=="end":
            break
    create_file(goals_dict)
    return goals_dict

dict_of_goals=set_goals()
# create_file(dict_of_goals)
goals_dict=get_info('tracker.csv')
write_in_file(dict_of_goals,goals_dict)
