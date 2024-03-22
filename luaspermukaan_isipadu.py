# Atur cara bagi mengira jumlah permukaan dan isipadu silinder

# Isytiharkan pemalar
pi=3.142
# Kod Input 
jejari=float(input("Masukkan jejari:"))
tinggi=float(input("Masukkan tinggi:"))

# Kod Proses
luas_permukaan=(2*pi*(jejari**2))+(2*pi*jejari*tinggi)
isi_padu=pi*jejari*jejari*tinggi

# Kod Output
print("Luas permukaan ialah",luas_permukaan)
print("Isipadu ialah",isi_padu)
