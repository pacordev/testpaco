# este codigo es la clase para conectar a la api de busqueda de libros
import requests

class OpenLibraryClient:
    BASE_URL = "https://openlibrary.org/search.json"

    def __init__(self):
        pass

    def search_by_title(self, title):
        # Validate that the title is not empty
        if not title or not title.strip():
            raise ValueError("El titulo del libro no puede estar vacio.")

        # Prepare the request parameters
        params = {'title': title.strip()}

        try:
            response = requests.get(self.BASE_URL, params=params)
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()

            # Return a simplified list of book titles and authors
            results = [
                {
                    'title': doc.get('title'),
                    'author': ', '.join(doc.get('author_name', []))
                }
                for doc in data.get('docs', [])
            ]
            return results

        except requests.RequestException as e:
            print(f"Ha ocurrido un error al conectarse a la API: {e}")
            return []
