
cent = float(input("ingres el valor de centavo: "))

dol = cent / 100
euro = dol * 0.8965
yen = dol * 101.5744
br = dol * 0.7702
mex = dol * 19.7843

print ("el valor en dol: " + str(dol))
print ("el valor en euro: " + str(euro))
print ("el valor en yen: " + str(yen))
print ("el valor en br: " + str(br))
print ("el valor en br: " + str(mex))

