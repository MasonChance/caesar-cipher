import string
import nltk
nltk.download('words', quiet=True)
from nltk.corpus import words


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
def crack(cryptid:str, margin:float=.8)-> list:
  perc_match = 0
  close_match_text = ''
  highest_shift = 0
  shift_perc = 0

  for i in range(27):
    sewer = decrypt(cryptid, i + 1).split(' ')
    for check in sewer:
      if check in words.words():
        perc_match += 1

    if perc_match / len(sewer) > margin:
      return [perc_match, i, ' '.join(sewer)]

    elif i == 26 and perc_match / len(sewer) < margin:
      return [shift_perc, highest_shift, close_match_text] if close_match_text != '' else f'no results found within {round((margin)*100)} percent accuracy or better. encryption may not be of type ceasar cypher'

    else:
      highest_shift = i
      shift_perc = perc_match / 100 or 0 
      if perc_match / len(sewer) > shift_perc:
        close_match_text = ' '.join(sewer)

      perc_match = 0
    continue
  return
    

    



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
