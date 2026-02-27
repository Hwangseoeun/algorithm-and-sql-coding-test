-- 코드를 작성해주세요
select fi.ID, FISH_NAME_INFO.FISH_NAME, fi.LENGTH from FISH_INFO fi
inner join FISH_NAME_INFO on fi.FISH_TYPE = FISH_NAME_INFO.FISH_TYPE
where fi.LENGTH = (select max(fi2.LENGTH) from FISH_INFO fi2 where fi.FISH_TYPE = fi2.FISH_TYPE)
order by fi.ID asc;