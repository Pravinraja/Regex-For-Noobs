import re
#Question 1:
with open('passwords.txt','r') as f:
   count = sum(len(re.findall( r'\bpassword\b', line)) for line in f)
   print("The word password occurs " + str(count) + " times ")

#Question 2:
with open('passwords.txt','r') as f:
   countall =sum(len(re.findall('[A-Z]|[a-z]|[0-9]|[!@#$%^&*].*?', w, re.M|re.I)) for w in f)
#print("The total number of letters, numbers, and special characters is " + str(countall))
with open('passwords.txt', 'r') as f:
    countnumber = sum(len(re.findall(r'\d+', line)) for line in f)
count_per= (countnumber/countall)*100
#print("The total amount of numbers is " + str(countnumber))
print("The percentage of 1 number occurences is " + str(count_per) + "%")

#Question 3:
with open('passwords.txt', 'r') as f:
    countletter = sum(len(re.findall('[A-Z]|[a-z].*?', w, re.M|re.I)) for w in f)
count_let= (countletter/countall)*100
#print("The total amount of letters is " + str(countletter))
print("The percentage of letter occurences is " + str(count_let) + "%")

#Question 4:
with open('passwords.txt', 'r') as f:
    countspecial = sum(len(re.findall('[!@#$%^&*].*?', w, re.M|re.I)) for w in f)
count_spc= (countspecial/countall)*100
#print("The total amount of special characters is " + str(countspecial))
print("The percentage of special characters is " + str(count_spc) + "%")

#Question 5:
with open('passwords.txt', 'r') as f:
    countspecialalpha = sum(len(re.findall('[A-Z]+[a-z]+[0-9]+[!@#$%^&*].*?', w, re.M|re.I)) for w in f)
count_spc1= (countspecialalpha/countall)*100
#print("The total amount of letter, number, and special character is " + str(countspecialalpha))
print("The percentage of letter, number, and special character is " + str(count_spc1) + "%")
#Question 6:

with open('passwords.txt', 'r') as f:
    countcharUpper = sum(len(re.findall( r'[A-Z].*?', line)) for line in f)
count_charUpper= (countcharUpper/countall)*100
#print("The total amount of upper case letters is " + str(countcharUpper))
print("The percentage of upper case letters is " + str(count_charUpper) + "%")
with open('passwords.txt', 'r') as f:
    countcharLower = sum(len(re.findall( r'[a-z].*?', line)) for line in f)
count_charLower= (countcharLower/countall)*100
#print("The total amount of lower case letters is " + str(countcharLower))
print("The percentage of lower case letters is " + str(count_charLower) + "%")

#Bonus Question
import re
with open('passwords.txt','r') as f:
   A =sum(len(re.findall('[A|a].*?', w, re.M|re.I)) for w in f)
#print("The total number of A " + str(A))
with open('passwords.txt','r') as f:
   E =sum(len(re.findall('[E|e].*?', w, re.M|re.I)) for w in f)
#print("The total number of E " + str(E))
with open('passwords.txt','r') as f:
   I =sum(len(re.findall('[I|i].*?', w, re.M|re.I)) for w in f)
#print("The total number of I " + str(I))
with open('passwords.txt','r') as f:
   O =sum(len(re.findall('[O|o].*?', w, re.M|re.I)) for w in f)
#print("The total number of O " + str(O))
with open('passwords.txt','r') as f:
   U =sum(len(re.findall('[U|u].*?', w, re.M|re.I)) for w in f)
#print("The total number of U " + str(U))
if A < E  or A < I or A < O or A < U :
    print("A is least frequent vowel")
elif E < A or E < I or E < O or E < U :
    print("E is least frequent vowel")
elif I < A or I < E or I < O or I < U :
    print("I is least frequent vowel")
elif O < A or O < I or O < E or I < U :
    print("O is least frequent vowel")
elif U < A or U < I or U < O or U < E :
    print("U is least frequent vowel")