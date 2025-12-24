# 🚀 Codelassian CNS - Quick Start

## ⚡ One-Command Setup

### Interactive Setup (Works from anywhere)
```bash
~/.codelassian/interactive-setup.sh
```

**That's it!** The script will:
- ✅ Guide you through project setup
- ✅ Create proper VS Code workspace  
- ✅ Enable context isolation
- ✅ Give you exact next steps

## 🚀 Manual Setup (If you prefer)

### Step 1: Verify CNS (5 sec)
```bash
~/.codelassian/verify-cns-setup.sh
```

### Step 2: Create Workspace (10 sec)
```bash
cd /path/to/your/project
~/.codelassian/setup-codelassian-workspace.sh project-name
code project-name.code-workspace
```

### Step 3: Test (5 sec)
Start new Codelassian thread → Should show your project name in CNS startup

Each workspace now gets **isolated context continuity**. Different projects = different context history.

---

## 📋 If You Need More Detail...

### ✅ Working Correctly
- **Different Workspaces** → **Different Context Files**
- **Context Preview** shows relevant previous work
- **Workspace Detection** shows correct project name

### ❌ Common Issues & Fixes
- **Opening folder instead of workspace** → Use `.code-workspace` files
- **Context mixing between projects** → Run verify script, check workspace setup
- **Scripts not found** → Check scripts exist: `ls ~/.codelassian/*.sh`

### 🔧 Quick Fixes
```bash
# Reset if things get weird
~/.codelassian/verify-cns-setup.sh

# Create new workspace
~/.codelassian/setup-codelassian-workspace.sh project-name
```

---

**For Complete Documentation:** [`implementation/STARTUP-INTEGRATION.md`](implementation/STARTUP-INTEGRATION.md)