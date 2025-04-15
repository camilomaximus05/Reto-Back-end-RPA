# Makefile para levantar el entorno completo del proyecto

# Variables
DJANGO_FOLDER=Registro_de_fronteras
LARAVEL_FOLDER=fronterasXM
BROWSER_USE_REPO=https://github.com/browser-use/Web-UI.git
BROWSER_USE_FOLDER=Web-UI

setup:
	@echo "Iniciando entorno del proyecto..."

	@echo "1. Instalando dependencias del backend (Django)..."
	pip install -r requirements.txt

	@echo "2. Aplicando migraciones de Django..."
	python manage.py migrate

	@echo "3. Levantando servidor de Django en puerto 8000..."
	cmd /C start cmd /K "python manage.py runserver 8000"

	@echo "4. Instalando dependencias del frontend (Laravel)..."
	cd $(LARAVEL_FOLDER) && composer install

	@echo "5. Levantando servidor Laravel en puerto 80..."
	cmd /C start cmd /K "cd $(LARAVEL_FOLDER) && php artisan serve --host=0.0.0.0 --port=80"

	@echo "6. Clonando y levantando Browser-Use Web-UI..."
	if not exist $(BROWSER_USE_FOLDER) git clone $(BROWSER_USE_REPO)
	cd $(BROWSER_USE_FOLDER) && docker compose up -d

	@echo "Entorno completo listo."

