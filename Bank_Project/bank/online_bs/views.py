from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse,redirect
from online_bs.models import Register
from online_bs.models import Transaction
from .models import Register
from django.views.decorators.csrf import csrf_protect 
from datetime import datetime
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)



def timedate():
    current_date_time = datetime.now()

    # Format the date and time as strings
    formatted_date = current_date_time.strftime('%Y-%m-%d')
    formatted_time = current_date_time.strftime('%H:%M:%S')

    # Print the formatted date and time
    print("Date:", formatted_date)
    print("Time:", formatted_time)

    return formatted_date, formatted_time

def home(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'home.html')


def user_registration(request):
    message=""
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        pswd = request.POST['password']
        mob = request.POST['mobile']
        dob = request.POST['dob']
        add = request.POST['address']
        # print(name,email,pswd,mob,dob,add)
        ins = Register(u_name=name,email=email,password=pswd,add=add,dob=dob,mob=mob)
        ins.save()
        message="Succesfully Registered"
    context={"message":message}
    return render(request, 'register.html',context)

@csrf_protect
def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        pswd = request.POST['password']

        data = get_object_or_404(Register, email=email, password=pswd)
        
        if data.email and data.password:
            global user_get
            user_get = data  # Store the Register instance in user_get
            print("user_get is...",user_get)
            return redirect('deposit')
            user_email = data.email
            user_password = data.password
        else:
            return render(request, 'login.html', {'error': 'Invalid login credentials'})
    return render(request, 'login.html')


@csrf_protect 
def deposit(request):
    context={}
    if request.method=="POST":
        money = request.POST['amt']
        print(money)
        date,time = timedate()
        user_instance = user_get
        ins = Transaction(user=user_instance,deposit=money,date=date)
        ins.save()
        message = f"You have deposited: {money}"
        context = {"message":message}
    return render(request, 'deposit.html',context)


def withdrawal(request):
    message=""
    msg={}
    if request.method=="POST":
        wd_money = request.POST['amt']
        print(wd_money)
        date,time = timedate()

        user_instance = user_get
        # Fetch all transactions for the user
        transactions = Transaction.objects.filter(user=user_instance)
        
        deposit_transactions = []
        withdrawal_transactions = []

        # Iterate through the queryset and categorize transactions
        for transaction in transactions:
            if transaction.deposit != 0.00:
                deposit_transactions.append(float(transaction.deposit))
            elif transaction.withdrawal != 0.00:
                withdrawal_transactions.append(float(transaction.withdrawal))

        # Calculate cumulative balance for deposit transactions
        cbd = sum(deposit_transactions)

        # Calculate cumulative balance for withdrawal transactions
        cbw = sum(withdrawal_transactions)

        limit_ = limit_withdraw()

        if cbw>=cbd:
            message="You Don't Have Enough Balance"
            print("exceed")

        elif cbw>=limit_:
            message="You Have Exceeded Monthly Limit"

        else:
            user_instance = user_get
            ins = Transaction(user=user_instance,withdrawal=wd_money,date=date)
            ins.save()
        msg = {'msg':message}
    return render(request, 'withdraw.html',msg)

def limit_withdraw():
    user_instance = user_get
        # Fetch all transactions for the user
    transactions = Transaction.objects.filter(user=user_instance)
    
    limit_db = []

    # Iterate through the queryset and categorize transactions
    for transaction in transactions:
        if transaction.limit != 0.00:
            limit_db.append(float(transaction.limit))

    total_limit = sum(limit_db)

    return total_limit


def report(request):
    # Fetch the user instance
    user_instance = user_get
    # Fetch all transactions for the user
    transactions = Transaction.objects.filter(user=user_instance)
    
    deposit_transactions = []
    withdrawal_transactions = []

    # Iterate through the queryset and categorize transactions
    for transaction in transactions:
        if transaction.deposit != 0.00:
            deposit_transactions.append(float(transaction.deposit))
        elif transaction.withdrawal != 0.00:
            withdrawal_transactions.append(float(transaction.withdrawal))

    # Calculate cumulative balance for deposit transactions
    cumulative_balance_deposit = sum(deposit_transactions)

    # Calculate cumulative balance for withdrawal transactions
    cumulative_balance_withdrawal = sum(withdrawal_transactions)

    print(f"Cumulative Balance for Deposits: {cumulative_balance_deposit}")
    print(f"Cumulative Balance for Withdrawals: {cumulative_balance_withdrawal}")
    global final_balance
    final_balance = cumulative_balance_deposit - cumulative_balance_withdrawal


    balance = 0

    for transaction in transactions:
        transaction.deposit = float(transaction.deposit)
        transaction.withdrawal = float(transaction.withdrawal)

        # Calculate cumulative balance after the transaction
        transaction.balance = round(balance + transaction.deposit - transaction.withdrawal, 2)
        
        # Update the balance for the next iteration
        balance = transaction.balance


   # The last value of balance after the loop
    context = {
        'transactions': transactions,
        'final_balance': final_balance
    }

    return render(request, 'report.html',context)






def set_limit(request):
    if request.method=="POST":
        limit = request.POST['amt']
        print(limit)
        date,time = timedate()
        user_instance = user_get
        ins = Transaction(user=user_instance,limit=limit,date=date)
        ins.save()


    return render(request, 'monthly_inc.html')


def request_exd_money(request):
    if request.method=="POST":
        wd_money = request.POST['amt']
        print(wd_money)
        user_instance = user_get
        date,time=timedate()
        ins = Transaction(user=user_instance,reqwithdraw=wd_money,date=date)
        ins.save()

    return render(request, 'request.html')


def req_withdrawal(request):
    reqwithdraw_db=[]
    user_instance = user_get
        # Fetch all transactions for the user
    transactions = Transaction.objects.filter(user=user_instance)
    for transaction in transactions:
        if transaction.reqwithdraw != 0.00:
            reqwithdraw_db.append(float(transaction.reqwithdraw))
    print(reqwithdraw_db)
    context = {'data':reqwithdraw_db}
    if request.method=='POST':
        wd_money = request.POST['amt']
        print(wd_money)
        date,time=timedate()
        ins = Transaction(user=user_instance,withdrawal=wd_money,date=date)
        ins.save()
    return render(request,'req_withdraw.html',context)



import csv

def download_report(request):
    # Assuming transactions and final_balance are available in your context
    user_instance = user_get
    # Fetch all transactions for the user
    transactions = Transaction.objects.filter(user=user_instance)

    final_bal = final_balance  # Replace this with your actual final balance

    # Create a response object with appropriate headers for CSV download
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="transaction_report.csv"'

    # Create a CSV writer
    csv_writer = csv.writer(response)
    
    # Write header row
    csv_writer.writerow(['Transaction Type', 'Date', 'Amount', 'Balance After Transaction'])
    balance = 0

    for transaction in transactions:
        transaction.deposit = float(transaction.deposit)
        transaction.withdrawal = float(transaction.withdrawal)

        # Calculate cumulative balance after the transaction
        transaction.balance = round(balance + transaction.deposit - transaction.withdrawal, 2)
        
        # Update the balance for the next iteration
        balance = transaction.balance
    # Write data rows
    for transaction in transactions:
        if transaction.deposit != 0.00:
            csv_writer.writerow(['Deposit', transaction.date, transaction.deposit, transaction.balance])
        elif transaction.withdrawal != 0.00:
            csv_writer.writerow(['Withdrawal', transaction.date, transaction.withdrawal, transaction.balance])

    # Write the final balance row
    csv_writer.writerow(['', '', 'Final Balance', final_bal])

    return response





