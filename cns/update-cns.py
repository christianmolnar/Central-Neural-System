#!/usr/bin/env python3
"""
Enhanced CNS Update System
Comprehensive CNS maintenance: context updates, learning evaluation, memory consolidation, and principle evolution
"""

import os
import sys
import subprocess
from datetime import datetime
from pathlib import Path

def get_cns_path():
    """Get the ~/.personal-cns directory path"""
    return os.path.expanduser("~/.personal-cns")

def capture_file_snapshot(file_path):
    """Capture a snapshot of a file before modification"""
    if not os.path.exists(file_path):
        return None
    
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except Exception as e:
        print(f"   Warning: Could not read {file_path} for snapshot: {e}")
        return None

def truncate_content(content, max_lines=50):
    """Truncate content for readability in context logs"""
    if not content:
        return content
    
    lines = content.split('\n')
    if len(lines) <= max_lines:
        return content
    
    truncated_lines = lines[:max_lines]
    truncated_lines.append(f"... [truncated {len(lines) - max_lines} more lines]")
    return '\n'.join(truncated_lines)

def detect_file_changes(file_path, before_content):
    """Detect and return changes made to a file"""
    if not os.path.exists(file_path):
        if before_content is not None:
            return {"status": "deleted", "before": truncate_content(before_content), "after": None}
        return None
    
    try:
        with open(file_path, 'r') as f:
            after_content = f.read()
        
        if before_content is None:
            return {"status": "created", "before": None, "after": truncate_content(after_content)}
        elif before_content != after_content:
            return {"status": "modified", "before": truncate_content(before_content), "after": truncate_content(after_content)}
        else:
            return {"status": "unchanged", "before": truncate_content(before_content), "after": truncate_content(after_content)}
    except Exception as e:
        print(f"   Warning: Could not read {file_path} for change detection: {e}")
        return None

def run_script_with_file_tracking(script_path, description, tracked_files=None, *args):
    """Run a CNS script with file change tracking"""
    print(f"🔄 {description}...")
    
    # Take snapshots of tracked files before execution
    file_snapshots = {}
    if tracked_files:
        for file_path in tracked_files:
            abs_path = file_path if os.path.isabs(file_path) else os.path.join(get_cns_path(), "cns", file_path)
            file_snapshots[abs_path] = capture_file_snapshot(abs_path)
    
    try:
        cmd = ["python3", script_path] + list(args)
        result = subprocess.run(cmd, cwd=os.path.dirname(script_path), 
                              capture_output=True, text=True, timeout=300)
        
        # Detect file changes after execution
        file_changes = {}
        if tracked_files:
            for file_path in tracked_files:
                abs_path = file_path if os.path.isabs(file_path) else os.path.join(get_cns_path(), "cns", file_path)
                before_content = file_snapshots.get(abs_path)
                change_info = detect_file_changes(abs_path, before_content)
                if change_info and change_info["status"] != "unchanged":
                    file_changes[abs_path] = change_info
        
        if result.returncode == 0:
            print(f"✅ {description} completed successfully")
            output_lines = result.stdout.strip().split('\n') if result.stdout.strip() else []
            
            # Show all output to user and capture for context logging
            modifications_found = []
            line_count = 1
            for line in output_lines:
                if line.strip():  # Only print non-empty lines
                    # Add numbers to key action lines
                    if any(indicator in line for indicator in ['✅', '🔄', '📝', '🔍', '📚', '🧠', '🚪', '📊', '⚠️', '💤', '🆕', '💭']):
                        print(f"   {line_count}. {line}")
                        line_count += 1
                    else:
                        print(f"      {line}")  # Indent sub-items
                else:
                    print()  # Print empty line for spacing
                
                # Capture file modifications for context logging
                if any(keyword in line.lower() for keyword in ['updated', 'created', 'modified', 'saved', 'renamed']):
                    if '.md' in line:
                        modifications_found.append(line.strip())
            
            return True, result.stdout, modifications_found, file_changes
        else:
            print(f"❌ {description} failed")
            if result.stderr:
                print(f"   Error: {result.stderr.strip()}")
            return False, result.stderr, [], file_changes
            
    except subprocess.TimeoutExpired:
        print(f"⏰ {description} timed out (5 minutes)")
        return False, "Timeout", [], {}
    except Exception as e:
        print(f"❌ {description} error: {e}")
        return False, str(e), [], {}

def run_script(script_path, description, *args):
    """Run a CNS script with error handling and output capture"""
    success, output, modifications, file_changes = run_script_with_file_tracking(script_path, description, None, *args)
    return success, output, modifications

def run_principle_evaluation():
    """Run the principle evaluation system"""
    script_path = os.path.join(get_cns_path(), "cns", "brain", "principle-evaluator.py")
    
    if not os.path.exists(script_path):
        print("❌ principle-evaluator.py not found")
        return False, None, [], {}
    
    # Track principle-related files
    tracked_files = [
        "brain/prime-principles.md",
        "brain/principle-evaluation-report.md"
    ]
    
    success, output, modifications, file_changes = run_script_with_file_tracking(
        script_path, "Evaluating prime principles", tracked_files
    )
    return success, output, modifications, file_changes

def run_user_pattern_learning():
    """Run the user pattern learning system"""
    script_path = os.path.join(get_cns_path(), "cns", "brain", "user-pattern-learner.py")
    
    if not os.path.exists(script_path):
        print("❌ user-pattern-learner.py not found")
        return False, None, [], {}
    
    # Track user pattern files
    tracked_files = [
        "brain/user-patterns.md",
        "memory/user-preferences.md"
    ]
    
    success, output, modifications, file_changes = run_script_with_file_tracking(
        script_path, "Analyzing user behavior patterns", tracked_files
    )
    return success, output, modifications, file_changes

def consolidate_memory_systems():
    """Consolidate and organize memory systems"""
    print("🧠 Consolidating memory systems...")
    
    modifications = []
    
    # Check episodic memory organization
    episodic_path = os.path.join(get_cns_path(), "cns", "memory", "episodic")
    if os.path.exists(episodic_path):
        learning_files = list(Path(episodic_path).glob("*.md"))
        print(f"   1. 📚 Found {len(learning_files)} episodic learning entries")
        
        # Organize by date if needed (future enhancement)
        recent_learnings = [f for f in learning_files 
                          if (datetime.now() - datetime.fromtimestamp(f.stat().st_mtime)).days <= 30]
        print(f"   2. 📅 {len(recent_learnings)} learnings from last 30 days")
    
    # Check context memory organization  
    context_path = os.path.join(get_cns_path(), "cns", "memory", "context")
    if os.path.exists(context_path):
        context_files = list(Path(context_path).glob("context-*.md"))
        print(f"   3. 📝 Found {len(context_files)} context files")
        
        # Cleanup old context files (keep most recent 5 per workspace)
        workspace_contexts = {}
        for context_file in context_files:
            filename = context_file.name
            if filename.count('-') >= 4:
                parts = filename.replace('.md', '').split('-')
                workspace = '-'.join(parts[4:])
                if workspace not in workspace_contexts:
                    workspace_contexts[workspace] = []
                workspace_contexts[workspace].append(context_file)
        
        total_deleted = 0
        deleted_files = []
        for workspace, files in workspace_contexts.items():
            if len(files) > 5:
                files.sort(key=lambda f: f.stat().st_mtime, reverse=True)
                for old_file in files[5:]:
                    try:
                        deleted_files.append(old_file.name)
                        old_file.unlink()
                        total_deleted += 1
                    except Exception as e:
                        print(f"   Warning: Could not delete {old_file.name}: {e}")
        
        if total_deleted > 0:
            print(f"   🧹 Cleaned up {total_deleted} old context files")
            modifications.append(f"Deleted {total_deleted} old context files: {', '.join(deleted_files[:3])}{'...' if len(deleted_files) > 3 else ''}")
    
    print("✅ Memory consolidation completed")
    return True, modifications

def run_reflex_system_updates():
    """Update reflex system based on recent learnings"""
    print("⚡ Updating reflex system...")
    
    modifications = []
    
    reflexes_path = os.path.join(get_cns_path(), "cns", "reflexes")
    if os.path.exists(reflexes_path):
        reflex_files = list(Path(reflexes_path).glob("*.md"))
        print(f"   1. ⚡ Found {len(reflex_files)} reflex definition files")
        
        # Check for last update timestamps
        for i, reflex_file in enumerate(reflex_files, 2):
            with open(reflex_file, 'r') as f:
                content = f.read()
            if "Last Updated" in content:
                print(f"   {i}. 📅 {reflex_file.name}: Contains update timestamp")
            else:
                print(f"   {i}. ⚠️  {reflex_file.name}: Missing update timestamp")
    
    print("✅ Reflex system update completed")
    return True, modifications

def analyze_cns_health():
    """Analyze CNS system health and return status data"""
    print("📊 Analyzing CNS system health...")
    
    health_data = {
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'components': {},
        'memory_systems': {},
        'files_modified': []
    }
    
    # Check component health
    components = {
        'startup-sequence.py': 'Core initialization system',
        'brain/principle-evaluator.py': 'Principle evaluation system',
        'brain/user-pattern-learner.py': 'User pattern learning system'
    }
    
    cns_path = os.path.join(get_cns_path(), "cns")
    
    for component, description in components.items():
        component_path = os.path.join(cns_path, component)
        if os.path.exists(component_path):
            stat = os.stat(component_path)
            health_data['components'][component] = {
                'status': 'active',
                'description': description,
                'last_modified': datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d %H:%M:%S'),
                'size': stat.st_size
            }
        else:
            health_data['components'][component] = {
                'status': 'missing',
                'description': description
            }
    
    # Memory system health
    memory_paths = ['memory/episodic', 'memory/context', 'memory/semantic', 'memory/procedural']
    
    for mem_path in memory_paths:
        full_path = os.path.join(cns_path, mem_path)
        if os.path.exists(full_path):
            if mem_path.endswith(('episodic', 'context')):
                file_count = len(list(Path(full_path).glob("*.md")))
                health_data['memory_systems'][mem_path] = {
                    'status': 'active',
                    'file_count': file_count
                }
            else:
                health_data['memory_systems'][mem_path] = {
                    'status': 'active',
                    'type': 'directory'
                }
        else:
            health_data['memory_systems'][mem_path] = {
                'status': 'missing'
            }
    
    # Print summary
    active_components = sum(1 for data in health_data['components'].values() if data['status'] == 'active')
    total_components = len(health_data['components'])
    
    active_memory = sum(1 for data in health_data['memory_systems'].values() if data['status'] == 'active')
    total_memory = len(health_data['memory_systems'])
    
    print(f"   1. 📊 System Health: {active_components}/{total_components} components active")
    print(f"   2. 🧠 Memory Systems: {active_memory}/{total_memory} systems active")
    
    return health_data

def main():
    """Main CNS update orchestration"""
    print("🧠 COMPREHENSIVE CNS UPDATE STARTING...")
    print("=" * 60)
    print()
    
    start_time = datetime.now()
    
    # Track update results and modifications
    results = {
        'context_update': False,
        'principle_evaluation': False,
        'user_pattern_learning': False,
        'memory_consolidation': False,
        'reflex_updates': False,
        'health_analysis': False
    }
    
    all_modifications = []
    all_outputs = []
    all_file_changes = {}
    
    # 1. Run principle evaluation
    print("🔄 PHASE 1: Principle Evaluation")
    print("-" * 30)
    results['principle_evaluation'], principle_output, principle_mods, principle_changes = run_principle_evaluation()
    if principle_output:
        all_outputs.append(f"PRINCIPLE EVALUATION: {principle_output.strip()}")
    all_modifications.extend(principle_mods)
    all_file_changes.update(principle_changes)
    print()
    
    # 2. Run user pattern learning
    print("🔄 PHASE 2: User Pattern Learning")
    print("-" * 30)
    results['user_pattern_learning'], pattern_output, pattern_mods, pattern_changes = run_user_pattern_learning()
    if pattern_output:
        all_outputs.append(f"USER PATTERN LEARNING: {pattern_output.strip()}")
    all_modifications.extend(pattern_mods)
    all_file_changes.update(pattern_changes)
    print()
    
    # 4. Consolidate memory systems
    print("🔄 PHASE 4: Memory Consolidation")
    print("-" * 30)
    results['memory_consolidation'], memory_mods = consolidate_memory_systems()
    all_modifications.extend(memory_mods)
    print()
    
    # 5. Update reflex systems
    print("🔄 PHASE 5: Reflex System Updates")
    print("-" * 30)
    results['reflex_updates'], reflex_mods = run_reflex_system_updates()
    all_modifications.extend(reflex_mods)
    print()
    
    # 6. Analyze system health
    print("🔄 PHASE 6: System Health Analysis")
    print("-" * 30)
    health_data = analyze_cns_health()
    results['health_analysis'] = health_data is not None
    print()
    
    # Final summary
    end_time = datetime.now()
    duration = end_time - start_time
    
    print("🎯 CNS UPDATE SUMMARY")
    print("=" * 60)
    
    success_count = sum(1 for success in results.values() if success)
    total_phases = len(results)
    
    for i, (phase, success) in enumerate(results.items(), 1):
        status = "✅" if success else "❌"
        print(f"{i}. {status} {phase.replace('_', ' ').title()}")
    
    print()
    print(f"📊 Success Rate: {success_count}/{total_phases} phases completed")
    print(f"⏱️  Duration: {duration.total_seconds():.1f} seconds")
    
    if all_modifications:
        print(f"📝 Files Modified: {len(all_modifications)}")
        for i, mod in enumerate(all_modifications, 1):
            print(f"   {i}. {mod}")
    
    # Create comprehensive context update
    context_summary_parts = [
        f"CNS maintenance completed with {success_count}/{total_phases} phases successful in {duration.total_seconds():.1f}s"
    ]
    
    if all_modifications:
        context_summary_parts.append(f"Files modified: {'; '.join(all_modifications)}")
    
    # Create detailed context entry
    context_details = []
    context_details.append("## CNS Maintenance Results")
    context_details.append(f"- **Timestamp**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    context_details.append(f"- **Duration**: {duration.total_seconds():.1f} seconds")
    context_details.append(f"- **Success Rate**: {success_count}/{total_phases} phases")
    context_details.append("")
    
    context_details.append("### Phase Results")
    for phase, success in results.items():
        status = "✅" if success else "❌"
        context_details.append(f"- {status} {phase.replace('_', ' ').title()}")
    context_details.append("")
    
    if all_modifications:
        context_details.append("### Files Modified")
        for mod in all_modifications:
            context_details.append(f"- {mod}")
        context_details.append("")
    
    # Add verbatim file content changes
    if all_file_changes:
        context_details.append("### Verbatim File Changes")
        for file_path, change_info in all_file_changes.items():
            file_name = os.path.basename(file_path)
            status = change_info["status"]
            
            context_details.append(f"#### {file_name} ({status})")
            
            if status == "created":
                context_details.append("**New Content:**")
                context_details.append("```")
                context_details.append(change_info["after"])
                context_details.append("```")
            elif status == "modified":
                context_details.append("**Before:**")
                context_details.append("```")
                context_details.append(change_info["before"])
                context_details.append("```")
                context_details.append("**After:**")
                context_details.append("```")
                context_details.append(change_info["after"])
                context_details.append("```")
            elif status == "deleted":
                context_details.append("**Deleted Content:**")
                context_details.append("```")
                context_details.append(change_info["before"])
                context_details.append("```")
            
            context_details.append("")
    
    if health_data:
        active_components = sum(1 for data in health_data['components'].values() if data['status'] == 'active')
        total_components = len(health_data['components'])
        active_memory = sum(1 for data in health_data['memory_systems'].values() if data['status'] == 'active')
        total_memory = len(health_data['memory_systems'])
        
        context_details.append("### System Health")
        context_details.append(f"- Components: {active_components}/{total_components} active")
        context_details.append(f"- Memory Systems: {active_memory}/{total_memory} active")
        context_details.append("")
    
    # Print maintenance summary
    if success_count == total_phases:
        print("🎉 All CNS systems updated successfully!")
    else:
        failed_phases = [phase for phase, success in results.items() if not success]
        print(f"⚠️  Some phases failed: {', '.join(failed_phases)}")
    
    return success_count == total_phases

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)