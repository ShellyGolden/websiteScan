from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import subprocess
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/scan")
async def scan_website(domain: str):
    if not domain:
        raise HTTPException(status_code=400, detail="Domain is required")

    try:
        result = subprocess.run(
            ["httpx", "-json", "-title", "-status-code", "-tech-detect", "-web-server", "-ip", "-cname", "-u", domain],
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            raise HTTPException(status_code=500, detail=f"Scanning failed: {result.stderr}")

        output_lines = result.stdout.strip().split("\n")
        parsed_results = [json.loads(line) for line in output_lines]

        if not parsed_results:
            raise HTTPException(status_code=500, detail="No results returned from HTTPX")

        scan_data = parsed_results[0]

        structured_response = {
            "domain": scan_data.get("input", domain),
            "related_ips": scan_data.get("a", []),
            "webpage_title": scan_data.get("title", "N/A"),
            "status_code": scan_data.get("status_code", None),
            "webserver": scan_data.get("webserver", "Unknown"),
            "technologies": scan_data.get("tech", []),
            "cnames": scan_data.get("cname", [])
        }

        return structured_response

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
