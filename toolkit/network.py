import json
import urllib.request
from toolkit.utils import Color, slow_print

def network_info():
    try:
        slow_print(Color.CYAN + "\nFetching IP & Location info...\n")

        url = "http://ip-api.com/json/"
        response = urllib.request.urlopen(url, timeout=10)
        data = json.loads(response.read().decode())

        if data["status"] != "success":
            print(Color.RED + "Failed to fetch network info")
            return

        print(Color.GREEN + "🌐 Network Information\n")
        print(Color.YELLOW + f"IP Address   : {data['query']}")
        print(Color.YELLOW + f"Country      : {data['country']}")
        print(Color.YELLOW + f"Region       : {data['regionName']}")
        print(Color.YELLOW + f"City         : {data['city']}")
        print(Color.YELLOW + f"ISP          : {data['isp']}")
        print(Color.YELLOW + f"Timezone     : {data['timezone']}")
        print(Color.YELLOW + f"Latitude     : {data['lat']}")
        print(Color.YELLOW + f"Longitude    : {data['lon']}")
        print(Color.RESET)

        input(Color.CYAN + "Press Enter to return to menu...")

    except Exception as e:
        print(Color.RED + f"Error: {e}")
