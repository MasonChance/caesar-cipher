
import pytest
from caesar_cipher.cipher import encrypt, decrypt, crack

def test_alpha_encrypt():
    jenny = 'five three oh nine'
    assert encrypt(jenny, 3) == 'ilyh wkuhh rk qlqh' 
    
def test_alpha_decrypt():
    gobbledy = 'ilyh wkuhh rk qlqh'
    assert decrypt(gobbledy, 3) == 'five three oh nine'

def test_alpha_crack():
    gobbledy = 'ilyh wkuhh rk qlqh'
    assert crack(gobbledy) == 'five three oh nine'