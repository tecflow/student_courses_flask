#  Student + Courses Management System (MongoDB + Flask)

---

## 📁 Collections & Schemas

### 🎓  students
Each document represents a student.

**Fields:**
- `_id`: ObjectId (automatically generated)
- `name`: string — student's full name
- `group`: string — group or class (e.g., "CS-101")


---

### 📚 courses
Each document represents a course.

**Fields:**
- `_id`: ObjectId
- `title`: string — name of the course
- `teacher`: string — name of the course teacher

---

### 📝 grades
Each document links a student to a course with their grade.

**Fields:**
- `_id`: ObjectId
- `student_id`: ObjectId — reference to a student
- `course_id`: ObjectId — reference to a course
- `grade`: number — grade value (e.g., 87)

---

## 🔧 Required Endpoints / Functionality

### 1. ➕ Add Student
- Accept student data (`name`, `group`)
- Save into `students` collection

`POST /add_student`
```json
{
  "name": "John Doe",
  "group": "CS-101"
}
```
---

### 2. ➕ Add Course
- Accept course data (`title`, `teacher`)
- Save into `courses` collection

`POST /add_course`


```json
{
  "title": "Introduction to Programming",
  "teacher": "Jane Smith"
}

```
---

### 3. 📝 Enroll Student in Course / Add Grade
- Accept `student_id`, `course_id`, and `grade`
- Insert or update grade in `grades` collection

`POST /enroll`

```json
{
  "student_id": "<STUDENT_OBJECT_ID>",
  "course_id": "<COURSE_OBJECT_ID>",
  "grade": 90
}
```
---

### 4. 📖 Get All Courses with Grades for a Student
- Accept a `student_id`
- Return all courses with titles, teachers, and grades that the student is enrolled in

`GET  /student_courses/<student_id>`


```json
[
  {
    "course_title": "Introduction to Programming",
    "teacher": "Jane Smith",
    "grade": 90
  },
  {
    "course_title": "Data Structures",
    "teacher": "John Brown",
    "grade": 85
  }
]
```
