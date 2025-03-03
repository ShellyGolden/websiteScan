# 🌍 Website Scanner

This project is a **full-stack web application** that scans a given domain and retrieves various details about it using the `httpx` CLI tool.\
It consists of:

- **Backend:** FastAPI (Python) server
- **Frontend:** React.js client

---

## 🚀 **Setup & Running the Project**

### 1️⃣ **Clone the Repository**

```bash
git clone https://github.com/YOUR_USERNAME/website-scanner.git
cd website-scanner
```

---

## 🖥 **Backend Setup (FastAPI)**

### 2️⃣ **Install GO (If not installed)**

`httpx` requires **Go** to be installed. If you don’t have it, install it from: 🔗 [**Download Go**](https://go.dev/dl/)

📌 **Verify installation with:**

```bash
go version
```

### 3️⃣ **Create & Activate Virtual Environment**

```bash
python -m venv .venv
source .venv/bin/activate  # For macOS/Linux
# On Windows (PowerShell)
.venv\Scripts\Activate
```

### 4️⃣ **Install Backend Dependencies**

```bash
pip install -r server/requirements.txt
```

### 5️⃣ **Install HTTPX CLI Tool**

The server uses the `httpx` CLI to scan websites. Install it via:

```bash
go install github.com/projectdiscovery/httpx/cmd/httpx@latest
```

📌 **Ensure **``** is in your system's **``** by running:**

```bash
httpx -version
```

If not found, add `~/go/bin/` (or `C:\Users\YourUser\go\bin\` on Windows) to your system `PATH`.

### 6️⃣ **Run the Server**

```bash
cd server
uvicorn main:app --reload
```

The server will run on:\
📍 ``

---

## 🎨 **Frontend Setup (React Client)**

### 7️⃣ **Navigate to **``** & Install Dependencies**

```bash
cd ../client
npm install
```

### 8️⃣ **Run the React App**

```bash
npm start
```

The frontend will be available at:\
📍 ``

---

## 🛠 **Testing the Solution**

1. Open the browser and go to ``.
2. Enter a domain (e.g., `google.com`) and click "Scan".
3. The application will fetch website details and display them.

### 🐞 **Troubleshooting**

- If **GO is not found**, install it from [Go Official Website](https://go.dev/dl/).
- If **HTTPX is not found**, ensure it’s installed and in your `PATH`.
- If **CORS issues occur**, restart the backend and ensure the CORS middleware is active.

---

## 📄 **Project Structure**

```
website-scanner/
│── client/       # React frontend
│── server/       # FastAPI backend
│── README.md     # This file
│── .gitignore
│── requirements.txt
```

📢 **Developed by SHELLY GOLDEN 🚀**

