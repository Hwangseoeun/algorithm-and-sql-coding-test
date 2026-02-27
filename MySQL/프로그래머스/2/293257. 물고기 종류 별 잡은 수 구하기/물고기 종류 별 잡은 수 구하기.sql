-- 코드를 작성해주세요
select
    count(*) as "FISH_COUNT",
    (select FISH_NAME from FISH_NAME_INFO where FISH_TYPE = fi.FISH_TYPE) as "FISH_NAME"
from FISH_INFO fi
inner join FISH_NAME_INFO fni on fi.FISH_TYPE = fni.FISH_TYPE
group by fi.FISH_TYPE
order by count(*) desc