from fastapi import APIRouter
from schemas import InteractionCreate, EditInteraction
from agent import run_agent
from tools import edit_interaction

router = APIRouter()


# ✅ LOG INTERACTION
@router.post("/log-interaction")
def log_interaction(data: InteractionCreate):

    result = run_agent(data.note)

    return {
        "message": "Interaction logged successfully",
        "ai_extracted": result
    }


# ✅ EDIT INTERACTION
@router.put("/edit-interaction")
def edit_interaction_route(data: EditInteraction):

    result = edit_interaction(
        data.interaction_id,
        data.updates
    )

    return {
        "message": "Interaction updated successfully",
        "updated_record": result
    }
