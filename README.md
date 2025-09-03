# Tarea TDD - Juego cacho

## Requisitos Previos
    Python 3.8 o superior
    pip (gestor de paquetes de Python)

## Crear un entorno virtual
    python3 -m venv .venv
    source .venv/bin/activate

## Instalar dependencias
    pip install pytest pytest-mock pytest-cov

## Para verificar la cobertura de los test
    pytest --cov=src --cov-report=term-missing

## Para correr el test de integración (que comprueba la implementación de todos los archivos)
    python3 -m pytest tests/test_integración.py::test_integracion_juego_completo_duda_incorrecta -v
