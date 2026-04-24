from flask import Flask, render_template, request, redirect, url_for, flash
from arquivo_usuarios import carregar_usuarios, salvar_usuarios, buscar_usuarios, reescrever_usuarios

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'

@app.route('/')
def index():
    usuarios = carregar_usuarios()
    return render_template('index.html', usuarios=usuarios)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form.get('nome')
        cpf = request.form.get('cpf')
        idade = request.form.get('idade')
        
        if not nome or not cpf or not idade:
            flash('Todos os campos são obrigatórios!', 'erro')
            return redirect(url_for('cadastro'))
        
        usuario = [nome, cpf, idade]
        salvar_usuarios(usuario)
        flash(f'Usuário {nome} cadastrado com sucesso!', 'sucesso')
        return redirect(url_for('index'))
    
    return render_template('cadastro.html')

@app.route('/buscar', methods=['GET', 'POST'])
def buscar():
    usuario = None
    if request.method == 'POST':
        cpf = request.form.get('cpf')
        usuarios = carregar_usuarios()
        usuario = buscar_usuarios(usuarios, cpf)
        
        if not usuario:
            flash(f'Nenhum usuário encontrado com CPF: {cpf}', 'aviso')
    
    return render_template('buscar.html', usuario=usuario)

@app.route('/editar/<cpf>', methods=['GET', 'POST'])
def editar(cpf):
    usuarios = carregar_usuarios()
    usuario = buscar_usuarios(usuarios, cpf)
    
    if not usuario:
        flash('Usuário não encontrado!', 'erro')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        nome = request.form.get('nome')
        idade = request.form.get('idade')
        
        if not nome or not idade:
            flash('Todos os campos são obrigatórios!', 'erro')
            return redirect(url_for('editar', cpf=cpf))
        
        usuario[0] = nome
        usuario[2] = idade
        
        # Atualizar a lista
        for i, u in enumerate(usuarios):
            if u[1] == cpf:
                usuarios[i] = usuario
                break
        
        reescrever_usuarios(usuarios)
        flash(f'Usuário {nome} atualizado com sucesso!', 'sucesso')
        return redirect(url_for('index'))
    
    return render_template('editar.html', usuario=usuario)

@app.route('/deletar/<cpf>', methods=['POST'])
def deletar(cpf):
    usuarios = carregar_usuarios()
    usuarios = [u for u in usuarios if u[1] != cpf]
    reescrever_usuarios(usuarios)
    flash('Usuário deletado com sucesso!', 'sucesso')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
