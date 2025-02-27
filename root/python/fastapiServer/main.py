# python -m uvicorn main:app --reload
import sqlite3
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

def commite(command, *args):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute(command, args)
    conn.commit()
    data = c.fetchall()
    conn.close()
    return data

commite("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    image_url TEXT NOT NULL,
    price REAL NOT NULL
)
""")

class Item(BaseModel):
    id: int = None
    name: str
    price: int
    image_url: str

app = FastAPI()

@app.get("/")
def root():
    return "Hello world"

@app.get("/items")
def GET_items():
    items = commite("SELECT id, name, price, image_url FROM products")
    data: List[Item] = []
    for item in items:
        data.append({
            "id": item[0],
            "name": item[1],
            "price": item[2],
            "image_url": item[3]
        })
    return data

@app.get("/items/{item_id}")
def GET_item(item_id: int) -> Item:
    item = commite("SELECT id, name, price, image_url FROM products WHERE id = ?", item_id)
    if item:
        return {
            "id": item[0][0],  # Accessing the first element from the result tuple
            "name": item[0][1],
            "price": item[0][2],
            "image_url": item[0][3]
        }
    return {"message": "Item not found"}



# @app.post("/items")
# def post_items(item: Item):
#     conn = sqlite3.connect("database.db")
#     cursor = conn.cursor()

#     cursor.execute("INSERT INTO products (name, price, image_url) VALUES (?, ?, ?)", 
#                    (item.name, item.price, item.image_url))
#     conn.commit()
#     conn.close()
#     return {"image_url":item.image_url "name": item.name, "price": item.price}


# @app.post("/items")
# def post_items(item: Item):
#     i_id = items[-1]['id'] + 1
#     if  item.id:
#         i_id=  item.id

#     items.append(
#         {"id":i_id, "name":item.name, "price":item.price}
#     )
#     return items[-1]



# Sait_Wikibogdan


# Навіщо створювати АРІ? 
# Які є переваги FastAPI? 
# простий фреймворк для створення серверу з автоматичною документацыэю та тестовою сторiнкою
# Як розшифровується АРІ? 
# Aplication Program Interface - мова спiлкування додаткiв / програм
# Що таке endpoint? 
# URL адреса для спiлкування клiэнта-сервера
# У чому різниця GET та POST?
# get отримання iнформацiйi а POST для вiдправки 
# Що таке документація?
# Документація в Python — це набір інструкцій, описів та коментарів, що пояснюють, як використовувати певні частини коду, бібліотеки чи модулі. Вона допомагає програмістам зрозуміти, як працює конкретний код, що він робить і як ним користуватися. Документація може бути:
