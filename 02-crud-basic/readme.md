Berikut adalah dokumentasi `README.md` lengkap untuk project FastAPI kamu di tahap 2 (`02-crud-basic`) — cocok untuk kamu taruh di GitHub atau dokumentasi internal:

---

```markdown
# FastAPI Basic CRUD – In-Memory

📦 *FastAPI CRUD API sederhana menggunakan struktur modular dan penyimpanan data in-memory.*

---

## 📁 Struktur Project

```

02-crud-basic/
├── main.py               # Entry point FastAPI
├── routers/
│   └── user.py           # CRUD logic + endpoint
└── schemas/
└── user.py           # Schema untuk validasi data

````

---

## 🚀 Cara Menjalankan

### 1. Aktifkan virtual environment

```bash
source /opt/fastapi/bin/activate
````

### 2. Jalankan Uvicorn dengan hot reload

```bash
cd /home/online/learn/fastapi/02-crud-basic
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

---

## 📚 Dokumentasi API (Swagger UI)

Buka:
[http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🔧 Endpoint CRUD

### ✅ POST `/users/`

Buat user baru

**Request Body:**

```json
{
  "id": 1,
  "name": "Didiet",
  "email": "didiet@example.com",
  "age": 30
}
```

**Response:**

```json
{
  "message": "User created",
  "user": { ... }
}
```

---

### ✅ GET `/users/`

Ambil semua user
**Response:** List user

---

### ✅ GET `/users/{user_id}`

Ambil user berdasarkan ID
**Response:** 1 user atau `404 Not Found`

---

### ✅ PUT `/users/{user_id}`

Update data user berdasarkan ID
**Body:** sama seperti POST
**Response:** user yang diperbarui

---

### ✅ DELETE `/users/{user_id}`

Hapus user berdasarkan ID
**Response:** pesan sukses

---

## 🧠 Catatan

* Data disimpan dalam list Python biasa (`users: list[User] = []`)
* Saat app dimatikan, semua data hilang
* Cocok untuk latihan dan testing struktur FastAPI modular

---

## 📦 Requirement

Pastikan `requirements-fastapi.txt` berisi:

```
fastapi
uvicorn[standard]
```

---

## 📌 Next Step

Lanjut ke:

> 🔄 Tahap 3: Integrasi SQLite atau PostgreSQL + SQLAlchemy ORM

---

## 🧑 Author

Built with ❤️ by Didiet | Belajar FastAPI secara terstruktur.

```

---

Kalau kamu setuju, saya bisa langsung simpan jadi file `README.md` di project kamu atau bantu buat versi markdown + PDF. Siap lanjut ke Tahap 3: Database?
```
