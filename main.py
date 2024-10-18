import uvicorn
from services.claim_process_service import ClaimProcessService
from services.queue_service import QueueService
from app import app
from schema import ClaimProcessRequest


@app.post("/claim_process/")
async def create_claim_process(claim_process_request: ClaimProcessRequest):
    # This will add claim process request into db
    claim_process_id = await ClaimProcessService.create(claim_process_request)

    # This will calculate the net fee
    await ClaimProcessService.calculate_net_fee(claim_process_id)

    # This will add the payment_service process into queue
    await QueueService.enqueue(queue_type='payment_service', payload={'claim_process_id': claim_process_id})

    return {"claim_process": claim_process_id}


# This is the handler that will be called periodically to run the queue
@app.post("/queue/")
async def process_queue():
    await QueueService.process_queue()
    return {"success": True}


@app.get("/")
async def status_check():
    return {"status": "OK"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
