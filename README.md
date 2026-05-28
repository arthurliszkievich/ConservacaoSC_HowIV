# 🌿 Conservação SC (ConservacaoSC_HowIV)

**Trabalho da faculdade de ADS**

Um sistema web desenvolvido em Django para cadastrar, gerenciar e dar visibilidade às Unidades de Conservação (Parques Nacionais, Reservas Biológicas, APAs, etc.) do estado de Santa Catarina. O projeto também permite que visitantes enviem comunicações/denúncias às entidades responsáveis por cada parque.

## 🚀 Funcionalidades

- **Autenticação:** Sistema de login e registro de usuários, com páginas de autenticação focadas em UI/UX moderna (split-screen).
- **Gerenciamento de UCs:** Usuários logados podem criar, editar e excluir Unidades de Conservação, Instituições e Municípios.
- **Upload de Mídia:** Suporte a upload de imagens para as Unidades de Conservação (configurado via Pillow).
- **Interface Pública:** Vitrine de parques cadastrados e páginas de detalhes dinâmicas.
- **Comunicações:** Sistema de formulários públicos onde visitantes podem enviar avisos (Pendente, Em Andamento, Resolvido) sobre as unidades (ex: denúncia ambiental, dúvida, aviso de incêndio).

## 🛠 Tecnologias Utilizadas

- **Backend:** Python 3.12, Django 5.x
- **Frontend:** HTML5, CSS3, Bootstrap 5.3.3, Google Fonts (Outfit)
- **Banco de Dados:** SQLite (padrão em ambiente de desenvolvimento)
- **Bibliotecas auxiliares:** Pillow (processamento de imagens)

## ⚙️ Como executar o projeto localmente

1. **Clone este repositório:**
   ```bash
   git clone https://github.com/arthurliszkievich/ConservacaoSC_HowIV.git
   cd ConservacaoSC_HowIV
   ```

2. **Crie um ambiente virtual (venv):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Linux/Mac
   # ou: venv\Scripts\activate no Windows
   ```

3. **Instale as dependências necessárias:**
   ```bash
   pip install django pillow
   ```
   *(Caso já possua um arquivo `requirements.txt`, rode `pip install -r requirements.txt`)*

4. **Execute as migrações do banco de dados:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Crie um superusuário (opcional, para acesso ao Django Admin):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Inicie o servidor de desenvolvimento:**
   ```bash
   python manage.py runserver
   ```

7. **Acesse no navegador:**
   - [http://127.0.0.1:8000](http://127.0.0.1:8000) (Site Principal)
   - [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) (Painel Admin)

## 📁 Estrutura do Projeto

- `/conservacao`: Arquivos de configuração global do projeto (`settings.py`, `urls.py`).
- `/unidades`: O App principal do Django.
  - `/models.py`: Modelos de banco de dados (`UnidadeConservacao`, `Instituicao`, `Municipio`, `Comunicacao`).
  - `/views.py`: A lógica por trás das requisições e respostas.
  - `/urls.py`: Rotas (endpoints) locais do app.
  - `/templates`: Arquivos HTML (páginas).
  - `/forms.py`: Formulários integrados do Django (`ModelForm`).
- `/media`: Diretório onde as imagens dos parques são salvas após o upload.

---
Desenvolvido com 💚 para a conservação do estado de Santa Catarina.
