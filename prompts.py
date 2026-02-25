"""
Prompts para generar contenido diario de Colombia-IA.
Cada día tiene un tema diferente para mantener variedad.
Los subtemas rotan por semana del año para evitar repetición.
"""

# Subtemas rotatorios por día (8 opciones = ciclo de 8 semanas)
SUBTOPICS = {
    # Lunes: Tendencias
    0: [
        "Agentes de IA autónomos",
        "RAG (Retrieval Augmented Generation)",
        "Modelos multimodales (texto + imagen + audio)",
        "IA generativa para código",
        "Fine-tuning accesible para todos",
        "IA en dispositivos edge/móviles",
        "Modelos de lenguaje pequeños (SLMs)",
        "IA para automatización de workflows",
    ],
    # Martes: Herramientas
    1: [
        "herramientas de IA para escribir y editar texto",
        "herramientas de IA para generar y editar imágenes",
        "herramientas de IA para audio y voz",
        "herramientas de IA para video",
        "herramientas de IA para programar",
        "herramientas de IA para productividad personal",
        "herramientas de IA para análisis de datos",
        "herramientas de IA para automatización",
    ],
    # Miércoles: Tips de prompting
    2: [
        "la técnica Chain of Thought (pensar paso a paso)",
        "la técnica Few-Shot (dar ejemplos)",
        "la técnica de Role-Playing (asignar un rol)",
        "cómo estructurar prompts largos",
        "cómo obtener respuestas más precisas",
        "cómo usar restricciones y formatos",
        "cómo iterar y mejorar prompts",
        "prompts para tareas específicas (resumir, traducir, analizar)",
    ],
    # Jueves: Datos/Estadísticas
    3: [
        "adopción de IA en empresas",
        "impacto de IA en el mercado laboral",
        "inversión global en IA",
        "productividad con herramientas de IA",
        "uso de IA generativa",
        "IA en diferentes industrias",
        "crecimiento de startups de IA",
        "acceso a IA en Latinoamérica",
    ],
    # Viernes: IA en LATAM
    4: [
        "startups de IA en Colombia",
        "startups de IA en México, Argentina o Brasil",
        "universidades con programas de IA en LATAM",
        "oportunidades de trabajo remoto en IA para LATAM",
        "retos de implementar IA en la región",
        "casos de éxito de IA en empresas latinoamericanas",
        "comunidades de IA en español",
        "gobierno y políticas de IA en LATAM",
    ],
    # Sábado: Conceptos
    5: [
        "LLM (Large Language Model)",
        "Tokens y tokenización",
        "Embeddings",
        "Fine-tuning",
        "RAG (Retrieval Augmented Generation)",
        "Prompt Engineering",
        "Temperatura y parámetros de generación",
        "Alucinaciones en IA",
    ],
    # Domingo: Temas de debate
    6: [
        "el futuro del trabajo con IA",
        "ética y sesgos en IA",
        "herramientas de IA favoritas",
        "cómo aprender sobre IA",
        "IA reemplazando vs augmentando humanos",
        "regulación de IA",
        "IA en educación",
        "privacidad y datos en IA",
    ],
}


def get_subtopic(day: int, week_number: int) -> str:
    """Retorna el subtema correspondiente al día y semana del año."""
    subtopics = SUBTOPICS[day]
    index = week_number % len(subtopics)
    return subtopics[index]


def get_prompt_with_subtopic(day: int, week_number: int) -> str:
    """Retorna el prompt del día con el subtema de la semana incluido."""
    base_prompt = PROMPTS[day]
    subtopic = get_subtopic(day, week_number)

    # Añadir instrucción específica del subtema al inicio del prompt
    subtopic_instruction = f"TEMA ESPECÍFICO PARA ESTA SEMANA: {subtopic}\n\nDebes hablar específicamente sobre este tema, no elijas otro.\n\n"

    return subtopic_instruction + base_prompt


SYSTEM_PROMPT = """Eres el editor de Colombia-IA, una comunidad de inteligencia artificial en Colombia y Latinoamérica.

Tu objetivo es crear contenido que sea:
- PRÁCTICO: Que la gente pueda aplicar hoy mismo
- CONCISO: Máximo 280 palabras, para leer rápido en el celular
- EN ESPAÑOL: Tono cercano, sin ser demasiado formal ni demasiado coloquial
- ACCIONABLE: Incluye pasos concretos, ejemplos o datos específicos

IMPORTANTE:
- NO inventes enlaces/URLs (solo menciona nombres de herramientas/recursos)
- NO uses información que pueda estar desactualizada
- Termina siempre con una pregunta o invitación a comentar
- Incluye hashtags relevantes al final: #IA #ColombiaIA #InteligenciaArtificial"""

# Lunes: Tendencia de la semana
PROMPT_MONDAY = """Genera un post sobre UNA tendencia actual en inteligencia artificial.

Formato:
🔥 Tendencia: [Nombre de la tendencia]

[Explicación de qué es y por qué importa en 2-3 oraciones]

📈 Por qué está en auge:
[2-3 razones en bullets cortos]

🎯 Cómo te afecta:
[1-2 aplicaciones prácticas para profesionales/emprendedores en LATAM]

💬 ¿Qué opinas de esta tendencia? ¿Ya la estás aplicando?

#IA #Tendencias #ColombiaIA #InteligenciaArtificial

Ejemplos de tendencias: Agentes de IA, RAG, modelos multimodales, IA generativa para código, fine-tuning accesible, IA en el edge, etc. Elige una que sea relevante y práctica."""

# Martes: Herramienta práctica
PROMPT_TUESDAY = """Genera un post sobre UNA herramienta de IA que sea:
- Práctica y que alguien pueda usar HOY mismo
- Gratuita o con plan gratuito generoso
- Útil para profesionales, emprendedores o estudiantes

Formato:
🛠️ Herramienta del día: [Nombre]

[Descripción de qué hace en 1-2 oraciones]

✅ Para qué sirve:
[3 casos de uso prácticos en bullets cortos]

🚀 Cómo empezar:
[Instrucción simple de 1-2 pasos, sin enlaces]

💬 ¿Ya la conocías? ¿Qué herramienta de IA usas todos los días?

#IA #Herramientas #ColombiaIA #InteligenciaArtificial

IMPORTANTE: No repitas herramientas obvias como ChatGPT o Midjourney. Sorprende con algo útil y menos conocido. Varía entre herramientas de: texto, imagen, audio, video, código, productividad, análisis de datos, automatización, etc."""

# Miércoles: Tip de prompting
PROMPT_WEDNESDAY = """Genera un post con UN tip práctico de prompting o productividad con IA.

Formato:
💡 Tip del día: [Título corto del tip]

[Explicación del problema que resuelve en 1 oración]

📝 Cómo hacerlo:
[Paso a paso simple, máximo 3 pasos]

✨ Ejemplo:
[Un ejemplo concreto de antes/después o un prompt de muestra]

🎯 Resultado: [Qué logras con este tip]

💬 ¿Tienes algún tip de prompting favorito? ¡Compártelo!

#IA #Prompting #Tips #ColombiaIA #InteligenciaArtificial

Ideas de tips: técnicas de prompting (chain of thought, few-shot, role-playing), atajos de productividad, formas de estructurar prompts, cómo obtener mejores respuestas, etc."""

# Jueves: Dato o estadística
PROMPT_THURSDAY = """Genera un post con UN dato o estadística interesante sobre IA.

Formato:
📊 Dato del día

[El dato/estadística presentado de forma impactante]

🔍 Contexto:
[Por qué este dato es importante o sorprendente en 2-3 oraciones]

💡 Qué significa para ti:
[Implicación práctica para profesionales/emprendedores en LATAM]

💬 ¿Te sorprende este dato? ¿Cómo crees que impactará tu industria?

#IA #Datos #ColombiaIA #InteligenciaArtificial

IMPORTANTE: Usa datos que sean razonablemente conocidos y verificables sobre adopción de IA, mercado laboral, productividad, inversión en IA, uso empresarial, etc. No inventes estadísticas específicas con porcentajes exactos si no estás seguro."""

# Viernes: IA en Latinoamérica
PROMPT_FRIDAY = """Genera un post sobre IA en el contexto de Latinoamérica o Colombia.

Formato:
🇨🇴 IA en nuestra región

[Tema: puede ser una empresa, iniciativa, oportunidad o reto de IA en LATAM]

🌎 De qué se trata:
[Explicación en 2-3 oraciones]

💪 Por qué importa para LATAM:
[2-3 puntos sobre relevancia regional]

🚀 Oportunidad:
[Cómo aprovechar esto o qué aprender de ello]

💬 ¿Conoces proyectos de IA en Colombia o LATAM? ¡Cuéntanos!

#IA #Colombia #LATAM #ColombiaIA #InteligenciaArtificial

Ideas: startups de IA en la región, universidades con programas de IA, oportunidades de trabajo remoto en IA, retos específicos de LATAM que la IA puede resolver, casos de éxito locales, etc."""

# Sábado: Concepto explicado simple
PROMPT_SATURDAY = """Genera un post explicando UN concepto de IA de forma simple, para alguien sin conocimientos técnicos.

Formato:
🎓 Aprende: [Nombre del concepto]

[Definición en 1 oración simple, como explicarías a un amigo]

🧠 Analogía:
[Una analogía de la vida real que lo haga fácil de entender]

⚡ En la práctica:
[1-2 ejemplos de cómo se usa este concepto en aplicaciones reales]

🎯 Para qué te sirve saberlo:
[Por qué es útil entender este concepto]

💬 ¿Te quedó claro? ¿Qué concepto de IA te gustaría que expliquemos?

#IA #Aprendizaje #ColombiaIA #InteligenciaArtificial

Ideas de conceptos: LLM, tokens, embeddings, fine-tuning, RAG, prompt engineering, temperatura, alucinaciones, contexto, API, modelo base vs chat, entrenamiento vs inferencia, etc."""

# Domingo: Pregunta para discusión
PROMPT_SUNDAY = """Genera una pregunta interesante para generar discusión en la comunidad sobre IA.

La pregunta debe ser:
- Abierta (no tiene respuesta correcta única)
- Relevante para profesionales y entusiastas de IA
- Que invite a compartir experiencias u opiniones
- Relacionada con IA y su impacto en trabajo/vida/sociedad

Formato:
🗳️ Pregunta de la semana

[La pregunta principal, clara y directa]

🤔 Contexto:
[1-2 oraciones dando contexto de por qué es relevante]

Opciones sugeridas (para que la gente elija o comente):
• [Opción A]
• [Opción B]
• [Opción C]
• Otra respuesta (comenta 👇)

💬 ¡Queremos saber tu opinión!

#IA #Debate #ColombiaIA #InteligenciaArtificial

Ideas de temas: futuro del trabajo con IA, ética en IA, herramientas favoritas, cómo aprendieron sobre IA, impacto en sus industrias, preocupaciones sobre IA, etc."""

# Mapeo de día a prompt
PROMPTS = {
    0: PROMPT_MONDAY,      # Lunes
    1: PROMPT_TUESDAY,     # Martes
    2: PROMPT_WEDNESDAY,   # Miércoles
    3: PROMPT_THURSDAY,    # Jueves
    4: PROMPT_FRIDAY,      # Viernes
    5: PROMPT_SATURDAY,    # Sábado
    6: PROMPT_SUNDAY,      # Domingo
}

DAY_NAMES = {
    0: "Lunes",
    1: "Martes",
    2: "Miércoles",
    3: "Jueves",
    4: "Viernes",
    5: "Sábado",
    6: "Domingo",
}
