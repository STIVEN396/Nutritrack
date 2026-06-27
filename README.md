# NutriTrack 🍎
Mini proyecto Django para rastreo de calorías y macronutrientes.

## Requisitos
- Python 3.10+
- pip

## Instalación rápida

```bash
# 1. Instalar Django
pip install django

# 2. Ir a la carpeta
cd nutritrack

# 3. Correr migraciones (crea la base de datos SQLite)
python manage.py migrate

# 4. Crear superusuario (opcional, para /admin)
python manage.py createsuperuser

# 5. Iniciar servidor
python manage.py runserver
```

Abrir: http://127.0.0.1:8000

## Flujo
1. Ir a /register → crear cuenta
2. Login → dashboard con los 4 donuts (Calorías, Proteína, Carbos, Grasa)
3. Llenar el formulario "Add Food" → se guarda en SQLite
4. Los donuts se actualizan automáticamente
5. Botón ✕ para borrar entradas

## Estructura
```
nutritrack/
├── manage.py
├── db.sqlite3          ← se crea al migrar
├── nutritrack/         ← configuración
│   ├── settings.py
│   └── urls.py
└── tracker/            ← app principal
    ├── models.py       ← FoodEntry (BD)
    ├── views.py        ← lógica
    ├── urls.py         ← rutas
    └── templates/
        └── tracker/
            ├── dashboard.html
            ├── login.html
            └── register.html
```
