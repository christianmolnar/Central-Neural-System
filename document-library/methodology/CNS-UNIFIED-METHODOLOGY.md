# Central Neural System - Unified Methodology Reference

**Last Updated**: 2025-10-23
**Status**: Canonical Reference
**Purpose**: Single source of truth for all CNS methodology and learning frameworks

## Overview

The Central Neural System (CNS) operates on three core architectural components:
- **Brain**: Prime Principles, decision frameworks, and identity
- **Memory**: Episodic learning, semantic knowledge, procedural patterns, context continuity  
- **Reflexes**: Automated quality assurance, error handling, and continuous improvement

## Prime Principles Management

### Location
- **Canonical Source**: `~/.codelassian/cns/brain/prime-principles.md`
- **Loading**: Dynamic loading via startup sequence
- **Updates**: Require explicit user approval only

### Evaluation Framework
- **Frequency**: Session startup + significant learning events
- **Process**: Automated analysis via `principle-evaluator.py`
- **Criteria**: Validity, relevance, usage patterns, learning contradictions
- **Proposals**: System proposes changes, never implements unilaterally

## Learning Methodology

### 6-Point Self-Reflection Protocol

Execute after every significant task or activity:

1. **What went well?**
   - Successful approaches and techniques
   - Positive outcomes and patterns to replicate

2. **What didn't work?**
   - Challenges encountered and failed approaches
   - Inefficient processes or unexpected complications

3. **What to do differently next time?**
   - Specific improvements to implement
   - Alternative approaches to try

4. **Update methodology if this represents a pattern**
   - Check if learning contradicts or enhances existing Prime Principles
   - Identify if multiple similar learnings suggest new principle needed

5. **Reference these learnings in future similar activities**
   - Tag learning with relevant keywords and contexts
   - Link to related previous learnings

6. **Document for team if applicable**
   - Share insights that could benefit others
   - Update shared documentation and templates

### Learning Documentation

**Template Location**: `/Users/cmolnar/.codelassian/document-library/architecture/LEARNING-TEMPLATE.md`

**Storage**: `~/.codelassian/cns/memory/episodic/learning-YYYY-MM-DD-activity-name.md`

**Required Sections**:
- Context and activity description
- What went well / didn't work / to do differently
- Action items for methodology updates
- Pattern recognition and principle implications

### Learning Analysis

**Corpus Analysis**: `principle-evaluator.py` analyzes all recent learnings to:
- Detect recurring patterns across multiple activities
- Identify principle contradictions or validations  
- Propose new principles based on validated patterns
- Evaluate principle usage and relevance

## Context Continuity

### Session Context Management
- **Location**: `~/.codelassian/cns/memory/context/context-YYYY-MM-DD-HHMMSS.md`
- **Purpose**: Seamless handoff between sessions
- **Content**: User requests, actions taken, outcomes, next steps
- **Maintenance**: Update throughout session as work progresses

### Context Restoration
- **Trigger**: CNS startup sequence
- **Process**: Load most recent context file and offer restoration
- **Benefits**: Continuity across 200k token limits and session breaks

## Quality Assurance Framework

### Automated Checks
- **Principle Adherence**: Validate actions against current Prime Principles
- **Learning Integration**: Ensure new learnings are properly documented
- **Context Updates**: Verify context files are maintained
- **Pattern Recognition**: Flag recurring issues or successes

### Error Handling
- **Detection**: Automated identification of principle violations or process failures
- **Response**: Immediate correction with learning documentation
- **Prevention**: Update reflexes and procedures based on error patterns

## Methodology Evolution

### Change Process
1. **Learning Accumulation**: Gather experience through normal operations
2. **Pattern Detection**: Automated analysis identifies trends and contradictions
3. **Proposal Generation**: System proposes specific methodology changes
4. **User Review**: Present changes with rationale and evidence
5. **Implementation**: Execute approved changes with version tracking
6. **Validation**: Monitor effectiveness and adjust as needed

### Change Types
- **Principle Updates**: Modify existing Prime Principles based on learning
- **New Principles**: Add principles for recurring validated patterns
- **Deprecation**: Remove principles that are no longer relevant
- **Process Refinement**: Improve learning, documentation, or evaluation processes

## Integration Points

### Startup Sequence
- Load Prime Principles from CNS brain
- Check for previous context and offer restoration
- Initialize learning and quality assurance systems
- Display current methodology status

### Task Completion
- Execute 6-Point Self-Reflection
- Document learnings in episodic memory
- Update context with outcomes and next steps
- Trigger principle evaluation if significant patterns detected

### Session End
- Finalize context documentation
- Queue learning analysis for next session
- Ensure all principle evaluations are completed

## Success Metrics

### Learning Effectiveness
- Reduction in repeated mistakes
- Improvement in problem-solving speed
- Increased pattern recognition accuracy

### Methodology Adaptation
- Frequency of principle updates based on validated learnings
- Accuracy of proposed methodology changes
- User satisfaction with automated improvements

### System Integration
- Context restoration success rate
- Automated quality check effectiveness
- Learning documentation completeness

---

*This unified methodology serves as the canonical reference for all CNS operations. Individual documents should reference this source rather than duplicating methodology descriptions.*