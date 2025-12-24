# Quality Checks

## Code Quality Validation

### Syntax and Style Checks
- **Check**: Run lint commands when available (npm run lint, ruff, etc.)
- **Frequency**: After any code modification
- **Threshold**: Zero lint errors or warnings
- **Action**: Fix all issues before considering task complete
- **Documentation**: Update procedural memory with successful patterns

### Type Safety Validation
- **Check**: Run typecheck commands when available (npm run typecheck, mypy, etc.)
- **Frequency**: After TypeScript or typed language modifications
- **Threshold**: Zero type errors
- **Action**: Resolve type issues or add appropriate type annotations
- **Documentation**: Record type patterns in semantic memory

### Test Execution Validation
- **Check**: Run test suites when available and appropriate
- **Frequency**: After code changes that could affect functionality
- **Threshold**: All tests passing
- **Action**: Fix failing tests or update tests if functionality changed intentionally
- **Documentation**: Update test patterns in procedural memory

## File Operation Quality Checks

### Path Validation
- **Check**: Verify file paths are absolute and correct
- **Frequency**: Before any file operation
- **Threshold**: Path exists and is accessible
- **Action**: Correct path or use search tools to find correct location
- **Documentation**: Record successful path patterns

### Content Accuracy Validation
- **Check**: Verify file content matches expected format and structure
- **Frequency**: After file read operations and before edits
- **Threshold**: Content is readable and properly formatted
- **Action**: Handle parsing errors and content inconsistencies gracefully
- **Documentation**: Update error handling patterns

### Edit Precision Validation
- **Check**: Ensure edit operations target exact content matches
- **Frequency**: Before executing edit_file operations
- **Threshold**: old_string matches file content exactly
- **Action**: Re-read file and adjust search strings for precision
- **Documentation**: Record successful edit patterns

## Context and Memory Quality Checks

### Context Continuity Validation
- **Check**: Verify context files are properly formatted and contain required sections
- **Frequency**: After context file creation and updates
- **Threshold**: All required sections present and properly formatted
- **Action**: Fix formatting issues and ensure complete context documentation
- **Documentation**: Update context management procedures

### Memory Consistency Validation
- **Check**: Ensure CNS memory files don't contain conflicting information
- **Frequency**: After memory updates and at session completion
- **Threshold**: No contradictory entries across memory files
- **Action**: Resolve conflicts based on timestamps and evidence
- **Documentation**: Record conflict resolution patterns

### Learning Integration Validation
- **Check**: Verify learnings are properly documented and categorized
- **Frequency**: After significant task completion
- **Threshold**: Learning entry contains all required elements
- **Action**: Complete learning documentation with proper categorization
- **Documentation**: Refine learning documentation templates

## Communication Quality Checks

### Response Conciseness Validation
- **Check**: Ensure responses are concise and direct per user preferences
- **Frequency**: Before sending responses to user
- **Threshold**: Response under 4 lines unless detail explicitly requested
- **Action**: Edit response to remove unnecessary verbosity
- **Documentation**: Update communication patterns

### Technical Accuracy Validation
- **Check**: Verify technical information and recommendations are accurate
- **Frequency**: Before providing technical guidance or solutions
- **Threshold**: Information matches current best practices and documentation
- **Action**: Verify against semantic memory and current documentation
- **Documentation**: Update technical knowledge base

### User Pattern Compliance Validation
- **Check**: Ensure responses align with documented user preferences
- **Frequency**: Before each user interaction
- **Threshold**: Compliance with established user patterns
- **Action**: Adjust response style to match user preferences
- **Documentation**: Update user pattern documentation

## Methodology Compliance Checks

### Golden Rules Adherence Validation
- **Check**: Verify all actions comply with active Golden Rules from AGENTS.md
- **Frequency**: Before executing any significant action
- **Threshold**: Full compliance with all applicable Golden Rules
- **Action**: Modify approach to ensure compliance
- **Documentation**: Record successful compliance patterns

### CNS Architecture Compliance Validation
- **Check**: Ensure all CNS operations follow established architecture
- **Frequency**: After any CNS file modifications
- **Threshold**: Architecture consistency maintained
- **Action**: Resolve architecture inconsistencies
- **Documentation**: Update architecture compliance procedures

### Security Standards Validation
- **Check**: Verify no secrets, keys, or sensitive information exposed
- **Frequency**: Before any file commits or public operations
- **Threshold**: Zero security risks identified
- **Action**: Remove or secure sensitive information immediately
- **Documentation**: Update security best practices

## Automated Quality Gates

### Pre-Commit Quality Gate
- **Triggers**: Before any git commit operations
- **Checks**: Lint, typecheck, test execution, security scan
- **Threshold**: All checks must pass
- **Action**: Fix issues or abort commit
- **Documentation**: Record successful commit patterns

### Task Completion Quality Gate
- **Triggers**: Before marking todos as completed
- **Checks**: All deliverables meet quality standards
- **Threshold**: Complete functionality with quality validation
- **Action**: Continue work until standards met
- **Documentation**: Update task completion procedures

### Session Handoff Quality Gate
- **Triggers**: At session completion
- **Checks**: Context properly documented, learnings recorded
- **Threshold**: Complete session documentation
- **Action**: Complete documentation before session end
- **Documentation**: Refine session handoff procedures

**Last Updated**: 2025-10-23T14:15:00Z