# PHP Adapter

Load when PHP source, `composer.json`, or established PHP tooling is in scope.

## Apply

- Respect the declared PHP version, extensions, autoloading, namespace, and project/framework conventions.
- Preserve strictness and static-analysis expectations; do not add suppressions or broaden types merely to pass.
- Validate external input and use safe platform/framework APIs for output escaping, files, processes, HTTP, and database access.
- Handle exceptions and errors at an appropriate boundary; do not convert failure into a silent success.
- Be explicit about nullable values, array shapes, numeric/string coercion, dates/time zones, and resource lifecycle.
- Treat Composer dependency and lockfile changes as gated according to project policy.

## Validate

Discover syntax, formatter, coding-standard, static-analysis, test, and build commands from the project. Do not assume PHPUnit, PHPStan, PHPCS, Composer scripts, or framework commands exist.
