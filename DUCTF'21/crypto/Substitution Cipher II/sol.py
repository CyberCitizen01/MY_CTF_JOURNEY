# DUCTF{}_!?'abcdefghijklmnopqrstuvwxyz0123456789
# n = 47
# Ujyw5dnFofaou0au3nx3Cn84

# from string import ascii_lowercase, digits
# CHARSET = "DUCTF{}_!?'"+ascii_lowercase+digits
# n = len(CHARSET) # = 47


# START = "DUCTF{}"
# FLAG = "Ujyw5dnFofaou0au3nx3Cn84"


# def decrypt(msg,f):
#     final = []
#     for letter in msg:
#         equation = f - CHARSET.find(letter)
#         sol = equation.roots()
#         print(sol)
#         index = sol[0][0]
#         #print(index)
#         try:
#             final.append(CHARSET[index])
#         except:
#             final.append("@")
#     return ''.join(final)

# P.<x> = PolynomialRing(GF(n))
# f = 41*x^6 + 15*x^5 + 40*x^4 + 9*x^3 +28*x^2 +27*x +1


# print(decrypt(FLAG,f))
