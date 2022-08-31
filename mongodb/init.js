db = db.getSiblingDB('admin');
db.createUser({user: "admin",pwd: "admin",roles: [ { role: "userAdminAnyDatabase", db: "admin" },{ role: "dbAdminAnyDatabase", db: "admin" },{ role: "readWriteAnyDatabase", db: "admin" } ]}); 
db = db.getSiblingDB('mydb');
db.createCollection('orders');
// db.colors.insert([{ _id : 1, first_name : 'Bob', last_name : 'Hopper', email : 'thebob@example.com' }]);
// db.colors.insert([{ _id : 2, first_name : 'abc', last_name : 'ddd', email : 'abdd@example.com' }]);
// db.colors.insert([{ _id : 3, first_name : 'OP', last_name : 'chat', email : 'opchat@example.com' }]);
// db.colors.insert([{ _id : 4, first_name : 'ABP', last_name : 'CP', email : 'abp@example.com' }]);


db.orders.insert([{_id: 3,first_name: "Casper",last_name: "Cufflin",gender: "Male",city: "Oguma",email: "ccufflin0@topsy.com"}]);
db.orders.insert([{_id: 4,first_name: "Sybila",last_name: "Loftie",gender: "Female",city: "Conchagua",email: "sloftie3@accuweather.com"}]);
db.orders.insert([{_id: 5,first_name: "Dario",last_name: "Palfrie",gender: "Male",city: "Nagu",email: "dpalfrie4@europa.eu"}]);

// {
//     "id": 6,
//     "first_name": "Clemente",
//     "last_name": "Peracco",
//     "gender": "Male",
//     "city": "Pastores",
//     "email": "cperacco5@microsoft.com"
//   }, {
//     "id": 7,
//     "first_name": "Nicola",
//     "last_name": "Spelman",
//     "gender": "Male",
//     "city": "Xêgar",
//     "email": "nspelman6@diigo.com"
//   }, {
//     "id": 8,
//     "first_name": "Sherri",
//     "last_name": "Laverack",
//     "gender": "Female",
//     "city": "Ágios Andréas",
//     "email": "slaverack7@google.com"
//   }, {
//     "id": 9,
//     "first_name": "Ralph",
//     "last_name": "Vanichkov",
//     "gender": "Male",
//     "city": "Huangnan",
//     "email": "rvanichkov8@nbcnews.com"
//   }, {
//     "id": 10,
//     "first_name": "North",
//     "last_name": "Nichol",
//     "gender": "Male",
//     "city": "As Sālimīyah",
//     "email": "nnichol9@shinystat.com"
//   }]
  

// db.orders.insert([{_id: 9,first_name: "Nicola",last_name: "Spelman",gender: "Male",city: "xeger",email: "nspelman6@diigo.com"}])