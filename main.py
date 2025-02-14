from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv(f".env")

senha = os.environ.get('PWD_DB')
print(f"{senha}")

senha = os.environ.get('API_KEY')
print(f"{senha}")

senha = os.environ.get('AWS_ACCESS_KEY')
print(f"{senha}")

senha = os.environ.get('PWD_POST')
print(f"{senha}")