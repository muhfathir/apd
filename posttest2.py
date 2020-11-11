import os

biodata_mahasiswa = []
persegi = []
energi_kinetik = []

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    clear_screen()
    print(">>>Silahkan Pilih<<<")
    print("1. Biodata Mahasiswa")
    print("2. Menghitung Keliling dan Luas Persegi")
    print("3. Menghitung Rumus Energi Kinetik")
    print("4. Keluar")
    pilih = input("Pilih menu> ")

    if(pilih == "1"):
        biodata()
    elif(pilih == "2"):
        menghitung_keliling_luas_persegi()
    elif(pilih == "3"):
        rumus_energi_kinetik()
    elif(pilih == "4"):
        print("Terimakasih sudah menggunakan aplikasi ini")
        exit()
    else:
        print("Kamu memilih menu yang salah!")
        back_to_menu()

def back_to_menu():
    print("\n")
    input("Tekan Enter untuk kembali...")
    menu()

def biodata():
    clear_screen()
    print("---Biodata---")
    nama = str(input("\nMasukan Nama Anda: "))
    biodata_mahasiswa.insert(0,nama)
    nim = int(input("Masukan NIM Anda: "))
    biodata_mahasiswa.insert(1,nim)
    kelas = str(input("Masukan Kelas Anda: "))
    biodata_mahasiswa.insert(2,kelas)
    clear_screen()
    print("---Biodata---")
    print("Nama: %s" % (biodata_mahasiswa[0]))
    print("NIM: %d" % (biodata_mahasiswa[1]))
    print("Kelas: %s" % (biodata_mahasiswa[2]))
    back_to_menu()

def menghitung_keliling_luas_persegi():
    clear_screen()
    print("---Menghitung Keliling dan Luas Persegi---")
    s = int(input("\nMasukan Panjang Sisi: ")) 

    luas = s**2
    persegi.insert(0,luas)
    keliling = 4 * s
    persegi.insert(1,keliling)

    print("\nLuas Persegi \t\t:",persegi[0])
    print("Keliling Persegi\t:",persegi[1])
    back_to_menu()

def rumus_energi_kinetik():
    clear_screen()
    print("---Menghitung Rumus Energi Kinetik---")
    m = int(input("Masukkan massa benda (kg) : "))
    v = float(input("Masukkan kecepatan benda (m/s) : "))

    Ek = 0.5*m*v**2
    energi_kinetik.insert(0,Ek)

    print("\nEnergi Kinetik \t\t: ", energi_kinetik[0])
    back_to_menu()

if __name__ == "__main__":
    while True:
        menu()
