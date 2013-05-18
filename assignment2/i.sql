select max(sim_value)
from (
     select A.docid as docid_a ,B.docid as docid_b,
     sum(A.count * B.count) as sim_value
     from
     (
     select * from frequency
     union
     select 'q' as docid, 'washington' as term, 1 as count 
     union
     select 'q' as docid, 'taxes' as term, 1 as count
     union 
     select 'q' as docid, 'treasury' as term, 1 as count
     ) as A join 
     (
     select 'q' as docid, 'washington' as term, 1 as count 
     union
     select 'q' as docid, 'taxes' as term, 1 as count
     union 
     select 'q' as docid, 'treasury' as term, 1 as count
     ) as B on A.term = B.term
     group by docid_a,docid_b
     );
