import tkinter as tk
from tkinter import filedialog, messagebox
from base64_util import Base64Util

class Base64App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerador de Base64")
        self.root.geometry("270x100")
        self.root.resizable(False, False)
        self.root.maxsize(270, 100)
        self.root.minsize(270, 100)         

        self.file_path = ""
        
        self.lbl_file_path = tk.Label(self.root, text="Nenhum arquivo selecionado")
        self.lbl_file_path.grid(row=0, column=0, columnspan=3, pady=5, sticky="w")

        self.btn_open_folder = tk.Button(self.root, text="Open Folder", command=self.open_folder)
        self.btn_open_folder.grid(row=1, column=0, padx=(5, 2), pady=5)

        self.btn_generate_base64 = tk.Button(self.root, text="Generate Base64", command=self.generate_base64)
        self.btn_generate_base64.grid(row=1, column=1, padx=(2, 2), pady=5)

        self.btn_copy_base64 = tk.Button(self.root, text="Copy Base64", command=self.copy_base64)
        self.btn_copy_base64.grid(row=1, column=2, padx=(2, 5), pady=5)

        self.txt_base64 = tk.Text(self.root, height=1, width=30)
        self.txt_base64.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

    def open_folder(self):
        self.file_path = filedialog.askopenfilename(title="Selecione um arquivo")
        if self.file_path:
            self.lbl_file_path.config(text=f"Arquivo: {self.file_path.split('/')[-1]}")

    def generate_base64(self):
        if self.file_path:
            try:
                encoded_data = Base64Util.encode_file(self.file_path)
                self.txt_base64.delete(1.0, tk.END)
                self.txt_base64.insert(tk.END, encoded_data)
                messagebox.showinfo("Sucesso", "Base64 gerado!")
            except Exception as e:
                messagebox.showerror("Erro", str(e))
        else:
            messagebox.showwarning("Aviso", "Nenhum arquivo selecionado.")

    def copy_base64(self):
        try:
            base64_text = self.txt_base64.get("1.0", tk.END).strip()

            if not base64_text:
                messagebox.showwarning("Aviso", "Nada para copiar. Gere o Base64 primeiro!")
                return

            self.root.clipboard_clear()
            self.root.clipboard_append(base64_text)
            self.root.update_idletasks()
            messagebox.showinfo("Sucesso", "Base64 copiado para a área de transferência!")

        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao copiar Base64: {str(e)}")