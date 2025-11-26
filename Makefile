# Makefile para executar testes do NerdHub

# Variáveis
PYTHON = python
TEST_RUNNER = run_tests.py
COVERAGE = coverage

# Targets
.PHONY: help test clean coverage install-deps

help:
	@echo "NerdHub - Comandos disponíveis:"
	@echo "  make test          - Executar todos os testes"
	@echo "  make coverage      - Executar testes com relatório de cobertura"
	@echo "  make install-deps  - Instalar dependências de teste"
	@echo "  make clean         - Limpar arquivos de cobertura"
	@echo "  make demo          - Executar demonstração interativa"

test:
	$(PYTHON) $(TEST_RUNNER)

install-deps:
	pip install -r tests/requirements.txt

coverage:
	$(COVERAGE) run --source='.' $(TEST_RUNNER)
	$(COVERAGE) report
	$(COVERAGE) html
	@echo "Relatório HTML gerado em htmlcov/index.html"

clean:
	rm -rf htmlcov/
	rm -f .coverage
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -type d -exec rm -rf {} +

demo:
	$(PYTHON) run_tests_demo.py

# Alias para comandos comuns
check: test
tests: test