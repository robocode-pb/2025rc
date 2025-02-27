# pip install -U g4f[all]
from g4f.client import Client 
client = Client() 

history = []
def chat(massage, useHistory=False):
    massage =[{"role": "user", "content": massage}]
    if useHistory:
        history.append(massage[0])
        massage = history
    print(f'\nAsk GPT : {massage[-1]['content']}\n Answer : ', end='')
    ai_response = client.chat.completions.create( 
            model="gpt-3.5-turbo", 
            messages=massage
        ).choices[0].message.content 
    print(ai_response)
    return ai_response


chat("Привіт як справи?")

while True:
    chat(input("\nЗапит  : "), useHistory=True)
