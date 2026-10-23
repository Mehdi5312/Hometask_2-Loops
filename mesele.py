def task1():
    for i in range(10, -1, -1):
        print(i)
    return 'Liftoff'


def task2():
    child=0
    adult=0
    for i in range(5):
        ans=int(input())
        if ans<18:
            child+=1
        else:
            adult+=1
    return 'Child: ', child, 'Adult: ', adult

# task3
# 1, 3, 5, 7, 9


def task4():
    total=0
    for i in range(5):
        price=int(input())
        total+=price
    return total, total/5


def task5():
    while True:
        password=input('Enter password: ')
        if len(password)<8:
            print('Too short, try again ')
        else:
            return 'Password accepted'

# task6
# 70
# 40
# 10
# -20
# Done



def task7():
    for i in range(1, 8):
        print(f'Day {i}: {i*1200}')


def task8():
    correct_username='admin'
    correct_password=1234
    for i in range(3):
        username=input('Enter username: ')
        password=input('Enter password: ')
        if username==correct_username and password==correct_password:
            return 'Welcome! '
    return 'Account locked'

def task9():
    balance=500
    while True:
        amount=input('Enter amount: ')
        if amount==0:
            return "Goodbye"
        elif amount<0:
            print('Invalid input')
        elif balance<amount:
            print('Insufficent funds')
        else:
            balance-= amount 
            print(balance)
        if balance==0:
            return


# task10
# Wrong pin 2 attempts left
# Wrong pin 1 attempts left
# Access granted 
# Attempts used: 3


def task11():
    m=0
    total=0
    count=0
    passed=0
    failed=0
    while True:
        score=int(input('Grade: '))
        count+=1
        total+=score
        if m<score:
            m=score
        if score<51:
            failed+=1
        else:
            passed+=1
        if score==-1:
            return passed, failed, m, total/count


def task12():
    space=20
    while True:
        ans=input()
        if ans.lower() == 'in':
            if space<20:
                space+=1
            else:
                print("Garage full")
        elif ans.lower() == 'out':
            if space>0:
                space-=1
            else:
                print('Garage empty')
        elif ans.lower()=='stop':
            return
        else:
            print('Command unknown')


def task13():
    hot=0
    hottest=0
    day=1
    for i in range(1, 8):
        weather=int(input(f'Day {i}: '))
        if weather>30:
            hot+=1
            if weather>hottest:
                hottest=weather
                day=i
    
    return 'Hot days: ', hot, 'Hottest:', day


def task14():
    password='secret'
    attempts = 0
    while True:
        entered = input("Password: ")
        if entered == password:
            print("Welcome")
            break
        if attempts==3:
            print('Account locked')
            break


def task15():
    word=input('Password: ')
    digit=True
    up=True
    low=True
    for i in word:
        if i.isdigit():
            digit=False
        elif i.isupper():
            up=False
        elif i.islower():
            low=False
    if digit:
        return 'Weak password: no  digits'
    elif up:
        return 'Weak password: no uppercase letters '
    elif low:
        return 'Weak password: no lowercase letters '
    else:
        return 'Strong password'


def task16():
    month=0
    money=50
    budget=0
    while budget<1000:
        budget+=money
        money+=10
        month+=1
        print(f'Month: {month}, budget: {budget}')
    return


# task17
# 105


def task18():
    pin=2580
    balance=1000
    attempt=0
    menu=False
    while True:
        attempt+=1
        ans=int(input("Enter pin: "))
        if ans==pin:
            menu=True
            break
        if attempt==3:
            return 'Card blocked'
    if menu:
        while True:
            print('''1 - Check balance 
2 - Deposit 
3 - Withdraw 
4 - Exit''' )
            op=int(input('\n'))
            if op==1:
                print(balance)
            elif op==2:
                amount=int(input('Enter amount: '))
                if amount<=0:
                    print('Rejected')
                else:
                    balance+=amount
            elif op==3:
                amount=int(input('Enter amount'))
                if amount<0 or amount>balance:
                    print('Invalid amount')
                else:
                    balance -= amount
            elif op == 4:
                print('Goodbye')
                return
            else:
                print('Invalid operation')


def task19():
    price=1.5
    total=0
    while total<price:
        amount=input('Insert coin: ')
        match amount:
            case 0.05|0.10|0.20|0.50|1:
                total+=amount
                print(f'Total: {total}')
            case _:
                print('Coin is not accepted.')
    print('Here is your water')
    if total>price:
        print(f'Change: {total-price}')
        return


def task20():
    for i in range(2, 100):
        k=True
        for j in range(2, i):
            if i%j==0:
                k=False
                break
        if k:
            print(i, end=' ')


# task21
# 101 102
# 201 202
# 301 302


def task22():
    for floor in range(1, 6):
        if floor==4:
            continue
        print(f'Floor {floor}:')
        for rooms in range(1, 5):
            if floor==4:
                break
            print(f' {floor*100+rooms}', end=' ')
        print('\n')



def task23():
    minutes=480
    i=0
    customers=0
    while minutes>0:
        i+=1
        time=int(input(f'Customer {i} needs (min): '))
        customers+=1
        minutes-=time
    minutes+=time
    customers-=1
    print('Sorry, come back tomorrow')
    print(f'Customers served: {customers}')
    print(f'Minutes left: {minutes}')


def task24():
    a, b, c=0, 0, 0
    spoiled=0
    while True:
        vote=input('VOTE: ')
        vote=vote.lower()
        if vote=='a':
            a+=1
        elif vote=='b':
            b+=1
        elif vote=='c':
            c+=1
        elif vote=='end':
            break
        else:
            spoiled+=1

    if a>b and a>c:
        highest='A'
    elif b>a and b>c:
        highest='B'
    elif c>a and c>b:
        highest='C'
    else:
        highest='Tie'
    print(f'A: {a}  B: {b}  C: {c}')
    print(f'Spoiled: {spoiled}')
    print(f'Winner: {highest}')


def task25():
    digits=input('Input: ')
    if len(digits)!=16 or not digits.isdigit():
        print('Must be 16 digits')
        return
    total=0
    for i in range(len(digits)-1, -1, -1):
        d=int(digits[i])
        if i%2==0:
            d*=2
            if d>9:
                d-=9

        total+=d
    if total%10==0:
        print('Valid')
        return
    else:
        print('Invalid')
        return

