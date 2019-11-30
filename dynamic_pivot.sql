select *
from   table( pivot(' select deptno
                      ,      job
                      ,      avg(sal) sal_avg
                      from   emp
                      group
                      by     deptno
                      ,      job
                    ')
            )
