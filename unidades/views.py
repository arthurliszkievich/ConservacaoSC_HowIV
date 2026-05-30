from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UnidadeConservacaoForm, ComunicacaoForm, InstituicaoForm, MunicipioForm

from django.shortcuts import render, get_object_or_404, redirect
from .models import UnidadeConservacao, Comunicacao

# ==========================================
# AUTENTICAÇÃO
# ==========================================

def registro_view(request):
    """Cria um novo usuário no sistema"""

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Depois de logado redireciona para a página principal
            messages.success(request, 'Conta criada com sucesso! Bem-vindo!')
            return redirect('painel')
    else:
        form = UserCreationForm()
    return render(request, 'usuario/registro.html', {'form': form})
    
def login_view(request):
    """Autentica um usuário existente"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('painel')
        else:
            messages.error(request, 'Usuário ou senha incorretos.')        
    return render(request, 'usuario/login.html')

def logout_view(request):
    """Desloga o usuário"""
    logout(request)
    messages.success(request, 'Logout realizado com sucesso.')
    return redirect('login')


# ==========================================
# PAINEL DO USUÁRIO (requer login)
# ==========================================

@login_required(login_url='/login/')
def nova_unidade_view(request):
    """Formulário para criar uma nova unidade"""
    if request.method == 'POST':
        form = UnidadeConservacaoForm(request.POST, request.FILES)  # request.FILES captura o upload
        if form.is_valid():
            unidade = form.save(commit=False) # Ainda não é salvo no banco
            unidade.criado_por = request.user # Define o Dono do post
            unidade.save() # Agora sim salva no banco
            form.save_m2m()# Salva a relação com os municipios (Many to Many)
            messages.success(request, 'Unidade criada com sucesso!')
            return redirect('painel')
    else:
        form = UnidadeConservacaoForm()
    return render(request, 'unidades/form_unidade.html', {'form': form, 'acao': 'Cadastrar'})

@login_required(login_url='/login/')
def apagar_unidade_view(request, unidade_id):
    """Apaga uma unidade (somente o dono pode apagar)."""
    unidade = get_object_or_404(UnidadeConservacao, id=unidade_id, criado_por=request.user)
    if request.method == 'POST':
        unidade.delete()
        messages.success(request, 'Unidade removida com sucesso')
        return redirect('painel')
    return render(request, 'unidades/confirmar_apagar.html', {'unidade': unidade})

@login_required(login_url='/login/')
def painel_view(request):
    minhas_unidades = UnidadeConservacao.objects.filter(criado_por=request.user)
    return render (request, 'unidades/painel.html', {'unidades': minhas_unidades})

@login_required(login_url='/login/')
def editar_unidade_view(request,unidade_id):
    unidade = get_object_or_404(UnidadeConservacao,id=unidade_id, criado_por=request.user)
    if request.method == 'POST':
        form = UnidadeConservacaoForm(request.POST, request.FILES, instance=unidade)  # request.FILES para imagem
        if form.is_valid():
            form.save()
            messages.success(request, 'Unidade atualizada com sucesso!')
            return redirect('painel')
    else:
        form = UnidadeConservacaoForm(instance=unidade)
    return render(request, 'unidades/form_unidade.html', {'form': form, 'acao': 'Editar', 'unidade': unidade})

@login_required(login_url='/login/')
def nova_instituicao_view(request):
    """Cadastrar uma nova Instituição."""
    if request.method == 'POST':
        form = InstituicaoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Instituição cadastrada com sucesso!')
            return redirect('painel')
    else:
        form = InstituicaoForm()
    return render(request, 'unidades/form_simples.html', {
        'form': form,
        'titulo': 'Nova Instituição',
        'voltar': 'painel'
    })

@login_required(login_url='/login/')
def novo_municipio_view(request):
    """Cadastrar um novo Município."""
    if request.method == 'POST':
        form = MunicipioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Município cadastrado com sucesso!')
            return redirect('painel')
    else:
        form = MunicipioForm()
    return render(request, 'unidades/form_simples.html', {
        'form': form,
        'titulo': 'Novo Município',
        'voltar': 'painel'
    })

            
# ==========================================
# PÁGINAS PÚBLICAS
# ==========================================

def index(request):
    from .models import Municipio
    todas_unidades = UnidadeConservacao.objects.all().order_by('nome')
    unidades = todas_unidades
    
    # Pesquisa por nome (busca texto livre)
    q = request.GET.get('q', '').strip()
    if q:
        unidades = unidades.filter(nome__icontains=q)
    
    # Filtro por município
    municipio_id = request.GET.get('municipio', '')
    if municipio_id:
        unidades = unidades.filter(municipios__id=municipio_id)

    # Filtro por unidade específica
    unidade_id = request.GET.get('unidade', '')
    if unidade_id:
        unidades = unidades.filter(id=unidade_id)

    municipios = Municipio.objects.all().order_by('nome')
    return render(request, 'unidades/index.html', {
        'unidades': unidades,
        'todas_unidades': todas_unidades,
        'municipios': municipios,
        'q': q,
        'municipio_selecionado': municipio_id,
        'unidade_selecionada': unidade_id,
    })

def detalhes(request, unidade_id):
    unidade = get_object_or_404(UnidadeConservacao, id=unidade_id)
    form = ComunicacaoForm()

    if request.method == 'POST':
        form = ComunicacaoForm(request.POST)
        if form.is_valid():
            nova_comunicacao = form.save(commit=False)
            nova_comunicacao.unidade = unidade
            nova_comunicacao.status = 0
            nova_comunicacao.save()
            messages.success(request, 'Comunicação enviada com sucesso!')
            return redirect('detalhes', unidade_id=unidade.id)

    return render(request, 'unidades/detalhes.html', {'unidade': unidade, 'form': form})

def comunicacao(request, unidade_id):
    """Mantida por compatibilidade – redireciona para detalhes"""
    return redirect('detalhes', unidade_id=unidade_id)