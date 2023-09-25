CASHING_PERCENT = 0.015 
TAX = 0.1
PERCENT_ADD = 0.03
account = 0 
count = 0 
operation = []
def add_cash(cash: float):
    global PERCENT_ADD, account, count
    if cash % 50 == 0:
        account+=cash
        count+=1
        operation.append(f'Операция пополнения счета {cash}')
        if count % 3 == 0:
            account=account + account * PERCENT_ADD
            print(f"Начислен процент за пополнения счета, сумма на счете равна {account}")
            operation.append(f'Операция начисления процентов {account * PERCENT_ADD}')
        else:
            print(f"Сумма на счете {account} y.e.")
        
    else:
        print("Сумма пополнения счета должна быть кратна 50 у.е.")

def take_cash(cash: float):
    global PERCENT_ADD, account, count
    expenses = cash + percent_cash(cash)
    if account > expenses:
        if cash % 50 == 0:
            account-=expenses
            count+=1
            operation.append(f"Операция снятия {cash }")
            if count % 3 == 0:
                account = account + account * PERCENT_ADD
                print(f"Начислен процент за пополнения счета, сумма на счете равна {account}")
                operation.append(f'Операция начисления процентов {account * PERCENT_ADD}')
            else:
                print(f"Сумма на счете {account} y.e.")
            
        else:
            print("Сумма снятия должна быть кратна 50 у.е.")
    else:
        print(f"Недостаточно денег на счете, баланс {account} y.e.")


def percent_cash(cash: float):
    global CASHING_PERCENT
    cash_percent = cash*CASHING_PERCENT
    if cash_percent < 30:
        cash_percent = 30
    elif cash_percent > 600:
        cash_percent = 600

    return cash_percent

def exit_bank():
    print("Рады вас видетеь снова!\n")
    exit()

while True:
    action = input("1 - пополнить\n2 - снять деньги\n3 - баланс\n4 -просмотр всех операций\n5 -выйти\n")
    if account > 5_000_000:
        account = account - account * TAX
        print(f"списан налог на богатство: ",  {account * TAX})
        operation.append(f'Операция списания налога {account * TAX}')

    if action == '1':
        cash = float(input("ВВедите сумму пополнения кратно 50 у.е. "))
        add_cash(cash)
    elif action == '2':
        cash = float(input("ВВедите сумму снятия кратно 50 у.е. "))
        take_cash(cash)
    elif action == '3':
        print("Баланс = ", account)
    elif action == '4':
        for i in operation:
            print(i)
    else:
        exit_bank()   