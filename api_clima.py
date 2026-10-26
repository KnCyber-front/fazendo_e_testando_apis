import requests 

api_key = "dd44a2af5ad344aa844140522262610"

url = "http://api.weatherapi.com/v1/current.json"

parametros = {
    "key": api_key,
    "q": "auto:ip",
    "lang" : "pt",
    
    
    
    
    }


resposta = requests.get(url, params=parametros)
print(resposta.json())