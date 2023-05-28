from abc import ABC, abstractmethod
from datetime import datetime

# Абстрактный класс для создания расписания
class Schedule(ABC):
    @abstractmethod
    def get_weekly_schedule(self):
        pass

    def get_today_schedule(self):
        today = datetime.now().strftime("%A").lower()
        schedule = self.get_weekly_schedule()
        if today in schedule:
            return schedule[today]
        else:
            return "Выходной"

# Конкретный класс для создания расписания на учебную неделю
class SchoolSchedule(Schedule):
    def get_weekly_schedule(self):
        return {
            "monday": "Выходной, но обрати внимание на домашку",
            "tuesday": "14:20 Корягин, Серов",
            "wednesday": "14:20 Захарчук",
            "thursday": "Смирнов, Шатовкин",
            "friday": "Военная кафедра",
            "saturday":"Лесько МАД ТМП"
        }

# Конкретный класс для создания расписания на рабочую неделю
class WorkSchedule(Schedule):
    def get_weekly_schedule(self):
        return {
            "monday": "1 ДЗ Корягина, 5-6 Серова",
            "tuesday": "2 ДЗ Корягина",
            "wednesday": "Шатовкин ДЗ",
            "thursday": "ТМП 4,5",
            "friday": "Доделать что нужно",
            "saturday":"ТМП 6"
        }

# Пример использования
print("1 - Расписание на сегодня, 2 - Расписание на неделю")
n = int(input())
if n ==1:
    school_schedule = SchoolSchedule()
    print("Расписание пар:")
    print(school_schedule.get_today_schedule())

    work_schedule = WorkSchedule()
    print("\nРасписание домашки:")
    print(work_schedule.get_today_schedule())
else:
    school_schedule = SchoolSchedule()
    print("Расписание пар:")
    print(school_schedule.get_weekly_schedule())

    work_schedule = WorkSchedule()
    print("\nРасписание домашки:")
    print(work_schedule.get_weekly_schedule())