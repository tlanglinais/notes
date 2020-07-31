Testing is simply verifying your code works properly

## Testing frameworks

There are a bunch of frameworks but Jest pairs nicely with React, since it is also made by Facebook and it comes pre-installed with `create-react-app`.

Jest comes with a handy feature that runs every time a file is saved:

```
[package.json]

"scripts": {
  ...
  "test": "jest --watch *.js" // watching all javascript files
}
```

> Pure function = function that has no side-effects, a constant input will ALWAYS output the same value.

Types of tests

- Unit tests
- Integration tests
- Automation tests

### Testing functions

- `it` - takes a parameter and a function as arguments. It runs the function with the parameter and whether the test passes / fails.

- `expect` - used every time you want to test a value. Append 'matcher' functions to assert values

```
  expect("hello").toBe("hello");
```

- `toBe` - used to compare primitive values or check referential identity of objects.

```
  expect("hello").toBe("hello");
```

## Unit tests
