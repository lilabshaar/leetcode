s = input()
d = {'I': '1', 'V': '5', 'X': '10', 'L': '50', 'C': '100', 'D': '500', 'M': '1000'}

for roman in s:
    if d[roman] < d[roman + 1]:
        d[roman + 1] - d[roman]
    else:
        d[roman] + d[roman + 1]
