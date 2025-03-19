def asosiy_menyu():
    print("1. Tovar tanlash\n2. Chiqish")
    tanlov = input("Tanlovni kiriting: ")
    if tanlov == '1':
        tovar_aformit()
    else:
        print("Dastur tugadi.")

def tovar_aformit():
    tovarlar = {
        "1": ("Telefon", 500),
        "2": ("Noutbuk", 1000),
        "3": ("Quloqchin", 100)
    }

    print("Tovarlar ro'yxati:")
    for id, (nom, narx) in tovarlar.items():
        print(f"{id}. {nom} - {narx}$")

    tanlov = input("Tovarni tanlang (ID): ")
    if tanlov not in tovarlar:
        print("Noto'g'ri tanlov.")
        return asosiy_menyu()

    miqdor = int(input("Miqdorini kiriting: "))
    nom, narx = tovarlar[tanlov]
    umumiy_narx = narx * miqdor

    print(f"\nTanlangan tovar: {nom}")
    print(f"Miqdor: {miqdor}")
    print(f"Umumiy narx: {umumiy_narx}$")

    tasdiq = input("Tovarni rasmiylashtirasizmi? (ha/yo'q): ")
    if tasdiq.lower() == 'ha':
        print("Tovar muvaffaqiyatli rasmiylashtirildi!")
    else:
        print("Rasmiylashtirish bekor qilindi.")

    asosiy_menyu()

asosiy_menyu()

import os

def asosiy_menyu():
    while True:
        print("\n--- Bosh menyu ---")
        print("1. Tovar tanlash va aformit qilish")
        print("2. Chiqish")

        tanlov = input("Tanlovni kiriting (1/2): ")
        
        if tanlov == '1':
            tovar_aformit()  # Tovar aformit bo'limiga o'tadi
        elif tanlov == '2':
            print("Dastur tugadi.")
            break
        else:
            print("Noto'g'ri tanlov! Qayta urinib ko'ring.")


def tovar_aformit():
    os.system('cls' if os.name == 'nt' else 'clear')  # Konsolni tozalaydi
    print("\n--- Tovar aformit qilish ---")

    # Tovarlar ro'yxati
    tovarlar = {
        "1": ("Telefon", 500),
        "2": ("Noutbuk", 1200),
        "3": ("Quloqchin", 150)
    }

    for id, (nom, narx) in tovarlar.items():
        print(f"{id}. {nom} - {narx}$")

    tanlov = input("Tovarni tanlang (ID): ")
    if tanlov not in tovarlar:
        print("Noto'g'ri tanlov! Bosh menyuga qaytish...")
        asosiy_menyu()

    miqdor = int(input("Miqdorini kiriting: "))
    nom, narx = tovarlar[tanlov]
    umumiy_narx = narx * miqdor

    print(f"\nSiz tanlagan tovar: {nom}")
    print(f"Miqdor: {miqdor}")
    print(f"Umumiy narx: {umumiy_narx}$")

    tasdiq = input("Tovarni aformit qilasizmi? (ha/yo'q): ")
    if tasdiq.lower() == 'ha':
        print("✅ Tovar muvaffaqiyatli rasmiylashtirildi!")
    else:
        print("❌ Rasmiylashtirish bekor qilindi.")

    # Bosh menyuga qaytish
    asosiy_menyu()


# Dastur ishga tushadi
asosiy_menyu()
import tkinter as tk

# Tovar aformit qilish funksiyasi
def tovar_aformit():
    aformit_oyna = tk.Toplevel(root)
    aformit_oyna.title("Tovar Aformit Qilish")
    aformit_oyna.geometry("400x300")

    tk.Label(aformit_oyna, text="Tovar tanlandi!", font=("Arial", 16)).pack(pady=20)
    tk.Button(aformit_oyna, text="Bosh menyuga qaytish", command=aformit_oyna.destroy).pack(pady=10)

# Asosiy oyna (Bosh menyu)
root = tk.Tk()
root.title("Bosh menyu")
root.geometry("400x300")

tk.Label(root, text="Buyurtma qilish tizimi", font=("Arial", 20)).pack(pady=20)

# "Buy Now" tugmasi bosilganda tovar_aformit funksiyasiga o'tadi
tk.Button(root, text="Buy Now", command=tovar_aformit, font=("Arial", 14)).pack(pady=10)

root.mainloop()

import tkinter as tk

# Tovarni aformit qilish funksiyasi
def tovar_aformit():
    aformit_oyna = tk.Toplevel(root)  # Yangi oyna ochadi
    aformit_oyna.title("Tovar Aformit Qilish")
    aformit_oyna.geometry("400x200")

    tk.Label(aformit_oyna, text="✅ Tovar muvaffaqiyatli rasmiylashtirildi!", font=("Arial", 14)).pack(pady=40)
    tk.Button(aformit_oyna, text="Bosh menyuga qaytish", command=aformit_oyna.destroy).pack(pady=20)

# Asosiy oyna (bosh menyu)
root = tk.Tk()
root.title("Bosh menyu")
root.geometry("400x300")

tk.Label(root, text="Buyurtma qilish tizimi", font=("Arial", 20)).pack(pady=30)

# "Buy Now" tugmasi bosilganda tovar_aformit() funksiyasiga o'tadi
buy_now_button = tk.Button(root, text="Buy Now", command=tovar_aformit, font=("Arial", 16))
buy_now_button.pack(pady=20)

root.mainloop()