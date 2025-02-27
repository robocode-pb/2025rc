import json
import requests

class AI:
    def __init__(self, model="Phind-70B"):
        self.model = model
        self.url = "https://https.extension.phind.com/agent/"
        self.headers = {
            "Content-Type": "application/json",
            "User-Agent": "",
            "Accept": "*/*",
            "Accept-Encoding": "Identity"
        }

    def create_request(self, commit_message):
        user_input = f"Пиши українською {commit_message}"
        return {
            "additional_extension_context": "",
            "allow_magic_buttons": True,
            "is_vscode_extension": True,
            "message_history": [{"content": user_input, "role": "user"}],
            "requested_model": self.model,
            "user_input": user_input
        }

    def get_main_text(self, response_text):
        full_text = ""
        for line in response_text.splitlines():
            if line.startswith("data: "):
                content = line[len("data: "):]
                try:
                    data = json.loads(content)
                    if data.get("choices") and "delta" in data["choices"][0] and "content" in data["choices"][0]["delta"]:
                        full_text += data["choices"][0]["delta"]["content"]
                except Exception as e:
                    print(f"Помилка під час парсингу рядка: {e}")
        return full_text

    def ask(self, commit_message):
        request_data = self.create_request(commit_message)
        response = requests.post(self.url, headers=self.headers, json=request_data)
        return self.get_main_text(response.text)
ai = AI()


print("Що таке phindAI?\n", ai.ask("Що таке phindAI?"), '\n')

while True:
    print("\nРезультат:\n", ai.ask(input("\n\nВведіть запит: ")))
