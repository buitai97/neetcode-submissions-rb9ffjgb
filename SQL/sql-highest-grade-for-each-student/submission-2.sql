-- Write your query below

select distinct on(student_id)
    *
from exam_results
order by student_id, score DESC, exam_id