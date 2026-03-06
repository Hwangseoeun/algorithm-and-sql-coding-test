-- 코드를 입력하세요
select distinct first_value(NAME) over(order by DATETIME) as "NAME"
from ANIMAL_INS;