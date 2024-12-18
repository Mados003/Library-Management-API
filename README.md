# Library Management API

This project is a Flask-based RESTful API for managing a library system with CRUD operations for books. It also provides Swagger-based interactive API documentation.

---

## Features
- Add, update, delete, and retrieve books.
- Search books by filters (author, genre, year).
- Swagger UI for API documentation.

---

## Requirements
- **Docker** installed.

---

## Instructions

### 1. Building and Running the Dockerized API

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Mados003/Library-Management-API.git
   cd Library-Management-API
   ```

2. **Build the Docker Image:**
   ```bash
   docker build -t library-api .
   ```

3. **Run the Docker Container:**
   ```bash
   docker run -p 5000:5000 library-api
   ```

4. **Verify the API is Running:**
   - Swagger UI: [http://localhost:5000/api-docs](http://localhost:5000/api-docs)
   - Example Endpoint: `GET /books` at [http://localhost:5000/books](http://localhost:5000/books)

---

### 2. Accessing Swagger API Documentation

1. **Open Swagger UI:**
   Navigate to:
   ```
   http://localhost:5000/api-docs
   ```

2. **Test Endpoints:**
   - Use **Try it out** in Swagger UI.
   - Example: `POST /books` with the following payload:
     ```json
      {
          "title": "gohary is the Goat",
          "author": "ahmed sameh",
          "published_year": "2004",
          "isbn": "3",
          "genre": "Football"
      }
     ```

---

## API Endpoints

| Method   | Endpoint        | Description             |
|----------|-----------------|-------------------------|
| `GET`    | `/books`        | Retrieve all books.     |
| `POST`   | `/books`        | Add a new book.         |
| `GET`    | `/books/<isbn>` | Retrieve a book by ISBN.|
| `PUT`    | `/books/<isbn>` | Update a book by ISBN.  |
| `DELETE` | `/books/<isbn>` | Delete a book by ISBN.  |
| `GET`    | `/books/search` | Search books by filters.|

