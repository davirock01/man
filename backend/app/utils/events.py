import json
import asyncio
from typing import Any, Dict
import redis.asyncio as aioredis
from app.core.config import settings


class EventBus:
    """Simple event bus using Redis Streams for async event handling."""
    
    def __init__(self):
        self.redis = None
    
    async def connect(self):
        """Connect to Redis."""
        self.redis = await aioredis.from_url(settings.REDIS_URL, decode_responses=True)
    
    async def disconnect(self):
        """Disconnect from Redis."""
        if self.redis:
            await self.redis.close()
    
    async def publish(self, event_type: str, data: Dict[str, Any]):
        """Publish an event to a stream."""
        if not self.redis:
            await self.connect()
        
        await self.redis.xadd(
            f"events:{event_type}",
            {"data": json.dumps(data)},
            maxlen=10000,  # Keep last 10k events
        )
    
    async def subscribe(self, event_type: str, consumer_group: str, consumer_name: str):
        """Subscribe to an event stream."""
        if not self.redis:
            await self.connect()
        
        stream_name = f"events:{event_type}"
        
        # Create consumer group if it doesn't exist
        try:
            await self.redis.xgroup_create(stream_name, consumer_group, id="0", mkstream=True)
        except aioredis.ResponseError:
            # Group already exists
            pass
        
        # Read from stream
        while True:
            try:
                events = await self.redis.xreadgroup(
                    consumer_group,
                    consumer_name,
                    {stream_name: ">"},
                    count=10,
                    block=5000,
                )
                
                for stream, messages in events:
                    for message_id, message_data in messages:
                        data = json.loads(message_data["data"])
                        yield message_id, data
                        
                        # Acknowledge message
                        await self.redis.xack(stream_name, consumer_group, message_id)
            except Exception as e:
                print(f"Error reading from stream: {e}")
                await asyncio.sleep(5)


# Global event bus instance
event_bus = EventBus()

