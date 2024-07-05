document.getElementById('deployForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const formData = new FormData(event.target);
    const data = {
        master_ip: formData.get('master_ip'),
        worker_ips: formData.getAll('worker_ips[]'),
        ssh_user: formData.get('ssh_user'),
        ssh_password: formData.get('ssh_password')
    };

    // Mostrar a tela de carregamento
    document.getElementById('loading').style.display = 'block';
    document.getElementById('output').innerHTML = '';

    console.log('Enviando dados para a API:', data);

    fetch('/deploy', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.text(); // Use .text() instead of .json()
    })
    .then(text => {
        // Esconder a tela de carregamento
        document.getElementById('loading').style.display = 'none';
        console.log('Resposta da API:', text);
        const formattedText = formatOutput(text);
        document.getElementById('output').innerHTML = formattedText;
    })
    .catch(error => {
        // Esconder a tela de carregamento
        document.getElementById('loading').style.display = 'none';
        console.error('Erro ao chamar a API:', error);
        document.getElementById('output').innerHTML = `<div class="error">Error: ${error.message}</div>`;
    });
});

function formatOutput(text) {
    let lines = text.split('data:');
    lines = lines.map(line => line.trim()).filter(line => line !== '');

    return lines.map(line => {
        if (line.includes('FAILED!')) {
            return `<div class="error">${line}</div>`;
        } else if (line.includes('PLAY') || line.includes('TASK')) {
            return `<div class="highlight">${line}</div>`;
        } else {
            return `<div>${line}</div>`;
        }
    }).join('');
}

