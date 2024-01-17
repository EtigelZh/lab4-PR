P = 997
Q = 463
n = P * Q
def euler(p, q) -> int:
  return (p - 1) * (q - 1)

def nod(a, b) -> int:
  while b:
    a, b = b, a%b
  return a

euler_n = euler(P, Q)

def get_e(euler_n) -> int:
  res = 3
  n = 1

  while nod(res, euler_n) != 1:
    res = 2**(2**n) + 1
    n += 1

  if res < euler_n:
    return res
  else:
    return -1

def inverse(a, m) -> int:
  for x in range(1, m):
      if (((a % m) * (x % m)) % m == 1):
          return x
  return -1

e = get_e(euler_n)
d = inverse(e, euler_n)

public_key = {
    'e': e,
    'n': n,
}

private_key = {
    'd': d,
    'n': n,
}

def encrypt(text, public_key) -> str:
  temp = [ord(symb)**public_key['e'] % public_key['n'] for symb in text]
  res = [chr(num) for num in temp]
  return "".join(res)

def decrypt(text, private_key) -> str:
  temp = [ord(symb)**private_key['d'] % private_key['n'] for symb in text]
  res = [chr(num) for num in temp]
  return "".join(res)

text = "Меня зовут Кира Йошикаге"
enc_m = encrypt(text, public_key)
print(enc_m)
desc_m = decrypt(enc_m, private_key)
print(desc_m)