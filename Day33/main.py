import requests
from datetime import datetime

MY_LAT = 32.085300
MY_LONG = 34.781769


def is_iss_overhead():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()["iss_position"]
    longtitude = float(data["longitude"])
    latitude = float(data["latitude"])

    iss = longtitude,latitude

    if MY_LAT - 5 <= longtitude <= MY_LAT +5 and MY_LONG - 5 <= longtitude <= MY_LONG +5:
        return True
    return False

def is_night():
    parameters = {
        "lat" : MY_LAT,
        "lng" : MY_LONG,
        "formatted" : 0
    }


    response =  requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()

    data = response.json()["results"]

    sunrise = int(data["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    
    if time_now >= sunset or time_now <= sunrise:
        return True
    
    return False


def main():
    if is_iss_overhead() and is_night():
        print("iss is just over your head and surely it's dark now")
    
    else:
        print("casual")


if __name__ == "__main__":
    main()