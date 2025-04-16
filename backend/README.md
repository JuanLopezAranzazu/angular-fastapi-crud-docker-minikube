# Backend

## Entorno virtual

Para el entorno virtual en linux
```bash
python3 -m venv venv
source venv/bin/activate # Para activar el entorno virtual
deactivate # Para desactivar el entorno virtual
```

Para el entorno virtual en windows
```bash
python -m venv venv
.\venv\Scripts\activate # Para activar el entorno virtual
.\venv\Scripts\deactivate # Para desactivar el entorno virtual
```

## Instalar dependencias

Para instalar dependencias
```bash
pip install -r requirements.txt
```

## Ejecución del programa

Para correr el programa puedes ejecutar el siguiente comando:
```bash
uvicorn app.main:app --reload
uvicorn app.main:app --reload --port 8080
```