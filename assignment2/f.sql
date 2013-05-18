select count(*)
from ((
      select docid  
      from frequency
      where term = 'transactions'
      )natural join
      (
      select docid  
      from frequency
      where term = 'world'
      )) as x;
