#!/bin/bash

# Personal CNS System Installation Script
# Installs Central Neural System for VS Code Copilot

set -e

echo "🧠 Personal CNS System Installation"
echo "===================================="
echo ""

# Determine installation directory
CNS_HOME="${HOME}/.personal-cns"

# Check if CNS already installed
if [ -d "$CNS_HOME" ]; then
    echo "⚠️  CNS already installed at $CNS_HOME"
    read -p "Do you want to overwrite? (y/n): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Installation cancelled."
        exit 0
    fi
    echo "Removing existing installation..."
    rm -rf "$CNS_HOME"
fi

# Create CNS directory
echo "📁 Creating CNS directory at $CNS_HOME..."
mkdir -p "$CNS_HOME"

# Copy CNS components
echo "📋 Copying CNS components..."
cp -r cns "$CNS_HOME/"
cp -r document-library "$CNS_HOME/"

# Make Python scripts executable
echo "🔧 Making Python scripts executable..."
chmod +x "$CNS_HOME/cns/startup-sequence.py"
chmod +x "$CNS_HOME/cns/process-learning.py"
chmod +x "$CNS_HOME/cns/update-cns.py"
chmod +x "$CNS_HOME/cns/brain/principle-evaluator.py"
chmod +x "$CNS_HOME/cns/brain/user-pattern-learner.py"

echo "✅ Python automation scripts deployed and ready"

# Create necessary subdirectories
echo "📂 Creating memory subdirectories..."
mkdir -p "$CNS_HOME/cns/memory/episodic"
mkdir -p "$CNS_HOME/cns/memory/context"

# Create a sample context file
echo "📝 Creating sample context file..."
cat > "$CNS_HOME/cns/memory/context/README.md" << 'EOF'
# Context Files

This directory contains session context files that enable continuity across chat sessions.

Context files are automatically created and managed by the CNS system during VS Code Copilot sessions.

## File Naming Convention
`context-YYYY-MM-DD-HHMMSS.md`

## Purpose
- Track user requests and actions taken
- Document decisions and their rationale
- Record learnings for future application
- Enable seamless handoff between sessions
EOF

# Create a sample episodic memory file
echo "🧠 Creating sample episodic memory file..."
cat > "$CNS_HOME/cns/memory/episodic/README.md" << 'EOF'
# Episodic Memory

This directory contains learning entries from significant tasks and experiences.

## File Naming Convention
`learning-YYYY-MM-DD-activity-name.md`

## Purpose
- Document what went well in completed tasks
- Record challenges and their solutions
- Capture patterns for future reuse
- Support continuous improvement

## Creating Learning Entries
After completing significant tasks, create a learning entry with:
- Context: What was the task/situation
- Approach: What strategy was used
- Outcome: What worked well
- Learnings: What to remember for next time
- Patterns: Reusable patterns identified
EOF

# Create episodic learning template
echo "📋 Creating learning template..."
cat > "$CNS_HOME/cns/memory/episodic/learning-template.md" << 'EOF'
# Learning Entry Template

**Date**: YYYY-MM-DD  
**Activity**: [Brief description of the task/activity]  
**Project**: [Project name if applicable]  
**Duration**: [Time spent]

## Context
[What was the situation? What prompted this task?]

## Approach
[What strategy/methodology was used? What tools were involved?]

## Implementation
[Key steps taken, decisions made, tools used]

## Outcome
### What Worked Well ✅
- [Success point 1]
- [Success point 2]
- [Success point 3]

### Challenges Encountered ⚠️
- [Challenge 1 and how it was resolved]
- [Challenge 2 and how it was resolved]

## Learnings
### Technical Learnings
- [Technical insight 1]
- [Technical insight 2]

### Process Learnings
- [Process improvement 1]
- [Process improvement 2]

### Patterns Identified
- [Reusable pattern 1]
- [Reusable pattern 2]

## For Next Time
### Do More Of
- [Practice to continue 1]
- [Practice to continue 2]

### Do Differently
- [Improvement 1]
- [Improvement 2]

### Avoid
- [Anti-pattern 1]
- [Anti-pattern 2]

## Related Resources
- [Link to documentation]
- [Link to code/files]
- [Link to related learnings]

---

**Tags**: [tag1, tag2, tag3]  
**Confidence**: [High/Medium/Low]  
**Reusability**: [High/Medium/Low]
EOF

# Create context template
echo "📄 Creating context template..."
cat > "$CNS_HOME/cns/memory/context/context-template.md" << 'EOF'
# Session Context

**Date**: YYYY-MM-DD  
**Time**: HH:MM:SS  
**Project**: [Project name]  
**Session ID**: [Unique identifier]

## Session Objectives
[What is the user trying to accomplish in this session?]

## User Requests
### Request 1
- **Time**: HH:MM
- **Request**: [User's request]
- **Actions Taken**: [What was done]
- **Tools Used**: [List of tools]
- **Outcome**: [Result]
- **Status**: [Complete/In Progress/Blocked]

## Decisions Made
1. **Decision**: [What was decided]
   - **Rationale**: [Why this decision]
   - **Alternatives Considered**: [Other options]
   - **Impact**: [Effect on project]

## Ongoing Tasks
- [ ] Task 1 - Status and next steps
- [ ] Task 2 - Status and next steps

## Learnings Captured
- [Learning 1 - reference to episodic entry]
- [Learning 2 - reference to episodic entry]

## Context for Next Session
### Current State
[Where things stand now]

### Next Steps
[What should happen next]

### Important Notes
[Any critical information to remember]

### Files Modified
- `path/to/file1.ext` - [What changed]
- `path/to/file2.ext` - [What changed]

## Related Context Files
- Previous: `context-YYYY-MM-DD-HHMMSS.md`
- Next: `context-YYYY-MM-DD-HHMMSS.md`

---

**Session Duration**: [Duration]  
**Requests Handled**: [Count]  
**Status**: [Active/Completed/Suspended]
EOF

# Create reflex state tracking file
echo "⚙️  Creating reflex state tracking..."
cat > "$CNS_HOME/cns/reflex-state.json" << 'EOF'
{
  "last_principle_evaluation": null,
  "last_pattern_analysis": null,
  "last_maintenance_run": null,
  "learning_count_since_eval": 0,
  "learning_count_since_pattern": 0,
  "total_learnings": 0
}
EOF

echo ""
echo "✅ Installation complete!"
echo ""
echo "📚 Next Steps:"
echo "1. Review and customize: $CNS_HOME/cns/brain/user-patterns.md"
echo "2. Review and customize: $CNS_HOME/cns/brain/prime-principles.md"
echo "3. Copy .github/copilot-instructions.md to your VS Code workspace"
echo "4. Restart VS Code or reload window"
echo "5. Start a new Copilot chat to verify CNS loads"
echo ""
echo "🤖 Python Automation Scripts Installed:"
echo "   • startup-sequence.py - CNS status display"
echo "   • process-learning.py - Capture critical learnings"
echo "   • update-cns.py - Comprehensive maintenance"
echo "   • principle-evaluator.py - Evaluate and update principles"
echo "   • user-pattern-learner.py - Analyze user patterns"
echo ""
echo "📖 Documentation: $CNS_HOME/document-library/"
echo ""
echo "🚀 Happy coding with your enhanced AI assistant!"
