#최소 3번 구매한 고객, 30일 넘게 즉 min과 max diff가 30 이상이고, refund rate가 20%보다 적은 고객
#refund rate는 환불 횟수/구매 횟수

SELECT customer_id
FROM customer_transactions
GROUP BY customer_id
HAVING SUM(transaction_type = 'purchase') >= 3
AND DATEDIFF(MAX(transaction_date), MIN(transaction_date)) >= 30
AND SUM(transaction_type = 'refund')/COUNT(*) < 0.2
ORDER BY customer_id