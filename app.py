from flask import Flask, request, jsonify, send_file, send_from_directory, render_template, Response
from flask_cors import CORS
import subprocess
import os

app = Flask(__name__)
CORS(app)

@app.route('/deploy', methods=['POST'])
def deploy():
    data = request.json
    master_ip = data['master_ip']
    worker_ips = data['worker_ips']
    ssh_user = data['ssh_user']
    ssh_password = data['ssh_password']

    # Atualizar inventário Ansible
    inventory_content = "[masters]\n"
    inventory_content += f"master ansible_host={master_ip} ansible_user={ssh_user} ansible_ssh_pass={ssh_password}\n\n"
    inventory_content += "[workers]\n"
    for idx, ip in enumerate(worker_ips):
        inventory_content += f"worker{idx+1} ansible_host={ip} ansible_user={ssh_user} ansible_ssh_pass={ssh_password}\n"
    inventory_content += "\n[all:vars]\n"
    inventory_content += "ansible_python_interpreter=/usr/bin/python3\n"

    with open('ansible/inventory.ini', 'w') as f:
        f.write(inventory_content)

    # Executar o playbook Ansible
#    result = subprocess.run(['ansible-playbook', '-i', 'ansible/inventory.ini', 'ansible/playbooks/kubernetes_cluster.yml'], capture_output=True, text=True)

# Função para gerar logs em tempo real
    def generate_logs():
        process = subprocess.Popen(['ansible-playbook', '-i', 'ansible/inventory.ini', 'ansible/playbooks/kubernetes_cluster.yml'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        for stdout_line in iter(process.stdout.readline, ""):
            yield f"data:{stdout_line}\n\n"
        process.stdout.close()
        return_code = process.wait()
        if return_code:
            for stderr_line in iter(process.stderr.readline, ""):
                yield f"data:{stderr_line}\n\n"
            process.stderr.close()

    return Response(generate_logs(), mimetype='text/event-stream')

    if result.returncode == 0:
        return jsonify({'status': 'success', 'output': result.stdout})
    else:
        return jsonify({'status': 'error', 'output': result.stderr}), 500

@app.route('/get-kubeconfig', methods=['GET'])
def get_kubeconfig():
    kubeconfig_path = '/home/ocs-user/.kube/config'
    try:
        return send_file(kubeconfig_path, as_attachment=True)
    except Exception as e:
        return str(e), 500

@app.route('/')
def serve_index():
    return render_template('index.html') 

@app.route('/<path:path>')
def serve_file(path):
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
