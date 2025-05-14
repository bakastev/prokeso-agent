from agent import cms_crm_agent, Deps, RunContext

# --- text_contents ---
@cms_crm_agent.tool
async def create_text_content(ctx: RunContext[Deps], content_info: dict) -> str:
    response = await ctx.deps.client.post(
        f'{ctx.deps.supabase_url}/rest/v1/text_contents',
        headers={
            'Authorization': f'Bearer {ctx.deps.supabase_api_key}',
            'Content-Type': 'application/json',
            'apikey': ctx.deps.supabase_api_key
        },
        json=content_info
    )
    return "Text-Content erfolgreich erstellt." if response.status_code == 201 else f"Fehler beim Erstellen: {response.text}"

@cms_crm_agent.tool
async def list_text_contents(ctx: RunContext[Deps]) -> list:
    response = await ctx.deps.client.get(
        f'{ctx.deps.supabase_url}/rest/v1/text_contents?select=*',
        headers={'Authorization': f'Bearer {ctx.deps.supabase_api_key}', 'apikey': ctx.deps.supabase_api_key}
    )
    return response.json() if response.status_code == 200 else []

@cms_crm_agent.tool
async def update_text_content(ctx: RunContext[Deps], id: str, update_data: dict) -> str:
    response = await ctx.deps.client.patch(
        f'{ctx.deps.supabase_url}/rest/v1/text_contents?id=eq.{id}',
        headers={
            'Authorization': f'Bearer {ctx.deps.supabase_api_key}',
            'Content-Type': 'application/json',
            'apikey': ctx.deps.supabase_api_key
        },
        json=update_data
    )
    return "Text-Content erfolgreich aktualisiert." if response.status_code == 204 else f"Fehler beim Aktualisieren: {response.text}"

@cms_crm_agent.tool
async def delete_text_content(ctx: RunContext[Deps], id: str) -> str:
    response = await ctx.deps.client.delete(
        f'{ctx.deps.supabase_url}/rest/v1/text_contents?id=eq.{id}',
        headers={'Authorization': f'Bearer {ctx.deps.supabase_api_key}', 'apikey': ctx.deps.supabase_api_key}
    )
    return "Text-Content erfolgreich gelöscht." if response.status_code == 204 else f"Fehler beim Löschen: {response.text}"

# --- products ---
@cms_crm_agent.tool
async def create_product(ctx: RunContext[Deps], product_info: dict) -> str:
    response = await ctx.deps.client.post(
        f'{ctx.deps.supabase_url}/rest/v1/products',
        headers={
            'Authorization': f'Bearer {ctx.deps.supabase_api_key}',
            'Content-Type': 'application/json',
            'apikey': ctx.deps.supabase_api_key
        },
        json=product_info
    )
    return "Produkt erfolgreich erstellt." if response.status_code == 201 else f"Fehler beim Erstellen: {response.text}"

@cms_crm_agent.tool
async def list_products(ctx: RunContext[Deps]) -> list:
    response = await ctx.deps.client.get(
        f'{ctx.deps.supabase_url}/rest/v1/products?select=*',
        headers={'Authorization': f'Bearer {ctx.deps.supabase_api_key}', 'apikey': ctx.deps.supabase_api_key}
    )
    print("DEBUG Supabase-Response:", response.status_code, response.text)
    return response.json() if response.status_code == 200 else []

@cms_crm_agent.tool
async def update_product(ctx: RunContext[Deps], id: str, update_data: dict) -> str:
    response = await ctx.deps.client.patch(
        f'{ctx.deps.supabase_url}/rest/v1/products?id=eq.{id}',
        headers={
            'Authorization': f'Bearer {ctx.deps.supabase_api_key}',
            'Content-Type': 'application/json',
            'apikey': ctx.deps.supabase_api_key
        },
        json=update_data
    )
    return "Produkt erfolgreich aktualisiert." if response.status_code == 204 else f"Fehler beim Aktualisieren: {response.text}"

@cms_crm_agent.tool
async def delete_product(ctx: RunContext[Deps], id: str) -> str:
    response = await ctx.deps.client.delete(
        f'{ctx.deps.supabase_url}/rest/v1/products?id=eq.{id}',
        headers={'Authorization': f'Bearer {ctx.deps.supabase_api_key}', 'apikey': ctx.deps.supabase_api_key}
    )
    return "Produkt erfolgreich gelöscht." if response.status_code == 204 else f"Fehler beim Löschen: {response.text}"

# --- customers ---
@cms_crm_agent.tool
async def create_customer(ctx: RunContext[Deps], customer_info: dict) -> str:
    response = await ctx.deps.client.post(
        f'{ctx.deps.supabase_url}/rest/v1/customers',
        headers={
            'Authorization': f'Bearer {ctx.deps.supabase_api_key}',
            'Content-Type': 'application/json',
            'apikey': ctx.deps.supabase_api_key
        },
        json=customer_info
    )
    return "Kunde erfolgreich erstellt." if response.status_code == 201 else f"Fehler beim Erstellen: {response.text}"

@cms_crm_agent.tool
async def list_customers(ctx: RunContext[Deps]) -> list:
    response = await ctx.deps.client.get(
        f'{ctx.deps.supabase_url}/rest/v1/customers?select=*',
        headers={'Authorization': f'Bearer {ctx.deps.supabase_api_key}', 'apikey': ctx.deps.supabase_api_key}
    )
    return response.json() if response.status_code == 200 else []

@cms_crm_agent.tool
async def update_customer(ctx: RunContext[Deps], id: str, update_data: dict) -> str:
    response = await ctx.deps.client.patch(
        f'{ctx.deps.supabase_url}/rest/v1/customers?id=eq.{id}',
        headers={
            'Authorization': f'Bearer {ctx.deps.supabase_api_key}',
            'Content-Type': 'application/json',
            'apikey': ctx.deps.supabase_api_key
        },
        json=update_data
    )
    return "Kunde erfolgreich aktualisiert." if response.status_code == 204 else f"Fehler beim Aktualisieren: {response.text}"

@cms_crm_agent.tool
async def delete_customer(ctx: RunContext[Deps], id: str) -> str:
    response = await ctx.deps.client.delete(
        f'{ctx.deps.supabase_url}/rest/v1/customers?id=eq.{id}',
        headers={'Authorization': f'Bearer {ctx.deps.supabase_api_key}', 'apikey': ctx.deps.supabase_api_key}
    )
    return "Kunde erfolgreich gelöscht." if response.status_code == 204 else f"Fehler beim Löschen: {response.text}"

# --- testimonials ---
@cms_crm_agent.tool
async def create_testimonial(ctx: RunContext[Deps], testimonial_info: dict) -> str:
    response = await ctx.deps.client.post(
        f'{ctx.deps.supabase_url}/rest/v1/testimonials',
        headers={
            'Authorization': f'Bearer {ctx.deps.supabase_api_key}',
            'Content-Type': 'application/json',
            'apikey': ctx.deps.supabase_api_key
        },
        json=testimonial_info
    )
    return "Testimonial erfolgreich erstellt." if response.status_code == 201 else f"Fehler beim Erstellen: {response.text}"

@cms_crm_agent.tool
async def list_testimonials(ctx: RunContext[Deps]) -> list:
    response = await ctx.deps.client.get(
        f'{ctx.deps.supabase_url}/rest/v1/testimonials?select=*',
        headers={'Authorization': f'Bearer {ctx.deps.supabase_api_key}', 'apikey': ctx.deps.supabase_api_key}
    )
    return response.json() if response.status_code == 200 else []

@cms_crm_agent.tool
async def update_testimonial(ctx: RunContext[Deps], id: str, update_data: dict) -> str:
    response = await ctx.deps.client.patch(
        f'{ctx.deps.supabase_url}/rest/v1/testimonials?id=eq.{id}',
        headers={
            'Authorization': f'Bearer {ctx.deps.supabase_api_key}',
            'Content-Type': 'application/json',
            'apikey': ctx.deps.supabase_api_key
        },
        json=update_data
    )
    return "Testimonial erfolgreich aktualisiert." if response.status_code == 204 else f"Fehler beim Aktualisieren: {response.text}"

@cms_crm_agent.tool
async def delete_testimonial(ctx: RunContext[Deps], id: str) -> str:
    response = await ctx.deps.client.delete(
        f'{ctx.deps.supabase_url}/rest/v1/testimonials?id=eq.{id}',
        headers={'Authorization': f'Bearer {ctx.deps.supabase_api_key}', 'apikey': ctx.deps.supabase_api_key}
    )
    return "Testimonial erfolgreich gelöscht." if response.status_code == 204 else f"Fehler beim Löschen: {response.text}"

# --- partners ---
@cms_crm_agent.tool
async def create_partner(ctx: RunContext[Deps], partner_info: dict) -> str:
    response = await ctx.deps.client.post(
        f'{ctx.deps.supabase_url}/rest/v1/partners',
        headers={
            'Authorization': f'Bearer {ctx.deps.supabase_api_key}',
            'Content-Type': 'application/json',
            'apikey': ctx.deps.supabase_api_key
        },
        json=partner_info
    )
    return "Partner erfolgreich erstellt." if response.status_code == 201 else f"Fehler beim Erstellen: {response.text}"

@cms_crm_agent.tool
async def list_partners(ctx: RunContext[Deps]) -> list:
    response = await ctx.deps.client.get(
        f'{ctx.deps.supabase_url}/rest/v1/partners?select=*',
        headers={'Authorization': f'Bearer {ctx.deps.supabase_api_key}', 'apikey': ctx.deps.supabase_api_key}
    )
    return response.json() if response.status_code == 200 else []

@cms_crm_agent.tool
async def update_partner(ctx: RunContext[Deps], id: str, update_data: dict) -> str:
    response = await ctx.deps.client.patch(
        f'{ctx.deps.supabase_url}/rest/v1/partners?id=eq.{id}',
        headers={
            'Authorization': f'Bearer {ctx.deps.supabase_api_key}',
            'Content-Type': 'application/json',
            'apikey': ctx.deps.supabase_api_key
        },
        json=update_data
    )
    return "Partner erfolgreich aktualisiert." if response.status_code == 204 else f"Fehler beim Aktualisieren: {response.text}"

@cms_crm_agent.tool
async def delete_partner(ctx: RunContext[Deps], id: str) -> str:
    response = await ctx.deps.client.delete(
        f'{ctx.deps.supabase_url}/rest/v1/partners?id=eq.{id}',
        headers={'Authorization': f'Bearer {ctx.deps.supabase_api_key}', 'apikey': ctx.deps.supabase_api_key}
    )
    return "Partner erfolgreich gelöscht." if response.status_code == 204 else f"Fehler beim Löschen: {response.text}"

# --- suppliers ---
@cms_crm_agent.tool
async def create_supplier(ctx: RunContext[Deps], supplier_info: dict) -> str:
    response = await ctx.deps.client.post(
        f'{ctx.deps.supabase_url}/rest/v1/suppliers',
        headers={
            'Authorization': f'Bearer {ctx.deps.supabase_api_key}',
            'Content-Type': 'application/json',
            'apikey': ctx.deps.supabase_api_key
        },
        json=supplier_info
    )
    return "Lieferant erfolgreich erstellt." if response.status_code == 201 else f"Fehler beim Erstellen: {response.text}"

@cms_crm_agent.tool
async def list_suppliers(ctx: RunContext[Deps]) -> list:
    response = await ctx.deps.client.get(
        f'{ctx.deps.supabase_url}/rest/v1/suppliers?select=*',
        headers={'Authorization': f'Bearer {ctx.deps.supabase_api_key}', 'apikey': ctx.deps.supabase_api_key}
    )
    return response.json() if response.status_code == 200 else []

@cms_crm_agent.tool
async def update_supplier(ctx: RunContext[Deps], id: str, update_data: dict) -> str:
    response = await ctx.deps.client.patch(
        f'{ctx.deps.supabase_url}/rest/v1/suppliers?id=eq.{id}',
        headers={
            'Authorization': f'Bearer {ctx.deps.supabase_api_key}',
            'Content-Type': 'application/json',
            'apikey': ctx.deps.supabase_api_key
        },
        json=update_data
    )
    return "Lieferant erfolgreich aktualisiert." if response.status_code == 204 else f"Fehler beim Aktualisieren: {response.text}"

@cms_crm_agent.tool
async def delete_supplier(ctx: RunContext[Deps], id: str) -> str:
    response = await ctx.deps.client.delete(
        f'{ctx.deps.supabase_url}/rest/v1/suppliers?id=eq.{id}',
        headers={'Authorization': f'Bearer {ctx.deps.supabase_api_key}', 'apikey': ctx.deps.supabase_api_key}
    )
    return "Lieferant erfolgreich gelöscht." if response.status_code == 204 else f"Fehler beim Löschen: {response.text}"

# --- images ---
@cms_crm_agent.tool
async def create_image(ctx: RunContext[Deps], image_info: dict) -> str:
    response = await ctx.deps.client.post(
        f'{ctx.deps.supabase_url}/rest/v1/images',
        headers={
            'Authorization': f'Bearer {ctx.deps.supabase_api_key}',
            'Content-Type': 'application/json',
            'apikey': ctx.deps.supabase_api_key
        },
        json=image_info
    )
    return "Bild erfolgreich erstellt." if response.status_code == 201 else f"Fehler beim Erstellen: {response.text}"

@cms_crm_agent.tool
async def list_images(ctx: RunContext[Deps]) -> list:
    response = await ctx.deps.client.get(
        f'{ctx.deps.supabase_url}/rest/v1/images?select=*',
        headers={'Authorization': f'Bearer {ctx.deps.supabase_api_key}', 'apikey': ctx.deps.supabase_api_key}
    )
    return response.json() if response.status_code == 200 else []

@cms_crm_agent.tool
async def update_image(ctx: RunContext[Deps], id: str, update_data: dict) -> str:
    response = await ctx.deps.client.patch(
        f'{ctx.deps.supabase_url}/rest/v1/images?id=eq.{id}',
        headers={
            'Authorization': f'Bearer {ctx.deps.supabase_api_key}',
            'Content-Type': 'application/json',
            'apikey': ctx.deps.supabase_api_key
        },
        json=update_data
    )
    return "Bild erfolgreich aktualisiert." if response.status_code == 204 else f"Fehler beim Aktualisieren: {response.text}"

@cms_crm_agent.tool
async def delete_image(ctx: RunContext[Deps], id: str) -> str:
    response = await ctx.deps.client.delete(
        f'{ctx.deps.supabase_url}/rest/v1/images?id=eq.{id}',
        headers={'Authorization': f'Bearer {ctx.deps.supabase_api_key}', 'apikey': ctx.deps.supabase_api_key}
    )
    return "Bild erfolgreich gelöscht." if response.status_code == 204 else f"Fehler beim Löschen: {response.text}" 