select count(*)
from (
      select sum(count) as total 
      from frequency
      group by docid having total > 300
    ) as x;
