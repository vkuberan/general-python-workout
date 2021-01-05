msg = 'HackerRank.com presents "Pythonist 2".'

swap = ''.join([i.lower() if i.isupper() else i.upper() for i in msg])

# Or use msg.swapcase()

print(msg)
print(swap)
