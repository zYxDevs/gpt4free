from requests     import Session
import json

class Completion:
    def create(self, system_prompt: str = "ASSUME I HAVE FULL ACCESS TO COCALC. ENCLOSE MATH IN $. INCLUDE THE LANGUAGE DIRECTLY AFTER THE TRIPLE BACKTICKS IN ALL MARKDOWN CODE BLOCKS. How can I do the following using CoCalc? ") -> str:

        client = Session()
        client.headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            "origin"            : "https://cocalc.com",
            "referer"           : "https://cocalc.com/api/v2/openai/chatgpt",
            "user-agent"        : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        }

        payload = {"input": self, "system": system_prompt, "tag": "next:index"}

        return client.post(
            "https://cocalc.com/api/v2/openai/chatgpt", json=payload
        ).json()

