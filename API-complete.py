import requests

base_url = "http://127.0.0.1:5000"
end_point = "/api/books"

while True:
    print("\nMenu:")
    print("1. GET all books")
    print("2. GET a specific book by ID")
    print("3. POST to create a new book")
    print("4. PATCH to update a book by ID")
    print("5. PUT to update a book by ID (replace the entire book)")
    print("6. DELETE a book by ID")
    print("7. Quit")

    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        try:
            response = requests.get(base_url + end_point)
            print("OUTPUT:", response.json())
        except Exception as e:
            print("An error occurred:", e)
        finally:
            print("Status Code:", response.status_code)

    elif choice == '2':
        book_id = input("Enter the book ID: ")
        try:
            response = requests.get(base_url + end_point + f'/{book_id}')
            print("OUTPUT:", response.json())
        except Exception as e:
            print("An error occurred:", e)
        finally:
            print("Status Code:", response.status_code)

    elif choice == '3':
        title = input("Enter the title: ")
        author = input("Enter the author: ")
        published_year = input("Enter the published year: ")
        data = {"title": title, "author": author, "published_year": published_year}
        try:
            response = requests.post(base_url + end_point, json=data)
            print("OUTPUT:", response.json())
        except Exception as e:
            print("An error occurred:", e)
        finally:
            print("Status Code:", response.status_code)

    elif choice == '4':
        book_id = input("Enter the book ID to update: ")
        title = input("Enter the new title (press Enter to skip): ")
        author = input("Enter the new author (press Enter to skip): ")
        published_year = input("Enter the new published year (press Enter to skip): ")
        data = {}
        if title:
            data["title"] = title
        if author:
            data["author"] = author
        if published_year:
            data["published_year"] = published_year

        try:
            response = requests.patch(base_url + end_point + f'/{book_id}', json=data)
            print("OUTPUT:", response.json())
        except Exception as e:
            print("An error occurred:", e)
        finally:
            print("Status Code:", response.status_code)

    elif choice == '5':
        book_id = input("Enter the book ID to update: ")
        title = input("Enter the new title: ")
        author = input("Enter the new author: ")
        published_year = input("Enter the new published year: ")
        data = {"title": title, "author": author, "published_year": published_year}
        try:
            response = requests.put(base_url + end_point + f'/{book_id}', json=data)
            print("OUTPUT:", response.json())
        except Exception as e:
            print("An error occurred:", e)
        finally:
            print("Status Code:", response.status_code)

    elif choice == '6':
        book_id = input("Enter the book ID to delete: ")
        try:
            response = requests.delete(base_url + end_point + f'/{book_id}')
            print("OUTPUT:", response.json())
        except Exception as e:
            print("An error occurred:", e)
        finally:
            print("Status Code:", response.status_code)

    elif choice == '7':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 7.")
