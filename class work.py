import requests

url = "http://universities.hipolabs.com/search?country=Kazakhstan"
response = requests.get(url).json()

i = 0
print('Университеты Казахстана: ')
for i in range(len(response)):
    print(f'{i}.', response[i]['name'])


choice = int(input('Введите номер университета, о котором хотите узнать больше: '))

print('Домен:', response[choice]['domains'],
      'Веб-страница:', response[choice]['web_pages'],
      'Название:', response[choice]['name'])


