# Testing

## Unit tests

Unit tests are used for testing React components and utilities. They are written in `.test.ts` or `.test.tsx` files located next to the code they test.

Run tests using `yarn test` command.

Unit tests use written using:

* [Vitest](https://vitest.dev/) as the test runner
* [@testing-library/react](https://testing-library.com/docs/react-testing-library/intro/) for testing React components
* [@testing-library/user-event](https://testing-library.com/docs/user-event/intro/) for simulating user interactions

## Integration tests

Integration tests are implemented using [Cypress framework](https://www.cypress.io/).

* Run all tests headless (CI mode): `yarn ci:test`
* Open Cypress GUI (requires dev server running): `yarn cypress open`

Integration tests are located in:

* `cypress/e2e/` - Test specifications
* `cypress/fixtures/` - Test data
* `cypress/support/` - Custom commands and utilities
