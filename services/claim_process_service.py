from db import db
from models import claim_processes, claim_process_items
from schema import ClaimProcessRequest, ClaimProcessItem


class ClaimProcessService:
    @classmethod
    async def create(cls, claim_process_request: ClaimProcessRequest):
        query = claim_processes.insert().values()
        claim_process_id = await db.execute(query)

        for claim_process_request_item in claim_process_request.items:
            query = claim_process_items.insert().values(claim_process_id=claim_process_id,
                                                        **dict(claim_process_request_item))
            await db.execute(query)

        return claim_process_id

    @classmethod
    async def calculate_net_fee(cls, claim_process_id: int):
        query = claim_process_items.select().where(claim_process_items.c.claim_process_id == claim_process_id)
        items = await db.fetch_all(query)

        total_net_fee = 0
        for item in items:
            item = ClaimProcessItem(**item)
            net_fee = item.provider_fee + item.member_coinsurance + item.member_copay - item.allowed_fee
            total_net_fee += net_fee

        query = claim_processes.update().where(claim_processes.c.id == claim_process_id).values(net_fee=total_net_fee)
        await db.execute(query)
