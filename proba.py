import math
def binomial(n,x,p):
  return (math.factorial(n)/(math.factorial(x)*math.factorial(n-x)))*pow(p,x)*pow(1-p,n-x)

def poisson(media,j):
  return (math.exp(-media)*pow(media,j))/math.factorial(j)


while 1:
  op=input("1 binomial, 2 poisson, 3 soma binomial, 4 soma poisson: ")
  if op == '1':
    n=float(input("N: "))
    x=float(input("X: "))
    p=float(input("P: "))
    print(binomial(n,x,p))

  elif op=='2':
    media=float(input("Media: "))
    j=float(input("J: "))
    print(poisson(media,j))

  elif op=='3':
    vet=[]
    num=int(input("numero de somas: "))
    n=float(input("N: "))
    p=float(input("P: "))
    for i in range(0,num):
      x=float(input("X{}: ".format(i+1)))
      vet.append(binomial(n,x,p))
    print(sum(vet))

  elif op=='4':
    vet=[]
    num=int(input("numero de somas: "))
    media=float(input("Media: "))
    for i in range(0,num):
      j=float(input("j{}: ".format(i+1)))
      vet.append(poisson(media,j))
    print(sum(vet))