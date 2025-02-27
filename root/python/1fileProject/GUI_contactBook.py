# pip install customtkinter CTkListbox
from customtkinter import *
from CTkListbox import *
import json


def save_contacts():
    with open('contacts.json', 'w') as f:
        json.dump(contacts, f, indent=4)

def read_contacts():
    try:
        with open('contacts.json', 'r') as f:
            return json.loads(f.read())
    except FileNotFoundError:
        save_contacts()
        return []

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    
    if not (name and phone): return

    contact = {"Name": name, "Phone": phone}
    contacts.append(contact)
    update_contact_list()
    clear_entries()
    save_contacts()

def delete_contact():
    selected_contact = contact_listbox.curselection()

    if not selected_contact: return

    index = selected_contact[0]
    contacts.pop(index)
    update_contact_list()
    save_contacts()

def clear_entries():
    name_entry.delete(0, END)
    phone_entry.delete(0, END)

def update_contact_list():
    contact_listbox.delete(0, END)
    for i, contact in enumerate(contacts):
        contact_listbox.insert(END, f'{i+1}: {contact["Name"]} - {contact["Phone"]}')



contacts = []

root = CTk()
root.title("Contact Book")
root.geometry("300x400")

contact_listbox = CTkListbox(root, height=10, width=40)
contact_listbox.pack(fill="both", expand=True, padx=10, pady=10)

delete_button = CTkButton(root, text="Delete", command=delete_contact)
delete_button.pack()


name_label = CTkLabel(root, text="Name")
name_label.pack()
name_entry = CTkEntry(root)
name_entry.pack()

phone_label = CTkLabel(root, text="Phone Number")
phone_label.pack()
phone_entry = CTkEntry(root)
phone_entry.pack()

add_button = CTkButton(root, text="Add to Contacts", command=add_contact)
add_button.pack(pady=10)

def switch_theme():
    current_theme = get_appearance_mode()
    if current_theme == "Light":
        set_appearance_mode("Dark")
    else:
        set_appearance_mode("Light")

theme_button = CTkButton(root, text="Switch Theme", command=switch_theme)
theme_button.pack(pady=10)


contacts = read_contacts()
update_contact_list()
# Запуск головного циклу додатка
root.mainloop()
