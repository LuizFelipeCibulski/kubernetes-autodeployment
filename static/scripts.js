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
    document.getElementById('output').textContent = '';

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
        return response.json();
    })
    .then(result => {
        // Esconder a tela de carregamento
        document.getElementById('loading').style.display = 'none';
        console.log('Resposta da API:', result);
        document.getElementById('output').textContent = result.status === 'success' ? result.output : `Error: ${result.output}`;
    })
    .catch(error => {
        // Esconder a tela de carregamento
        document.getElementById('loading').style.display = 'none';
        console.error('Erro ao chamar a API:', error);
        document.getElementById('output').textContent = `Error: ${error.message}`;
    });
});

