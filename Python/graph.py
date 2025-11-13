import tkinter as tk
from tkinter import ttk, messagebox

# IMPORTAR funciones de laligainfo.py
from laligainfo import obtener_tabla_posiciones, obtener_goleadores, guardar_csv

class LaLigaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Liga Española 2024/25")
        self.root.geometry("950x600")

        # Frame de botones
        frame_botones = tk.Frame(root)
        frame_botones.pack(pady=10)

        tk.Button(frame_botones, text="Tabla de posiciones", command=self.mostrar_posiciones, width=20).grid(row=0, column=0, padx=5)
        tk.Button(frame_botones, text="Tabla de goleadores", command=self.mostrar_goleadores, width=20).grid(row=0, column=1, padx=5)
        tk.Button(frame_botones, text="Descargar tablas", command=self.descargar_tablas, width=20).grid(row=0, column=2, padx=5)
        tk.Button(frame_botones, text="Salir", command=root.quit, width=20).grid(row=0, column=3, padx=5)

        # Frame de la tabla con scroll
        self.frame_tabla = tk.Frame(root)
        self.frame_tabla.pack(pady=10, fill=tk.BOTH, expand=True)

        self.scroll_y = tk.Scrollbar(self.frame_tabla, orient=tk.VERTICAL)
        self.scroll_x = tk.Scrollbar(self.frame_tabla, orient=tk.HORIZONTAL)

        self.tree = ttk.Treeview(
            self.frame_tabla,
            yscrollcommand=self.scroll_y.set,
            xscrollcommand=self.scroll_x.set
        )
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scroll_y.config(command=self.tree.yview)
        self.scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        self.scroll_x.config(command=self.tree.xview)
        self.scroll_x.pack(side=tk.BOTTOM, fill=tk.X)

    def mostrar_tabla(self, df):
        # Limpiar tabla
        self.tree.delete(*self.tree.get_children())
        self.tree["columns"] = list(df.columns)
        self.tree["show"] = "headings"

        for col in df.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor="center")

        for _, row in df.iterrows():
            self.tree.insert("", tk.END, values=list(row))

    def mostrar_posiciones(self):
        df = obtener_tabla_posiciones()
        if df.empty:
            messagebox.showwarning("Advertencia", "No hay datos de posiciones disponibles.")
        else:
            self.mostrar_tabla(df)

    def mostrar_goleadores(self):
        df = obtener_goleadores()
        if df.empty:
            messagebox.showwarning("Advertencia", "No hay datos de goleadores disponibles.")
        else:
            self.mostrar_tabla(df)

    def descargar_tablas(self):
        try:
            guardar_csv(obtener_tabla_posiciones(), "tabla_posiciones.csv")
            guardar_csv(obtener_goleadores(), "tabla_goleadores.csv")
            messagebox.showinfo("Descarga completada", "Las tablas se han descargado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al descargar: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = LaLigaApp(root)
    root.mainloop()
