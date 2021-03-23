SELECT N, ( case when P is null then 'Root' when N not in (select distinct P from BST where P is not null) then 'Leaf' else 'Inner' end ) as nodeType 
FROM BST 
ORDER BY N;
