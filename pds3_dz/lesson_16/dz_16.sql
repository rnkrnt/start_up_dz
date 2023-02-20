USE pds;
SELECT * FROM employees order by FIRST_NAME asc;

USE pds;
SELECT FIRST_NAME, LAST_NAME, SALARY, SALARY*0.15 AS TAX FROM employees;

USE pds;
SELECT sum(SALARY) FROM employees;

USE pds;
SELECT max(SALARY) as MAX_SALARY, min(SALARY) as MAX_SALARY FROM employees;

USE pds;
SELECT avg(SALARY) as AVERAGE_SALARY, count(FIRST_NAME) as WORKERS FROM employees;