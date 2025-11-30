import requests
import math
from datetime import datetime, timezone

import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("AMENTUM_API_KEY")

LAT = -25.55
LON = -48.30

now = datetime.now(timezone.utc)
YEAR = now.year
MONTH = now.month
DAY = now.day
HOUR = now.hour

HEADERS = {
    "Accept": "application/json",
    "API-Key": API_KEY
}

def request_api(variable):
    url = "https://ocean.amentum.io/nemo/phys"

    params = {
        "latitude": LAT,
        "longitude": LON,
        "year": YEAR,
        "month": MONTH,
        "day": DAY,
        "hour": HOUR,
        "depth": 0,
        "variable": variable
    }

    print("\n============== REQUEST ==============")
    print("Variable:", variable)
    print("Params:", params)

    response = requests.get(url, headers=HEADERS, params=params)
    print("Status:", response.status_code)
    print("\nRAW JSON:\n", response.text)

    if response.status_code == 200:
        return response.json()
    return None


if __name__ == "__main__":
    print("Data/Hora:", now.strftime("%Y-%m-%d %H:%M:%S"))

    temp = request_api("thetao")
    sal = request_api("so")
    u = request_api("uo")
    v = request_api("vo")
    level = request_api("zos")

    # Cálculo velocidade e direção da corrente
    if u and v:
        uval = u.get("value", 0)
        vval = v.get("value", 0)
        speed = math.sqrt(uval*uval + vval*vval)
        direction = math.degrees(math.atan2(vval, uval))
        print("\nSPEED (m/s):", speed)
        print("DIRECTION (°):", direction)
