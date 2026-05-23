-- Обновите цены товаров для записей, где product_id ≤ 5 и цена меньше 10000, увеличить цену на 5%.
UPDATE prices
SET price = price * 1.05
WHERE product_id <= 5 AND price < 10000;