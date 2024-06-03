async function fetchTrends() {
    const response = await fetch('/run-script');
    const data = await response.json();
    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = `
        <h2>These are the most happening topics as on ${data.date_time}</h2>
        <ul>
            <li>${data.top_trends[0]}</li>
            <li>${data.top_trends[1]}</li>
            <li>${data.top_trends[2]}</li>
            <li>${data.top_trends[3]}</li>
            <li>${data.top_trends[4]}</li>
        </ul>
        <p>The IP address used for this query was ${data.ip_address}.</p>
        <h3>Here’s a JSON extract of this record from the MongoDB:</h3>
        <pre>${JSON.stringify(data, null, 4)}</pre>
    `;
}
