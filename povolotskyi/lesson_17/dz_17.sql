USE pds;
SELECT count(distinct(JOB_ID)) FROM employees;

USE pds;
SELECT avg(SALARY) AS AVERAGE_SALARY_DEP90, count(FIRST_NAME) FROM employees where DEPARTMENT_ID = 90;

use pds;
select count(first_name), JOB_ID as Total from employees group by JOB_ID

USE pds;
SELECT FIRST_NAME, LAST_NAME, DEPARTMENT_ID FROM employees;

use pds;
select e.first_name, e.LAST_NAME, e.JOB_ID, e.DEPARTMENT_ID, d.DEPARTMENT_NAME from
employees e join departments d on (e.DEPARTMENT_ID = d.DEPARTMENT_ID) join locations l on
(d.LOCATION_ID = l.LOCATION_ID) where l.CITY = "London"