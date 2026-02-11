# Colombia-IA Telegram Bot

Bot que publica automáticamente contenido diario de IA en el canal de Telegram de [Colombia-IA](https://colombia-ia.github.io/).

## Qué hace

Todos los días a las 7:00 AM (hora Colombia), el bot genera y publica contenido de IA usando Gemini 2.0 Flash:

| Día | Contenido |
|-----|-----------|
| Lunes | 🔥 Tendencia de la semana |
| Martes | 🛠️ Herramienta práctica |
| Miércoles | 💡 Tip de prompting |
| Jueves | 📊 Dato/estadística |
| Viernes | 🇨🇴 IA en Latinoamérica |
| Sábado | 🎓 Concepto explicado |
| Domingo | 🗳️ Pregunta para discusión |

## Setup en 5 minutos

### 1. Crear bot en Telegram

1. Abre Telegram y busca `@BotFather`
2. Envía `/newbot` y sigue las instrucciones
3. Guarda el **token** que te da (algo como `123456789:ABCdefGHI...`)

### 2. Crear canal en Telegram

1. Crea un nuevo canal (puede ser público o privado)
2. Si es público, elige un username (ej: `@colombia_ia`)
3. Ve a configuración del canal > Administradores > Agregar administrador
4. Busca tu bot y agrégalo con permiso de **publicar mensajes**

### 3. Obtener API key de Gemini

1. Ve a [Google AI Studio](https://aistudio.google.com/apikey)
2. Crea una API key (es gratis)
3. Guarda la key

### 4. Configurar el repositorio

1. Haz fork de este repo o clónalo en tu organización
2. Ve a **Settings > Secrets and variables > Actions**
3. Agrega estos secrets:

| Secret | Valor |
|--------|-------|
| `GEMINI_API_KEY` | Tu API key de Google AI Studio |
| `TELEGRAM_BOT_TOKEN` | El token de @BotFather |
| `TELEGRAM_CHANNEL_ID` | `@tucanal` (con @) o el ID numérico |

### 5. Activar GitHub Actions

1. Ve a la pestaña **Actions** del repo
2. Habilita los workflows si están desactivados
3. Ejecuta manualmente "Daily AI Post" para probar

## Ejecución local (para desarrollo)

```bash
# Clonar repo
git clone https://github.com/Colombia-IA/telegram-bot.git
cd telegram-bot

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# o: venv\Scripts\activate  # Windows

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
cp .env.example .env
# Edita .env con tus credenciales

# Ejecutar (modo prueba, no publica)
python bot.py --dry-run

# Ejecutar simulando un día específico
python bot.py --day tuesday --dry-run

# Ejecutar y publicar de verdad
python bot.py
```

## Estructura del proyecto

```
├── bot.py              # Script principal
├── prompts.py          # Prompts para cada día
├── requirements.txt    # Dependencias
├── .env.example        # Ejemplo de variables
├── .github/
│   └── workflows/
│       └── daily_post.yml  # GitHub Action
└── README.md
```

## Opcional: Grupo de discusión

Para que cada post tenga comentarios:

1. Crea un grupo de Telegram
2. En el canal, ve a **Configuración > Discusión**
3. Vincula el grupo

Ahora cada post del canal tendrá automáticamente una sección de comentarios.

## Costos

**$0** - Todo es gratis:
- GitHub Actions: gratis para repos públicos
- Gemini 2.0 Flash: gratis hasta 1500 requests/día (usamos 1)
- Telegram Bot API: gratis

## Contribuir

Este proyecto es parte de [Colombia-IA](https://colombia-ia.github.io/). Si tienes ideas para mejorar los prompts o agregar funcionalidades, abre un issue o PR.

## Licencia

MIT
