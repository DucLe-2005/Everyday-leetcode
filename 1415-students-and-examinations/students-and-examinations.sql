# Write your MySQL query statement below
-- select s.student_id, student_name, subject_name, count(subject_name) as attended_exams
-- from students s
-- left join examinations e on e.student_id = s.student_id
-- group by s.student_id, e.subject_name
-- order by s.student_id ASC;

select st.student_id, st.student_name, sb.subject_name, count(ex.subject_name) as attended_exams
from students st
cross join subjects sb
left join examinations ex on ex.student_id = st.student_id and sb.subject_name = ex.subject_name
group by st.student_id, sb.subject_name
order by st.student_id, sb.subject_name;