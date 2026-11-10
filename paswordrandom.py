import secrets
import string
x = string.printable.replace(' ', ' ').replace('\t', ' ').replace('\n', ' ').replace('\n', ' ')
y = ' '.join(secrets.choice(x)  for _ in range (16))
print(y)