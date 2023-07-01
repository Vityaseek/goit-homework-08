from datetime import datetime, timedelta
from faker import Faker
from faker.providers import profile
from collections import defaultdict

list1 = [{"name": "Bill", "birthdate": '01.07.2023'}, {"name": 'Jill', "birthdate": "02.07.2023"},
         {"name": 'Petr', "birthdate": '03.07.2023'}, {"name": 'Petroo', "birthdate": '04.07.2023'}, {
             "name": 'Lisa', "birthdate": '05.07.2023'},
         {"name": 'Kisa', "birthdate": '06.07.2023'}, {
             "name": 'Visa', "birthdate": '07.07.2023'},
         {"name": 'Bisa', "birthdate": '08.07.2023'}]


def get_random_users() -> list:
    list1 = []
    my_dict = {}
    for i in range(10):
        fake = Faker()
        fake.add_provider(profile)
        proof = fake.profile()
        my_dict["name"] = proof["name"]
        my_dict['birthdate'] = proof['birthdate']
        my_dict2 = my_dict.copy()
        list1.append(my_dict2)
    return list1


def get_birthdays_per_week(*args):
    days_of_week = defaultdict(list)
    curerent_day = datetime.now()
    for kee in args:
        for key in kee:
            for name, birth in key.items():
                if name == 'birthdate':
                    birth = datetime.strptime(birth, '%d.%m.%Y')
                    if curerent_day.month == birth.month:
                        td = timedelta(weeks=1)
                        next_week = curerent_day + td
                        if birth.day >= curerent_day.day and birth.day <= next_week.day:
                            if birth.weekday() == 5:
                                td = timedelta(days=2)
                                monday = td + birth
                                happy = datetime.strftime(monday, '%A')
                                days_of_week[happy].append(key["name"])
                            elif birth.weekday() == 6:
                                td = timedelta(days=1)
                                monday = td + birth
                                happy = datetime.strftime(monday, '%A')
                                days_of_week[happy].append(key["name"])
                            elif birth.weekday() <= 4:
                                happy = datetime.strftime(birth, "%A")
                                days_of_week[happy].append(key["name"])
            else:
                continue
    print(days_of_week)


if __name__ == '__main__':
    get_birthdays_per_week(list1)
