# NerdHub - E-commerce de Produtos Nerd

NerdHub é um e-commerce desenvolvido em Django para venda de produtos nerd, incluindo Funko Pop's, action figures, camisetas, acessórios e outros itens relacionados a cultura pop, games e filmes.

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+**
- **Django 5.1+**
- **SQLite** (banco de dados de desenvolvimento)
- **HTML5 & CSS3**
- **JavaScript**

## 📋 Funcionalidades

- Catálogo de produtos organizados por marcas e categorias
- Visualização detalhada de produtos
- Sistema de carrinho de compras
- Sistema de avaliações e comentários
- Controle de estoque
- Gestão de pedidos
- Autenticação de usuários (cadastro e login)
- Páginas institucionais (Sobre, Suporte)

## 📦 Versionamento

Este projeto utiliza o versionamento semântico (Semantic Versioning - SemVer) para gerenciar as versões do software. O formato da versão segue a estrutura **MAJOR.MINOR.PATCH**, onde:

- **MAJOR** (Principal): Incrementado quando há mudanças incompatíveis na API ou funcionalidades principais que quebram a compatibilidade.
- **MINOR** (Secundária): Incrementado quando há adições de funcionalidades compatíveis com versões anteriores.
- **PATCH** (Correção): Incrementado quando há correções de bugs ou pequenas melhorias que não afetam a compatibilidade.

### Exemplos de Versionamento:
- `v1.0.0`: Primeira versão estável do projeto, com funcionalidades básicas implementadas(Exemplo MAJOR).
- `v1.1.0`: Adição de novas funcionalidades compatíveis, como melhorias no sistema de carrinho(Exemplo MINOR).
- `v1.1.1`: Correção de bugs menores, como ajustes na interface(Exemplo PATCH).
- `v2.0.0`: Mudanças significativas, como reestruturação completa do sistema ou quebra de compatibilidade.

A versão atual do projeto é **v1.0.0**, representando o lançamento inicial com todas as funcionalidades básicas do e-commerce implementadas.

### Funcionalidades da Versão v1.0.0:
- **Catálogo de Produtos**: Organização de produtos por marcas (Marvel, Star Wars, Disney, PlayStation, Xbox) e categorias, com imagens principais e adicionais.
- **Sistema de Carrinho e Pedidos**: Adição de produtos ao carrinho, ajuste de quantidades, cálculo de totais e finalização de pedidos.
- **Avaliações e Comentários**: Sistema de reviews com comentários e notas de 1 a 5 estrelas para produtos.
- **Controle de Estoque**: Gestão de quantidades disponíveis para cada produto.
- **Autenticação de Usuários**: Cadastro, login e perfil de usuário.
- **Páginas Institucionais**: Seções "Sobre" e "Suporte" com informações da empresa e atendimento.

## 🚀 Instalação

1. **Clone o repositório:**
   ```bash
   git clone <url-do-repositorio>
   cd UC12_Projeto_NerdHub.1
   ```

2. **Crie um ambiente virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute as migrações:**
   ```bash
   python manage.py migrate
   ```

5. **Crie um superusuário (opcional):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Inicie o servidor de desenvolvimento:**
   ```bash
   python manage.py runserver
   ```

7. **Acesse a aplicação:**
   Abra seu navegador e visite `http://127.0.0.1:8000`

## 📁 Estrutura do Projeto

```
UC12_Projeto_NerdHub.1/
├── Nerdhub/              # Configurações do projeto Django
├── nucleo/               # App principal com funcionalidades do e-commerce
├── usuarios/             # App de gestão de usuários
├── media/                # Arquivos de upload (imagens de produtos)
├── static/               # Arquivos estáticos (CSS, JS, imagens)
├── manage.py             # Script de gerenciamento do Django
└── README.md             # Este arquivo
```

## 🎯 Funcionalidades Principais

### Catálogo de Produtos
- Visualização de produtos em grade na página inicial
- Filtragem por marcas famosas (Marvel, Star Wars, Disney, etc.)
- Página de detalhes com informações completas do produto

### Carrinho de Compras
- Adição e remoção de produtos
- Ajuste de quantidades
- Cálculo automático de totais
- Finalização de pedidos

### Sistema de Usuários
- Cadastro de novos usuários
- Autenticação e login
- Perfil de usuário

### Gestão de Conteúdo
- Página "Sobre" com informações da empresa
- Página "Suporte" com chat de atendimento

## 🎨 Design e Interface

O projeto utiliza um design responsivo com:
- Cores temáticas relacionadas ao universo nerd
- Layout intuitivo e fácil de navegar
- Ícones e imagens atrativas
- Experiência otimizada para desktop e mobile

## 📝 Próximos Passos

Funcionalidades planejadas para implementações futuras:
- Sistema de pagamento integrado
- Busca avançada de produtos
- Sistema de descontos e cupons
- Área administrativa completa
- Recuperação de senha
- Lista de desejos
- Avaliações por estrelas
- Notificações por email

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.

## 📧 Contato

Seu Nome - (ainda nao criei o email)

Link do Projeto: [https://github.com/DanxzSleepy/UC12_Projeto_NerdHub.1](https://github.com/seu-usuario/UC12_Projeto_NerdHub.1)