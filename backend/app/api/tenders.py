from fastapi import APIRouter

router = APIRouter()

# Temporary MVP data
TENDERS = [
    {
        "id": 1,
        "title": "Supply of Electrical Cables",
        "department": "Power Ministry"
    },
    {
        "id": 2,
        "title": "IT Hardware Procurement",
        "department": "NIC"
    },
    {
        "id": 3,
        "title": "Security Services Contract",
        "department": "Indian Railways"
    }
]

@router.get("/")
def list_tenders():
    return TENDERS

@router.get("/{tender_id}")
def get_tender(tender_id: int):
    for tender in TENDERS:
        if tender["id"] == tender_id:
            return tender
    return {"error": "Tender not found"}
