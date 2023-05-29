
def break_into_hour_min_sec(seconds):
    hours = seconds//3600
    mins = (seconds - hours*3600)//60
    secs = (seconds - mins*60 - hours*3600)
    return hours,mins,secs


hour,min,sec = break_into_hour_min_sec(5000)

print(hour,min,sec)