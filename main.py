import os

senha = os.environ.get('PWD_DB', "<SECRET>")
print(f"{senha}")

senha = os.environ.get('API_KEY', "<SECRET>")
print(f"{senha}")

senha = os.environ.get('AWS_ACCESS_KEY', "354646874")
print(f"{senha}")

senha = os.environ.get('PWD_POST', "<SECRET>")
print(f"{senha}")
