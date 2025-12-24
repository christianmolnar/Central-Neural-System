# CNS Prime Principles

**Last Updated**: 2025-12-23
**Status**: Active
**Evaluation Cycle**: Every session startup + significant learning events

## Core Operating Principles

### 1. Source Control and CI
- Use appropriate remotes for your version control system
- All work happens on feature branches; create PRs to `main`
- Require code review and green CI pipelines before merge
- Keep tests green locally and in CI

**Validation Status**: ✅ Active
**Last Validated**: 2025-12-23
**Confidence**: High

---

### 2. Change Hygiene
- Small, focused commits/PRs with clear titles and descriptions
- Update CHANGELOG.md for user-visible changes
- Use conventional commits style (e.g., feat:, fix:, docs:, chore:, ci:)

**Validation Status**: ✅ Active
**Last Validated**: 2025-12-23
**Confidence**: High

---

### 3. Project Documentation
- Maintain clear, concise documentation
- Link documentation to relevant project management tools
- Keep README files up-to-date with current project state

**Validation Status**: ✅ Active
**Last Validated**: 2025-12-23
**Confidence**: High

---

### 4. Secrets and Safety
- Never commit secrets; use environment variables
- Prefer least-privilege access patterns
- Implement security best practices

**Validation Status**: ✅ Active
**Last Validated**: 2025-12-23
**Confidence**: High

---

### 5. Documentation Best Practices
- Prefer concise documentation linked from README
- Mirror critical operating docs in-repo when practical
- Use consistent documentation formats

**Validation Status**: ✅ Active
**Last Validated**: 2025-12-23
**Confidence**: High

---

### 6. Context Continuity Management
- Create session context files in `~/.personal-cns/cns/memory/context/` folder
- Name format: `context-YYYY-MM-DD-HHMMSS.md`
- Track all user requests, actions taken, and outcomes
- Purpose: Enable seamless handoff between sessions
- Include: timestamps, user requests, tool calls made, results achieved, next steps
- Update throughout session as work progresses

**Validation Status**: ✅ Active
**Last Validated**: 2025-12-23
**Confidence**: High

---

### 7. Self-Evaluation and Continuous Improvement
- After every significant activity or task completion, perform self-evaluation
- Document in `~/.personal-cns/cns/memory/episodic/` folder
- Name format: `learning-YYYY-MM-DD-activity-name.md`
- Include: What went well, what didn't work, what to do differently next time
- Reference these learnings in future similar activities
- Update methodology based on validated learnings

**Validation Status**: ✅ Active
**Last Validated**: 2025-12-23
**Confidence**: High

---

### 8. Quality Assurance
- Run lint and type checking before marking tasks complete
- Ensure tests pass before committing
- Validate security and performance considerations
- Follow established code patterns and conventions

**Validation Status**: ✅ Active
**Last Validated**: 2025-12-23
**Confidence**: High

---

### 9. User Preference Alignment
- Learn and apply user's coding style and preferences
- Adapt communication style to user expectations
- Follow established project patterns and conventions
- Respect user's workflow and tooling choices

**Validation Status**: ✅ Active
**Last Validated**: 2025-12-23
**Confidence**: High

---

### 10. Workflow Optimization
- Use task lists for complex multi-step operations
- Provide real-time progress updates
- Document decisions and their rationale
- Create clear handoff points for continuation

**Validation Status**: ✅ Active
**Last Validated**: 2025-12-23
**Confidence**: High

---

## Evaluation Framework

### Principle Health Indicators
- **Active**: Principle is current, relevant, and being followed
- **Under Review**: Principle needs clarification or updating
- **Deprecated**: Principle is no longer relevant and should be removed
- **Proposed**: New principle identified from learning patterns

### Evaluation Triggers
1. **Session Startup**: Quick validation of all principles
2. **Learning Events**: Check if new learning contradicts or enhances principles
3. **Pattern Detection**: Analysis of learning corpus for new principle candidates
4. **User Request**: Manual principle review and updates

### Change Management
- All principle changes require explicit user approval
- Proposed changes include rationale and evidence
- Version history maintained for principle evolution tracking

## Customization

These principles serve as a starting template. You should customize them based on:
- Your development methodology
- Your tech stack and tooling
- Your team's standards
- Your personal preferences

To customize, edit this file and adjust principles to match your needs.
