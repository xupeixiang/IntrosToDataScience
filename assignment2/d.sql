select count(*)
from (
      select * 
      from frequency
      where term = 'parliament'
    ) as x;
