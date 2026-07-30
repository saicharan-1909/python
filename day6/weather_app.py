# import requests

# url = "https://jsonplaceholder.typicode.com/users/1"

# response = requests.get(url)

# print("Status Code:", response.status_code)
# print(response.text)


# import requests

# url = "https://jsonplaceholder.typicode.com/users/1"

# response = requests.get(url)

# data = response.json()

# print("Name:", data["name"])
# print("Username:", data["username"])
# print("Email:", data["email"])
# print("Phone:", data["phone"])
# print("Website:", data["website"])
# print("Company:", data["company"]["name"])
# print("City:", data["address"]["city"])
# print("Zip Code:", data["address"]["zipcode"])


import requests
city = input("Enter City Name: ")
url = f"https://wttr.in/{city}?format=j1"
try:
  response = requests.get(url)
  data = response.json()

  current = data["current_condition"][0]

  temperature = current["temp_C"]
  humidity = current["humidity"]
  wind_speed = current["windspeedKmph"]
  condition = current["weatherDesc"][0]["value"]

  print("\n======= Weather Report =======")
  print("City:", city)
  print("Condition:", condition)
  print("Temperature:", temperature, "°C")
  print("Humidity:", humidity, "%")
  print("Wind Speed:", wind_speed, "km/h")

except Exception as e:
    print("Something went wrong:", e)