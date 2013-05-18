select value
from (
     select A.row_num as row_num ,B.col_num as col_num,
     sum(A.value * B.value) as value
     from A join B on A.col_num = B.row_num
     group by row_num,col_num
     )
where row_num = 2 and col_num = 3;
