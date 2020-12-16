import random
# Map Functionality


def print_iterator(header, it):
    print(header)
    print('*' * len(header))
    for x in it:
        print(x, end=' ')
    print("\n\n")  # New Line


result = map(lambda x, y: (x+y), [i for i in range(1, 20)], [
    random.randint(1, 999999) for i in range(1, 20)])

print_iterator("Addition: ", result)

result = map(lambda x: x.upper(), [
    'welcome', 'hello', 'world!!!', 'bye bye', '2020???'])
print_iterator('Strings To Upper Case', result)
