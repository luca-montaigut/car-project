from fastapi import FastAPI, HTTPException
from app.models import CarRequest
from app.openai_service import generate_image

app = FastAPI()


@app.post("/generate-car-image")
async def generate_car_image(car_request: CarRequest):
    model = car_request.model
    color = car_request.color

    if not model or not color:
        raise HTTPException(status_code=400, detail="Model and color are required")

    try:
        image_url = generate_image(model, color)
        return {"image_url": image_url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
