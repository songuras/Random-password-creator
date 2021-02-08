# import 
import string
import random

def useing_key():
  char = ((string.ascii_letters)+(string.ascii_uppercase)+(string.digits)+(string.hexdigits)+(string.punctuation))
  key_words=(list(char))
  return key_words
key_words2 = (useing_key())
run= True
while run:
  # a for password lenth:  ########
  print("")
  a=int(input("şifre uzunluğunu girin : "))
  print("")
  #b for asking n times pasword
  b = int(input("kaç şifre istersiniz : "))
  print("")
  print("")
  # This first for loop 
  for x in range(0,b):
    password=""
    #second for loop
    for x in range(0,a):
      pasword_Gen = random.choice(key_words2)
      password = (password + pasword_Gen)
    print("__"*100)
    print("|                                  ")
    print("şifreniz =  " ,password)
    print("|"+"__"*100)
  
  print("")
  # To exit Or  Not use input()
  run=input("çıkış için  A veya a ya devam etmek için herhangi başka bir tuşa basın ")
  if run == "A" or run== "a":
    run= False
  
  if run == False:
    print("")
