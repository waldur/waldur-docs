## Linking a local version of the Waldur SDK with Yarn

You can use your local development version of the Waldur SDK in your project by leveraging [Yarn link](https://classic.yarnpkg.com/lang/en/docs/cli/link/).

1. In the Waldur SDK directory, run:
    ```bash
    yarn link
    ```

2. In the Waldur HomePort directory, run:
    ```bash
    yarn link waldur-js-client
    ```

This will symlink your local Waldur SDK into Waldur HomePort for development and testing.
