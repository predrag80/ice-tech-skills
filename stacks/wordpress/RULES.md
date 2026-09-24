# WordPress Adapter

Load for WordPress core integration, plugins, themes, blocks, WP-CLI commands, or WordPress database/API behavior. Also load PHP and JavaScript adapters as evidenced by changed files.

## Apply

- Use supported WordPress APIs and existing project prefixes/namespaces; avoid direct core modifications.
- Sanitize and validate input, escape output at the destination, and use `$wpdb->prepare()` or higher-level APIs for queries.
- Verify capability and intent separately: use capability checks plus nonces for state-changing requests. Nonces are not authorization.
- Register hooks deliberately with correct timing, priority, accepted arguments, and removable callbacks where lifecycle matters.
- Keep translation-ready user text and preserve semantic/accessibility behavior in themes and blocks.
- Treat options, post meta, cron, caches/transients, REST/AJAX endpoints, multisite, and activation/uninstall flows as persistent or distributed state.
- Account for supported WordPress/PHP versions and avoid relying on load order or globals without evidence.

## Validate

Use project-defined PHP and front-end commands. Depending on scope, consider coding standards, static analysis, tests, asset build, REST permission callbacks, escaping/sanitization, database query safety, and manual behavior in an appropriate WordPress environment.
