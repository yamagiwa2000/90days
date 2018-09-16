import datetime
import sys
import re

args = sys.argv

def r90days(now, stage):
    if stage == "report":
        date_report = now + datetime.timedelta(days=90)
        return date_report
    elif stage == "from":
        date_from = now + datetime.timedelta(days=75)
        return date_from
    elif stage == "end":
        date_end = now + datetime.timedelta(days=97)
        return date_end

def repoday(now):
    today = now.strftime('%d/%b/%Y (%a)')
    return today

if __name__ == "__main__":
    if len(args) == 2:
        pattern = r"\d{8}$"
        if re.match(pattern, args[1]):
            argy = str(args[1])[:4]
            argm = str(args[1])[4:6]
            argd = str(args[1])[6:8]
            now = datetime.datetime(int(argy), int(argm), int(argd))
            today = "Entry date"
        else:
            print("90days.py: Please input date with following format, yyyymmdd ex) 20180909")
            sys.exit()
    else:
        now = datetime.datetime.now()
        today = "Today"

    print("\n===== 90days Report Period ===== \n")
    print(today, "is ...\t", repoday(now))

    print("90days report date is ...\t", repoday(r90days(now, "report")), "\n")

    print("please send report: \nfrom ...\t", repoday(r90days(now, "from")))

    print("untill ...\t", repoday(r90days(now, "end")), "\n")

    print("================================\n")
