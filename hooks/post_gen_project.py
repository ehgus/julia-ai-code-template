import subprocess
import os
import sys


def run_command(command, description):
    print(f"Running: {description}...")
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error during {description}: {e}")
        sys.exit(1)


package_name = "{{ cookiecutter.package_name }}"
package_dir = f"{package_name}.jl"

# 1. Create XP Directory Structure
directories = [
    "iterations",
    "spikes",
    "resources/code-examples/similar-packages",
    "resources/code-examples/algorithms",
    "resources/code-examples/patterns",
    "resources/documentation/internal-specs",
    "resources/documentation/api-drafts",
    "resources/documentation/technical-notes",
    "resources/data/test-cases",
    "resources/data/validation-data",
    "resources/external/papers",
    "resources/external/reference-libs",
    "resources/external/competitor-analysis",
]

for d in directories:
    os.makedirs(d, exist_ok=True)

# 2. Generate Julia package
# We use julia -e to call Pkg.generate
run_command(
    f'julia -e "using Pkg; Pkg.generate(\\"{package_name}\\")"',
    "Julia package generation",
)

# 3. Rename to .jl convention
if os.path.exists(package_name):
    os.rename(package_name, package_dir)
else:
    print(f"Expected directory {package_name} not found after Pkg.generate")
    sys.exit(1)

# 4. Add extra directories required by the XP workflow inside the package
os.makedirs(os.path.join(package_dir, "test"), exist_ok=True)
os.makedirs(os.path.join(package_dir, "docs", "src"), exist_ok=True)

# 5. Create initial README.md for the package
package_readme_content = f"""# {package_dir}

Note: 🚧 This package is under active development. APIs may change without notice.

{{ cookiecutter.description }}

## Overview

Expand on the description to explain what this package does and why it exists.

## Installation

This package is currently under development. You can install it using Julia's package manager:

```julia
using Pkg
Pkg.add(url="https://github.com/{{ cookiecutter.github_username }}/{package_dir}")
```
"""

with open(os.path.join(package_dir, "README.md"), "w") as f:
    f.write(package_readme_content)

# 6. Initialize git
run_command("git init", "Git initialization")

print("\nProject initialized successfully!")
print(f"Julia package created at {package_dir}")
