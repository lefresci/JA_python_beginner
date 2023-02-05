import math
import argparse


parser = argparse.ArgumentParser(
                    prog='Loan Calculator',
                    description='You can calculate annuity or differential loan parameters in this function')

parser.add_argument('-t', '--type',
                    choices=['annuity', 'diff'])
parser.add_argument('-pri', '--principal', type=int, default=0)
parser.add_argument('-per', '--periods', type=int, default=0)
parser.add_argument('-i', '--interest')
parser.add_argument('-pay', '--payment', type=int, default=0)

args = parser.parse_args()
try:
    interest = float(args.interest) / (12 * 100)
except TypeError:
    print('Incorrect parameters.')
    quit()


def differentiate_payment(loan, periods, loan_interest):
    total = 0
    for month in range(1, periods + 1):
        diff = math.ceil(loan / periods + loan_interest * (loan - loan * (month - 1) / periods))
        print(f'Month {month}: payment is {diff}')
        total += diff
    print('\nOverpayment =', total - loan)


def annuity_payment(loan, periods, loan_interest):
    annuity = math.ceil(loan * (loan_interest * (1 + loan_interest) ** periods) / ((1 + loan_interest) ** periods - 1))
    print(f'Your annuity payment = {annuity}!')
    print('Overpayment =', annuity * periods - loan)
    pass


def monthly_payments(loan, monthly, loan_interest):
    try:
        months = math.ceil(math.log(monthly / (monthly - loan_interest * loan), 1 + loan_interest))
    except ZeroDivisionError:
        months = math.ceil(loan / monthly)
    years = months // 12
    months -= years * 12
    msg = 'It will take '
    if years > 0:
        msg += f'{years} year{"s" if years > 1 else ""}'
    if months > 0:
        msg += f'{" and " if years > 0 else ""}{months} month{"s" if months > 1 else ""}'
    msg += ' to repay this loan!'
    print(msg)
    print('Overpayment =', monthly * (months + years * 12) - loan)
    pass


def loan_principal(annuity, periods, loan_interest):
    loan = math.floor(annuity / ((loan_interest * (1 + loan_interest) ** periods)
                                 / ((1 + loan_interest) ** periods - 1)))
    print(f'Your loan principal = {loan}!')
    print('Overpayment =', annuity * periods - loan)
    pass


def main(x):
    if x == 'diff':
        differentiate_payment(args.principal, args.periods, interest)
        return
    if x == 'annuity' and args.principal == 0:
        loan_principal(args.payment, args.periods, interest)
        return
    if x == 'annuity' and args.periods == 0:
        monthly_payments(args.principal, args.payment, interest)
        return
    if x == 'annuity':
        annuity_payment(args.principal, args.periods, interest)
        return


if __name__ == '__main__':
        main(args.type)
