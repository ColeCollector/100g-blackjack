#!python3

def value(hand):
  '''
  input:
  list hand: hand is a list of strings that contains the cards in the hand
  eg: ['AH','3D','4S']
  
  return:
  int the total value of the hand
  may return a list if the hand contains an Ace
  eg:
  '''
  x = 0
  x1 = 0
  forbidden = ['A', 'K', 'Q', 'J', 'T']
  for i in range(0,len(hand)):
    if hand[i][0] not in forbidden:
      x = x + int(hand[i][0])
      x1 = x1 + int(hand[i][0])

    elif hand[i][0] == 'A':
      x = x + 1
      x1 = x1 + 11

    if hand[i][0] == 'Q' or hand[i][0] == 'K' or hand[i][0] == 'T' or hand[i][0] == 'J':
     x = x + 10
     x1 = x1 + 10

  if x == x1:
    print(x)
    return x
  else:
    print(x,x1)
    return [x,x1]


def main():
  assert value(['AH','3D','4S']) ==[8,18]
  assert value(['KH','TD']) == 20
  assert value(['3D','8H']) == 11
  assert value(['KC','6S','QD']) == 26

if __name__ == "__name__":
  main()
