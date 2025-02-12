#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Parse JSON response
  const todos = JSON.parse(body);
  const completeObj = {};

  // Count completed tasks per user
  todos.forEach(task => {
    if (task.completed) {
      completeObj[task.userId] = (completeObj[task.userId] || 0) + 1;
    }
  });

  console.log(completeObj);
});
