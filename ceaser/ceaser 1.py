
data = input('Enter a 5-letter string: ')

letters = ''
for ch in data:
  if ch.isalpha():
    letters += ch
  else:
    print('Error: Non-letter characters found in input data.')

shifted_letters = ''
for ch in letters:
  shifted_letters += chr((ord(ch) - ord('a') + 5) % 26 + ord('a'))

with open('1.txt', 'w') as f:
  f.write(shifted_letters)

with open('2.txt', 'w') as f:
  f.write(data)
