# Discord Bot

Este es un bot sencillo desarrollado en **Python** usando la librería [discord.py](https://discordpy.readthedocs.io/) y [dotenv](https://pypi.org/project/python-dotenv/) para la gestión de variables de entorno.

El bot incluye funcionalidades básicas como:

- Mensaje de bienvenida automático a nuevos miembros.
- Moderación de mensajes (bloqueo de ciertas palabras).
- Comandos simples (`hello`, `assing`, `remove`, `secret`).
- Manejo de roles dentro del servidor.

---

## Requisitos

Antes de ejecutar el bot, asegúrate de tener:

- **Python 3.8 o superior**
- Una cuenta de **Discord** y un **servidor** donde usar el bot.
- Una **aplicación de Discord** registrada desde [Discord Developer Portal](https://discord.com/developers/applications).
- La librería **discord.py** instalada.

---

## Instalación

# 1. Clona este repositorio o copia el código en tu proyecto

git clone <url-del-repo>
cd discord-bot

# 2. Crea un entorno virtual (opcional pero recomendado)

python -m venv venv
source venv/bin/activate # En Linux/Mac
venv\Scripts\activate # En Windows

# 3. Instala las dependencias necesarias

pip install -r requirements.txt

## Ejecución

```bash
python main.py
```

## Funcionalidades

### 🔹 Eventos

- **on_ready** → Indica en consola que el bot está listo.
- **on_member_join** → Envía un mensaje privado de bienvenida a nuevos miembros.
- **on_message** →
  - Elimina mensajes que contengan la palabra prohibida `"shit"`.
  - Responde con advertencia al usuario que la use.

### 🔹 Comandos

- **!hello** → Responde con un saludo al autor.
- **!assing** → Asigna el rol definido en `secret_role`.
- **!remove** → Quita el rol definido en `secret_role`.
- **!secret** → Solo accesible para quienes tengan el rol `developer`.
  - En caso de no tenerlo, el bot mostrará un mensaje indicando falta de permisos.

---

## Logs

El bot genera un archivo **`discord.log`** donde guarda:

- Errores
- Actividad del bot
