import requests


def ip_checker(ip):
    if ip == "127.0.0.1":
        final_str = """
ISP: Local IP
City Lat/Lon: (0) / (0)
        """
        return final_str
    response = requests.get("http://ip-api.com/json/" + ip)
    if response.status_code == 200:
        json = response.json()
        final_str = f"""ISP: {json['isp']}
City Lat/Lon: ({json['lat']}) / ({json['lon']})"""
        return final_str
