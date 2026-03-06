#모든 SELL 전에는 BUY가 있음. 모든 BUY 후에는 SELL가 있음
#partition by stock_name으로 operation_day를 기준으로 rank를 매기고, join해서 뺀 후 더하기?

WITH cte AS (SELECT *, ROW_NUMBER() OVER (PARTITION BY stock_name ORDER BY operation_day) AS rnk
FROM Stocks)

SELECT stock_name, SUM(CASE WHEN operation = 'Sell' THEN price ELSE -price END) AS capital_gain_loss
FROM cte
GROUP BY stock_name
