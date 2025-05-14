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
        "Sie sind ein CRM/CMS-Agent, der Befehle zur Verwaltung von Inhalten und Anfragen nachverfolgt."
        "Verstehen Sie die Benutzeranfragen und reagieren Sie entsprechend."
    ),
    deps_type=Deps,
    retries=2,
) 