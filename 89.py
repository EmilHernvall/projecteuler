ROMAN_NUMERALS = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
NUMERALS_ROMAN = dict([(v,k) for k,v in ROMAN_NUMERALS.items()])
def parse_roman(num):
    nums = [ROMAN_NUMERALS[x] for x in num]
    res = sum([(x - sum([y for y in nums[0:i] if y < x]))
               for i, x in enumerate(nums) if x >= max(nums[i+1:]+[0])])

    return res

def format_roman(num):
    out = ""
    while num > 0:
        c = sorted([x for x in NUMERALS_ROMAN.keys() if x <= num], reverse=True)[0]
        num -= c
        out += NUMERALS_ROMAN[c]

    out = (out.replace("DCCCC", "CM")
              .replace("CCCC", "CD")
              .replace("LXXXX", "XC")
              .replace("XXXX", "XL")
              .replace("VIIII", "IX")
              .replace("IIII", "IV"))

    return out

with open('p089_roman.txt', 'r') as fh:
    print sum([len(l.strip())-len(format_roman(parse_roman(l.strip()))) for l in fh])
