# Colombia-IA Telegram Bot

## Resumen del Proyecto

Bot de Telegram que publica automáticamente 1 post diario sobre IA para la comunidad Colombia-IA. El contenido es generado por Gemini 2.0 Flash y publicado via GitHub Actions (gratis, sin servidor).

## Enlaces Importantes

- **Organización GitHub**: https://github.com/orgs/Colombia-IA/
- **Página web**: https://colombia-ia.github.io/
- **Canal Telegram**: @colombia_ia (por crear)

## Stack Técnico

- **Python 3.11+**
- **Gemini 2.0 Flash** - Generación de contenido (free tier: 1500 req/día)
- **Telegram Bot API** - Publicación via HTTP requests
- **GitHub Actions** - Cron scheduler (gratis)

## Estructura del Proyecto

```
telegram_group_colombia_ia/
├── bot.py                    # Script principal (~100 líneas)
├── prompts.py                # Prompts por día + subtemas rotatorios por semana
├── requirements.txt          # google-genai, requests
├── .env                      # Variables secretas (NO commitear)
├── .env.example              # Ejemplo de variables necesarias
├── .gitignore                # Excluye .env y __pycache__
├── .github/
│   └── workflows/
│       └── daily_post.yml    # Cron: 9:00 AM Colombia (14:00 UTC)
├── README.md                 # Setup en 5 minutos
└── claude.md                 # Este archivo
```

## Calendario de Contenido

| Día | Tema | Emoji |
|-----|------|-------|
| Lunes | Tendencia de la semana en IA | 🔥 |
| Martes | Herramienta de IA práctica | 🛠️ |
| Miércoles | Tip de prompting/productividad | 💡 |
| Jueves | Dato o estadística de IA | 📊 |
| Viernes | IA en Latinoamérica | 🇨🇴 |
| Sábado | Concepto de IA explicado simple | 🎓 |
| Domingo | Pregunta para discusión (poll) | 🗳️ |

## Sistema de Subtemas Rotatorios

Para evitar contenido repetitivo, cada día tiene 8 subtemas que rotan según el número de semana del año. Esto garantiza variedad durante 8 semanas antes de repetir.

Ejemplo para Martes (Herramientas):
- Semana 1: herramientas de texto
- Semana 2: herramientas de imagen
- Semana 3: herramientas de audio
- ...hasta semana 8, luego reinicia

Los subtemas están definidos en `prompts.py` en el diccionario `SUBTOPICS`. Para modificarlos, edita ese diccionario.

## Variables de Entorno

```bash
GEMINI_API_KEY=         # API key de Google AI Studio
TELEGRAM_BOT_TOKEN=     # Token de @BotFather
TELEGRAM_CHANNEL_ID=    # @colombia_ia
```

## Decisiones de Diseño

1. **Contenido Evergreen vs Noticias**: Se optó por contenido práctico/evergreen porque:
   - Genera más engagement
   - No caduca
   - Diferencia a la comunidad de cuentas de noticias genéricas
   - Si la comunidad pide noticias, se puede añadir grounding después

2. **Gemini 2.0 Flash vs otras opciones**:
   - Gratis (1500 req/día, usamos 1)
   - Buen español
   - API simple (nueva librería google-genai)

3. **requests vs python-telegram-bot**:
   - requests es más ligero
   - Solo necesitamos sendMessage y sendPoll
   - Menos dependencias = menos problemas

## Comandos Útiles

```bash
# Ejecutar localmente
python bot.py

# Ejecutar un día específico (para testing)
python bot.py --day monday

# Ver logs de GitHub Actions
# Ir a: Actions > Daily AI Post > último run
```

## TODO Futuro (no para MVP)

- [ ] Añadir grounding para noticias reales si la comunidad lo pide
- [ ] Métricas de engagement
- [ ] Integración con grupo de discusión
- [ ] Posts especiales para fechas importantes
