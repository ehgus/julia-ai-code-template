# Project

See @{{ cookiecutter.package_name }}.jl/README.md for project overview.

## Project Structure & Agent Coordination

### Directory Structure
```
project-root/
├── PROGRESS.md                      # TODO backlog with tagged tasks
├── iterations/                      # XP iteration cycles
│   ├── iter-feature-name/          # Descriptive iteration names
│   │   ├── planning.md             # User stories, tasks for this iteration
│   │   ├── test-failures.md        # RED phase - failing tests
│   │   ├── implementation.md       # GREEN phase - make tests pass
│   │   ├── refactor-notes.md       # REFACTOR phase - improve code
│   │   └── retrospective.md        # What we learned
│   └── ...                         # Keep last 3-10, archive older ones
├── spikes/                          # Timeboxed research experiments
├── resources/                       # Private resources & reference materials
│   ├── code-examples/              # Reference implementations & snippets
│   │   ├── similar-packages/       # Code from similar Julia packages
│   │   ├── algorithms/             # Algorithm implementations to reference
│   │   └── patterns/               # Useful Julia coding patterns
│   ├── documentation/              # Private docs & specifications
│   │   ├── internal-specs/         # Internal specifications & requirements
│   │   ├── api-drafts/             # API design drafts & iterations
│   │   └── technical-notes/        # Technical research & analysis
│   ├── data/                       # Test data & validation datasets
│   │   ├── test-cases/             # Complex test scenarios & edge cases
│   │   └── validation-data/        # Data for algorithm validation
│   └── external/                   # External resources & dependencies
│       ├── papers/                 # Academic papers & research materials
│       ├── reference-libs/         # External library code for reference
│       └── competitor-analysis/    # Analysis of competing solutions
├── {{ cookiecutter.package_name }}.jl/                          # Public Julia package repository
│   ├── src/                        # jl-implementer responsibility
│   ├── test/                       # jl-tester responsibility
│   ├── docs/                       # jl-documenter responsibility
│   ├── Project.toml
│   └── README.md
└── CLAUDE.md                       # This file - project command center
```

### Agent Responsibilities - XP Workflow

#### TDD Cycle (Red-Green-Refactor)
- **jl-tester**: Writes failing tests FIRST in @{{ cookiecutter.package_name }}.jl/test/, defines API through test expectations
  - Documents test approach in @iterations/[current]/test-failures.md
  - Uses @resources/data/test-cases/ for complex scenarios

- **jl-implementer**: Makes tests pass in @{{ cookiecutter.package_name }}.jl/src/, implements minimal code to satisfy tests
  - Documents implementation in @iterations/[current]/implementation.md
  - Documents refactoring in @iterations/[current]/refactor-notes.md
  - References @resources/code-examples/patterns/

- **jl-documenter**: Updates docs incrementally in @{{ cookiecutter.package_name }}.jl/docs/ alongside implementation
  - Living documentation - update with each iteration
  - Adds docstrings to @{{ cookiecutter.package_name }}.jl/src/ (only location documenter touches src/)
  - Uses @resources/documentation/ for templates

#### Just-in-Time Research & Review
- **jl-explorer**: Task decomposition and quick ecosystem research
  - Breaks complex requests into small, independent iterations (1-3 days each)
  - Identifies which subtasks are independent vs. dependent
  - Conducts just-in-time research for current iteration needs
  - Stores findings in @spikes/
  - Uses @resources/ for reference materials

- **jl-critic**: Reviews design decisions and code quality during iterations
  - Documents architectural decisions in @iterations/[current]/planning.md
  - Evaluates architectural options before tests are written

#### Iteration Management
- Current iteration planning: @iterations/[current]/planning.md
- Backlog: @PROGRESS.md with tagged TODOs
- Retrospectives: @iterations/[current]/retrospective.md
- Keep last 3-10 iterations, archive older ones to git tags

### Cross-Session Continuity Protocol

#### Session Startup Routine
1. **Read this CLAUDE.md** for project overview
2. **Check @PROGRESS.md** to see current iteration and backlog
3. **Read @iterations/[current]/planning.md** for current tasks
4. **Check recent @iterations/ retrospectives** for learnings
5. **Begin work** with full context restored

#### Session Ending Routine
1. **Update current iteration files** (planning.md, implementation.md, etc.)
2. **Update @PROGRESS.md** if completing tasks or iteration

#### Cross-Agent Communication
- **Iteration context**: Current work tracked in @iterations/[current]/
- **Research findings**: Store in @spikes/

## Development Guidelines

Each specialized agent has detailed expertise and guidelines. Refer to their prompts for specific instructions:

- **Code standards, REPL philosophy, error handling, display policy**: See jl-implementer agent
- **Testing strategy and comprehensive test suite implementation**: See jl-tester agent
- **Documentation with Documenter.jl and docstring standards**: See jl-documenter agent
- **Task decomposition, iteration planning, and ecosystem exploration**: See jl-explorer agent
- **Design critique and AI-assisted development suitability**: See jl-critic agent

## Notes for Claude Code Usage

### Context Management
- Always reference this CLAUDE.md first for project understanding
- Check @PROGRESS.md for current iteration and TODO backlog
- Current work tracked in @iterations/[current]/ directory
- Explore @resources/ for additional context and examples
- Check @pairing-artifacts/ for collaboration notes
- Review recent @iterations/ retrospectives for learnings

### XP Workflow
- **Test-first**: jl-tester writes failing tests, jl-implementer makes them pass
- **Pair programming**: Agents collaborate through pairing-artifacts/
- **Short iterations**: Complete features in days, tracked in iterations/
- **Continuous refactoring**: Document in refactor-notes.md
- **Living documentation**: jl-documenter updates incrementally

### Quality Gates
- All public code follows Julia community standards
- Experimental approaches documented in spikes/ and pairing-artifacts/
- REPL experience is prioritized throughout development
- Performance considered from iteration planning
- Retrospectives capture learnings for continuous improvement
