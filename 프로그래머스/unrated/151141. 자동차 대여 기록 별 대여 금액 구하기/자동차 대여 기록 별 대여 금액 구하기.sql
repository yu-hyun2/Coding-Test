SELECT
    HISTORY_ID,
    ROUND(RENTAL_PERIOD * DISCOUNT_FEE, 0) AS FEE
FROM(
    
    SELECT
        HISTORY_ID,
        RENTAL_PERIOD,
        DAILY_FEE - (DAILY_FEE * (DC_RATE / 100)) AS DISCOUNT_FEE
    FROM (

        SELECT
            HISTORY_ID,
            DAILY_FEE,
            RENTAL_PERIOD,
            CASE
                WHEN RENTAL_PERIOD >= 90 THEN (SELECT DISCOUNT_RATE
                                              FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
                                              WHERE CAR_TYPE = '트럭'
                                              AND DURATION_TYPE = '90일 이상')
                WHEN RENTAL_PERIOD >= 30 THEN (SELECT DISCOUNT_RATE
                                              FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
                                              WHERE CAR_TYPE = '트럭'
                                              AND DURATION_TYPE = '30일 이상')
                WHEN RENTAL_PERIOD >= 7 THEN (SELECT DISCOUNT_RATE
                                              FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
                                              WHERE CAR_TYPE = '트럭'
                                              AND DURATION_TYPE = '7일 이상')     
                ELSE 0.00
            END AS DC_RATE

        FROM (
            SELECT C.CAR_ID, C.DAILY_FEE, H.HISTORY_ID, H.END_DATE - H.START_DATE + 1 RENTAL_PERIOD
            FROM CAR_RENTAL_COMPANY_CAR C, CAR_RENTAL_COMPANY_RENTAL_HISTORY H
            WHERE C.CAR_ID = H.CAR_ID
                AND C.CAR_TYPE='트럭'
            )
    )
)
ORDER BY 
    FEE DESC, HISTORY_ID DESC;