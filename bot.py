#!/usr/bin/env python3
"""
Colombia-IA Telegram Bot
Publica automáticamente contenido diario de IA generado por Gemini.
"""

import os
import sys
import argparse
from datetime import datetime
import pytz
import requests
from google import genai
from google.genai import types

from prompts import PROMPTS, SYSTEM_PROMPT, DAY_NAMES

# Configuración
COLOMBIA_TZ = pytz.timezone("America/Bogota")
TELEGRAM_API_URL = "https://api.telegram.org/bot{token}/{method}"


def get_env_var(name: str) -> str:
    """Obtiene variable de entorno o falla con mensaje claro."""
    value = os.environ.get(name)
    if not value:
        print(f"Error: Variable de entorno {name} no configurada")
        sys.exit(1)
    return value


def get_day_of_week(override: str = None) -> int:
    """Retorna el día de la semana (0=Lunes, 6=Domingo)."""
    if override:
        days = {
            "monday": 0, "tuesday": 1, "wednesday": 2, "thursday": 3,
            "friday": 4, "saturday": 5, "sunday": 6,
            "lunes": 0, "martes": 1, "miercoles": 2, "jueves": 3,
            "viernes": 4, "sabado": 5, "domingo": 6,
        }
        return days.get(override.lower(), 0)

    now = datetime.now(COLOMBIA_TZ)
    return now.weekday()


def generate_content(day: int) -> str:
    """Genera contenido usando Gemini 1.5 Flash."""
    api_key = get_env_var("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    prompt = PROMPTS[day]
    day_name = DAY_NAMES[day]

    print(f"Generando contenido para {day_name}...")

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
        ),
    )

    if not response.text:
        print("Error: Gemini no generó contenido")
        sys.exit(1)

    return response.text


def send_telegram_message(text: str) -> bool:
    """Envía mensaje al canal de Telegram."""
    token = get_env_var("TELEGRAM_BOT_TOKEN")
    channel_id = get_env_var("TELEGRAM_CHANNEL_ID")

    url = TELEGRAM_API_URL.format(token=token, method="sendMessage")

    payload = {
        "chat_id": channel_id,
        "text": text,
        "parse_mode": "Markdown",
        "disable_web_page_preview": True,
    }

    print(f"Enviando mensaje a {channel_id}...")

    response = requests.post(url, json=payload, timeout=30)

    if response.status_code != 200:
        print(f"Error de Telegram: {response.status_code}")
        print(response.text)
        return False

    result = response.json()
    if not result.get("ok"):
        print(f"Error de Telegram API: {result}")
        return False

    print("Mensaje enviado exitosamente!")
    return True


def send_telegram_poll(question: str, options: list[str]) -> bool:
    """Envía encuesta al canal de Telegram (para domingos)."""
    token = get_env_var("TELEGRAM_BOT_TOKEN")
    channel_id = get_env_var("TELEGRAM_CHANNEL_ID")

    url = TELEGRAM_API_URL.format(token=token, method="sendPoll")

    payload = {
        "chat_id": channel_id,
        "question": question,
        "options": options,
        "is_anonymous": False,
        "allows_multiple_answers": False,
    }

    print(f"Enviando encuesta a {channel_id}...")

    response = requests.post(url, json=payload, timeout=30)

    if response.status_code != 200:
        print(f"Error de Telegram: {response.status_code}")
        print(response.text)
        return False

    result = response.json()
    if not result.get("ok"):
        print(f"Error de Telegram API: {result}")
        return False

    print("Encuesta enviada exitosamente!")
    return True


def main():
    """Función principal."""
    parser = argparse.ArgumentParser(description="Colombia-IA Telegram Bot")
    parser.add_argument(
        "--day",
        type=str,
        help="Día a simular (monday, tuesday, etc.) para testing",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Solo genera contenido, no publica en Telegram",
    )
    args = parser.parse_args()

    # Determinar día
    day = get_day_of_week(args.day)
    day_name = DAY_NAMES[day]
    print(f"=== Colombia-IA Bot - {day_name} ===")

    # Generar contenido
    content = generate_content(day)

    print("\n--- Contenido generado ---")
    print(content)
    print("--- Fin del contenido ---\n")

    if args.dry_run:
        print("Modo dry-run: no se publicó en Telegram")
        return

    # Publicar en Telegram
    success = send_telegram_message(content)

    if not success:
        sys.exit(1)

    print("=== Proceso completado ===")


if __name__ == "__main__":
    main()
