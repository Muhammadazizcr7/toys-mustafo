import tkinter as tk
from tkinter import messagebox

# Tovarlar ma'lumotlari (Nomi, Narxi)
tovarlar = {
    "Telefon": 800,
    "Noutbuk": 1500,
    "Quloqchin": 100,
    "Smart Watch": 300,
    "Televizor": 2000
}

# Savatni saqlash uchun lug'at
savat = {}

# Savatga tovar qo'shish funksiyasi
def savatga_qosh(tovar, miqdor):
    if tovar in savat:
        savat[tovar] += miqdor
    else:
        savat[tovar] = miqdor
    messagebox.showinfo("✅ Qo'shildi", f"{tovar} dan {miqdor} dona savatga qo'shildi!")

# Savatni ko'rish va hisoblash
def savatni_korish():
    if not savat:
        messagebox.showinfo("❗ Bo'sh savat", "Sizning savatingiz bo'sh!")
        return
    
    umumiy_narx = sum(tovarlar[tovar] * miqdor for tovar, miqdor in savat.items())
    savat_ma'lumot = "\n".join([f"{tovar} - {miqdor} dona - {tovarlar[tovar]}$" for tovar, miqdor in savat.items()])
    
    messagebox.showinfo("🛒 Savat", f"{savat_ma'lumot}\n\nUmumiy narx: {umumiy_narx}$")
    
    # Rasmiylashtirishni taklif qilish
    if messagebox.askyesno("✅ Rasmiylashtirish", "Tovarlarni aformit qilasizmi?"):
        tovar_aformit(umumiy_narx)

# Buyurtmani rasmiylashtirish
def tovar_aformit(umumiy_narx):
    messagebox.showinfo("✅ Muvaffaqiyatli", f"Buyurtma qabul qilindi!\nUmumiy summa: {umumiy_narx}$")
    savat.clear()  # Savatni tozalash
    asosiy_menyu()  # Bosh menyuga qaytish

# Asosiy menyuni yaratish
def asosiy_menyu():
    # Eski oynani tozalash
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="📦 Amazon-Style Buyurtma Tizimi", font=("Arial", 20)).pack(pady=20)
    tk.Label(root, text="Tanlang va savatga qo'shing:", font=("Arial", 14)).pack(pady=10)

    for tovar, narx in tovarlar.items():
        frame = tk.Frame(root)
        frame.pack(pady=5)
        
        tk.Label(frame, text=f"{tovar} - {narx}$", font=("Arial", 12)).pack(side=tk.LEFT, padx=10)

        miqdor_kirit = tk.Entry(frame, width=5)
        miqdor_kirit.pack(side=tk.LEFT)

        btn_qoshish = tk.Button(frame, text="➕ Savatga qo'shish", 
                                command=lambda t=tovar, e=miqdor_kirit: savatga_qosh(t, int(e.get() or 0)))
        btn_qoshish.pack(side=tk.LEFT, padx=5)

    tk.Button(root, text="🛒 Savatni ko'rish", command=savatni_korish, font=("Arial", 14)).pack(pady=20)
    tk.Button(root, text="❌ Chiqish", command=root.quit, font=("Arial", 14)).pack(pady=10)

# Dastur oynasini boshlash
root = tk.Tk()
root.title("Amazon-Style Buyurtma Tizimi")
root.geometry("600x500")

asosiy_menyu()

root.mainloop()