SELECT Prices.product_id, COALESCE(ROUND(SUM(UnitsSold.units * Prices.price * 1.0) / SUM(UnitsSold.units), 2), 0) AS average_price
FROM UnitsSold
RIGHT JOIN Prices
ON Prices.start_date <= UnitsSold.purchase_date 
AND UnitsSold.purchase_date < Prices.end_date 
AND UnitsSold.product_id = Prices.product_id
GROUP BY Prices.product_id