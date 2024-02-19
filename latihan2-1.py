#berat badan berdasarkan BMI dan tinggi badan
def beratbadan(bmi, tinggi):
    return bmi * tinggi**2

#input
tinggi = float(input("Masukkan tinggi badan anda dalam meter: "))
bmi = float(input("Masukkan nilai BMI yang diinginkan: "))

#fungsi bb
berat = beratbadan(bmi, tinggi)

#hasil
print(f"berat badan yang dibutuhkan {berat:.2f} kilogram.")