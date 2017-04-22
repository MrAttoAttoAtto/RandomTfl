import requests
import time
stopId = '490003688E'
def getTimeToNextBus():
    r = requests.get(r'https://api.tfl.gov.uk/StopPoint/' + stopId + r'/arrivals')
    json_result = r.json()
    secsFromStop = []
    for x in json_result:
        secsFromStop.append(x['timeToStation'])
    secsFromStop.sort()
    ans = str(secsFromStop[0]) + ' seconds to bus on ' + str(time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime()))
    print(json_result)
    print(ans)
    return ans
while True:
    value = getTimeToNextBus()
    with open('TFL Data.txt', 'a') as text_file:
        text_file.write(value + '\n')
    time.sleep(300)
    
    
