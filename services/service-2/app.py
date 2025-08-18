from fastapi import FastAPI, HTTPException
import json
from pathlib import Path

app = FastAPI()

db_path = Path("/app/bbdd/agents.json")

# Obtener todos los agentes
@app.get("/agent")
def get_agents():
    with open(db_path, "r") as f:
        data = json.load(f)

    agents = [item["name"] for item in data]
    return {"agents": agents}

# Obtener el rol de un agente
@app.get("/agent/{name}/role")
def get_agent_role(name: str):
    with open(db_path, "r") as f:
        data = json.load(f)
    
    for item in data:
        if item["name"].lower() == name.lower():
            return {"role": item["role"]}

    raise HTTPException(status_code=404, detail="Agent not found")

# Obtener el pick rate de un agente
@app.get("/agent/{name}/pick_rate")
def get_agent_pick_rate(name: str):
    with open(db_path, "r") as f:
        data = json.load(f)
    
    for item in data:
        if item["name"].lower() == name.lower():
            return {"pick_rate": item["pick_rate"]}

    raise HTTPException(status_code=404, detail="Agent not found")
