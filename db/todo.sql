CREATE TABLE IF NOT EXISTS tasks
   (
     idTask integer primary key autoincrement,
     task VARCHAR(255) NOT NULL,
     status VARCHAR(255) NOT NULL,
     creation_date VARCHAR(30) NOT NULL
   );
