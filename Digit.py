#Def function untuk digit Awal
def digitAwal(x,y):
    z = x**y            # x pangkat y
    str_z = str(z)      # mengubah hasil pangkat ke string
    return(str_z[0])    # mengambil angka paling depan dari string

print(digitAwal(10,8))  # Print hasil
print(digitAwal(2,3))
print(digitAwal(6,3))


#Def function untuk digit Akhir
def digitAkhir(x,y):
    z = x**y            # x pangkat y (bisa sama dengan digit awal karena beda def function(internal))
    str_z = str(z)      # mengubah hasil pangkat ke string
    return(str_z[-1])   # mengambil angka paling akhir dari string

print(digitAkhir(10,8)) # Print hasil
print(digitAkhir(2,3))
print(digitAkhir(6,3))