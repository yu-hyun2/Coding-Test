# # 1. 요거트와 우유를 구매한 ID 정보
# SELECT *
# FROM CART_PRODUCTS A
# WHERE NAME IN ('Milk','Yogurt')
# ORDER BY NAME


SELECT A.CART_ID
FROM CART_PRODUCTS A JOIN CART_PRODUCTS B ON A.CART_ID = B.CART_ID 
WHERE A.NAME='Yogurt' AND B.NAME='Milk'
GROUP BY A.CART_ID