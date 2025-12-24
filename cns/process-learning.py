#!/usr/bin/env python3
"""
CNS Learning Protocol Script
Handles "Learn this:" commands by processing and integrating learning into CNS memory systems.
"""

import os
import sys
from datetime import datetime
import json

def process_learning(learning_content):
    """Process a learning command and integrate into CNS memory systems."""
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cns_dir = os.path.dirname(os.path.abspath(__file__))
    
    print("🧠 CNS LEARNING PROTOCOL ACTIVATED")
    print(f"📅 Timestamp: {timestamp}")
    print(f"📚 Learning Content: {learning_content}")
    print("")
    
    # 1. Document in episodic memory
    episodic_dir = os.path.join(cns_dir, "memory", "episodic")
    os.makedirs(episodic_dir, exist_ok=True)
    
    episodic_file = os.path.join(episodic_dir, f"learning-{datetime.now().strftime('%Y-%m-%d-%H%M%S')}.md")
    
    episodic_content = f"""# Critical Learning Captured
**Timestamp**: {timestamp}
**Source**: User "Learn this:" command
**Priority**: Critical

## Learning Content
{learning_content}

## Integration Status
- ✅ Documented in episodic memory
- ✅ Added to best practices

## Application Scope
This learning applies to all future sessions and similar scenarios across projects.

## CNS Integration
Learning integrated into Central Neural System for immediate application and future reference.
"""
    
    with open(episodic_file, 'w') as f:
        f.write(episodic_content)
    
    print(f"✅ Step 1: Episodic memory updated: {episodic_file}")
    
    # 2. Update semantic memory (best practices)
    semantic_dir = os.path.join(cns_dir, "memory", "semantic")
    best_practices_file = os.path.join(semantic_dir, "best-practices.md")
    
    if os.path.exists(best_practices_file):
        with open(best_practices_file, 'r') as f:
            content = f.read()
        
        new_entry = f"""
## Critical Learning - {timestamp}
**Source**: User "Learn this:" command

{learning_content}

---
"""
        
        # Append to best practices
        updated_content = content + new_entry
        
        with open(best_practices_file, 'w') as f:
            f.write(updated_content)
        
        print(f"✅ Step 2: Semantic memory (best-practices.md) updated")
    else:
        print("⚠️  Step 2: best-practices.md not found, creating new file")
        with open(best_practices_file, 'w') as f:
            f.write(f"""# Best Practices

## Critical Learning - {timestamp}
**Source**: User "Learn this:" command

{learning_content}

---
""")
        print(f"✅ Step 2: Created new best-practices.md with learning")
    
    # 3. Integration confirmation
    print("")
    print("🎯 CNS LEARNING INTEGRATION COMPLETE")
    print("📝 Learning captured in multiple memory systems")
    print("🔄 Available for immediate application")
    print("🧠 Integrated into CNS for future sessions")
    print("")
    print("Learning content has been processed and integrated into the Central Neural System.")
    
    return {
        "success": True,
        "timestamp": timestamp,
        "episodic_file": episodic_file,
        "learning_content": learning_content
    }

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 process-learning.py \"<learning content>\"")
        sys.exit(1)
    
    learning_content = " ".join(sys.argv[1:])
    result = process_learning(learning_content)
    
    if result["success"]:
        sys.exit(0)
    else:
        sys.exit(1)