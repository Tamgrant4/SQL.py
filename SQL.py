# q
# Task 1
Insert members into the Members table

INSERT INTO Members (name, age)

VALUES:('John Smith', 30), ('Jane Doe', 25),
('Michael Lee', 42),('Sarah Jones', 28)

Insert sample workout sessions for some members (assuming foreign key constraints are met)
INSERT Into WorkoutSessions (member_id, session_date, session_time, activity)
VALUES (1, '2024-07-02', 'Morning', 'Cardio'),
(2, '2024-07-02', 'Morning', 'Strength Training'),
(3, '2024-07-01', 'Evening', 'Yoga');

#Task 2

-- Update Jane Doe's workout session time to evening
UPDATE WorkoutSessions
SET session_time = 'Evening'
WHERE member_id = (SELECT id FROM Members WHERE name = 'Jane Doe');

#Task 3

-- Delete John Smith's record from the Members table (assuming no cascading deletes)
DELETE FROM Members
WHERE name = 'John Smith';

-- If cascading deletes are enabled, you might need to delete related workout sessions first:
DELETE FROM WorkoutSessions
WHERE member_id = (SELECT id FROM Members WHERE name = 'John Smith');
DELETE FROM Members
WHERE name = 'John Smith';
