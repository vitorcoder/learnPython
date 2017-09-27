import datetime
import pytz


time_zones = {'1': 'Africa/Casablanca',
              '2': 'Africa/Mogadishu',
              '3': 'America/Sao_Paulo',
              '4': 'America/Los_Angeles',
              '5': 'Asia/Tokyo',
              '6': 'Asia/Shanghai',
              '7': 'Europe/Moscow',
              '8': 'Europe/London',
              '9': 'Australia/Melbourne'
}


print("Please, choose one time zone, enter 0 to quit.")

for zone in sorted(time_zones):
    print("{} - {}".format(zone, time_zones[zone]))
    
while True:
    choice = input()
    
    if choice == '0':
        break;
        
    if choice in time_zones.keys():
        tz_to_display = pytz.timezone(time_zones[choice])
        world_time = datetime.datetime.now(tz=tz_to_display)
        print("Time in {} is {} {}".format(time_zones[choice], world_time.strftime('%A %x %X %z'), world_time.tzname()))
        print('Local time is {}'.format(datetime.datetime.now().strftime('%A %x %X %z')))
        print('UTC time is {}'.format(datetime.datetime.utcnow().strftime('%A %x %X %z')))
        