import requests


class QueryAPI:
    def __init__(self) -> None:
        self.code = "101010100"
        self.url = "http://www.weather.com.cn/data/sk"

    def get(self, city_code="101010100"):
        city_url = self.url + "/" + str(city_code) + ".html"
        response = requests.get(city_url)
        response.encoding = "utf-8"
        response_result = response.json()
        result = dict()
        result["城市"] = response_result["weatherinfo"]["city"]
        result["风向"] = response_result["weatherinfo"]["WD"]
        result["温度"] = response_result["weatherinfo"]["temp"]
        result["风力"] = response_result["weatherinfo"]["WS"]
        result["湿度"] = response_result["weatherinfo"]["SD"]
        return result
    


if __name__ == "__main__":
    weather = QueryAPI()
    city_code = "101010100"
    re = weather.get(city_code)
    for key,value in re.items():
        print(key,value)
