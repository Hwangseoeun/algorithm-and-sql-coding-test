select child.ITEM_ID, child.ITEM_NAME, child.RARITY from ITEM_TREE it
join ITEM_INFO parent on parent.ITEM_ID = it.PARENT_ITEM_ID
join ITEM_INFO child on child.ITEM_ID = it.ITEM_ID
where parent.RARITY like "RARE"
order by child.ITEM_ID desc;
