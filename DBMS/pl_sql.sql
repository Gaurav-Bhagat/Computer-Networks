--1
VARIABLE c VARCHAR2(5);  -- Declare a bind variable

-- EXEC :c := 'E002';  -- Assign input (Use single quotes for VARCHAR2)

DECLARE
    e_name EMP.EMP_NAME%TYPE;
    e_code EMP.EMP_CODE%TYPE := :c;  -- Use bind variable
BEGIN
    SELECT EMP_NAME INTO e_name 
    FROM EMP  
    WHERE EMP_CODE = e_code;

    DBMS_OUTPUT.PUT_LINE('EMP_NAME: ' || e_name);
EXCEPTION
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('No employee found with the given code.');
END;


-- syntax for GOTO

-- GOTO label;
-- *****
-- *****
-- <<label>>
-- statement


-- LOOP
--    -- Code block
--    IF condition THEN
--       EXIT;   ----> break;
--    END IF;
-- END LOOP;


-- LOOP
--     -- Code block
--     EXIT WHEN condition;  ---> exit can contains cond. on which you wnat to exit the loop
-- END LOOP;


-- DECLARE
--      counter NUMBER;
-- BEGIN
--      DBMS_OUTPUT.PUT_LINE('PL/SQL FOR LOOP EXECUTION');
--      FOR counter IN 1..5 LOOP                                -->for loop 
--          DBMS_OUTPUT.PUT_LINE('COUNTER VALUE: '|| counter);
--      END LOOP;
-- END;


-- DECLARE
--      counter NUMBER;
-- BEGIN
--      DBMS_OUTPUT.PUT_LINE('PL/SQL FOR LOOP EXECUTION');
--      FOR counter IN REVERSE 1..5 LOOP                                -->for loop (5 4 3 2 1 )
--          DBMS_OUTPUT.PUT_LINE('COUNTER VALUE: '|| counter);
--      END LOOP;
-- END;


--2

create table TempEmp(
    E_CODE VARCHAR2(3) PRIMARY KEY,
    E_NAME VARCHAR2(30),
    BASIC NUMBER
);

VARIABLE a VARCHAR2(3);
VARIABLE b VARCHAR2(30);
VARIABLE c NUMBER;

-- EXEC :a := 'E01';   -- Ensure `E_CODE` is assigned
-- EXEC :b := 'Alice';
-- EXEC :c := 50000;

DECLARE 
    e_code TempEmp.E_CODE%TYPE := :a; 
    e_name TempEmp.E_NAME%TYPE := :b;
    e_basic TempEmp.BASIC%TYPE := :c;
BEGIN
    INSERT INTO TempEmp (E_CODE, E_NAME, BASIC) VALUES (e_code, e_name, e_basic);
    
    COMMIT;  
    DBMS_OUTPUT.PUT_LINE('Row inserted.');
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
        DBMS_OUTPUT.PUT_LINE('Error: Employee already exists!');
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error: ' || SQLERRM);
END;
/

SELECT * FROM TEMPEMP;


--3
DECLARE
    CURSOR EMP_CURSOR IS
        SELECT EMP_NAME, BASIC FROM EMP ORDER BY BASIC DESC;
    T_NAME EMP.EMP_NAME%TYPE;
    T_BASIC EMP.BASIC%TYPE;
BEGIN
    OPEN EMP_CURSOR;

    FOR COUNTER IN 1..5 LOOP
        FETCH EMP_CURSOR INTO T_NAME ,T_BASIC;
        DBMS_OUTPUT.PUT_LINE('EMPLOYEE NAME: ' || T_NAME || ' EMPLOYEE BASIC: ' || T_BASIC);
    END LOOP;
    CLOSE EMP_CURSOR;
END;

-- 4) Accept a department code from the user. Delete all the employee rows with that department
-- code. Show how many rows have been deleted.

-- SELECT * FROM EMP;
-- SELECT * FROM DEPT2;

ALTER TABLE EMP ADD is_deleted CHAR(1) DEFAULT 'N'; 

VARIABLE D NUMBER(3);
DECLARE
    DC DEPT2.DEPTCODE%TYPE := :D;
    CURSOR D_CURSOR IS
        SELECT EMP_CODE FROM EMP WHERE DEPT_CODE = DC;
    EC EMP.EMP_CODE%TYPE;
BEGIN
    OPEN D_CURSOR;

    LOOP
        FETCH D_CURSOR INTO EC;
        EXIT WHEN D_CURSOR%NOTFOUND; 

        -- DELETE FROM EMP WHERE EMP_CODE = EC;                  --PARMANENT DELETE
        UPDATE EMP SET is_deleted = 'Y' WHERE EMP_CODE = EC;     --SHALLOW DELETE
        DBMS_OUTPUT.PUT_LINE('E_CODE: ' || EC || ' IS DELETED');
    END LOOP;

    DBMS_OUTPUT.PUT_LINE('TOTAL ROWS: ' || D_CURSOR%ROWCOUNT);
    CLOSE D_CURSOR;
END;
/

SELECT * FROM EMP;

UPDATE EMP SET is_deleted = 'N' WHERE DEPT_CODE = 101; -- Restore employee 


--5
    
