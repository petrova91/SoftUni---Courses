a_sm = int(input())
b_sm = int(input())
c_sm = int(input())
percent = float(input())
V_sm = a_sm * b_sm * c_sm
V_dc = V_sm / 1000
litters = V_dc - (V_dc * percent)/100
print (litters)