
SELECT items.name, sellers.name
FROM items
LEFT JOIN sellers
ON items.sellerId = sellers.id
WHERE sellers.rating > 4;
