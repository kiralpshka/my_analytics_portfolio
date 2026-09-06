 Топ-3 ученика по платежам
SELECT s.name, SUM(p.amount) as total_paid
FROM students s
JOIN payments p ON s.id = p.student_id
GROUP BY s.name
ORDER BY total_paid DESC
LIMIT 3;

 Выручка по курсам
SELECT s.course, SUM(p.amount) as total_revenue
FROM students s
JOIN payments p ON s.id = p.student_id
GROUP BY s.course;

 Количество учеников на курсах
SELECT course, COUNT(*) as students_count
FROM students
GROUP BY course;
