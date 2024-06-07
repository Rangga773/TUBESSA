function crackPassword() {
    const algorithm = document.getElementById('algorithm').value;
    const charset = document.getElementById('charset').value;
    const maxLength = parseInt(document.getElementById('maxLength').value);
    const correctPassword = document.getElementById('correctPassword').value;

    fetch('/crack_password', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            algorithm: algorithm,
            charset: charset,
            max_length: maxLength,
            correct_password: correctPassword
        }),
    })
    .then(response => response.json())
    .then(data => {
        const { found_password, duration } = data;
        document.getElementById('result').innerText = `Found Password: ${found_password}\nDuration: ${duration.toFixed(4)} seconds`;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
