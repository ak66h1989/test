from pandas import *
from numpy import *
import timeit

def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)

def moveDisk(fp,tp):
    print("moving disk from",fp,"to",tp)

moveTower(3,"A","C","B")


def toStr(n,base):
   convertString = "0123456789ABCDEF"
   if n < base:
      return convertString[n]
   else:
        print(convertString[n%base])
        return toStr(n//base,base) + convertString[n%base]

print(toStr(769,10))

def recDC(coinValueList,change,knownResults):
   minCoins = change
   if change in coinValueList:
      knownResults[change] = 1
      return 1
   elif knownResults[change] > 0:
      return knownResults[change]
   else:
       for i in [c for c in coinValueList if c <= change]:
         numCoins = 1 + recDC(coinValueList, change-i,
                              knownResults)
         if numCoins < minCoins:
            minCoins = numCoins
            knownResults[change] = minCoins
   return minCoins

print(recDC([1,5,10,25],63,[0]*64))



def f(n):
    y=n
    if n>0:
        n -= 1
        print(n)
        f(n)
    else:
        return -100


a = f(10)
print(a)

y = 1


def recDC(coinValueList,change,knownResults):
    knownResults[0]=1
    f(10, knownResults)
    return knownResults

def f(n, knownResults):
    knownResults[1] = n
print(recDC([1,5,10,25],63,[0]*64))

def dpMakeChange(coinValueList,change,minCoins,coinsUsed):
    for cents in range(change+1):
        coinCount = cents
        newCoin = 1
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
               coinCount = minCoins[cents-j]+1
               newCoin = j
        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin
        print('change:', change, 'cents:', cents, 'minCoins:', minCoins, 'coinsUsed:', coinsUsed)
    return minCoins[change]

def main(amnt):
    clist = [1,5,10,21,25]
    coinsUsed = [0]*(amnt+1)
    coinCount = [0]*(amnt+1)
    dpMakeChange(clist, amnt, coinCount, coinsUsed)
main(10)

def dpMakeChange(coinValueList,change,minCoins,coinsUsed):
   for cents in range(change+1):
      coinCount = cents
      newCoin = 1
      for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
               coinCount = minCoins[cents-j]+1
               newCoin = j
      minCoins[cents] = coinCount
      coinsUsed[cents] = newCoin
   return minCoins[change]

%timeit recDC([1,5,10,25],63,[0]*64)
%prun -l 4 recDC([1,5,10,25],63,[0]*64)

%timeit dpMakeChange([1,5,10,21,25],63,[0]*(63+1),[0]*(63+1))
%prun -l 4 recDC([1,5,10,25],63,[0]*64)