from fastapi import FastAPI
from routes import router
from fastapi.middleware.cors import CORSMiddleware   # ✅ IMPORT HERE

app = FastAPI(title="AI First CRM - HCP Module")


# ✅ ADD CORS RIGHT AFTER app creation
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# include routes AFTER middleware
app.include_router(router)


@app.get("/")
def home():
    return {"status": "AI CRM Backend Running"}
