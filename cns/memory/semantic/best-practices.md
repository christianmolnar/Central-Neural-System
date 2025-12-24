# Best Practices

## Code Quality
- Run lint and type checking before completion
- Follow consistent code style and conventions
- Write self-documenting code with clear variable names
- Keep functions small and focused on single responsibility

## Testing
- Write tests for critical functionality
- Maintain test coverage for core business logic
- Run test suites before committing changes
- Use appropriate testing patterns (unit, integration, e2e)

## Documentation
- Keep README files up-to-date
- Document complex algorithms and business logic
- Maintain CHANGELOG for user-visible changes
- Use clear, concise language in documentation

## Version Control
- Use meaningful commit messages (conventional commits)
- Create small, focused commits
- Work on feature branches
- Review code before merging

## Security
- Never commit secrets or API keys
- Use environment variables for sensitive data
- Implement least-privilege access patterns
- Validate and sanitize user input

## Performance
- Profile before optimizing
- Consider scalability in design
- Optimize critical paths
- Use appropriate data structures and algorithms

---

**Note**: This file accumulates learnings over time. Add new best practices as you discover them.

**Last Updated**: 2025-12-23

## Critical Learning - 2025-12-23 23:21:16
**Source**: User "Learn this:" command

Documentation Organization Standards:

1. **Folder Structure**: All documentation must be organized in proper subdirectories, never at project root
   - Create /docs/ if it doesn't exist
   - Use subdirectories: /docs/architecture/, /docs/implementation/, /docs/status/, /docs/guides/, /docs/reference/

2. **Status Files Naming**: Point-in-time status files MUST be date-prefixed
   - Format: YYYY-MM-DD-description.md
   - Example: 2025-12-23-PHASE-1-COMPLETE.md (NOT PHASE-1-COMPLETE.md)
   - Rationale: Prevents confusion, enables chronological tracking

3. **Project Context Awareness**: In multi-folder workspaces, always verify which project I'm working on
   - Check current working directory
   - Ask user if unclear which project to modify
   - Don't assume based on terminal location alone

4. **Implementation vs User Commands**: Distinguish between:
   - Implementation details (scripts, paths) - for documentation only
   - User commands (natural language) - what users actually use
   - CNS should execute scripts automatically when user uses plain English commands

---

## Critical Learning - 2025-12-23 23:26:20
**Source**: User "Learn this:" command

Test learning capture

---

## Critical Learning - 2025-12-23 23:39:28
**Source**: User "Learn this:" command

Documentation must be organized in /docs/ subdirectories with proper structure (architecture, implementation, status, guides, reference). Status files must be date-prefixed as YYYY-MM-DD-description.md. Always verify which project when in multi-folder workspaces. Never create docs at project root.

---
