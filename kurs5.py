# bir sayının asal olup olmadığını kontrol eden fonksiyon oluşturma
def is_prime(number):
  if number <= 1:
    return False
  for i in range(2, number):
    if (number % i) == 0:
      return False
  return True
# bir kelimenin tersini alan fonksiyon oluşturma
def reverse_word(word):
  reversed_word = ""
  for i in range(len(word) - 1, -1, -1):
    reversed_word += word[i]
  return reversed_word