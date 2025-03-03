import React, { useState } from "react";
import axios from "axios";
import ScanForm from "./components/ScanForm";
import ScanResults from "./components/ScanResults";

function App() {
    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const handleScan = async (domain) => {
        setLoading(true);
        setError(null);
        setData(null);

        console.log(`scanning ${domain}`)

        try {
            const response = await axios.get(`http://127.0.0.1:8000/api/scan?domain=${domain}`);
            console.log('api response: ', response)
            console.log('data: ', response.data)
            setData(response.data);
        } catch (err) {
            console.error('error fetching')
            setError("Failed to scan the domain. Please try again.");
        }

        setLoading(false);
    };

    return (
        <div style={{ textAlign: "center", marginTop: "50px" }}>
            <h1>Website Scanner</h1>
            <ScanForm onScan={handleScan} />
            {loading ? <p>Scanning...</p> : <ScanResults data={data} error={error} />}
        </div>
    );
}

export default App;
