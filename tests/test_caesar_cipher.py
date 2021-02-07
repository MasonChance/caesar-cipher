
import pytest
from caesar_cipher.cipher import encrypt, decrypt, crack

def test_alpha_encrypt():
    jenny = 'five three oh nine'
    assert encrypt(jenny, 3) == 'ilyh wkuhh rk qlqh' 
    
def test_alpha_decrypt():
    gobbledy = 'ilyh wkuhh rk qlqh'
    assert decrypt(gobbledy, 3) == 'five three oh nine'

def test_alpha_crack_success():
    gobbledy = 'ilyh wkuhh rk qlqh'
    assert crack(gobbledy)[2] == 'five three oh nine'

def test_alpha_crack_fail():
    gobbledy = 'ilupbyh wkuuiohh rpklk qoioiolqh'
    assert crack(gobbledy) == 'no results found within 80 percent accuracy or more. encryption may not be of type ceasar cypher'