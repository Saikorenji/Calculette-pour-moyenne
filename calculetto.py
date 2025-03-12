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
    frame_entry = tk.Frame(frame, bg="#e6e6e6", padx=10, pady=5, relief="ridge", borderwidth=2)
    frame_entry.pack(pady=5, fill="x")

    label_note = tk.Label(frame_entry, text="Note :", font=("Arial", 10), bg="#e6e6e6")
    label_note.grid(row=0, column=0, padx=5)
    entry_note = tk.Entry(frame_entry, width=10, font=("Arial", 12), borderwidth=2, relief="solid")
    entry_note.grid(row=0, column=1, padx=5)

    label_coeff = tk.Label(frame_entry, text="Coefficient :", font=("Arial", 10), bg="#e6e6e6")
    label_coeff.grid(row=0, column=2, padx=5)
    entry_coeff = tk.Entry(frame_entry, width=10, font=("Arial", 12), borderwidth=2, relief="solid")
    entry_coeff.grid(row=0, column=3, padx=5)

    btn_supprimer = tk.Button(frame_entry, text="X", font=("Arial", 10, "bold"), bg="#ff4d4d", fg="white",
                              command=lambda: supprimer_champs(frame_entry, entry_note, entry_coeff))
    btn_supprimer.grid(row=0, column=4, padx=5)

    entries.append((entry_note, entry_coeff, frame_entry))

def supprimer_champs(frame_entry, entry_note, entry_coeff):
    frame_entry.destroy()
    # Vérification avant suppression pour éviter les erreurs
    if (entry_note, entry_coeff, frame_entry) in entries:
        entries.remove((entry_note, entry_coeff, frame_entry))

def reinitialiser():
    if entries:
        supprimer_champs(*entries[0])
        root.after(50, reinitialiser)  # Supprime un élément toutes les 50ms pour éviter le gel

def reset_entries():
    global entries
    entries.clear()

# Configuration de la fenêtre principale
root = tk.Tk()
root.title("Calcul de Moyenne Pondérée")
root.geometry("450x500")
root.configure(bg="#f0f0f0")

# Titre principal
title_label = tk.Label(root, text="Calcul de Moyenne Pondérée", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#333")
title_label.pack(pady=10)

# Cadre pour contenir les champs de saisie
frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=10, padx=20, fill="both")

entries = []

# Boutons
btn_ajouter = tk.Button(root, text="Ajouter une note", command=ajouter_champs, font=("Arial", 12), 
                        bg="#4CAF50", fg="white", padx=10, pady=5, width=20)
btn_ajouter.pack(pady=5)

btn_calculer = tk.Button(root, text="Calculer la moyenne", command=calculer_moyenne, font=("Arial", 12), 
                         bg="#008CBA", fg="white", padx=10, pady=5, width=20)
btn_calculer.pack(pady=5)

btn_reinitialiser = tk.Button(root, text="Réinitialiser", command=lambda: [reinitialiser(), reset_entries()], font=("Arial", 12), 
                              bg="#f44336", fg="white", padx=10, pady=5, width=20)
btn_reinitialiser.pack(pady=5)

root.mainloop()
