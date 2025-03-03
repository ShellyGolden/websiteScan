import React, { useState } from "react";

function ScanForm({ onScan }) {
    const [domain, setDomain] = useState("");

    const handleSubmit = (e) => {
        e.preventDefault();
        if (domain.trim()) {
            onScan(domain);
        }
    };

    return (
        <div>
            <h2>Enter a Domain to Scan</h2>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    value={domain}
                    onChange={(e) => setDomain(e.target.value)}
                    placeholder="enter a domain..."
                />
                <button type="submit">Scan</button>
            </form>
        </div>
    );
}

export default ScanForm;
