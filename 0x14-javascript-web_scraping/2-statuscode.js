#!/usr/bin/node
// script that display the status code of a GET request.
const axios = require('axios').default;

const urls = process.argv[2];

axios
  .get(urls)
  .then((response) => {
    console.log('code: ' + response.status);
  })
  .catch((err) => console.log('code: ' + err.response.status));
