total=int(input("total = "))
setelah_diskon = total

if (1000000>total<2000000):
	diskon=total*(5/100)
elif (total>2000000):
	diskon=total*(10/100)
else:
	diskon=total*(0/100)

setelah_diskon=total-diskon

print("diskonnya yaitu: ",diskon)
print("harga setelah diskon: ",setelah_diskon)