import json
import random
from datetime import datetime

# Preço inicial do Bitcoin em USD
bitcoin_price = 50000.0

# Lista para armazenar transações
transaction_history = {}

def save_transactions():
    with open('transactions.json', 'w') as f:
        json.dump(transaction_history, f)

def load_transactions():
    try:
        with open('transactions.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def update_transaction_history(username, action, amount, price):
    if username not in transaction_history:
        transaction_history[username] = []
    transaction_history[username].append({
        'action': action,
        'amount': amount,
        'price': price,
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    save_transactions()

def buy_bitcoin(users, username):
    global bitcoin_price
    try:
        amount = float(input("Quanto dinheiro você deseja usar para comprar Bitcoin? "))
        if amount <= 0:
            print("O valor deve ser maior que zero.")
            return
        if amount > users[username]['balance']:
            print("Saldo insuficiente!")
            return
        
        bitcoin_purchased = amount / bitcoin_price
        
        users[username]['balance'] -= amount
        users[username]['bitcoin'] += bitcoin_purchased
        save_users(users)

        # Atualiza o preço do Bitcoin após a compra
        update_bitcoin_price()

        # Atualiza o histórico de transações
        update_transaction_history(username, 'buy', bitcoin_purchased, bitcoin_price)

        print(f"Você comprou {bitcoin_purchased:.6f} BTC.")
    except ValueError:
        print("Entrada inválida! Por favor, insira um número.")

def sell_bitcoin(users, username):
    global bitcoin_price
    try:
        amount = float(input("Quanto Bitcoin você deseja vender? "))
        if amount <= 0:
            print("A quantidade deve ser maior que zero.")
            return
        if amount > users[username]['bitcoin']:
            print("Você não possui essa quantidade de Bitcoin!")
            return
        
        money_earned = amount * bitcoin_price
        
        users[username]['bitcoin'] -= amount
        users[username]['balance'] += money_earned
        save_users(users)

        # Atualiza o preço do Bitcoin após a venda
        update_bitcoin_price()

        # Atualiza o histórico de transações
        update_transaction_history(username, 'sell', amount, bitcoin_price)

        print(f"Você vendeu {amount:.6f} BTC e ganhou ${money_earned:.2f}.")
    except ValueError:
        print("Entrada inválida! Por favor, insira um número.")

def view_transaction_history(users, username):
    if username in transaction_history and transaction_history[username]:
        print("Histórico de Transações:")
        for transaction in transaction_history[username]:
            print(f"{transaction['timestamp']}: {transaction['action'].capitalize()} {transaction['amount']:.6f} BTC a ${transaction['price']:.2f}")
    else:
        print("Nenhuma transação registrada.")

def transfer_bitcoin(users, username):
    recipient = input("Digite o nome de usuário do destinatário: ")
    if recipient not in users:
        print("Usuário não encontrado.")
        return
    
    try:
        amount = float(input("Quanto Bitcoin você deseja transferir? "))
        if amount <= 0:
            print("A quantidade deve ser maior que zero.")
            return
        if amount > users[username]['bitcoin']:
            print("Você não possui essa quantidade de Bitcoin!")
            return
        
        users[username]['bitcoin'] -= amount
        users[recipient]['bitcoin'] += amount
        save_users(users)

        # Atualiza o histórico de transações
        update_transaction_history(username, 'transfer to ' + recipient, amount, bitcoin_price)
        update_transaction_history(recipient, 'transfer from ' + username, amount, bitcoin_price)

        print(f"Você transferiu {amount:.6f} BTC para {recipient}.")
    except ValueError:
        print("Entrada inválida! Por favor, insira um número.")

def add_money(users, username):
    try:
        amount = float(input("Quanto dinheiro você deseja adicionar? "))
        if amount <= 0:
            print("O valor deve ser maior que zero.")
            return
        
        users[username]['balance'] += amount
        save_users(users)
        print(f"Você adicionou ${amount:.2f} ao seu saldo.")
    except ValueError:
        print("Entrada inválida! Por favor, insira um número.")

def view_balance(users, username):
    balance = users[username]['balance']
    bitcoin = users[username]['bitcoin']
    print(f"Seu saldo é: ${balance:.2f} e você possui {bitcoin:.6f} BTC.")

def update_bitcoin_price():
    global bitcoin_price
    # Atualiza o preço do Bitcoin com um valor aleatório (exemplo: entre 40000 e 60000)
    bitcoin_price = random.uniform(40000, 60000)

def user_menu(users, username):
    while True:
        print("\nMenu do Usuário:")
        print("1. Adicionar Dinheiro")
        print("2. Comprar Bitcoin")
        print("3. Vender Bitcoin")
        print("4. Ver Saldo")
        print("5. Ver Preço Atual do Bitcoin")
        print("6. Ver Histórico de Transações")
        print("7. Transferir Bitcoin")
        print("8. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            add_money(users, username)
        elif choice == '2':
            buy_bitcoin(users, username)
        elif choice == '3':
            sell_bitcoin(users, username)
        elif choice == '4':
            view_balance(users, username)
        elif choice == '5':
            print(f"O preço atual do Bitcoin é: ${bitcoin_price:.2f}")
        elif choice == '6':
            view_transaction_history(users, username)
        elif choice == '7':
            transfer_bitcoin(users, username)
        elif choice == '8':
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    users = load_users()
    transaction_history = load_transactions()  # Carrega o histórico de transações

    while True:
        main_menu()
        choice = input("Escolha uma opção: ")

        if choice == '1':
            register(users)
        elif choice == '2':
            login(users)
        elif choice == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida!")
