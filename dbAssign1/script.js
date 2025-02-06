// Map of department codes and names
let deptCode = new Map([
    ['01', 'CSE'],
    ['02', 'ECE'],
    ['03', 'ME'],
    ['04', 'CE']
]);

let students = [];  

function populateDeptDropdown() {
    const deptSelect = document.getElementById('dept');
    deptCode.forEach((deptName, deptCode) => {
        const option = document.createElement('option');
        option.value = deptCode;
        option.textContent = deptName;
        deptSelect.appendChild(option);
    });
}

function showAddForm() {
    document.getElementById('addStudentForm').style.display = 'block';
    document.getElementById('searchStudentForm').style.display = 'none';
    document.getElementById('displayAllForm').style.display = 'none';
    document.getElementById('deleteStudentForm').style.display = 'none'; // Hide delete form
}

function showSearchForm() {
    document.getElementById('searchStudentForm').style.display = 'block';
    document.getElementById('addStudentForm').style.display = 'none';
    document.getElementById('displayAllForm').style.display = 'none';
    document.getElementById('deleteStudentForm').style.display = 'none'; // Hide delete form
}

function showDisplayAll() {
    document.getElementById('displayAllForm').style.display = 'block';
    document.getElementById('addStudentForm').style.display = 'none';
    document.getElementById('searchStudentForm').style.display = 'none';
    document.getElementById('deleteStudentForm').style.display = 'none'; // Hide delete form
    displayAllStudents();
}

function showDeleteForm() {
    document.getElementById('deleteStudentForm').style.display = 'block';
    document.getElementById('addStudentForm').style.display = 'none';
    document.getElementById('searchStudentForm').style.display = 'none';
    document.getElementById('displayAllForm').style.display = 'none';
}

function addStudent() {
    const roll = document.getElementById('roll').value;
    const name = document.getElementById('name').value;
    const address = document.getElementById('address').value;
    const phone = document.getElementById('phone').value;
    const dept = document.getElementById('dept').value;

    if (students.some(student => student.roll === roll)) {
        alert("Roll number already exists.");
        return;
    }

    const newStudent = { roll, name, address, phone, deptCode: dept };
    students.push(newStudent);
    alert('Student added successfully!');
    cancelForm('addStudentForm');
}

function searchStudent() {
    const roll = document.getElementById('searchRoll').value;
    const student = students.find(s => s.roll === roll);

    if (student) {
        const deptName = deptCode.get(student.deptCode);
        document.getElementById('studentDetails').innerHTML = `
            <p><strong>Roll Number:</strong> ${student.roll}</p>
            <p><strong>Name:</strong> ${student.name}</p>
            <p><strong>Department:</strong> ${deptName}</p>
            <p><strong>Address:</strong> ${student.address}</p>
            <p><strong>Phone:</strong> ${student.phone}</p>
        `;
    } else {
        document.getElementById('studentDetails').innerHTML = '<p>Student not found.</p>';
    }
}

function displayAllStudents() {
    let studentList = '';
    students.forEach(student => {
        const deptName = deptCode.get(student.deptCode);
        studentList += `
            <div>
                <p><strong>Roll Number:</strong> ${student.roll}</p>
                <p><strong>Name:</strong> ${student.name}</p>
                <p><strong>Department:</strong> ${deptName}</p>
                <p><strong>Address:</strong> ${student.address}</p>
                <p><strong>Phone:</strong> ${student.phone}</p>
            </div>
            <hr>
        `;
    });
    document.getElementById('studentList').innerHTML = studentList || '<p>No students to display.</p>';
}

function deleteStudent() {
    const roll = document.getElementById('deleteRoll').value;
    const studentIndex = students.findIndex(s => s.roll === roll);

    if (studentIndex !== -1) {
        students.splice(studentIndex, 1);
        alert('Student deleted successfully!');
        cancelForm('deleteStudentForm');
    } else {
        alert('Student not found.');
    }
}

function cancelForm(formId) {
    document.getElementById(formId).style.display = 'none';
}

populateDeptDropdown();
