from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import subprocess
import json
import shutil

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API endpoint to scan a given domain using HTTPX.
@app.get("/api/scan")
async def scan_website(domain: str):
    if not domain:
        raise HTTPException(status_code=400, detail="Domain is required")

    raw_scan_data = execute_httpx_scan(domain)
    parsed_results = parse_httpx_output(raw_scan_data)

    if not parsed_results:
        raise HTTPException(status_code=500, detail="No results returned from HTTPX")

    structured_response = format_scan_results(parsed_results[0], domain)
    return structured_response


# Executes the HTTPX command to scan the given domain and returns the raw output.
def execute_httpx_scan(domain: str) -> str:
    #Check if HTTPX is installed before executing the command
    if not shutil.which("httpx"):
        raise HTTPException(status_code=500, detail="httpx is not installed or not found in PATH")

    try:
        #Runs HTTPX with a 300-second timeout to avoid indefinite hanging
        result = subprocess.run(
            ["httpx", "-json", "-title", "-status-code", "-tech-detect", "-web-server", "-ip", "-cname", "-timeout", "300", "-u", domain],
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            raise HTTPException(status_code=500, detail=f"Scanning failed: {result.stderr.strip()}")

        # Ensure the output is not empty before returning
        output = result.stdout.strip()
        if not output:
            raise HTTPException(status_code=500, detail="HTTPX returned empty output")

        return output

    except subprocess.TimeoutExpired:
        # Handle case where HTTPX scan takes longer than 300 seconds
        raise HTTPException(status_code=500, detail="HTTPX scan timed out")

    except Exception as e:
        # Catch any unexpected errors and return them
        raise HTTPException(status_code=500, detail=str(e))


#Parses the JSON output from HTTPX and returns a list of dictionaries.
def parse_httpx_output(output: str):
    try:
        output_lines = output.split("\n")
        return [json.loads(line) for line in output_lines]
    except json.JSONDecodeError as e:
        raise HTTPException(status_code=500, detail=f"Failed to parse scan results: {str(e)}")


#Formats the parsed scan data into a structured response.
def format_scan_results(scan_data: dict, domain: str) -> dict:
    return {
        "domain": scan_data.get("input", domain),
        "related_ips": scan_data.get("a", []),
        "webpage_title": scan_data.get("title", "N/A"),
        "status_code": scan_data.get("status_code", None),
        "webserver": scan_data.get("webserver", "Unknown"),
        "technologies": scan_data.get("tech", []),
        "cnames": scan_data.get("cname", [])
    }