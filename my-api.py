import requests
import json

def buscar_dados():
    request = requests.get("https://blog-gus-api.vercel.app/get-all-posts")
    todos = json.loads(request.content)
    # print(todos)
    print(todos[1]['title'])
    print(todos[1]['text'])

if __name__ == '__main__':
    buscar_dados()