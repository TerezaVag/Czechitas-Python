import requests
# cast 1
#22834958
subject = int(input("Zadej IČO subjektu: "))
response = requests.get("https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/" + str(subject))
responseJson = response.json()
print(responseJson["obchodniJmeno"])
print(responseJson["sidlo"]["textovaAdresa"])

# cast 2
name = input("Zadej nazev subjektu: ")
url = "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat"
headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}
data = '{"obchodniJmeno":"' + name + '"}'
postResponse = requests.post(url, headers=headers, data=data).json()
print(postResponse["pocetCelkem"])
for value in postResponse["ekonomickeSubjekty"]:
  print(value["obchodniJmeno"] + ", " + value["ico"])
