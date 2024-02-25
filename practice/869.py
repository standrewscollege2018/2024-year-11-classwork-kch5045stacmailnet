# Write your code here :-)
stories = int(input())
cards = 0
for a in range(1, stories + 1):
    cards = cards + (2 * a)
for b in range(1, stories):
    cards = cards + b
print(cards)
