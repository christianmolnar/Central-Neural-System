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
echo "📖 Documentation: $CNS_HOME/document-library/"
echo ""
echo "🚀 Happy coding with your enhanced AI assistant!"
