from db import db
from schema import ClaimProcess
from models import claim_processes


class PaymentService:
    @classmethod
    async def process_payment(cls, claim_process_id: int):
        query = claim_processes.select().where(claim_processes.c.id == claim_process_id)
        claim_process = await db.fetch_one(query)
        claim_process = ClaimProcess(**claim_process)

        print(claim_process)
        # process payment handler here
