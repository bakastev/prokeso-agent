from agent import cms_crm_agent, Deps, RunContext

@cms_crm_agent.tool
async def create_product(ctx: RunContext[Deps], product_info: dict) -> str:
    """Erstellt ein neues Produkt in der Supabase-Tabelle."""
    response = await ctx.deps.client.post(
        f'{ctx.deps.supabase_url}/rest/v1/products',
        headers={
            'Authorization': f'Bearer {ctx.deps.supabase_api_key}',
            'Content-Type': 'application/json'
        },
        json=product_info
    )
    if response.status_code == 201:
        return "Produkt erfolgreich erstellt."
    else:
        return f"Fehler beim Erstellen des Produkts: {response.text}" 