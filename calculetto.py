import tkinter as tk
from tkinter import messagebox

def calculer_moyenne():
    try:
        if not entries:
            messagebox.showinfo("Résultat", "Aucune note saisie.")
            return
        
        notes_coefficients = []
        for entry_pair in entries:
            note = float(entry_pair[0].get())
            coeff = float(entry_pair[1].get())
            notes_coefficients.append((note, coeff))
        
        total_points = sum(note * coeff for note, coeff in notes_coefficients)
        total_coefficients = sum(coeff for _, coeff in notes_coefficients)
        
        moyenne = total_points / total_coefficients if total_coefficients != 0 else 0
        messagebox.showinfo("Résultat", f"La moyenne pondérée est : {moyenne:.2f}")
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer des valeurs valides.")

def ajouter_champs():
    frame_entry = tk.Frame(frame, bg="#f0f0f0")
    frame_entry.pack(pady=5)

    label_note = tk.Label(frame_entry, text="Note :", font=("Arial", 10), bg="#f0f0f0")
    label_note.pack(side=tk.LEFT, padx=5)
    entry_note = tk.Entry(frame_entry, width=10, font=("Arial", 12))
    entry_note.pack(side=tk.LEFT, padx=5)

    label_coeff = tk.Label(frame_entry, text="Coefficient :", font=("Arial", 10), bg="#f0f0f0")
    label_coeff.pack(side=tk.LEFT, padx=5)
    entry_coeff = tk.Entry(frame_entry, width=10, font=("Arial", 12))
    entry_coeff.pack(side=tk.LEFT, padx=5)

    btn_supprimer = tk.Button(frame_entry, text="X", font=("Arial", 10), bg="#f44336", fg="white", 
                              command=lambda: supprimer_champs(frame_entry, entry_note, entry_coeff))
    btn_supprimer.pack(side=tk.LEFT, padx=5)

    entries.append((entry_note, entry_coeff, frame_entry))

def supprimer_champs(frame_entry, entry_note, entry_coeff):
    entry_note.destroy()
    entry_coeff.destroy()
    frame_entry.destroy()

def reinitialiser():
    for entry_pair in entries[:]:
        supprimer_champs(*entry_pair)
    entries.clear()

def reset_entries():
    global entries
    entries = []

root = tk.Tk()
root.title("Calcul de Moyenne Pondérée")
root.geometry("400x500")
root.configure(bg="#f0f0f0")

frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=20)

entries = []

btn_ajouter = tk.Button(root, text="Ajouter une note", command=ajouter_champs, font=("Arial", 12), bg="#4CAF50", fg="white", padx=10, pady=5)
btn_ajouter.pack(pady=5)

btn_calculer = tk.Button(root, text="Calculer la moyenne", command=calculer_moyenne, font=("Arial", 12), bg="#008CBA", fg="white", padx=10, pady=5)
btn_calculer.pack(pady=5)

btn_reinitialiser = tk.Button(root, text="Réinitialiser", command=lambda: [reinitialiser(), reset_entries()], font=("Arial", 12), bg="#f44336", fg="white", padx=10, pady=5)
btn_reinitialiser.pack(pady=5)

root.mainloop()
