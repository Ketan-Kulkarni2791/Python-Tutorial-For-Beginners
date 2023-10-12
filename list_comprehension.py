squares = []
for i in range(10):
    squares.append(i * i)
print(squares)


txns = [1.09, 23.56, 57.84, 4.56, 6.78]
TAX_RATE = .08
def get_price_with_tax(txn):
    return txn * (1 + TAX_RATE)
final_prices = map(get_price_with_tax, txns)
print(list(final_prices))


squares = [i * i for i in range(10)]
print(squares)


txns = [1.09, 23.56, 57.84, 4.56, 6.78]
TAX_RATE = .08
def get_price_with_tax(txn):
    return txn * (1 + TAX_RATE)
final_prices = [get_price_with_tax(i) for i in txns]
print(final_prices)


sentence = "India's Chandrayan-3 mission is an huge success!"
vowels = [i for i in sentence if i in 'aeiou']
print(vowels)


sentence = 'The rocket, who was named Chandrayan-3, came back from Moon because he missed his friends.'
def is_consonant(letter):
    vowels = 'aeiou'
    return letter.isalpha() and letter.lower() not in vowels
consonants = [i for i in sentence if is_consonant(i)]
print(consonants)
