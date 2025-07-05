# con este codigo, creamos una pequenia pantalla para hacer la busqueda de lbros
import tkinter as tk
from tkinter import messagebox
from llamado_api import OpenLibraryClient

class BookSearchApp:
    def __init__(self, root):
        self.client = OpenLibraryClient()
        self.root = root
        self.root.title("OpenLibrary Book Search")

        # Title input
        self.label = tk.Label(root, text="Enter Book Title:")
        self.label.pack(pady=5)

        self.title_entry = tk.Entry(root, width=50)
        self.title_entry.pack(pady=5)

        # Search button
        self.search_button = tk.Button(root, text="Search", command=self.search_books)
        self.search_button.pack(pady=5)

        # Results listbox
        self.results_listbox = tk.Listbox(root, width=80, height=15)
        self.results_listbox.pack(pady=10)

    def search_books(self):
        title = self.title_entry.get()
        self.results_listbox.delete(0, tk.END)

        try:
            results = self.client.search_by_title(title)
            if results:
                for book in results[:10]:  # Show top 10 results
                    display_text = f"{book['title']} by {book['author']}"
                    self.results_listbox.insert(tk.END, display_text)
            else:
                self.results_listbox.insert(tk.END, "No results found.")
        except ValueError as ve:
            messagebox.showerror("Input Error", str(ve))

if __name__ == "__main__":
    root = tk.Tk()
    app = BookSearchApp(root)
    root.mainloop()
