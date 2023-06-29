from datetime import datetime, timedelta
from faker import Faker
from faker.providers import profile
from collections import defaultdict


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


def get_birthdays_per_week(*args) -> list:
    next = ''
    mond = ''
    curerent_day = datetime.now()
    args = get_random_users()
    for kee in args:
        for key, value in kee.items():
            if key == 'birthdate':
                if value.weekday() != 5 and value.weekday() != 6:
                    td = timedelta(weeks=1)
                    next_week = curerent_day + td
                    happy = datetime.strftime(next_week, '%A')
                    if not next:
                        x = f"{happy} : {kee['name']}"
                        next += x
                    else:
                        next += f', {kee["name"]}'

                else:
                    mon = datetime(year=2023, day=3, month=7)
                    # td1 = datetime.weekday(mon)
                    happy_day = datetime.strftime(mon, '%A')
                    if not mond:
                        x = f"{happy_day} : {kee['name']}"
                        mond += x
                    else:
                        mond += f', {kee["name"]}'
            else:
                continue
    print(next)
    print(mond)


get_birthdays_per_week()
