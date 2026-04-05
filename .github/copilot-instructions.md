# Coding Conventions

## General

- Prefer clarity over cleverness. Code is read more often than it is written.
- Write self-documenting code; add comments only where intent is not obvious.
- Keep functions small and focused on a single responsibility.
- Avoid magic numbers — use named constants.

## C++

Follow the [Google C++ Style Guide](https://google.github.io/styleguide/cppguide.html):

### Naming
- Types (classes, structs, enums, type aliases): `PascalCase` — e.g. `MyClass`, `UrlTable`
- Variables and function parameters: `snake_case` — e.g. `table_name`, `num_entries`
- Class data members: `snake_case` with trailing underscore — e.g. `table_name_`
- Constants and `constexpr` values: `kPascalCase` — e.g. `kMaxRetries`
- Functions and methods: `PascalCase` — e.g. `OpenFile()`, `ComputeSum()`
- Namespaces: `snake_case` — e.g. `websearch::index`
- Macros (avoid where possible): `ALL_CAPS_WITH_UNDERSCORES`

### Headers
- Use `#pragma once` for header guards.
- Include headers in this order: related `.h`, C system, C++ standard library, third-party, project headers. Separate each group with a blank line.
- Prefer forward declarations over full `#include` where possible.

### Code Style
- Use `nullptr` instead of `NULL` or `0` for pointers.
- Use `const` wherever applicable; prefer `constexpr` over `const` for compile-time constants.
- Prefer `std::unique_ptr` / `std::shared_ptr` over raw pointers for ownership.
- Prefer range-based `for` loops over index loops when the index is not needed.
- Pass non-trivial objects by `const&` unless a copy or move is intended.
- Avoid `using namespace std;` in header files.
- Limit line length to 80 characters.
- Use 2-space indentation (Google style).

### Error Handling
- Do not use exceptions unless the codebase already uses them.
- Return error codes or use `absl::Status` / `std::expected` where appropriate.

## Python

Follow [PEP 8](https://peps.python.org/pep-0008/) and [PEP 257](https://peps.python.org/pep-0257/):

### Naming
- Modules and packages: `snake_case`
- Classes: `PascalCase`
- Functions, methods, variables: `snake_case`
- Constants: `ALL_CAPS`
- Private members: prefix with `_`

### Code Style
- Use 4-space indentation.
- Limit line length to 88 characters (compatible with `black` formatter).
- Use f-strings over `.format()` or `%` formatting.
- Use type hints on all function signatures.
- Prefer `pathlib.Path` over `os.path` for file operations.

### Imports
- Group imports: standard library, third-party, local. Separate groups with a blank line.
- Avoid wildcard imports (`from module import *`).

### Docstrings
- All public functions, classes, and modules must have docstrings.
- Use Google-style docstrings:
  ```python
  def fetch_data(url: str, timeout: int = 30) -> dict:
      """Fetch JSON data from the given URL.

      Args:
          url: The endpoint to fetch from.
          timeout: Request timeout in seconds.

      Returns:
          Parsed JSON response as a dictionary.

      Raises:
          requests.HTTPError: If the response status is not 2xx.
      """
  ```

## Code Generation Guidelines

When generating new code:
1. Match the naming and formatting conventions for the file's language above.
2. Prefer standard library solutions over external dependencies when practical.
3. Include type annotations for all new Python functions.
4. Do not add boilerplate comments like `# End of function` or `/* TODO */` unless asked.
5. Do not generate `using namespace std;` in C++ files.
6. Generate unit tests alongside new logic when a test file or framework already exists in the project.
