document.addEventListener('DOMContentLoaded', function() {
    const fileInput = document.getElementById('fileInput');
    const analyzeButton = document.getElementById('analyzeButton');
    const resultsDiv = document.getElementById('results');

    fileInput.addEventListener('change', function(event) {
        const file = event.target.files[0];
        if (file) {
            analyzeButton.disabled = false;
        } else {
            analyzeButton.disabled = true;
        }
    });

    analyzeButton.addEventListener('click', function() {
        const formData = new FormData();
        formData.append('file', fileInput.files[0]);

        fetch('/analyze', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            resultsDiv.innerHTML = '';
            const pre = document.createElement('pre');
            pre.textContent = JSON.stringify(data, null, 2);
            resultsDiv.appendChild(pre);
        })
        .catch(error => {
            console.error('Error:', error);
            resultsDiv.innerHTML = '<p>Error analyzing the file.</p>';
        });
    });
});