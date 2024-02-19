#mencari f(x)
def fungsi(x):
    return 2 * x**3 + 2 * x + 15 / x

#input dan hasil
x = int(input("Masukkan bilangan bulat: "))
hasil = fungsi(x)
print(f"Hasil dari f({x}) adalah {hasil}.")