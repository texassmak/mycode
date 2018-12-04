#!/usr/bin/env python3
message = 'I recommend you eat '
print('What is your weight? (in pounds) ')  # asks user to input body weight in pounds

weight = float(input()) #sets object for their weight inputted

if weight >= 250:
    message = message + 'at least 200 grams of protein daily.'
elif weight >= 200:
    message = message + 'at least 160 grams of protein daily.'
elif weight >= 175:
    message = message + 'at least 130 grams of protein daily.'
else:
    message = message + 'at least 80-100 grams of protein daily.'
print(message)
