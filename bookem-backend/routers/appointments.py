from fastapi import APIRouter
from models.appointments import AppointmentIn


router = APIRouter()

@router.post("/appointments")
def create_appointment(appointment: AppointmentIn):
    print("appointment", appointment)
    return appointment
