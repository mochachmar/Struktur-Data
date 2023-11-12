class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama

    def validate_input(self, prompt, data_type):
        while True:
            try:
                value = data_type(input(prompt))
                return value
            except ValueError:
                print(
                    "Input salah. Masukkan Nilai dengan tipe data yang benar (Float) !")

    def hitung_nilai(self):
        nilai_tugas_1 = self.validate_input("Nilai Tugas 1: ", float)
        nilai_tugas_2 = self.validate_input("Nilai Tugas 2: ", float)
        nilai_tugas_3 = self.validate_input("Nilai Tugas 3: ", float)
        nilai_uts_mid = self.validate_input("Nilai UTS (MID): ", float)
        nilai_uas_final = self.validate_input("Nilai UAS (FINAL): ", float)
        nilai_kehadiran = self.validate_input(
            "Nilai Kehadiran (Absensi): ", float)
        total_nilai_tugas = (nilai_tugas_1 + nilai_tugas_2 + nilai_tugas_3) / 3
        total_nilai_akhir = (total_nilai_tugas * 20 / 100) + (nilai_uts_mid *
                                                              30 / 100) + (nilai_uas_final * 40 / 100) + (nilai_kehadiran * 10 / 100)

        if total_nilai_akhir >= 85:
            grade = "A"
        elif total_nilai_akhir >= 80 and total_nilai_akhir <= 85:
            grade = "A-"
        elif total_nilai_akhir >= 75 and total_nilai_akhir <= 80:
            grade = "B+"
        elif total_nilai_akhir >= 70 and total_nilai_akhir <= 75:
            grade = "B"
        elif total_nilai_akhir >= 65 and total_nilai_akhir <= 70:
            grade = "B-"
        elif total_nilai_akhir >= 60 and total_nilai_akhir <= 65:
            grade = "C+"
        elif total_nilai_akhir >= 55 and total_nilai_akhir <= 60:
            grade = "C"
        elif total_nilai_akhir >= 40 and total_nilai_akhir <= 55:
            grade = "D"
        else:
            grade = "E"

        print("\nOutput Rangkuman Nilai Yang Didapat")
        print("NIM:", self.nim)
        print("Nama Mahasiswa:", self.nama)
        print("Nilai Tugas:", total_nilai_tugas)
        print("Nilai UTS (MID):", nilai_uts_mid)
        print("Nilai UAS (FINAL):", nilai_uas_final)
        print("Nilai Kehadiran (Absensi):", nilai_kehadiran)
        print("Mendapatkan Nilai Akhir:", total_nilai_akhir)
        print("Nilai Huruf (Grade):", grade)
        print("Lulus:", total_nilai_akhir >= 60)
