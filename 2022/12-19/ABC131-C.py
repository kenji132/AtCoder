import math
A,B,C,D = map(int, input().split())
gcd = math.gcd(C,D)
lcm = C*D//gcd
print(B-A+1 - (((B // C) - ((A-1) // C)) + ((B // D) - ((A-1) // D)) - ((B // lcm) - ((A-1) // lcm))))