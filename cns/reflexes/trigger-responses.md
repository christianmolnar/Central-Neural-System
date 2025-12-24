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

### Context Continuity Request
- **Trigger**: Previous session context detected
- **Response**: Ask specific question about restoring context
- **Rationale**: Enable seamless session handoff
- **Priority**: High
- **Implementation**: "Do you want to restore the context from the last session? Answer Yes if you would like to do that."

### Complex Task Detection
- **Trigger**: Task requiring 3+ distinct steps identified
- **Response**: Create todo list for task management
- **Rationale**: Better organization and progress tracking
- **Priority**: High
- **Implementation**: Use update_todos tool with clear priorities

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

### Context Loss Emergency
- **Trigger**: Session context cannot be loaded or is corrupted
- **Response**: Attempt recovery from available context files, create new context
- **Escalation**: Inform user of context loss and start fresh session
- **Implementation**: Search for recent context files, extract what's recoverable

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

### Task Completion Trigger ⚠️ MANDATORY
- **Trigger**: Task completed (detected by completion language: "done", "complete", "finished", "deployed", etc.)
- **Response**: AUTOMATICALLY execute context update BEFORE responding to user
- **Rationale**: Ensure context continuity and prevent context loss
- **Priority**: CRITICAL - BLOCKING
- **Implementation**: 
  1. Detect completion language in response being formulated
  2. BEFORE sending response, execute: `cd ~/.codelassian/cns && python3 update-context.py activity "[what was done]"`
  3. ONLY THEN send completion response to user
  4. This is NOT optional - context update is BLOCKING requirement

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

### Explicit Learning Command
- **Trigger**: User message starts with "Learn this:"
- **Response**: Execute comprehensive CNS learning protocol
- **Rationale**: Capture critical lessons and integrate into CNS memory systems
- **Priority**: Critical
- **Implementation**: 
  1. Extract learning content after "Learn this:"
  2. Document in episodic memory with timestamp
  3. Update context with learning integration
  4. Save to workspace memory for persistence
  5. Confirm learning captured and integrated

## CRITICAL Enforcement Pattern

### Before ANY Response Containing Completion Language
**Mandatory Checklist:**
□ Task is actually complete (tests pass, code works, docs updated)
□ Context update executed: `update-context.py activity "[what was done]"`
□ Context update output confirmed
□ ONLY THEN: Respond to user with completion message

**Completion language includes:**
- "done", "complete", "completed", "finished"  
- "deployed", "implemented", "built", "created"
- "fixed", "resolved", "updated", "changed"
- "ready", "working", "success", "✅"

**If you catch yourself about to say completion language:**
1. STOP
2. Update context FIRST
3. THEN respond

This is a BLOCKING requirement. No exceptions.

**Last Updated**: 2025-12-03T20:35:00Z