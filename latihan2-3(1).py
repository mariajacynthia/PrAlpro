gaji = int(input("masukkan gaji yang diinginkan Rp "))
jam_kerja = int(input("masukkan jam kerja per minggu: ")) * 5
pendapatan_sebelum_pajak = gaji * jam_kerja
pendapatan_setelah_pajak = pendapatan_sebelum_pajak - (pendapatan_sebelum_pajak * 14 / 100)
pakaian_aksesoris = pendapatan_setelah_pajak * 10 / 100
alattulis = pendapatan_setelah_pajak * 1 / 100
sedekah = (pendapatan_setelah_pajak - (pakaian_aksesoris + alattulis)) * (25 / 100)
sedekah2 = (pendapatan_setelah_pajak - (pakaian_aksesoris + alattulis)) * (25 / 100)
yatim = 0
dhuafa = 0

while sedekah2 > 1000:
    sedekah2 -= 1000
    yatim += (1000 * (30 / 100))
    dhuafa += (1000 * (70 / 100))

print(f"pendapatan_sebelum_pajak: Rp {pendapatan_sebelum_pajak}")
print(f"pendapatan_setelah_pajak: Rp {pendapatan_setelah_pajak}")
print(f"biaya yang digunakan untuk membeli pakaian dan aksesoris: Rp {pakaian_aksesoris}")
print(f"biaya yang digunakan untuk membeli alat tulis: Rp {alattulis}")
print(f"jumlah uang yang digunakan budi untuk sedekah: Rp {sedekah}")
print(f"jumlah uang yang diberikan budi untuk kaum yatim: Rp {yatim}")
print(f"jumlah uang yang diberikan budi untuk kaum dhuafa: Rp {dhuafa}")