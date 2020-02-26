# ExpressJS Notes

Express is a lightweight framework for building web applications in Node.js. It is mostly used for building `REST` apis.

`REST` = `RE`presentational `S`tate `T`ransfer

CRUD Operations - Create, Read, Update, Delete

## HTTP Methods:

| HTTP Method | Request                                          | Response                                                |
| ----------- | ------------------------------------------------ | ------------------------------------------------------- |
| **GET**     | **GET** /api/customers                           | [{ id: 1, name: ‘Tanner’ },<br>{id: 2, name: ‘Tanner’}] |
| **POST**    | **POST** /api/customers<br>{ name: ‘Tanner’ }    | { id: 3, name: ‘Tanner’ }                               |
| **PUT**     | **PUT** /api/customers/1<br>{ name: ‘New Name’ } | { id: 1, name: ‘New Name’ }                             |
| **DELETE**  | **DELETE** /api/customer/1                       | {"message": 'success'}                                  |

---

## Environment Variables

Express has access to environment variables through `process.env`
This is most commonly used in server deployment to access the PORT:

```
const port = process.env.PORT || 3000;
app.listen(port, () => console.log('Server started on port ${port}');
```

This checks to see if there is an environment variable named PORT - if not it starts the server on port 3000.

To set environment variables in windows powershell, use the following command:

```
$env:PORT = 5000
```

---

## Server Setup

The basics of an express server are routes and the `listen` method:

```
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Hello world');
});

const port = process.env.PORT || 3000;
app.listen(port, () => console.log(`Listening on port ${port}`);
```

---

## Running the server

Run the app with the following command:

```
node app.js
```

---

## Express generator

This creates an application skeleton to speed up production.

Install either way:

```
npx express-generator
#Earlier versions of node
npm i -g express-generator
```

Run the generator:

```
express --view=pug myapp
```

This will create an app named myapp in the current directory and set the view engine to Pug.

---

## Basic Routing

Routing refers to how an application responds to a client request to an endpoint - a URI and HTTP request method.
Each route can have one or more handler functions, which are executed when the route is matched.

```
app.get('/', function (req, res) {
  res.send('Hello World!')
});
app.post('/', function (req, res) {
  res.send('Got a POST request')
});
app.put('/user', function (req, res) {
  res.send('Got a PUT request at /user')
});
app.delete('/user', function (req, res) {
  res.send('Got a DELETE request at /user')
});
```

---

## Serving static files in Express

To serve static files such as images, CSS files and JS files, use the `express.static` built-in middleware function.
Example:

```
app.use(express.static('public'));
```

Now you can load the files that are in the public directory:

```
http://localhost:3000/images/kitten.jpg
http://localhost:3000/css/style.css
http://localhost:3000/js/app.js
http://localhost:3000/images/bg.png
http://localhost:3000/hello.html
```

To create a virtual path prefix (where the path does not actually exist in the file system) for files that are served by the `express.static` function, specify a mount path:

```
app.use('/static', express.static('public'));
```

Now you can load the files in the public directory:

```
http://localhost:3000/static/images/kitten.jpg
http://localhost:3000/static/css/style.css
http://localhost:3000/static/js/app.js
http://localhost:3000/static/images/bg.png
http://localhost:3000/static/hello.html
```

It is safer to use the absolute path of the directory:

```
app.use('/static', express.static(path.join(__dirname, 'public')))
```

---

## 404 Response

In Express, 404 responses are not the result of an error, but the absence of work to do. Express checks all middleware functions and routes and if none of them responded, you can handle the 404 by adding a middleware function at the very bottom of the stack:

```
app.use(function (req, res, next) {
  res.status(404).send("Sorry can't find that!")
})
```

---

## Error Handling

You define error-handling middleware in the same way as other middleware, except with 4 arguments:

```
app.use(function (err, req, res, next) {
  console.error(err.stack)
  res.status(500).send("Something broke!")
})
```

---

# Routing

A route method is derived from one of the HTTP methods, and is attached to an instance of the `express` class:

```
// GET method route
app.get('/', (req, res) => {
  res.send('GET request to the homepage');
});

// POST method route
app.post('/', (req, res) => {
  res.send('POST request to the homepage');
});
```

## Request parameters:

The request has a parameter called `params` that makes all route parameters accessible:

```
app.get('/api/courses/:id', (req, res) => {
  res.send(courses[req.params.id]);
});
```

You can have more than one route parameter:

```
app.get('api/posts/:year/:month', (req.res) => {
  res.send(req.params);
});

localhost:3000/api/posts/2019/7
// Server responds with { year: 2019, month: 7 }
```

The `req` object also has access to query parameters:

```
// localhost:3000/api/posts/2019/7?sortBy=name

app.get('api/posts/:year/:month', (req.res) => {
  res.send(req.query);
});

// Server responds with { sortBy: 'name' }
```

## Response Methods:

| Method           | Description                                                                           |
| ---------------- | ------------------------------------------------------------------------------------- |
| res.download()   | Prompt a file to be downloaded.                                                       |
| res.end()        | End the response process.                                                             |
| res.json()       | Send a JSON response.                                                                 |
| res.jsonp()      | Send a JSON response with JSONP support.                                              |
| res.redirect()   | Redirect a request.                                                                   |
| res.render()     | Render a view template.                                                               |
| res.send()       | Send a response of various types.                                                     |
| res.sendFile()   | Send a file as an octet stream.                                                       |
| res.sendStatus() | Set the response status code and send its string representation as the response body. |

## app.route()

You can create chainable route handlers for a route path using `app.route()`. Because the path is specified at a single location, creating modular routes is helpful.
Example:

```
app.route('/book')
  .get(function (req, res) {
    res.send('Get a random book')
  })
  .post(function (req, res) {
    res.send('Add a book')
  })
  .put(function (req, res) {
    res.send('Update the book')
  })
```

---

## express.Router

Use the `express.Router` class to create modular, mountable route handlers. A Router instance is a complete middleware and routing system - it is often referred to as a “mini-app”.

```
// birds.js
var express = require('express');
var router = express.Router();

// middleware that is specific to this router
router.use(function timeLog(req, res, next) {
  console.log('Time: ', Date.now());
  next();
}
// define the home page route
router.get('/', function (req, res) {
  res.send('About birds');
});
module.exports = router;
```

Then load the router module in the app:

```
var birds = require('./birds');
// ...
app.use('/birds', birds);
```

---

## Middleware

Functions that have access to the `req` and `res` objects as well as the `next` function (the next middleware function in the stack).

myLogger middleware example:

```
var myLogger = function (req, res, next) {
  console.log('Logged');
  next();
}
```

To load middleware, call `app.use()`:

```
var express = require('express');
var app = express();

app.use(myLogger);

app.get('/', function (req, res) {
  res.send('Hello World!');
});

app.listen(3000);
```

Every time the app receives a request, it prints the message “Logged” to the terminal.
