# Challenge 4: User Registration & Authentication API

This challenge covers standard user registration, credential validation, cryptographic hashing, and login authentication for REST APIs.

## Problem Description
Implement the registration and authentication endpoints with rigorous input validation, conflict detection, password hashing, and user profile retrieval.

### User Model (`User`):
- `id`: integer (auto-increment primary key)
- `username`: string (unique, required)
- `email`: string (unique, required)
- `password`: string (hashed string, required)
- `role`: `'USER'` or `'ADMIN'` (default: `'USER'`)
- `createdAt`: Date / timestamp

---

### Endpoints

#### 1. `POST /api/auth/register`
Register a new user account.

**Request Body (JSON):**
```json
{
  "username": "sarah_connor",
  "email": "sarah@skynet.com",
  "password": "StrongPassword123!"
}
```

**Input Validation (HTTP 400 Bad Request):**
- `username`: 3-20 characters, alphanumeric and underscores only (`/^[a-zA-Z0-9_]{3,20}$/`).
- `email`: valid email string containing `@` and `.`.
- `password`: at least 8 characters, at least 1 uppercase letter (`[A-Z]`), at least 1 digit (`[0-9]`), and at least 1 special character (`[!@#$%^&*]`).
- If any check fails, return HTTP **`400 Bad Request`** with `{ "error": "Invalid registration details" }`.

**Conflict Checks (HTTP 409 Conflict):**
- If `username` already exists in database: return HTTP **`409 Conflict`** with `{ "error": "Username already taken" }`.
- If `email` already exists in database: return HTTP **`409 Conflict`** with `{ "error": "Email already in use" }`.

**Password Hashing & Response (HTTP 201 Created):**
- Passwords must NOT be stored in plain text. Use `hashPassword(password)` (SHA-256).
- Save user to the database.
- Return HTTP **`201 Created`** with the created user object, **strictly excluding the `password` field**.

---

#### 2. `POST /api/auth/login`
Authenticate existing user.

**Request Body (JSON):**
```json
{
  "username": "sarah_connor",
  "password": "StrongPassword123!"
}
```

**Validation & Authentication Rules:**
- If `username` or `password` is missing $\to$ return HTTP **`400 Bad Request`**.
- If user does not exist or `hashPassword(password) !== user.password` $\to$ return HTTP **`401 Unauthorized`** with `{ "error": "Invalid credentials" }`.
- If valid $\to$ return HTTP **`200 OK`**:
```json
{
  "message": "Login successful",
  "user": {
    "id": 1,
    "username": "sarah_connor",
    "email": "sarah@skynet.com",
    "role": "USER"
  }
}
```

---

#### 3. `GET /api/users/:id`
Fetch user profile by ID.

**Rules:**
- If user with `id` does not exist $\to$ return HTTP **`404 Not Found`** with `{ "error": "User not found" }`.
- Return HTTP **`200 OK`** with user profile object (**excluding password**).

---

### Files to Edit
- [controllers/auth.js](file:///Users/arseniizarudniuk/test/code_tasks_prep/goldman_sachs/node_task4_user_registration/controllers/auth.js)
- [routes/auth.js](file:///Users/arseniizarudniuk/test/code_tasks_prep/goldman_sachs/node_task4_user_registration/routes/auth.js)

### Running Tests
```bash
python3 run_tests.py
# or
npm test
```
