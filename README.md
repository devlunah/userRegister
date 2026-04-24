# Sistema de Registro de Usuários - Flask Web App

## 📋 Sobre

Projeto para praticar desenvolvimento de aplicações web com Flask, convertendo um sistema de registro de usuários em terminal para uma aplicação web moderna.

## 🚀 Funcionalidades

- ✅ Listar todos os usuários cadastrados
- ✅ Cadastrar novo usuário
- ✅ Buscar usuário por CPF
- ✅ Editar dados do usuário
- ✅ Deletar usuário
- ✅ Interface responsiva e moderna
- ✅ Validação de dados no servidor

## 📦 Instalação

1. **Clone ou baixe o repositório**

2. **Crie um ambiente virtual (opcional mas recomendado)**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

## ▶️ Como Executar

1. **Navegue até a pasta do projeto**
```bash
cd c:\Users\sonda.lunahsc\Programação\userRegister
```

2. **Execute a aplicação**
```bash
python app.py
```

3. **Abra seu navegador**
Acesse: `http://localhost:5000`

## 📁 Estrutura do Projeto

```
userRegister/
├── app.py                      # Arquivo principal da aplicação Flask
├── arquivo_usuarios.py         # Funções de manipulação de arquivos
├── cadastro_usuarios.py        # Funções de cadastro (legacy)
├── menu.py                     # Menu em terminal (legacy)
├── main.py                     # Arquivo main antigo (legacy)
├── usuarios.txt                # Arquivo com dados dos usuários
├── requirements.txt            # Dependências do projeto
├── README.md                   # Este arquivo
├── templates/                  # Templates HTML
│   ├── base.html              # Template base
│   ├── index.html             # Página inicial
│   ├── cadastro.html          # Formulário de cadastro
│   ├── editar.html            # Formulário de edição
│   └── buscar.html            # Página de busca
└── static/                     # Arquivos estáticos
    └── css/
        └── style.css          # Estilos CSS
```

## 🎓 Conceitos Aprendidos

Neste projeto você vai praticar:

### Flask Basics
- **Rotas**: Criar rotas com `@app.route()` e diferentes métodos HTTP (GET, POST)
- **Templates**: Usar Jinja2 para renderizar HTML dinâmico
- **Formulários**: Trabalhar com `request.form` para receber dados

### Funcionalidades Web
- **Redirect**: Redirecionar o usuário após ações
- **Flash Messages**: Mostrar mensagens ao usuário
- **URLs Dinâmicas**: Usar `url_for()` para gerar URLs dinamicamente
- **Métodos HTTP**: GET para requisições e POST para submissões

### Integração de Dados
- Reutilizar lógica do arquivo `arquivo_usuarios.py`
- Persistência de dados em arquivo de texto
- Validação de entrada do usuário

## 💡 Dicas de Aprendizado

1. **Entenda as Rotas**: Estude como cada rota (/, /cadastro, /buscar, etc) funciona
2. **Explore os Templates**: Veja como Jinja2 renderiza o HTML dinâmico
3. **Debug Mode**: Flask está em `debug=True` - qualquer mudança recarrega automaticamente
4. **Browser DevTools**: Use F12 para inspeccionar o HTML e CSS
5. **Adicione Funcionalidades**: Tente adicionar:
   - Validação de CPF
   - Ordenação de usuários
   - Busca por nome
   - Paginação
   - Exportar dados para CSV

## 🔧 Próximos Passos

- Adicionar banco de dados (SQLite, PostgreSQL)
- Implementar autenticação de usuários
- Adicionar mais validações
- Criar API REST
- Deploy em um servidor real

## 📝 Anotações Pessoais

Sinta-se livre para modificar e experimentar! Este é um projeto de aprendizado.

---

**Versão**: 1.0
**Última atualização**: Abril 2026
