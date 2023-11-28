import math

a = lambda x: x**2
b = lambda x, y: math.sqrt(x*2 + y*2)
c = lambda *args: sum(args) / len(args)
d = lambda s: "".join(set(s))

#fungsi a 
result_a = a(8)
print(result_a)

#fungsi b
result_b = b(2, 2)
print(result_b)

#fungsi c
result_c = c(2,4,6,8,10)
print(result_c)

#fungsi d
result_d = d("M IQBAL AL ANSHORI")
print(*result_d," ")