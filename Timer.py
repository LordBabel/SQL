time = int(input("Enter a time in seconds: "))
hours = time // 3600
minutes = (time-hours*3600)//60
seconds = time-(hours*3600+minutes*60)

for x in range(time):
    print(hours, "hours", minutes, "minutes and", seconds, "seconds.")
    if seconds == 0:
        if hours == 0:
            if minutes == 0:
                print("Your time is up!")
                break
        minutes -= 1
        seconds = 59
        if minutes == 0:
            if hours != 0:
                hours -= 1
                minutes = 59
                seconds = 59
    if minutes == 0:
        minutes = 59
        hours -= 1
    if hours == 0:
        minutes -= 1
    seconds -= 1
    