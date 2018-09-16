import datetime
import sys
import re

args = sys.argv

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

print("\n===== 90days Report Period ===== \n")
print(today, "is ...\t", repoday(now))

date_report = now + datetime.timedelta(days=90)
print("90days report date is ...\t", repoday(date_report), "\n")

date_from = now + datetime.timedelta(days=75)
print("please send report: \nfrom ...\t", repoday(date_from))

date_end = now + datetime.timedelta(days=97)
print("untill ...\t", repoday(date_end), "\n")

print("================================\n")
