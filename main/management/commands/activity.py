import datetime
import random

from django.core.management.base import BaseCommand

from main.models import UserActivityPeriod


class Command(BaseCommand):
    help = "Save randomly generated stock record values."

    ### Get random start date and time...
    def start_date(self):
        # Naively generating a random date
        day = random.randint(1, 28)
        month = random.randint(1, 12)
        year = random.randint(2014, 2016)
        time = random.randint(1,23)
        second = random.randint(0,59)
        s1 = random.randint(0,59)
        m1 = random.randint(1,342380)
        return datetime.datetime(year, month, day, time, second,s1,m1)
    ### Get random end date and time
    def end_date(self):
        day = random.randint(1, 28)
        month = random.randint(1, 12)
        year = random.randint(2017, 2020)
        time = random.randint(1,23)
        second = random.randint(0,59)
        s1 = random.randint(0,59)
        m1 = random.randint(1,342380)
        return datetime.datetime(year, month, day, time, second,s1,m1)

    def handle(self, *args, **options):
        records = []
        #List of timezones...
        timeZoneList = ["Asia/Kolkata","America/Los_Angeles","Pacific/Pitcairn","Antarctica/Mawson","Pacific/Saipan"]
        #List of names ...
        nameList = ["Shubhi","Shubhra","Surbhi","Abhishek","Shagun"]
        for _ in range(100):
            kwargs = {
                'real_name':random.choice(nameList),
                'tz':random.choice(timeZoneList),
                'start_time': self.start_date(),
                'end_time':self.end_date(),
            }
            record = UserActivityPeriod(**kwargs)
            records.append(record)
        UserActivityPeriod.objects.bulk_create(records)
        self.stdout.write(self.style.SUCCESS('Records saved successfully.'))