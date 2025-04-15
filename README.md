# 🛰 Registro de Fronteras — Sistema Integrado de Automatización

Este proyecto integra tres componentes:

1. **Backend** en Django (`Registro_de_fronteras`)
2. **Frontend** en Laravel (`frontera.mx`)
3. **Automatización con Web UI de Browser-Use (Docker)**

Su propósito es automatizar el diligenciamiento de formularios a partir de datos recogidos por la API y enviados automáticamente por un navegador controlado por Browser-Use.

---

## 📁 Estructura del Proyecto

```bash
├── Registro_de_fronteras/   # Backend Django
├── fronteraXM/             # Frontend Laravel
├── browser-use/             # Automatización (solo Docker)
├── Makefile
├── README.md
└── .env.example
```


## 🔐 Variables de Entorno

Copia el archivo `.env.example` y renómbralo a `.env` en la raíz del proyecto Django:

```bash
cp .env.example .env
```

### Contenido de ejemplo (`.env`):

```env
SECRECT_KEY = django-insecure-XXXXX-XXXXX-XXXX
DB_HOST = localhost
DB_PORT = 5432
DB_PASSWORD = password
DB_NAME = database
```

---

## 🛠️ Instalación y Ejecución

### 1. Instalar `Makefile`

```powershell
    choco install make
```

### 2. Instalar todo con `Makefile`

Este proyecto incluye un `Makefile` que automatiza todo el entorno.

### Comandos principales

| Comando            | Qué hace                                                                 |
|--------------------|--------------------------------------------------------------------------|
| `make setup`       | Instala dependencias y levanta el backend en el puerto **8000**          |
| `make frontend`    | Instala dependencias y levanta el frontend en el puerto **80**           |
| `make browser`     | Clona y ejecuta Browser-Use en Docker                                    |
| `make reset`       | Borra migraciones y reinicia la base de datos Django                    |

> ⚠️ **Ejecuta `make setup` y `make frontend` en consolas diferentes.** Composer no funciona bien si no se lanza en su propia terminal.

---

## 🌐 Accesos Locales

| Componente     | URL                             |
|----------------|---------------------------------|
| Backend API    | http://localhost:8000/api/      |
| Frontend       | http://localhost:80             |
| Web UI Browser | http://localhost:3000           |

---

## 🤖 Automatización con Browser-Use

Browser-Use debe clonarse desde GitHub si no está presente:

```bash
git clone https://github.com/browser-use/browser-use.git
cd browser-use
docker-compose up -d
```

También puedes usar:

```bash
make browser
```

Esto lanzará el Web UI de automatización en `http://localhost:7788`.

---

## 🧠 Prompt para Browser-Use

Copia y pega esta prompt en la Web UI de Browser-Use:

```
Visita http://localhost:80 en el navegador.

1. Espera a que cargue completamente la página con el formulario de curvas LBC.
2. Haz una petición GET a la URL http://localhost:8000/api/formulario/ultimo/
3. Espera la respuesta JSON.
4. Usa los siguientes campos del JSON para completar el formulario web:

- Campo "Curva": escribe el valor `"LBC"`
- Campo "Fecha": usa la fecha actual del sistema (formato YYYY-MM-DD)
- Campo "Frontera": selecciona el ID contenido en `frontera_id`
- Campo "Nombre del registro": toma el nombre del usuario desde `registro.usuario.nombre`
- Campo "Número de Certificación": usa el `id` del objeto `documento`
- Campo "Entidad Certificadora": escribe el texto `"CREG"`

5. Una vez diligenciado el formulario, haz clic en el botón "Guardar" (o su equivalente).
6. Espera el mensaje o señal que confirme que el formulario fue enviado exitosamente.
```

---

## 🧹 Limpieza del Proyecto

Si deseas reiniciar todo el entorno:

```bash
make reset
```

Esto eliminará migraciones y reconstruirá la base de datos.
