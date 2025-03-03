import React from "react";

function ScanResults({ data, error }) {
    if (error) {
        return <p style={{ color: "red" }}>{error}</p>;
    }

    if (!data) {
        return <p>No scan data available.</p>;
    }

    console.log("📊 Displaying Scan Data:", data); // לוודא שהנתונים מגיעים לכאן

    return (
        <div style={{
            textAlign: "left",
            maxWidth: "600px",
            margin: "20px auto",
            padding: "20px",
            border: "1px solid #ccc",
            borderRadius: "8px",
            backgroundColor: "#f9f9f9"
        }}>
            <h2>Scan Results</h2>
            <table style={{ width: "100%", borderCollapse: "collapse" }}>
                <tbody>
                    <tr>
                        <td><strong>Domain:</strong></td>
                        <td>{data.domain}</td>
                    </tr>
                    <tr>
                        <td><strong>Related IPs:</strong></td>
                        <td>{data.related_ips && data.related_ips.length > 0 ? data.related_ips.join(", ") : "N/A"}</td>
                    </tr>
                    <tr>
                        <td><strong>Webpage Title:</strong></td>
                        <td>{data.webpage_title || "N/A"}</td>
                    </tr>
                    <tr>
                        <td><strong>Status Code:</strong></td>
                        <td>{data.status_code || "N/A"}</td>
                    </tr>
                    <tr>
                        <td><strong>Webserver:</strong></td>
                        <td>{data.webserver || "Unknown"}</td>
                    </tr>
                    <tr>
                        <td><strong>Technologies:</strong></td>
                        <td>{data.technologies && data.technologies.length > 0 ? data.technologies.join(", ") : "N/A"}</td>
                    </tr>
                    <tr>
                        <td><strong>CNAMEs:</strong></td>
                        <td>{data.cnames && data.cnames.length > 0 ? data.cnames.join(", ") : "N/A"}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    );
}

export default ScanResults;
