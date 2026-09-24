# TypeScript Adapter

Load with the JavaScript adapter when TypeScript files or `tsconfig` evidence are in scope.

## Apply

- Follow the project's compiler settings and project references; do not loosen strictness to accommodate a change.
- Model domain states precisely with narrowing, discriminated unions, generics, and explicit boundary types where they reduce invalid states.
- Treat external input as `unknown` until runtime validation establishes its shape.
- Avoid `any`, unsafe assertions, non-null assertions, and suppression comments unless the invariant is proven and documented.
- Preserve emitted/runtime behavior: types vanish, enums/modules may emit code, and build tooling may use settings different from the editor.
- Keep public types compatible with their consumers and generated declarations.

## Validate

Use the project's configured typecheck/build path. Editor diagnostics alone are not a `PASS`. When types or compiler configuration change, validate downstream packages or consumers within scope.
