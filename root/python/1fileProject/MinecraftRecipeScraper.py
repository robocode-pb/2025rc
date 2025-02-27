# pip install beautifulsoup4 pandas

from requests import get                                       # Імпортуємо бібліотеку для відправки HTTP-запитів
from bs4      import BeautifulSoup                             # Імпортуємо BeautifulSoup для парсингу HTML
from pandas   import DataFrame                                 # Імпортуємо pandas для роботи з таблицями
from json     import dump                                      # Імпортуємо json для збереження даних у файл

class MinecraftRecipeScraper:
    def __init__(self) -> None:
        self.soup       = None                                # Ініціалізуємо змінну для збереження HTML-коду сторінки
        self.data_frame = None                                # Ініціалізуємо змінну для збереження даних у форматі DataFrame

    def scrape_url(self) -> None:
        url = 'https://www.minecraftcrafting.info'            # URL-адреса сторінки з рецептами
        self.soup = BeautifulSoup(get(url).text,"html.parser")# Парсимо HTML-код сторінки

    def get_tables_data(self) -> DataFrame:
        tables  = self.soup.find_all('table')[1:]             # Знаходимо всі таблиці на сторінці, пропускаючи першу
        headers = self.soup.find_all('h2')                    # Знаходимо всі заголовки h2 (назви таблиць)
        data_tables = []                                      # Створюємо список для збереження даних

        for i, table in enumerate(tables):                    # Проходимося по всіх знайдених таблицях
            table_rows = table.find_all('tr')[1:]             # Знаходимо всі рядки, окрім заголовка
            data_tables.append({                              # Додаємо назву таблиці
                    'table_name': headers[i].text.rstrip(), 
                    'table_data': []
                })  
            
            for row in table_rows:                            # Проходимося по кожному рядку таблиці
                cells = row.find_all('td')                    # Отримуємо всі комірки рядка
                data_tables[i]['table_data'].append({         # Додаємо дані у відповідний список
                    'name': cells[0].text, 
                    'ingredients': cells[1].text,
                    'image': f"https://www.minecraftcrafting.info/{cells[2].find('img')['src']}",
                    'description': cells[3].text
                })
        
        self.data_frame = DataFrame(data_tables)              # Перетворюємо зібрані дані у DataFrame
        print(self.data_frame)
        return self.data_frame                                # Повертаємо отриману таблицю
    
    def save_to_json(self) -> None:
        if self.data_frame is not None:  return None          # Перевіряємо, чи є дані для збереження
        with open("recipes.json", 'w') as f:                  # Збереження у JSON
            dump(self.data_frame.to_dict(orient='records'), f, indent=4)
    
    def test():                                               # Приклад використання класу
        rs = MinecraftRecipeScraper()                         # Створюємо екземпляр класу
        rs.scrape_url()                                       # Завантажуємо HTML-сторінку
        rs.get_tables_data()                                  # Отримуємо дані
        rs.save_to_json()                                     # Зберігаємо дані у файл


MinecraftRecipeScraper.test()                                 # Викликаємо метод test() для демонстрації роботи класу

with open('recipes.html', 'w') as f:
    f.write('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Minecraft Recipe</title>
    <style>body{background-color:#1e1e1e;color:white;display:flex;flex-wrap:wrap;gap:20px;justify-content:center;}.recipe{background:#333;padding:15px;border-radius:8px;width:250px;}img{width:100%;}</style>
</head>
<body>
    <script>
        fetch('recipes.json')
            .then(response => response.json())
            .then(data => {
                data.forEach(table => {
                    table.table_data.forEach(recipe => {
                        const recipeElement = document.createElement('div');
                        recipeElement.classList.add('recipe');
                        recipeElement.innerHTML = `
                            <h2>${recipe.name}</h2>
                            <img src="${recipe.image}" alt="${recipe.name}">
                            <p><strong>Ingredients:</strong> ${recipe.ingredients}</p>
                            <p>${recipe.description}</p>
                        `;
                        document.body.appendChild(recipeElement);
                    });
                });
            })
            .catch(error => console.error('Error loading recipes:', error));
    </script>
</body>
</html>
    ''')
    
print('\n Відкрийте recipes.html з live server \n')