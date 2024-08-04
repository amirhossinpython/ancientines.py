document.getElementById('convertButton').addEventListener('click', function() {
    const inputText = document.getElementById('inputText').value;

    fetch('/convert', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: inputText }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('cuneiformOutput').innerText = `متن به خط میخی:\n${data.cuneiform}`;
        document.getElementById('pahlaviOutput').innerText = `متن به خط پهلوی:\n${data.pahlavi}`;
        document.getElementById('manaviOutput').innerText = `متن به خط مانوی:\n${data.manavi}`;
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});

