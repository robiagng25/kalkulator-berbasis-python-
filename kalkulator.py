def app_penjumlahan():
    print("*** Program Penjumlahan ***")
    try:
        angka1 = int(input("angka1: "))
        angka2 = int(input("angka2: "))
        hasil = angka1 + angka2
        print("hasil penjumlahan", hasil)
    except ValueError:
        print("Eror: Masukan angka yang valid")
    print("*** Program penjumlahan selesai ***")
    input("Enter untuk lanjut")
    
def app_pengurangan():
    print("*** Program Pengurangan ***")
    try:
        angka1 = int(input("angka1: "))
        angka2 = int(input("angka2: "))
        hasil = angka1 - angka2
        print("hasil pengurangan", hasil)
    except ValueError:
        print("Eror: Masukan angka yang valid")
    print("*** Program pengurangan selesai ***")
    input("Enter untuk lanjut")
    
def app_perkalian():
    print("*** Program Perkalian ***")
    try:
        angka1 = int(input("angka1: "))
        angka2 = int(input("angka2: "))
        hasil = angka1 * angka2
        print("hasil perkalian", hasil)
    except ValueError:
        print("Eror: masukan angka yang valid")
    print("*** Program perkalian selesai ***")
    input("Enter untuk lanjut")
    
def app_pembagian():
    print("*** Program Pembagian ***")
    try:
        angka1 = int(input("angka1: "))
        angka2 = int(input("angka2: "))
        hasil = angka1 / angka2
        print("hasil pembagian", hasil)
    except ValueError:
        print("Eror: masukan angka yang valid")
    except ZeroDivisionError:
        print("Eror: Tidak bisa membeagi dengan nol")
    print("*** Program pembagian selesai ***")
    input("Enter untuk lanjut")
    
def app_menu():
    while True:
        print("*** Program Kalkulator sedrhana for all ***")
        print("1. Penjumlahan")
        print("2. pengurangan")
        print("3. Perkalian")
        print("4. Pembagian")
        print("5. keluar")
        print("*** Program Kalkulator Sederhana ***")
        
        try:
            pilihan = int(input("Pilihan: "))

            if pilihan == 1:
                app_penjumlahan()
            elif pilihan == 2:
                app_pengurangan()
            elif pilihan == 3:
                app_perkalian()
            elif pilihan == 4:
                app_pembagian()
            elif pilihan == 5:
                print("=== SAMPAI JUMPA LAGI ===")
                break
            else:
                print("Error: Pilihan tidak valid")
        except ValueError:
            print("Error: Masukkan nomor pilihan yang valid")

app_menu()
