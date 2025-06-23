from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from gsheet import append_to_sheet

# Enable docs for testing
app = FastAPI(docs_url="/docs", redoc_url="/redoc")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://ayuvanaa.com", "http://localhost:3000", "*"],  # "*" is for testing, remove later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/submit-registration")
async def submit_registration(
    name: str = Form(...),
    age: int = Form(...),
    gender: str = Form(...),
    phone: str = Form(...),
    language: str = Form(...),
    wake_time: str = Form(None),
    sleep_time: str = Form(None),
    exercise_time: str = Form(None),
    breakfast_time: str = Form(None),
    lunch_time: str = Form(None),
    dinner_time: str = Form(None),
    medicine_times: str = Form(None),
    medicine_reason: str = Form(None),
    health_condition: str = Form(None),
    others: str = Form(None),
    consent: bool = Form(...)
):
    try:
        row = [
            name, age, gender, phone, language, wake_time, sleep_time,
            exercise_time, breakfast_time, lunch_time, dinner_time,
            medicine_times, medicine_reason, health_condition, others, consent
        ]
        append_to_sheet(row)
        return {"status": "success", "message": "Registration submitted successfully."}
    except Exception as e:
        return {"status": "error", "message": str(e)}
