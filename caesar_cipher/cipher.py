import string



# base form for encrypt-> decrypt. numeric only. 
def encrypt_num_str(plain:str, key:int)-> str:
  cryptid = ''
  for char in plain:
    cryptid += str((int(char) + key) %10)
  return cryptid

def decrypt_num_str(cryptid, key):
  return encrypt(cryptid, -key)


def encrypt(plain:str, key:int)-> str:
  cryptid = ''
  table = {}
  cypher = {}
  for i, char in enumerate(string.ascii_lowercase):
    table[f'{char}'] = i   
    cypher[f'{(int(table[char]) - key) % 26}'] = char

  for char in plain:
    if char == ' ':
      cryptid += ' '
    else:
      char = int(table[f'{char.lower()}'])
      cryptid += cypher[f'{char}']
  return cryptid
  

def decrypt(cryptid, key):
  return encrypt(cryptid, -key)

#first attempt brute force w/comparison to natural langlib 
def crack(cryptid):
  




if __name__ == "__main__":
  # 867  plain
  # 3    key
  # expected 190
  print(encrypt("abc", 3))
  # 190 cryptid in
  # 3 key (known)
  # expected 867
  # print(decrypt('190', 3))
  # 'five three oh nine' plain
  # 3 key
  # 'ilyh wkuhh rk qlqh'
