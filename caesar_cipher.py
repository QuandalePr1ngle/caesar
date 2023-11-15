err = 1
import time

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def Encrypt(text, rotation): #Encrypts the entered text
  r = ""
  for character in text: #For every characrer in text  
    if (alphabet.find(character) == -1):
      r += character
    else:
      r += (alphabet[(alphabet.find(character) + rotation) % len(alphabet)])
  return r

def Decrypt(text, rotation): #Decrypts the entered text
  r = ""
  for c in text:
    if (alphabet.find(c) == -1):
      r += c
    else:
      r += (alphabet[(alphabet.find(c) - rotation) % len(alphabet)])
  return r

ChooseMode = """
1. Encrypt text
2. Decrypt text
3. Bruteforce all rotations
Choose mode: """
mode = int(input(ChooseMode))
if mode == 1:
  text = input("Enter the text (Use CAPS): ")
  rotation = int(input("Enter the rotation: "))
  print("Encrypted: " + Encrypt(text, rotation))
elif mode == 2:
  text = input("Enter the text (Use CAPS): ")
  rotation = int(input("Enter the rotation: "))
  print("Decrypted: " + Decrypt(text, rotation))
elif mode == 3:
  text = input("Enter the text (Use CAPS): ")
  print("Bruteforcing...")
  time.sleep(1)
  for n in range(26):
    time.sleep(0.1)
    print(str(n)+" Decrypted: " + Decrypt(text, n))
  
  
  
