from db import db
from typing import Dict, Any
from schema import Queue
from models import queues
from services.payment_service import PaymentService


class QueueService:
    @classmethod
    async def enqueue(cls, queue_type: str, payload: Dict[str, Any]):
        query = queues.insert().values(type=queue_type, locked=False, payload=payload)
        return await db.execute(query)

    @classmethod
    async def lock_queue(cls, queue_id: int):
        query = queues.update().where(queues.c.id == queue_id).values(locked=True)
        await db.execute(query)


    @classmethod
    async def lock_queue(cls, queue_id: int):
        query = queues.update().where(queues.c.id == queue_id).values(locked=True)
        await db.execute(query)


    @classmethod
    async def delete_queue(cls, queue_id: int):
        query = queues.delete().where(queues.c.id == queue_id)
        await db.execute(query)

    @classmethod
    async def process_queue(cls):
        query = queues.select().where(queues.c.locked == False)
        queue_items = await db.fetch_all(query)

        for item in queue_items:
            queue_item = Queue(**item)

            if queue_item.type == 'payment_service':
                await cls.lock_queue(item.id)
                await PaymentService.process_payment(queue_item.payload['claim_process_id'])
                await cls.delete_queue(item.id)
