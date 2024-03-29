SELECT A.APNT_NO, 
        P.PT_NAME, 
        P.PT_NO, 
        A.MCDP_CD,
        D.DR_NAME,
        A.APNT_YMD
FROM PATIENT P JOIN APPOINTMENT A ON P.PT_NO = A.PT_NO JOIN DOCTOR D ON A.MDDR_ID = D.DR_ID
WHERE A.MCDP_CD = 'CS' 
    AND A.APNT_YMD LIKE '2022-04-13%' 
    AND A.APNT_CNCL_YN = 'N'
ORDER BY A.APNT_YMD


# SELECT APNT_NO, PT_NAME, PT_NO, C.MCDP_CD, DR_NAME, APNT_YMD
# FROM DOCTOR D, (SELECT A.APNT_NO, 
#                     P.PT_NAME, 
#                     P.PT_NO, 
#                     A.MCDP_CD,
#                     A.MDDR_ID,
#                     A.APNT_YMD
#                 FROM PATIENT P JOIN APPOINTMENT A ON P.PT_NO = A.PT_NO
#                 WHERE A.MCDP_CD = 'CS' 
#                     AND A.APNT_YMD LIKE '2022-04-13%' 
#                     AND A.APNT_CNCL_YN = 'N') C
# WHERE D.DR_ID = C.MDDR_ID
# ORDER BY A.APNT_YMD


# 오답 코드 
# SELECT A.APNT_NO, 
#         P.PT_NAME, 
#         P.PT_NO, 
#         A.MCDP_CD, (
#         SELECT DR_NAME 
#         FROM DOCTOR D 
#         WHERE D.DR_ID = A.MDDR_ID) AS DR_NAME, 
#         A.APNT_YMD
# FROM PATIENT P JOIN APPOINTMENT A ON P.PT_NO = A.PT_NO
# WHERE A.MCDP_CD = 'CS' AND A.APNT_YMD LIKE '2022-04-13%'
# ORDER BY A.APNT_YMD