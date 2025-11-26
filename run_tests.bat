@echo off
REM Script para executar testes do NerdHub no Windows

echo ====================================================
echo 🚀 NerdHub - Testes Automatizados
echo ====================================================

REM Verificar se o Python está instalado
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python não encontrado. Por favor, instale o Python.
    pause
    exit /b 1
)

echo ✅ Python encontrado

REM Verificar se estamos no diretório correto
if not exist "manage.py" (
    echo ❌ Por favor, execute este script a partir do diretório raiz do projeto!
    pause
    exit /b 1
)

echo ✅ Diretório do projeto verificado

REM Instalar dependências de teste (se necessário)
if exist "tests\requirements.txt" (
    echo 🔄 Instalando dependências de teste...
    pip install -r tests\requirements.txt
    if %errorlevel% neq 0 (
        echo ⚠️ Erro ao instalar dependências, continuando...
    )
)

echo 🔍 Executando testes...

REM Executar testes
python run_tests.py

if %errorlevel% equ 0 (
    echo.
    echo 🎉 Todos os testes passaram com sucesso!
) else (
    echo.
    echo ❌ Alguns testes falharam. Verifique a saída acima.
)

echo.
echo 📄 Documentação completa disponível em: TESTING_DOCUMENTATION.md
echo 📁 Código dos testes disponível em: tests\test_comprehensive.py

echo.
echo Pressione qualquer tecla para sair...
pause >nul