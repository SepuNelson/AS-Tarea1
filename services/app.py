from fastapi import FastAPI, HTTPException
import json
from pathlib import Path

app = FastAPI()

db_path = Path("/app/bbdd/players.json")

# Obtener todos los jugadores
@app.get("/players")
def get_players():
    with open(db_path, "r") as f:
        data = json.load(f)

    players = [item["player"] for item in data]
    return {"players": players}

# Obtener el equipo de un jugador
@app.get("/players/{name}/team")
def get_player_team(name: str):
    with open(db_path, "r") as f:
        data = json.load(f)
    
    for item in data:
        if item["player"].lower() == name.lower():
            return {"team": item["team"]}
    
    raise HTTPException(status_code=404, detail="Player not found")

# Obtener el rol de un jugador
@app.get("/players/{name}/rol")
def get_player_role(name: str):
    with open(db_path, "r") as f:
        data = json.load(f)
    
    for item in data:
        if item["player"].lower() == name.lower():
            return {"rol": item["rol"]}
    
    raise HTTPException(status_code=404, detail="Player not found")

# Obtener el agente principal de un jugador
@app.get("/players/{name}/main_agent")
def get_player_main_agent(name: str):
    with open(db_path, "r") as f:
        data = json.load(f)
    
    for item in data:
        if item["player"].lower() == name.lower():
            return {"main_agent": item["main_agent"]}
    
    raise HTTPException(status_code=404, detail="Player not found")
