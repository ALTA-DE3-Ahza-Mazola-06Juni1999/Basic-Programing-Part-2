'''
Input Harga: 370000
Input Diskon: 15
Output: harga yang harus dibayar adalah Rp. 314.500
'''
harga = int(input("Masukkan harga "))
diskon = int(input("Masukkan diskon "))

harga_diskon =(harga * diskon) / 100
harga_bayar = harga - harga_diskon
print(harga_bayar)