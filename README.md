# 🌍 Website Scanner

This project is a **full-stack web application** that scans a given domain and retrieves various details about it using the `httpx` CLI tool.  
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
`httpx` requires **Go** to be installed. If you don’t have it, install it from:
🔗 **[Download Go](https://go.dev/dl/)**

📌 **Verify installation with:**
```bash
go version
```

### 3️⃣ **Install HTTPX CLI Tool**
The server uses the `httpx` CLI to scan websites. Install it via:
```bash
go install github.com/projectdiscovery/httpx/cmd/httpx@latest
```

📌 **Ensure `httpx` is in your system's `PATH` by running:**
```bash
httpx -version
```
If not found, add `~/go/bin/` (or `C:\Users\YourUser\go\bin\` on Windows) to your system `PATH`.

### 4️⃣ **Create & Activate Virtual Environment**
```bash
python -m venv .venv
source .venv/bin/activate  # For macOS/Linux
# On Windows (PowerShell)
.venv\Scripts\Activate
```

### 5️⃣ **Install Backend Dependencies**
```bash
pip install -r server/requirements.txt
```

### 6️⃣ **Run the Server**
```bash
cd server
uvicorn main:app --reload
```
The server will run on:  
📍 **`http://127.0.0.1:8000`**

---

## 🎨 **Frontend Setup (React Client)**

### 7️⃣ **Navigate to `client` & Install Dependencies**
```bash
cd ../client
npm install
```

### 8️⃣ **Run the React App**
```bash
npm start
```
The frontend will be available at:  
📍 **`http://localhost:3000`**

---

## 🛠 **Testing the Solution**
1. Open the browser and go to **`http://localhost:3000`**.
2. Enter a domain (e.g., `google.com`) and click "Scan".
3. The application will fetch website details and display them.

### 🐞 **Troubleshooting**
- If **GO is not found**, install it from [Go Official Website](https://go.dev/dl/).
- If **HTTPX is not found**, ensure it’s installed and in your `PATH`.
- If **CORS issues occur**, restart the backend and ensure the CORS middleware is active.

---

## 📄 **Project Structure**
```
websiteScanner/
│── .venv/               # Virtual environment
│── client/              # React frontend
│   ├── node_modules/    # Dependencies (not committed)
│   ├── public/          # Static files
│   ├── src/             # React components
│   ├── package.json     # Frontend dependencies
│   └── README.md        # Frontend-specific README (optional)
│── server/              # FastAPI backend
│   ├── .venv/           # Backend virtual environment
│   ├── main.py          # Backend API
│   ├── requirements.txt # Backend dependencies
│── .gitignore           # Git ignore file
│── README.md            # This file
```

📢 **Developed by SHELLY GOLDEN 🚀**