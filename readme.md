## Streaming crypto trades data

Got a python script that consumes trades data from binance and produces messages to azure eventhubs.

Databricks notebook processes eventhubs with pyspark and writes delta tables.

Power BI using partner connect to Databricks streams and visualize data

### Streaming system
!["Stream"](/docs/stream.png)

## Silver layer table
!["Silver Layer Table"](/docs/silver-layer.png)
The gold layer of this stream system holds separate table for each symbol

## PowerBI  databricks streaming visualizations
!["Power BI Of Silver Layer Table"](/docs/powerbi.png)

Useful links: 
- [https://github.com/malvik01/Real-Time-Streaming-with-Azure-Databricks](https://github.com/malvik01/Real-Time-Streaming-with-Azure-Databricks)
- [https://www.youtube.com/watch?v=pwWIegHgNRw](https://www.youtube.com/watch?v=pwWIegHgNRw)
- [https://github.com/binance/binance-spot-api-docs/blob/master/web-socket-streams.md](https://github.com/binance/binance-spot-api-docs/blob/master/web-socket-streams.md)