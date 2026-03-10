# Julia AI Code Template

A comprehensive project template for Julia package development using AI agents (like Claude Code or Opencode), designed around Extreme Programming (XP) principles.

This template is optimized for **Test-Driven Development (TDD)** and **Red-Green-Refactor** cycles with specialized subagents.

## Quick Start

Generate your new project using `cookiecutter`:

```bash
# Install cookiecutter if you haven't already
pip install cookiecutter

# Generate project from this template
cookiecutter https://github.com/ehgus/julia-ai-code-template
```

### 1. Initialization Parameters

When running the command, you will be prompted for:
- `project_name`: The name of the root directory (e.g., `FastMatrixProject`)
- `package_name`: The name of the Julia package (e.g., `FastMatrix`)
- `description`: A brief description of the package
- `github_username`: Your GitHub username for installation links

The post-generation hook will automatically:
- Create the XP iteration structure (`iterations/`, `spikes/`, `resources/`)
- Initialize the Julia package using `Pkg.generate()`
- Rename it to the `.jl` convention (e.g., `FastMatrix.jl`)
- Set up `PROGRESS.md` and `CLAUDE.md`
- Initialize a git repository

## Philosophy: Extreme Programming for AI Development

This template adapts Extreme Programming practices for AI-assisted Julia package development:

- **Test-Driven Development (TDD)**: The `jl-tester` agent writes tests first, defining the API. The `jl-implementer` then makes those tests pass with minimal code.
- **Role-Based Workflow**: Specialized agents (`jl-tester`, `jl-implementer`, `jl-critic`, `jl-documenter`, `jl-explorer`) provide focused perspectives.
- **Short Iteration Cycles**: Decompose features into independent, iteration-sized subtasks (1-3 days).
- **Living Documentation**: Documentation is updated incrementally with each change.

## Opencode Compatibility

The agents in this template are located in `.opencode/agents/` and are designed to be used as system prompts for **Opencode** or other agentic coding platforms.

To use an agent, point your agentic tool to the relevant markdown file in `.opencode/agents/`.

## Directory Structure

```
project-name/
├── .opencode/
│   └── agents/                      # Specialized agent system prompts
├── PROGRESS.md                      # TODO tracking & current status
├── CLAUDE.md                        # Project command center
├── AGENTS.md                        # General AI agent guidelines
├── iterations/                      # Short development cycles (XP iterations)
├── spikes/                          # Timeboxed research (XP practice)
├── resources/                       # Private resources & references
└── PackageName.jl/                  # Public Julia package
    ├── src/                        # Package source code
    ├── test/                       # Test suite (TDD)
    ├── docs/                       # Documenter.jl documentation
    └── Project.toml                # Package metadata
```

## Agentic Workflow (XP/TDD)

Refer to `AGENTS.md` for detailed instructions on how AI agents should operate within this structure.

1. **RED**: Write failing tests in `test/` (Agent: `jl-tester`).
2. **GREEN**: Implement minimal code in `src/` to pass tests (Agent: `jl-implementer`).
3. **REFACTOR**: Improve code quality while keeping tests passing.
4. **DOCS**: Update docstrings and documentation incrementally (Agent: `jl-documenter`).
