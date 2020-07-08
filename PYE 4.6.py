#Creating the computepay function
def computepay (h,r):
    if h > 40:
        reg = r * h
        otp = (h - 40) * (r * 0.5)
        xp = reg + otp
    else:
        xp = h * r
    return xp
hrs = input("Enter Hours")
h = float(hrs)
rate = input("Enter Rate")
r = float(rate)
p = computepay(h, r)
print("Pay:", p)