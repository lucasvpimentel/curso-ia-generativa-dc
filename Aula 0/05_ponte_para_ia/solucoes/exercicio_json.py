# SOLUÇÃO - Módulo 5
import json

config = {
    "modelo": "gemini",
    "versao": 1.5
}

json_texto = json.dumps(config)
print(json_texto)
