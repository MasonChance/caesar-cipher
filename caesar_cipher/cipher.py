

def encrypt(plain:str, key:int)-> str:
  cryptid = ''
  for char in plain:
    cryptid += str(((int(char) + key) %10))
  return cryptid

def decrypt(cryptid, key):
  return encrypt(cryptid, -key)



if __name__ == "__main__":
  # 867  plain
  # 3    key
  # expected 190
  print(encrypt("867", 3))
  # 190 cryptid in
  # 3 key (known)
  # expected 867
  print(decrypt('190', 3))
  