# Trigger Responses

## Automatic Responses

### Session Start Trigger
- **Trigger**: New chat session initiated
- **Response**: Execute Enhanced Brain startup sequence
- **Rationale**: Ensure methodology and context continuity
- **Priority**: Critical
- **Implementation**: Automatic via AGENTS.md rule
- **Structural Guarantee**: ALL startup output must appear as PRIMARY message content in a code block BEFORE any other commentary. Use this exact format:
  ```
  ---
  ## CENTRAL NEURAL SYSTEM INITIALIZATION OUTPUT
  [COMPLETE UNMODIFIED STARTUP OUTPUT HERE IN CODE BLOCK]
  ---
  ```
  ONLY after this code block can any other text or questions appear.

### Learning Capture Command
- **Trigger**: User message starts with "Learn this:"
- **Response**: Execute process-learning.py to capture learning
- **Rationale**: Capture critical lessons in CNS memory systems
- **Priority**: Critical
- **Implementation**: `python3 ~/.personal-cns/cns/process-learning.py "[content after 'Learn this:']"`

### Complex Task Detection
- **Trigger**: Task requiring 3+ distinct steps identified
- **Response**: Create todo list and document in implementation plans (.md files)
- **Rationale**: Better organization and progress tracking
- **Priority**: High
- **Implementation**: Track progress in /docs/implementation/ folder

### Code Quality Trigger
- **Trigger**: Code changes made to project files
- **Response**: Execute lint and typecheck commands when available
- **Rationale**: Maintain code quality standards
- **Priority**: High
- **Implementation**: Run npm run lint, npm run typecheck, or equivalent

### File Operation Trigger
- **Trigger**: File edit operation requested
- **Response**: Read file first to understand current state
- **Rationale**: Prevent conflicts and ensure accurate changes
- **Priority**: High
- **Implementation**: Use read_files tool before edit operations

### API Failure Trigger
- **Trigger**: Confluence/Jira API operation fails
- **Response**: Troubleshoot and retry, never create manual workarounds
- **Rationale**: Maintain automated workflow integrity
- **Priority**: Medium
- **Implementation**: Systematic error analysis and resolution

### Quality Threshold Trigger
- **Trigger**: Work not meeting established quality standards
- **Response**: Refine approach and re-execute until standards met
- **Rationale**: Maintain consistent high-quality deliverables
- **Priority**: Medium
- **Implementation**: Iterative improvement process

## Emergency Responses

### Memory Access Emergency
- **Trigger**: CNS memory files cannot be loaded
- **Response**: Verify ~/.personal-cns/ structure, attempt recovery
- **Escalation**: Inform user of memory access issue and suggest CNS maintenance
- **Implementation**: Check file permissions, verify installation, run update-cns.py if needed

### Critical Error Emergency
- **Trigger**: System error preventing normal operation
- **Response**: Document error, attempt graceful recovery
- **Escalation**: Inform user of limitation and suggest alternatives
- **Implementation**: Error logging and user communication

### Security Issue Emergency
- **Trigger**: Potential security risk detected (secrets, exposed data)
- **Response**: Halt operation, secure sensitive information
- **Escalation**: Alert user to security concern immediately
- **Implementation**: Immediate stop and security validation

### Critical Output Display Reflex
- **Trigger**: Any response that must display complete unmodified output (startup, maintenance, context updates, etc.)
- **Response**: Enforce strict message structure
- **Rationale**: Ensure user sees complete information before any assistant interpretation
- **Priority**: Critical
- **Implementation**: 
  1. First block: Complete unmodified output in code fence
  2. Horizontal separator (---)
  3. Only after: Commentary, questions, or follow-up actions
  4. NEVER wrap critical output in function results formatting
  5. NEVER mix assistant commentary with critical output in same paragraph
  6. Validation: Before sending response, verify output is visually separated and unmodified

## Learning Integration Responses

### Task Completion Trigger
- **Trigger**: Significant task completed
- **Response**: Offer to capture learnings
- **Rationale**: Document successful patterns for future reuse
- **Priority**: Medium
- **Implementation**: After complex tasks, ask: "Would you like me to capture learnings from this task?"

### Successful Pattern Recognition
- **Trigger**: Successful completion of significant task
- **Response**: Document pattern in episodic memory (in addition to mandatory context update above)
- **Rationale**: Enable pattern reuse in similar future scenarios
- **Priority**: Medium
- **Implementation**: Update episodic.md with successful patterns

### Methodology Improvement Opportunity
- **Trigger**: Validated improvement to existing methodology
- **Response**: Update relevant CNS components and AGENTS.md if applicable
- **Rationale**: Continuous methodology evolution
- **Priority**: Low
- **Implementation**: Systematic methodology updates

### User Preference Detection
- **Trigger**: Consistent user behavior pattern identified
- **Response**: Update user-patterns.md and user-preferences.md
- **Rationale**: Better alignment with user expectations
- **Priority**: Low
- **Implementation**: Pattern documentation and application

### CNS Maintenance Command
- **Trigger**: User says "Run CNS maintenance" or "Update CNS"
- **Response**: Execute update-cns.py for comprehensive maintenance
- **Rationale**: Periodic CNS optimization and learning consolidation
- **Priority**: Medium
- **Implementation**: `python3 ~/.personal-cns/cns/update-cns.py` and display report

## Quality Assurance Patterns

### Before Marking Task Complete
**Quality Checklist:**
□ Task is actually complete (tests pass, code works, docs updated)
□ Code passes lint checks (if applicable)
□ Type checking successful (if applicable)
□ Documentation updated
□ Security validated (no secrets exposed)
□ Prime Principles adhered to

**For Significant Tasks:**
- Document outcomes in /docs/implementation/ or /docs/status/ folders
- Offer to capture learnings: "Would you like me to capture learnings from this task?"
- If yes, guide through learning documentation process

**Last Updated**: 2025-12-23