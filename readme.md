## Streaming crypto trades data

Got a python script that consumes trades data from binance and produces messages to azure eventhubs.

Databricks notebook consumes eventhubs with pyspark and writes delta tables.

To be done:
 - Transformations
 - Aggregations
 - Visualization in PowerBI

### Stream 
!["Strea,"](/docs/stream.png)

Useful links: 
- [https://github.com/malvik01/Real-Time-Streaming-with-Azure-Databricks](https://github.com/malvik01/Real-Time-Streaming-with-Azure-Databricks)
- [https://www.youtube.com/watch?v=pwWIegHgNRw](https://www.youtube.com/watch?v=pwWIegHgNRw)
- [https://github.com/binance/binance-spot-api-docs/blob/master/web-socket-streams.md](https://github.com/binance/binance-spot-api-docs/blob/master/web-socket-streams.md)