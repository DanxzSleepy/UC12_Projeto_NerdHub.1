#!/usr/bin/env python
"""
Script de demonstração para executar os testes automatizados do NerdHub.
Este script mostra como executar os testes e gerar relatórios.
"""

import os
import sys
import subprocess
import time

def run_command(command, description):
    """Executa um comando e mostra sua saída"""
    print(f"\n{'='*60}")
    print(f"🔧 {description}")
    print(f"📝 Comando: {command}")
    print(f"{'='*60}")
    
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.stdout:
            print("✅ Saída:")
            print(result.stdout)
        if result.stderr:
            print("⚠️ Erros:")
            print(result.stderr)
        return result.returncode == 0
    except Exception as e:
        print(f"❌ Erro ao executar comando: {e}")
        return False

def main():
    print("🚀 Demonstração de Testes Automatizados - NerdHub")
    print("================================================")
    
    # Verificar se estamos no diretório correto
    if not os.path.exists('manage.py'):
        print("❌ Por favor, execute este script a partir do diretório raiz do projeto!")
        return
    
    print("📁 Diretório atual:", os.getcwd())
    
    # Criar diretório de testes se não existir
    os.makedirs('tests', exist_ok=True)
    
    print("\n📋 Etapas da demonstração:")
    print("1. Instalar dependências de teste")
    print("2. Executar testes básicos")
    print("3. Gerar relatório de cobertura")
    
    input("\nPressione Enter para começar...")
    
    # Etapa 1: Instalar dependências
    print("\n🔄 Etapa 1: Instalando dependências de teste")
    if os.path.exists('tests/requirements.txt'):
        success = run_command("pip install -r tests/requirements.txt", "Instalando dependências de teste")
        if not success:
            print("⚠️ Continuando mesmo com erro na instalação...")
    else:
        print("ℹ️ Arquivo tests/requirements.txt não encontrado, pulando instalação...")
    
    # Etapa 2: Executar testes
    print("\n🔍 Etapa 2: Executando testes automatizados")
    time.sleep(2)
    
    success = run_command("python run_tests.py", "Executando suite de testes")
    
    if success:
        print("\n🎉 Todos os testes passaram com sucesso!")
    else:
        print("\n❌ Alguns testes falharam. Verifique a saída acima.")
    
    # Etapa 3: Gerar relatório de cobertura (se disponível)
    print("\n📊 Etapa 3: Gerando relatório de cobertura")
    time.sleep(2)
    
    # Verificar se coverage está instalado
    coverage_installed = run_command("coverage --version", "Verificando se coverage está instalado")
    
    if coverage_installed:
        run_command("coverage run --source='.' run_tests.py", "Executando testes com coleta de cobertura")
        run_command("coverage report", "Gerando relatório de cobertura")
        run_command("coverage html", "Gerando relatório HTML de cobertura")
        print("\n📂 Relatório HTML salvo em: htmlcov/index.html")
    else:
        print("ℹ️ Coverage não está instalado. Para gerar relatórios de cobertura:")
        print("   pip install coverage")
    
    print("\n" + "="*60)
    print("🎯 Demonstração concluída!")
    print("="*60)
    print("\n📄 Documentação completa disponível em: TESTING_DOCUMENTATION.md")
    print("📁 Código dos testes disponível em: tests/test_comprehensive.py")

if __name__ == "__main__":
    main()