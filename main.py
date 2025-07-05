from llamado_api import OpenLibraryClient

def main():
    client = OpenLibraryClient()
    user_input = input("Captura un libro a buscar: ")

    try:
        books = client.search_by_title(user_input)
        if books:
            print("\nResultado de busqueda:")
            for book in books[:10]:  # Display up to 10 results
                print(f"- {book['title']} by {book['author']}")
        else:
            print("No se encontraron resultados.")
    except ValueError as ve:
        print(f"Error de captura: {ve}")

if __name__ == "__main__":
    main()
