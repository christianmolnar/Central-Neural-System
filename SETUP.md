# Setup Guide - Personal CNS for VS Code Copilot

## Quick Installation

### Option 1: Automated Installation (Recommended)
```bash
cd ~/Repos/personal-cns-system
./install.sh
```

The script will:
- Create `~/.personal-cns/` directory
- Copy CNS components
- Create necessary subdirectories
- Set up initial memory structure

### Option 2: Manual Installation
```bash
# Create CNS home directory
mkdir -p ~/.personal-cns

# Copy components
cp -r cns ~/.personal-cns/
cp -r document-library ~/.personal-cns/

# Create memory subdirectories
mkdir -p ~/.personal-cns/cns/memory/episodic
mkdir -p ~/.personal-cns/cns/memory/context
```

## VS Code Configuration

### Step 1: Copy Copilot Instructions
For each VS Code workspace where you want CNS enabled:

```bash
# Navigate to your project
cd ~/your-project

# Create .github directory if it doesn't exist
mkdir -p .github

# Copy the Copilot instructions
cp ~/Repos/personal-cns-system/.github/copilot-instructions.md .github/
```

### Step 2: Restart VS Code
- Close and reopen VS Code, OR
- Run command: "Developer: Reload Window"

### Step 3: Verify Installation
1. Open VS Code Copilot Chat
2. Start a new conversation
3. You should see CNS initialization message:
   ```
   🧠 CENTRAL NEURAL SYSTEM LOADED
   ...
   ✅ CNS OPERATIONAL - Enhanced development assistance active
   ```

## Customization

### Essential Customizations

#### 1. User Patterns (`~/.personal-cns/cns/brain/user-patterns.md`)
Define your coding style and preferences:
```markdown
## Communication Preferences
- **Response Style**: Concise and direct
- **Code Comments**: Only for complex logic
- **Emoji Usage**: Never
- **Explanation Depth**: Direct answers
```

#### 2. Prime Principles (`~/.personal-cns/cns/brain/prime-principles.md`)
Adapt the operating principles to your methodology. The template includes:
- Source Control and CI
- Change Hygiene
- Project Documentation
- Secrets and Safety
- Quality Assurance
- etc.

Edit or add principles based on your development practices.

#### 3. User Preferences (`~/.personal-cns/cns/memory/user-preferences.md`)
Configure detailed preferences for:
- Coding style patterns
- Communication style
- Workflow preferences
- Tool usage patterns
- Project preferences

### Optional Customizations

#### Quality Checks (`~/.personal-cns/cns/reflexes/quality-checks.md`)
Adjust quality thresholds and validation rules

#### Error Handling (`~/.personal-cns/cns/reflexes/error-handling.md`)
Customize error recovery procedures

#### Best Practices (`~/.personal-cns/cns/memory/semantic/best-practices.md`)
Add your own best practices and learnings

## Directory Structure

After installation:
```
~/.personal-cns/
├── cns/
│   ├── brain/
│   │   ├── identity.md              # AI assistant identity
│   │   ├── capabilities.md          # Enhanced capabilities
│   │   ├── prime-principles.md      # Operating principles
│   │   ├── decision-framework.md    # Decision process
│   │   └── user-patterns.md         # User coding patterns
│   ├── memory/
│   │   ├── episodic/                # Learning entries
│   │   ├── semantic/                # Knowledge base
│   │   │   └── best-practices.md
│   │   ├── procedural/              # Workflow patterns
│   │   │   └── workflow-patterns.md
│   │   ├── context/                 # Session contexts
│   │   └── user-preferences.md      # Detailed preferences
│   ├── reflexes/
│   │   ├── trigger-responses.md     # Automatic behaviors
│   │   ├── error-handling.md        # Error recovery
│   │   └── quality-checks.md        # Quality validation
│   └── integration/
│       └── prompt-engineering.md    # Prompt strategies
└── document-library/
    ├── architecture/
    ├── methodology/
    ├── implementation/
    └── project-adaptations/
```

## Per-Project Setup

For each project where you want CNS:

1. **Copy Copilot Instructions**
   ```bash
   cp ~/Repos/personal-cns-system/.github/copilot-instructions.md .github/
   ```

2. **Commit to Version Control** (Optional)
   ```bash
   git add .github/copilot-instructions.md
   git commit -m "docs: Add CNS Copilot instructions"
   ```

3. **Reload VS Code**
   - Reload window or restart VS Code

## Verification

### Test CNS Loading
1. Open VS Code Copilot Chat
2. Type: "Hello, can you confirm CNS is loaded?"
3. Copilot should reference CNS components and Prime Principles

### Test Context Continuity
1. Complete a small task in one chat session
2. Start a new chat session
3. Copilot should be able to reference previous session context

### Test Learning Integration
1. Complete a significant task
2. Check `~/.personal-cns/cns/memory/episodic/` for learning entries
3. Start new session and ask about recent learnings

## Troubleshooting

### CNS Not Loading
- Verify `~/.personal-cns/cns/` exists
- Check `.github/copilot-instructions.md` exists in workspace
- Restart VS Code completely
- Check VS Code Copilot Chat settings

### Files Not Found
- Ensure installation completed successfully
- Verify paths in copilot-instructions.md use `~/.personal-cns/`
- Check file permissions

### Copilot Not Following Principles
- Review and clarify prime-principles.md
- Ensure user-patterns.md is customized
- Explicitly reference principles in chat

## Updates

To update CNS:
```bash
cd ~/Repos/personal-cns-system
git pull  # If using git
./install.sh  # Reinstall
```

**Note**: This will overwrite `~/.personal-cns/cns/` but preserve your customizations if they're in version control.

## Support

For issues or questions:
- Review documentation in `~/.personal-cns/document-library/`
- Check GitHub issues (if repository is published)
- Customize and adapt to your needs - CNS is fully extensible

---

**Version**: 1.0.0  
**Last Updated**: 2025-12-23
