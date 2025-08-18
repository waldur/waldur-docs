# Waldur plugins

## Plugin as extension

Waldur extensions are developed as auto-configurable plugins. One plugin
can contain several extensions which is a pure Django application by its
own. In order to be recognized and automatically connected to Waldur
some additional configuration required.

Extensions' URLs will be registered automatically only if
`settings.WALDUR_CORE['EXTENSIONS_AUTOREGISTER']` is `True`, which is
default.

Create a class inherited from
`waldur_core.core.WaldurExtension`. Implement methods which
reflect your app functionality. At least `django_app()`
should be implemented.

Add an entry point of name `waldur_extensions` to `pyproject.toml`:

> ``` toml
> [project.entry-points.waldur_extensions]
> waldur_demo = "waldur_demo.extension:DemoExtension"
> ```

## Plugin documentation

1. Keep plugin's documentation within plugin's code repository.

2. The documentation page should start with plugin's title and
    description.

3. Keep plugin's documentation page structure similar to the Waldur's main documentation page:

    **Guide** - should contain at least **installation** steps.
    **API** - should include description of API extension, if any.
