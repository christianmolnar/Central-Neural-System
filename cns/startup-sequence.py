#!/usr/bin/env python3
"""
Central Neural System Startup Sequence (Simplified)
Displays CNS initialization status and loaded components
"""

import os
import glob
from datetime import datetime
from pathlib import Path

def get_cns_path():
    """Get the ~/.personal-cns directory path"""
    return os.path.expanduser("~/.personal-cns")

def load_recent_learnings(limit=5):
    """Load recent learning entries from CNS episodic memory with full summaries"""
    episodic_path = os.path.join(get_cns_path(), "cns", "memory", "episodic")
    
    learnings = []
    
    if not os.path.exists(episodic_path):
        return learnings
    
    learning_files = glob.glob(os.path.join(episodic_path, "learning-*.md"))
    # Filter out template file
    learning_files = [f for f in learning_files if 'template' not in f.lower()]
    learning_files.sort(reverse=True)  # Newest first
    
    for file_path in learning_files[:limit]:
        try:
            with open(file_path, 'r') as f:
                content = f.read()
            
            filename = os.path.basename(file_path)
            
            # Extract timestamp from filename (learning-YYYY-MM-DD-HHMMSS.md)
            # Format: learning-2025-12-23-233928.md
            parts = filename.replace('.md', '').replace('learning-', '').split('-')
            if len(parts) >= 4:
                date_part = f"{parts[0]}-{parts[1]}-{parts[2]}"
                time_part = parts[3]
                if len(time_part) == 6:
                    timestamp = f"{date_part} {time_part[:2]}:{time_part[2:4]}:{time_part[4:6]}"
                else:
                    timestamp = date_part
            else:
                timestamp = "Unknown time"
            
            # Extract learning content from "## Learning Content" section
            learning_content = ""
            lines = content.split('\n')
            capture = False
            content_lines = []
            
            for line in lines:
                if line.strip() == "## Learning Content":
                    capture = True
                    continue
                elif line.strip().startswith('##') and capture:
                    break
                elif capture and line.strip() and not line.startswith('**'):
                    content_lines.append(line.strip())
            
            # Join content lines and extract first sentence or meaningful chunk
            if content_lines:
                full_content = ' '.join(content_lines)
                # Remove markdown formatting and list markers
                full_content = full_content.replace('**', '').replace('*', '').replace('- ', '').replace('1. ', '').replace('2. ', '').replace('3. ', '')
                # Remove extra whitespace
                full_content = ' '.join(full_content.split())
                # Try to get first sentence
                sentence_end = full_content.find('. ')
                if sentence_end > 30 and sentence_end < 150:
                    learning_content = full_content[:sentence_end + 1]
                elif len(full_content) > 120:
                    learning_content = full_content[:120] + "..."
                else:
                    learning_content = full_content
            
            # If no content found, use first non-header line
            if not learning_content:
                for line in lines:
                    if line.strip() and not line.startswith('#') and not line.startswith('**'):
                        learning_content = line.strip()[:120]
                        break
            
            learnings.append({
                'timestamp': timestamp,
                'summary': learning_content if learning_content else "Learning captured",
                'file': filename
            })
        except Exception as e:
            continue
    
    return learnings

def check_cns_component(component_path, component_name):
    """Check if a CNS component exists"""
    full_path = os.path.join(get_cns_path(), component_path)
    exists = os.path.exists(full_path)
    return exists, full_path

def display_startup_sequence():
    """Display CNS startup sequence and loaded components"""
    
    print("=" * 60)
    print("🧠 CENTRAL NEURAL SYSTEM INITIALIZATION")
    print("=" * 60)
    print()
    
    # Check brain components
    print("📚 BRAIN COMPONENTS:")
    brain_components = [
        ("cns/brain/identity.md", "Identity & Purpose"),
        ("cns/brain/capabilities.md", "Enhanced Capabilities"),
        ("cns/brain/prime-principles.md", "Operating Principles"),
        ("cns/brain/decision-framework.md", "Decision Framework"),
        ("cns/brain/user-patterns.md", "User Patterns")
    ]
    
    for path, name in brain_components:
        exists, _ = check_cns_component(path, name)
        status = "✅" if exists else "❌"
        print(f"   {status} {name}")
    
    print()
    
    # Check memory systems
    print("💾 MEMORY SYSTEMS:")
    
    # Episodic memory
    episodic_path = os.path.join(get_cns_path(), "cns", "memory", "episodic")
    episodic_count = len([f for f in glob.glob(os.path.join(episodic_path, "*.md")) if 'template' not in f.lower()]) if os.path.exists(episodic_path) else 0
    print(f"   ✅ Episodic Memory ({episodic_count} learnings)")
    
    # Recent learnings with full summaries
    recent_learnings = load_recent_learnings(limit=5)
    if recent_learnings:
        print()
        print("   📝 Recent Learnings (last 5):")
        for i, learning in enumerate(recent_learnings, 1):
            print(f"      {i}. [{learning['timestamp']}]")
            print(f"         {learning['summary']}")
            if i < len(recent_learnings):
                print()
    
    print()
    # Semantic memory
    semantic_exists, _ = check_cns_component("cns/memory/semantic/best-practices.md", "Semantic")
    status = "✅" if semantic_exists else "❌"
    print(f"   {status} Semantic Memory (Best Practices)")
    
    # Procedural memory
    procedural_exists, _ = check_cns_component("cns/memory/procedural/workflow-patterns.md", "Procedural")
    status = "✅" if procedural_exists else "❌"
    print(f"   {status} Procedural Memory (Workflow Patterns)")
    
    # User preferences
    prefs_exists, _ = check_cns_component("cns/memory/user-preferences.md", "User Preferences")
    status = "✅" if prefs_exists else "❌"
    print(f"   {status} User Preferences")
    
    print()
    
    # Check reflex system
    print("⚡ REFLEX SYSTEM:")
    reflex_components = [
        ("cns/reflexes/trigger-responses.md", "Trigger Responses"),
        ("cns/reflexes/error-handling.md", "Error Handling"),
        ("cns/reflexes/quality-checks.md", "Quality Checks")
    ]
    
    for path, name in reflex_components:
        exists, _ = check_cns_component(path, name)
        status = "✅" if exists else "❌"
        print(f"   {status} {name}")
    
    print()
    
    # Check integration strategies
    print("🔗 INTEGRATION:")
    integration_exists, _ = check_cns_component("cns/integration/prompt-engineering.md", "Prompt Engineering")
    status = "✅" if integration_exists else "❌"
    print(f"   {status} Prompt Engineering Strategies")
    
    print()
    print("=" * 60)
    print("✅ CENTRAL NEURAL SYSTEM OPERATIONAL")
    print("=" * 60)
    print()

if __name__ == "__main__":
    display_startup_sequence()
