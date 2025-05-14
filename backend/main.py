import os
from dotenv import load_dotenv
load_dotenv()  # <-- Muss GANZ OBEN stehen, vor allen anderen Imports!

print("DEBUG: OPENAI_API_KEY =", os.environ.get("OPENAI_API_KEY"))
from fastapi import FastAPI, Request
from agent import cms_crm_agent, Deps
import httpx
import os
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

@app.post("/api/agent")
async def agent_endpoint(request: Request):
    data = await request.json()
    user_message = data.get("message")
    async with httpx.AsyncClient() as client:
        deps = Deps(
            client=client,
            supabase_api_key=os.environ["SUPABASE_API_KEY"],
            supabase_url=os.environ["SUPABASE_URL"]
        )
        reply = await cms_crm_agent.run(user_message, deps=deps)
    return {"reply": reply} 