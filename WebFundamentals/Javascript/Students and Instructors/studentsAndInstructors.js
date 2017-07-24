var students = [ 
     {first_name:  'Michael', last_name : 'Jordan'},
     {first_name : 'John', last_name : 'Rosales'},
     {first_name : 'Mark', last_name : 'Guillen'},
     {first_name : 'KB', last_name : 'Tonel'}
];

list(students);

function list(students) {
    for(var student in students) {
        console.log(students[student].first_name + " " + students[student].last_name);
    }
}

var users = {
 'Students': [ 
     {first_name:  'Michael', last_name : 'Jordan'},
     {first_name : 'John', last_name : 'Rosales'},
     {first_name : 'Mark', last_name : 'Guillen'},
     {first_name : 'KB', last_name : 'Tonel'}
  ],
 'Instructors': [
     {first_name : 'Michael', last_name : 'Choi'},
     {first_name : 'Martin', last_name : 'Puryear'}
  ]
 };

listBoth(users);

function listBoth(users) {
    console.log("Students");
    var count = 1;
    for(var student in users.Students) {
        console.log(count + " - " + users.Students[student].first_name + " " + users.Students[student].last_name + " " + (users.Students[student].last_name.length + users.Students[student].first_name.length));
        count++;
    }
    console.log("Instructors");
    count = 1;
    for(var instructor in users.Instructors) {
        console.log(count + " - " + users.Instructors[instructor].first_name + " " + users.Instructors[instructor].last_name + " " + (users.Instructors[instructor].first_name.length + users.Instructors[instructor].last_name.length));
        count++;
    }
 }