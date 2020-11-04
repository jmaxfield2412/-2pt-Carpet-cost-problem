#Carpet cost problem
#Write a subroutine that outputs the cost of fitting a carpet using 3 parameters
#L = int(input("What is the length?")
#W = int(input("What is the width?")
#C = int("What is the price of the carpet per metre squared?")
L = 7
W = 6
C = 17

#Subroutine that finds the size of the room
def SizeInM2(L):
  return (L * W)

#Subroutine to calculate price
def Price(S):
  return ((S * (C+3)) + (L * 2) + (W * 2) + 50)

#Main Programme
S = SizeInM2(L)
P = Price(S)
print("The price of a",L,"m by",W,"m carpet at £",C,"per metre squared is £",P)