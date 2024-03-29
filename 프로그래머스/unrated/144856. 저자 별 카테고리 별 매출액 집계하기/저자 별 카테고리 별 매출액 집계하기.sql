SELECT 
    AU.AUTHOR_ID, 
    AU.AUTHOR_NAME, 
    ID.CATEGORY, 
    ID.TOTAL_SALES
FROM
    (SELECT 
        A.AUTHOR_ID, 
        A.AUTHOR_NAME
    FROM 
        AUTHOR A JOIN BOOK B ON A.AUTHOR_ID = B.AUTHOR_ID
    GROUP BY 
        AUTHOR_ID
    ) AU JOIN

    (SELECT 
        B.AUTHOR_ID, 
        B.CATEGORY, 
        SUM(BS.SALES * B.PRICE) AS TOTAL_SALES
    FROM 
        BOOK B JOIN BOOK_SALES BS ON B.BOOK_ID = BS.BOOK_ID
    WHERE 
        BS.SALES_DATE LIKE '2022-01%'
    GROUP BY 
        AUTHOR_ID, 
        CATEGORY
    ) ID ON AU.AUTHOR_ID = ID.AUTHOR_ID
ORDER BY 
    ID.AUTHOR_ID, 
    ID.CATEGORY DESC