# Quick Start - Personal CNS System

Get up and running with CNS for VS Code Copilot in 5 minutes.

## Installation (2 minutes)

```bash
# 1. Clone or download this repository
cd ~/Repos/personal-cns-system

# 2. Run the installer
./install.sh
```

The installer creates `~/.personal-cns/` with all CNS components.

## VS Code Setup (2 minutes)

```bash
# Navigate to any project
cd ~/your-project

# Copy Copilot instructions
mkdir -p .github
cp ~/Repos/personal-cns-system/.github/copilot-instructions.md .github/

# Reload VS Code
# Command Palette (Cmd+Shift+P): "Developer: Reload Window"
```

## Verify (1 minute)

1. Open VS Code Copilot Chat
2. Start new conversation
3. Look for initialization message:
   ```
   🧠 CENTRAL NEURAL SYSTEM LOADED
   ✅ CNS OPERATIONAL
   ```

## Customize (Optional, 5-10 minutes)

Edit these files to match your preferences:

```bash
# Your coding style and preferences
code ~/.personal-cns/cns/brain/user-patterns.md

# Your operating principles
code ~/.personal-cns/cns/brain/prime-principles.md
```

## That's It!

You now have an AI assistant that:
- ✅ Learns your coding style
- ✅ Remembers context across sessions
- ✅ Follows your principles automatically
- ✅ Improves through continuous learning

## Next Steps

- Read [SETUP.md](SETUP.md) for detailed configuration
- Explore [document-library/](document-library/) for full documentation
- Customize CNS components to fit your workflow

---

**Need help?** Check [SETUP.md](SETUP.md) for troubleshooting.
