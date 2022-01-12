import datetime as dt
import requests
import json
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

api_key = "your API key here"

mylat = your latitude here
mylon = your longitude here
myurl =  "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=imperial" % (mylat, mylon, api_key)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []

# This function is called periodically from FuncAnimation
def animate(i, xs, ys):
    myResponse = requests.get(myurl)
    myData = json.loads(myResponse.text)
    myCurrent = myData["current"]["temp"]

    # Read temperature (Celsius) from TMP102
    myTemp = round(myCurrent, 2)

    # Add x and y to lists
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(myTemp)

    # Limit x and y lists to 20 items
    xs = xs[-100:]
    ys = ys[-100:]

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys, label = "Current Temp")

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Temp over Time')
    plt.ylabel('Temperature (°F)')
    plt.legend()

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)
plt.show()
