import random

random.seed(20)
numero = random.randint(0, 100)
print(numero)

import secrets

numero = secrets.choice(range(0, 100))
print(numero)

print(secrets.token_hex(32))
print(secrets.token_bytes(32))
print(secrets.token_urlsafe(32))