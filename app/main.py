from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from mangum import Mangum
from app.model import OptimizeRequest, OptimizeResponse, SlotResult
from app.compute import compute_optimal_slots

'''
FastAPI application for the meeting slots optimizer.
'''

app = FastAPI(title = "Optimal meeting slot scheduler")

@app.get("/health", response_class=JSONResponse)
def health_check():
    return {"status": "ok"}

@app.post("/api/v1/meetings/optimize", response_model=OptimizeResponse)
def optimize(req: OptimizeRequest):
    max_count, winners = compute_optimal_slots(req.meetingName, [p.dict() for p in req.participants])
    if max_count <= 0 or not winners:
        raise HTTPException(status_code=400, detail="No matching time slots")

    response = OptimizeResponse(
        meetingName=req.meetingName,
        optimalSlots=[SlotResult(**w) for w in winners],
        maxParticipants=max_count
    )
    return response

handler = Mangum(app)