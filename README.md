# -Least-Common-Multiple-Code
# My Python Solution For Finding  Least Common Multiple


#Least Common Multiple: Code

def lcm(a, b): #Here is the function for the lowest common multiple
  assert a > 0 and b > 0
  return a*b // gcd(a,b)
  
def gcd(a, b): #Here is the function I created for the greatest common divisor
  return gcd(b, a%b) if b else a

print(lcm(24, 16)) # This algorithm is efficient. You can try any two positive large numbers and see it for yourself
