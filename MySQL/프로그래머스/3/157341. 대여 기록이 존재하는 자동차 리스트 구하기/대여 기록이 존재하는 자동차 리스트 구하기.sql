-- 코드를 입력하세요
SELECT distinct cr.CAR_ID
from CAR_RENTAL_COMPANY_CAR cr
inner join CAR_RENTAL_COMPANY_RENTAL_HISTORY crh on cr.CAR_ID = crh.CAR_ID
where cr.CAR_TYPE like "세단" and month(crh.START_DATE) = 10
order by cr.CAR_ID desc;