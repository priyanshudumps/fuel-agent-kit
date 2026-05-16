# Contributing

Thanks for taking time to improve Fuel Agent Kit. This guide covers the local
setup, validation commands, and pull request expectations for contributors.

## Local Setup

1. Install Node.js 18 or newer.
2. Install package dependencies:

   ```bash
   npm install
   ```

3. Build the package:

   ```bash
   npm run build
   ```

## Development Workflow

Create a branch for each change:

```bash
git checkout -b my-change
```

Use focused commits and keep each pull request scoped to one bug fix, feature,
or documentation update. Before opening a pull request, run the same checks used
by the project:

```bash
npm run ci
```

If you only need a narrower check while iterating, these scripts are available:

| Command | Purpose |
| --- | --- |
| `npm run build` | Builds the package with tsup |
| `npm run test` | Runs the Vitest test suite |
| `npm run lint` | Type-checks the project |
| `npm run check-format` | Checks Prettier formatting |
| `npm run check-exports` | Validates package exports |

## Code Style

- Write TypeScript that passes the existing `tsconfig` checks.
- Format changed files with Prettier.
- Prefer small functions with explicit parameter types for exported APIs.
- Keep wallet, model-provider, and network errors actionable for users.
- Do not commit generated build output unless maintainers ask for it.

## Security

Fuel Agent Kit works with wallet private keys and model provider API keys. Never
commit secrets, test keys with real funds, or screenshots that expose private
credentials. Use environment variables or a local secret manager when testing.

## Pull Requests

When opening a pull request, include:

- a short summary of the change
- the issue number, if one exists
- the commands you ran to validate the change
- screenshots or logs for user-facing behavior, when useful

For larger changes, describe the tradeoffs or compatibility impact so reviewers
can focus on the important decisions.
