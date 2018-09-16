import datetime
import sys
import re

args = sys.argv

class R90days(datetime.datetime):
    def __init__(self, now):
        self.now = now

    def date_report(self):
        date_report = self.now + datetime.timedelta(days=90)
        return date_report
    def date_from(self):
        date_from = self.now + datetime.timedelta(days=75)
        return date_from
    def date_end(self):
        date_end = self.now + datetime.timedelta(days=97)
        return date_end

def repoday(now):
    today = now.strftime('%d/%b/%Y (%a)')
    return today

if len(args) == 2:
    pattern = r"\d{8}"
    if re.match(pattern, args[1]):
        argy = str(args[1])[:4]
        argm = str(args[1])[4:6]
        argd = str(args[1])[6:8]
        now = datetime.datetime(int(argy), int(argm), int(argd))
        today = "Entry date"
    else:
        print("90days.py: Please input date with following format, 20180907")
        sys.exit()
else:
    now = datetime.datetime.now()
    today = "Today"

re90 = R90days(now)
print(type(re90.date_report))
print(type(re90.date_from))
print(type(re90.date_end))

print("\n===== 90days Report Period ===== \n")
print(today, "is ...\t", repoday(now))

print("90days report date is ...\t", repoday(re90.date_report), "\n")

print("please send report: \nfrom ...\t", repoday(re90.date_from))

print("untill ...\t", repoday(re90.date_end), "\n")

print("================================\n")
