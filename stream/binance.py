import asyncio
import websockets
import json
from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub import EventData
import time

# {
#   "e": "trade",       // Event type
#   "E": 1672515782136, // Event time
#   "s": "BNBBTC",      // Symbol
#   "t": 12345,         // Trade ID
#   "p": "0.001",       // Price
#   "q": "100",         // Quantity
#   "b": 88,            // Buyer order ID
#   "a": 50,            // Seller order ID
#   "T": 1672515782136, // Trade time
#   "m": true,          // Is the buyer the market maker?
#   "M": true           // Ignore
# }

column_names = [
    "event_type",
    "event_time",
    "symbol",
    "trade_id",
    "price",
    "quantity",
    "buyer_order_id",
    "seller_order_id",
    "trade_time",
    "is_market_maker",
    "ignore_field"
]

async def subscribe_to_trade(symbol, producer_client):
    uri = f"wss://stream.binance.com:9443/ws/{symbol.lower()}@trade"
    async with websockets.connect(uri) as websocket:
        while True:
            message = await websocket.recv()
            dict_message = json.loads(message)
            # will send all values as string, cant figure out the schema in pyspark
            data = {column_names[i]: str(dict_message[key]) for i, key in enumerate(dict_message)}
            print(data)

            event_data = EventData(body=str(data))
            await producer_client.send(event_data, partition_key=data['symbol'])
            time.sleep(2)
            

async def main():
    symbols = ["BNBBTC", "ETHBTC"]
     
    connection_str = ""
    producer = EventHubProducerClient.from_connection_string(conn_str=connection_str)

    producer_client = producer._create_producer()

    try:
        tasks = [subscribe_to_trade(symbol, producer_client) for symbol in symbols]
        await asyncio.gather(*tasks)
    finally:
        await producer.close()
asyncio.run(main())

