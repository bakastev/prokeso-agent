import os
from dataclasses import dataclass
import httpx
import logfire
from pydantic_ai import Agent, RunContext

logfire.configure(send_to_logfire='if-token-present')

@dataclass
class Deps:
    client: httpx.AsyncClient
    supabase_api_key: str
    supabase_url: str

cms_crm_agent = Agent(
    'openai:gpt-4o',
    system_prompt=(
        "Du bist ein CRM/CMS-Agent mit direktem Zugriff auf die Supabase-Datenbank. "
        "Du kannst folgende Aktionen als Tools ausführen: Produkte, Kunden, Testimonials, Partner, Lieferanten, Bilder, Textbausteine und Kontaktanfragen anlegen, auflisten, aktualisieren und löschen. "
        "Nutze IMMER die verfügbaren Tools, um Benutzeranfragen zu beantworten. "
        "Antworte niemals mit 'Ich habe keinen Zugriff', sondern führe die passende Tool-Operation aus und gib das Ergebnis zurück."
    ),
    deps_type=Deps,
    retries=2,
)

import agent_tools 