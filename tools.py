import json
from datetime import datetime
from groq import Groq
from config import GROQ_API_KEY
from database import interaction_collection
from bson import ObjectId


client = Groq(api_key=GROQ_API_KEY)


# ✅ LOG INTERACTION TOOL
def extract_and_store_interaction(note: str):

    prompt = f"""
You are an AI assistant for a pharma CRM.

Extract structured data from the interaction note.

Return ONLY valid JSON.
Do NOT add explanations.

Format:

{{
"doctor_name": "",
"summary": "",
"sentiment": "Positive | Neutral | Negative",
"follow_up_action": ""
}}

Interaction note:
{note}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    content = response.choices[0].message.content

    print("LLM RESPONSE:", content)

    # ✅ Safe JSON extraction
    start = content.find("{")
    end = content.rfind("}") + 1
    json_string = content[start:end]

    data = json.loads(json_string)

    result = interaction_collection.insert_one({
        "doctor_name": data.get("doctor_name"),
        "summary": data.get("summary"),
        "sentiment": data.get("sentiment"),
        "follow_up": data.get("follow_up_action"),
        "raw_note": note,
        "created_at": datetime.utcnow()
    })

    data["id"] = str(result.inserted_id)

    return data


# ✅ EDIT INTERACTION TOOL
def edit_interaction(interaction_id: str, updates: dict):

    result = interaction_collection.update_one(
        {"_id": ObjectId(interaction_id)},
        {"$set": updates}
    )

    if result.modified_count == 0:
        return {"message": "No interaction updated"}

    updated_doc = interaction_collection.find_one(
        {"_id": ObjectId(interaction_id)}
    )

    updated_doc["_id"] = str(updated_doc["_id"])

    return updated_doc
