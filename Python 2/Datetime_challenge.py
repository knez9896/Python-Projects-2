import datetime


now_utc = datetime.datetime.utcnow()


portland_offset = -7  
nyc_offset = -4      
london_offset = 0    


portland_time = now_utc + datetime.timedelta(hours=portland_offset)
nyc_time = now_utc + datetime.timedelta(hours=nyc_offset)
london_time = now_utc + datetime.timedelta(hours=london_offset)


opening_hour = 9
closing_hour = 17


def is_open(branch_time):
    if opening_hour <= branch_time.hour < closing_hour:
        return "Open"
    else:
        return "Closed"


print("Portland branch is", is_open(portland_time), "- Current time:", portland_time.strftime("%Y-%m-%d %H:%M:%S"))
print("New York City branch is", is_open(nyc_time), "- Current time:", nyc_time.strftime("%Y-%m-%d %H:%M:%S"))
print("London branch is", is_open(london_time), "- Current time:", london_time.strftime("%Y-%m-%d %H:%M:%S"))
