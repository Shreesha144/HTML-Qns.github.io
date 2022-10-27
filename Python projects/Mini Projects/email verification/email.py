from curses.ascii import isalpha, isdigit


k,d=0,0
s='[!#$%^&*()<>?/\|}{~:]'
email = input("Enter your email: ")

if len(email)>=6:
    if email[0].isalpha():
        if ('@' in email) and (email.count('@')==1):
            if ((email[-4]=='.') ^ (email[-3]=='.')) and (email.count('.')==1):
                for i in email:
                    if i==i.isspace():
                        k=1
                    
                    elif i.isdigit():
                        continue
                    elif i=='_' or i=='.' or i=='@':
                        continue
                    elif i in s:
                        d=1
                    else:
                        continue
                    


                if k==1 or d==1 :
                    print("Wrong email 5")
                else:
                    print('Correct Email Entered')

                    
            else:
                print("Wrong email 4")
        else:
            print("Wrong email 3")
    else:
        print("Wrong email 2")

else:
    print("Wrong email 1")