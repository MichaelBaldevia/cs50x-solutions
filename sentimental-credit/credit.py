# TODO
from cs50 import get_int
from cs50 import get_string

credit_card_number = get_int("Credit Card Number: ")
credit_card_length =  len(str(credit_card_number))

#get every number
number = [int(a) for a in str(credit_card_number)]
#Pass number
original_length = [int(a) for a in str(credit_card_number)]
#Multiply every 2nd number and get sum if greater than 10
z = credit_card_length - 1
while z > 0:
    number[z-1] = number[z-1] * 2
    if number[z-1] > 9:
        double_digit = [int(a) for a in str(number[z-1])]
        number[z-1] = double_digit[0] + double_digit[1]
    z = z - 2

#Get credit card number value
credit_card_sum = sum(number)

#Classify Credit card
#if credit card starts with 4 and length is 13 or 16
if (((original_length[0] == 4 and credit_card_length == 13) or (original_length[0] == 4 and credit_card_length == 16)) and credit_card_sum  % 10 == 0):
    print("VISA")
#if credit card starts with 34, 37 and length is 15
elif ((original_length[0] == 3 and (original_length[1] == 4 or original_length[1] == 7)) and credit_card_length == 15 and credit_card_sum % 10 == 0):
    print("AMEX")
#if credit card starts with 51, 52, 53, 54, 55 and length is 16
elif ((original_length[0] == 5 and (original_length[1] == 1 or original_length[1] == 2 or original_length[1] == 3 or original_length[1] == 4 or original_length[1] == 5)) and credit_card_sum % 10 == 0 and credit_card_length == 16):
    print("MASTERCARD")
else:
    print("INVALID")
