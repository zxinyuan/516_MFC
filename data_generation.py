import numpy as np
import pickle
import random
import string
import datetime


'''
local data schema: 
students: student_id (PK), age, first_name, last_name
healthcenters: center_id (PK), location_id
activity: actitvity_id (PK), location_id, date
participation: participation_id (PK), activity_id, student_id
location: location_id (PK), address, city
testlog: test_id (PK), result, date, student_id
vaccination: brand_id (PK)
vaccinationhistory: history_id (PK), brand_id, student_id, dose_number, date
'''

        
def read_name_from_txt():
    firstname = []
    surname = []
    with open('./name.txt', 'r') as f:
        line = f.readlines()
        num = 0
        for i in line:
            i = i.replace('\n', '')
            firstname.append(i)
            num += 1
        print('number of first name in the list: {}'.format(num))
    with open('./surname.txt', 'r') as f:
        line = f.readlines()
        num = 0
        for i in line:
            i = i.replace('\n', '')
            surname.append(i)
            num += 1
        print('number of last name in the list: {}'.format(num))
    return firstname, surname


def generate_random_date():
    start_date = datetime.date(2022, 1, 1)
    end_date = datetime.date(2022, 4, 5)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)

    return random_date


def generate_data_students(num):
    '''
    students: student_id (PK), age, first_name, last_name
    '''
    students = []
    firstname_list, surname_list = read_name_from_txt()
    letters = string.digits
    
    for i in range(num):
        student = {}
        student['student_id'] = '0' * (7 - len(str(i))) + str(i)
        student['age'] = random.sample(list(range(18, 30)), 1)[0]
        student['first_name'] = random.sample(firstname_list, 1)[0]
        student['last_name'] = random.sample(surname_list, 1)[0]
        students.append(student)
        print(student)
    with open('./students.pickle', 'wb') as f:
        pickle.dump(students, f)

    print('==> finished students data generation.')


def generate_data_location(num):
    '''
    location: location_id (PK), address, city
    '''
    locations = []
    letters = string.digits
    
    for i in range(num):
        location = {}
        location['location_id'] = '0' * (9 - len(str(i))) + str(i)
        location['address'] = 'Duke University Campus'
        location['city'] = 'Durham'
        locations.append(location)
        print(location)
    with open('./locations.pickle', 'wb') as f:
        pickle.dump(locations, f)

    print('==> finished location data generation.')


def generate_data_healthcenters(num):
    '''
    healthcenters: center_id (PK), location_id
    num: 1000 max
    '''
    healthcenters = []
    letters = string.digits
    
    for i in range(num):
        healthcenter = {}
        healthcenter['center_id'] = '0' * (3 - len(str(i))) + str(i)
        healthcenter['location_id'] = '0' * 6 + ''.join(random.choice(letters) for i in range(3))
        healthcenters.append(healthcenter)
        print(healthcenter)
    with open('./healthcenters.pickle', 'wb') as f:
        pickle.dump(healthcenters, f)

    print('==> finished healthcenters data generation.')


def generate_data_activity(num):
    '''
    activity: actitvity_id (PK), location_id, date
    '''
    activitys = []
    letters = string.digits
    
    for i in range(num):
        activity = {}
        activity['activity_id'] = '0' * (5 - len(str(i))) + str(i)
        activity['location_id'] = '0' * 6 + ''.join(random.choice(letters) for i in range(3))
        activity['date'] = generate_random_date()
        activitys.append(activity)
        print(activity)
    with open('./activitys.pickle', 'wb') as f:
        pickle.dump(activitys, f)

    print('==> finished activity data generation.')


def generate_data_participation(num):
    '''
    participation: participation_id (PK), activity_id, student_id
    '''
    participations = []
    letters = string.digits
    
    for i in range(num):
        participation = {}
        participation['participation_id'] = '0' * (9 - len(str(i))) + str(i)
        participation['activity_id'] = '0' * 2 + ''.join(random.choice(letters) for i in range(3))
        participation['student_id'] = '0' * 3 + ''.join(random.choice(letters) for i in range(4))
        participations.append(participation)
        print(participation)
    with open('./participations.pickle', 'wb') as f:
        pickle.dump(participations, f)

    print('==> finished participation data generation.')


def generate_data_testlog(num):
    '''
    testlog: test_id (PK), result, date, student_id
    '''
    testlogs = []
    letters = string.digits
    
    for i in range(num):
        testlog = {}
        testlog['test_id'] = '0' * (9 - len(str(i))) + str(i)
        if random.uniform(0, 1) > 0.9:
            testlog['result'] = True
        else:
            testlog['result'] = False
        testlog['date'] = generate_random_date()
        testlog['student_id'] = '0' * 3 + ''.join(random.choice(letters) for i in range(4))
        testlogs.append(testlog)
        print(testlog)
    with open('./testlogs.pickle', 'wb') as f:
        pickle.dump(testlogs, f)

    print('==> finished testlog data generation.')


def generate_data_vaccination(num):
    '''
    vaccination: brand_id (PK)
    '''
    vaccinations = []
    letters = string.digits
    
    for i in range(num):
        vaccination = {}
        vaccination['brand_id'] = '0' * (5 - len(str(i))) + str(i)
        vaccinations.append(vaccination)
        print(vaccination)
    with open('./vaccinations.pickle', 'wb') as f:
        pickle.dump(vaccinations, f)

    print('==> finished vaccination data generation.')


def generate_data_vaccinationhistory(num):
    '''
    vaccinationhistory: history_id (PK), brand_id, student_id, dose_number, date
    '''
    vaccinationhistorys = []
    letters = string.digits
    
    for i in range(num):
        vaccinationhistory = {}
        vaccinationhistory['history_id'] = '0' * (9 - len(str(i))) + str(i)
        vaccinationhistory['brand_id'] = '0' * 2 + ''.join(random.choice(letters) for i in range(3))
        vaccinationhistory['student_id'] = '0' * 3 + ''.join(random.choice(letters) for i in range(4))
        vaccinationhistory['dose_number'] = random.sample(list(range(1, 4)), 1)[0]
        vaccinationhistory['date'] = generate_random_date()
        vaccinationhistorys.append(vaccinationhistory)
        print(vaccinationhistory)
    with open('./vaccinationhistorys.pickle', 'wb') as f:
        pickle.dump(vaccinationhistorys, f)

    print('==> finished vaccinationhistory data generation.')


if __name__ == '__main__':

    print('==> data generation')

    generate_data_students(10000)
    
    generate_data_activity(1000)

    generate_data_healthcenters(1000)

    generate_data_location(1000)

    generate_data_participation(2000)

    generate_data_testlog(20000)

    generate_data_vaccination(1000)

    generate_data_vaccinationhistory(10000)

    print('==> finished.')