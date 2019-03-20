import requests  

id = "84600bca7507293656495e8972aec659"
endpoint = "http://api.openweathermap.org/data.2.5/weather"

def query_weather(city):
    pd = {'q': city, 'units':'metric', 'appid':id}
    endpoint = "http://api.openweathermap.org/data/2.5/weather"
    response = requests.get(endpoint, params=pd)
    return jsonify(response)['main']['temp']

#response1 = query_weather(pd)
#if response1.status_code == 200:
    #print(response1.text)
#else:
  #  response1 = query_weather(pd)

#print(response.url)
#print(response.status_code)
#print(response.text)

def jsonify(response):
    json_response = response.json()
    return json_response

print("The temperature in {} is {}".format('London', query_weather('London')))

#json_response1 = jsonify(response1)
#print("\n")
#print(json_response1)

#print(json_response1['main']['temp'])