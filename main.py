from datetime import datetime as dt


class biomedRecords():
    from datetime import datetime as dt
    days_of_week = ['monday', 'tuesday', 'wednesday',
                    'thursday', 'friday', 'saturday', 'sunday']
    weekday = days_of_week[:4]
    weekend = days_of_week[-2:]
    call_rates = [39, 45, 55]
    std_days_leave = 29
    basic_salary_scale = [34774, 36198, 38463, 39535, 40556, 42969, 44530,
                          46106, 47708, 49308, 50913, 52546, 54190, 55853, 57469, 58580]

    def __init__(self, name: str):
        self.name = name.capitalize()

    def serviceTime(self, start_date, end_date=dt.now()):
        self.start_date = start_date
        self.end_date = end_date
        delta = end_date - start_date
        return delta

    def jobTitle(self, title):
        self.title = title.capitalize()
        words = title.split()
        if 'Basic' in words:
            self.basicGrade, self.seniorGrade = True, False
        else:
            self.basicGrade, self.seniorGrade = False, True

    def jobGrade(self, grade: int):
        assert grade <= len(
            biomedRecords.basic_salary_scale), f'Grade cannot be more than {len(biomedRecords.basic_salary_scale)}'
        self.grade = grade

    def hoursPerWeek(self, hrs_Week):
        self.hours_Week = hrs_Week
        self.fract_of_full_time = hrs_Week/35
        if self.fract_of_full_time == 1:
            self.full_time = True
        else:
            self.full_time = False

    def salary(self):
        lim = 35000
        if self.full_time:
            grossYearlySalary = biomedRecords.basic_salary_scale[(
                self.grade-1)]

        else:
            grossYearlySalary = (self.fract_of_full_time *
                                 biomedRecords.basic_salary_scale[(self.grade-1)])

        if grossYearlySalary < lim:
            netYearlySalary = (grossYearlySalary*0.8)

        else:
            diff = grossYearlySalary - lim
            netYearlySalary = (grossYearlySalary*0.8) + (diff*0.6)

        return grossYearlySalary, netYearlySalary

    def call_pre(self, days: list, hrs: list):
        self.days = days
        self.hrs = hrs

        call_hrs = dict(zip(days, hrs))

        days = [i.lower() for i in days]
        self.pre_total = 0

        for i, j in call_hrs.items():
            if i in biomedRecords.weekday:
                self.pre_total += (j*biomedRecords.call_rates[0])
            else:
                self.pre_total += (j*biomedRecords.call_rates[1])
        return self.pre_total

    def call_post(self, days: list, hrs: list):
        self.days = days
        self.hrs = hrs

        call_hrs = dict(zip(days, hrs))

        days = [i.lower() for i in days]
        self.post_total = 0

        for i, j in call_hrs.items():
            if i in biomedRecords.weekend:
                self.post_total += (j*biomedRecords.call_rates[1])
            else:
                self.post_total += (j*biomedRecords.call_rates[2])
        return self.post_total

    def total(self):
        print(
            f'{self.name} has made a total of €{(self.pre_total + self.post_total):,} on call')

    def days_leave(self):
        if self.full_time:
            no_of_days = biomedRecords.std_days_leave
        else:
            no_of_days *= self.fract_of_full_time
        return no_of_days


employee1 = biomedRecords('brvgha')
print(employee1.serviceTime(start_date=dt(2021, 9, 21)))
employee1.jobTitle('Basic Grade Medical Scientist')
employee1.jobGrade(4)
employee1.hoursPerWeek(35)


test = employee1.call_pre(
    days=['monday', 'tuesday', 'saturday'], hrs=[4, 4, 8])

test1 = employee1.call_post(
    days=['wednesday', 'thursday', 'sunday'], hrs=[8, 8, 8])
salary = employee1.salary()
