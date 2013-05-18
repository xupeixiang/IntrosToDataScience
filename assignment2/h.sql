/*
 * The query is still running after a dinner, so I give up
 * and write h_specific.sql for the specific query
 */

select sim_value
from (
     select A.docid as docid_a ,B.docid as docid_b,
     sum(A.count * B.count) as sim_value
     from frequency as A join frequency as B on A.term = B.term
     group by docid_a,docid_b
     having docid_a < docid_b 
     )
where docid_a = '10080_txt_crude' and docid_b = '17035_txt_earn';
