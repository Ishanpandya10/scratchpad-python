numb_div_dict: dict = {}

for x in range(1, 1000):
    divisors = []
    for div in range(1, x + 1):
        if x % div == 0:
            divisors.append(x / div)

    numb_div_dict[x] = len(divisors)

# print(numb_div_dict)

max_value = numb_div_dict[max(numb_div_dict, key=lambda dict_key: numb_div_dict[dict_key])]
# print(max_value)

for key, val in numb_div_dict.items():
    if val == max_value:
        print(str(key) + ":" + str(val))
