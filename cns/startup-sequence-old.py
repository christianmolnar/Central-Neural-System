#!/usr/bin/env python3
"""
Central Neural System Startup Sequence
Implements the full startup routine per STARTUP-INTEGRATION.md
"""

import os
import json
import glob
import uuid
from datetime import datetime
from pathlib import Path

def get_cns_path():
    """Get the ~/.personal-cns directory path"""
    return os.path.expanduser("~/.personal-cns")

def load_recent_learnings(limit=5):
    """Load recent learning entries from CNS episodic memory"""
    episodic_path = os.path.join(get_cns_path(), "cns", "memory", "episodic")
    
    learnings = []
    
    # Load from CNS episodic memory (individual learning files)
    if os.path.exists(episodic_path):
        learning_files = glob.glob(os.path.join(episodic_path, "*.md"))
        # Sort by filename (which contains date) to get chronological order, newest first
        learning_files.sort(reverse=True)
        
        for i, file_path in enumerate(learning_files[:limit]):
            try:
                with open(file_path, 'r') as f:
                    content = f.read()
                    
                filename = os.path.basename(file_path)
                # Extract activity name from filename
                if filename.startswith('learning-'):
                    # Format: learning-YYYY-MM-DD-activity-name.md
                    parts = filename.replace('.md', '').split('-')
                    if len(parts) >= 4:
                        activity = '-'.join(parts[4:])
                    else:
                        activity = "Unknown Activity"
                else:
                    # Other episodic memory files
                    activity = filename.replace('.md', '').replace('-', ' ').title()
                    
                # Extract comprehensive summary from content
                lines = content.split('\n')
                summary = ""
                
                # Look for key learning content in order of preference
                for line in lines:
                    # Check for ## Key Learning Principles section
                    if line.startswith('## Key Learning Principles'):
                        # Find the first principle after this heading
                        line_index = lines.index(line)
                        for j in range(line_index + 1, min(line_index + 15, len(lines))):
                            following_line = lines[j]
                            stripped = following_line.strip()
                            if stripped.startswith('1.') or stripped.startswith('-'):
                                # Extract the first principle
                                principle = stripped
                                if principle.startswith('1.'):
                                    principle = principle[2:].strip()
                                elif principle.startswith('-'):
                                    principle = principle[1:].strip()
                                
                                # Handle markdown formatting like **Bold**: content
                                if '**' in principle and ':' in principle:
                                    # Extract the full principle, removing markdown but keeping structure
                                    summary = principle.replace('**', '').strip()
                                elif ':' in principle:
                                    # Keep both the bold part and the explanation
                                    summary = principle.replace('**', '').strip()
                                else:
                                    summary = principle.replace('**', '')
                                break
                        if summary:
                            break
                    
                    # Fallback to ## Context section
                    elif line.startswith('## Context') and not summary:
                        line_index = lines.index(line)
                        for following_line in lines[line_index:line_index + 5]:
                            if following_line.strip() and not following_line.startswith('##'):
                                summary = following_line.strip()[:100] + "..." if len(following_line.strip()) > 100 else following_line.strip()
                                break
                        if summary:
                            break
                    
                    # Last resort: use title
                    elif line.startswith('# ') and not summary:
                        title = line.replace('# ', '').strip()
                        if 'Learning:' in title:
                            summary = title.split('Learning:', 1)[1].strip()
                        else:
                            summary = title
                        break
                
                if not summary:
                    summary = f"Learning about {activity.replace('-', ' ')}"
                    
                learnings.append({
                    'filename': filename,
                    'activity': activity,
                    'summary': summary,
                    'path': file_path
                })
                
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
                continue
    
    return learnings[:limit]

def get_current_workspace():
    """Determine the current workspace/project directory from environment and context"""
    import sys
    import subprocess
    
    # Method 0: Check CURRENT working directory's git repo (handles mid-session switches)
    current_dir = os.getcwd()
    try:
        result = subprocess.run(['git', 'rev-parse', '--show-toplevel'], 
                              capture_output=True, text=True, cwd=current_dir)
        if result.returncode == 0:
            repo_root = result.stdout.strip()
            return os.path.basename(repo_root)
    except:
        pass
    
    # Method 1: Extract from current working directory path if in /Repos/
    if '/Repos/' in current_dir:
        project_path = current_dir.split('/Repos/')[-1]
        project_name = project_path.split('/')[0]
        return project_name
    
    # Method 2: Check for CODELASSIAN_WORKSPACE_DIR passed from AGENTS.md startup (fallback)
    codelassian_workspace_dir = os.environ.get('CODELASSIAN_WORKSPACE_DIR')
    if codelassian_workspace_dir and os.path.exists(codelassian_workspace_dir):
        # Try to get git repo name first
        try:
            result = subprocess.run(['git', 'rev-parse', '--show-toplevel'], 
                                  capture_output=True, text=True, cwd=codelassian_workspace_dir)
            if result.returncode == 0:
                repo_root = result.stdout.strip()
                return os.path.basename(repo_root)
        except:
            pass
        # Fallback to directory name
        return os.path.basename(codelassian_workspace_dir)
    
    # Method 3: Check if we're in VS Code - use the workspace root from environment
    workspace_folder = os.environ.get('WORKSPACE_FOLDER')
    if workspace_folder:
        return os.path.basename(workspace_folder)
    
    # Method 2: Check for VS Code specific environment variables
    vscode_workspace = os.environ.get('VSCODE_CWD')
    if vscode_workspace and vscode_workspace != '/' and '/Repos/' in vscode_workspace:
        return os.path.basename(vscode_workspace)
    
    # Method 3: Check command line arguments for workspace hint
    if len(sys.argv) > 1 and '--workspace=' in ' '.join(sys.argv):
        for arg in sys.argv:
            if arg.startswith('--workspace='):
                return arg.split('=', 1)[1]
    
    # Method 4: Check if we're in a git repository and use repo name (PRIORITIZED)
    current_dir = os.getcwd()
    try:
        result = subprocess.run(['git', 'rev-parse', '--show-toplevel'], 
                              capture_output=True, text=True, cwd=current_dir)
        if result.returncode == 0:
            repo_root = result.stdout.strip()
            return os.path.basename(repo_root)
    except:
        pass
    
    # Method 5: Extract the project name from the current working directory
    # This handles paths like /Users/cmolnar/Repos/project-name
    if '/Repos/' in current_dir:
        project_path = current_dir.split('/Repos/')[-1]
        # Get just the first part (project name) if there are subdirectories
        project_name = project_path.split('/')[0]
        return project_name
    
    # Method 6: Try to find workspace by looking at current directory
    # If we're in the .codelassian/cns directory, we need to find the actual workspace
    if '.codelassian' in current_dir:
        # Try to read the last used workspace from a tracking file
        tracking_file = os.path.join(get_cns_path(), 'current-workspace.txt')
        if os.path.exists(tracking_file):
            try:
                with open(tracking_file, 'r') as f:
                    workspace = f.read().strip()
                    if workspace:
                        return workspace
            except:
                pass
        
        # Fallback: look in common repo locations
        user_home = os.path.expanduser('~')
        repos_path = os.path.join(user_home, 'Repos')
        if os.path.exists(repos_path):
            # Get the most recently modified directory in Repos
            try:
                dirs = [d for d in os.listdir(repos_path) 
                       if os.path.isdir(os.path.join(repos_path, d)) and not d.startswith('.')]
                if dirs:
                    # Sort by modification time, most recent first
                    dirs.sort(key=lambda d: os.path.getmtime(os.path.join(repos_path, d)), reverse=True)
                    return dirs[0]
            except:
                pass
    
    # Fallback: use the basename of the current directory
    return os.path.basename(current_dir)

def find_latest_context_by_name(context_name):
    """Find the most recent context file with the given context name"""
    context_path = os.path.join(get_cns_path(), "cns", "memory", "context")
    
    if not os.path.exists(context_path):
        return None
    
    # Get all context files with this name (new naming convention: [context-name]-[date].md)
    context_pattern = os.path.join(context_path, f"{context_name}-*.md")
    context_files = glob.glob(context_pattern)
    
    if not context_files:
        return None
    
    # Sort by filename timestamp (newest first) and return latest
    context_files.sort(reverse=True)
    return context_files[0]

def get_available_context_names():
    """Get all available context names from existing context files, sorted by most recent"""
    context_path = os.path.join(get_cns_path(), "cns", "memory", "context")
    
    if not os.path.exists(context_path):
        return []
    
    context_files = glob.glob(os.path.join(context_path, "*.md"))
    context_info = {}  # context_name -> latest_timestamp
    
    for context_file in context_files:
        filename = os.path.basename(context_file).replace('.md', '')
        
        # Extract context name and timestamp from filename
        context_name = None
        timestamp = None
        
        if filename.startswith('context-') and filename.count('-') >= 4:
            # Old format: context-YYYY-MM-DD-HHMMSS-workspace.md
            parts = filename.split('-')
            if len(parts) >= 5:
                context_name = '-'.join(parts[4:])  # Everything after timestamp
                timestamp = '-'.join(parts[1:4]) + '-' + parts[3]  # YYYY-MM-DD-HHMMSS
        else:
            # New format: [context-name]-YYYY-MM-DD-HHMMSS.md
            import re
            match = re.search(r'^(.+?)-(\d{4}-\d{2}-\d{2}-\d{6})$', filename)
            if match:
                context_name = match.group(1)
                timestamp = match.group(2)
        
        if context_name and timestamp:
            # Keep track of the latest timestamp for each context name
            if context_name not in context_info or timestamp > context_info[context_name]:
                context_info[context_name] = timestamp
    
    # Sort context names by latest timestamp (newest first)
    sorted_contexts = sorted(context_info.items(), key=lambda x: x[1], reverse=True)
    
    return [context_name for context_name, timestamp in sorted_contexts]

def get_workspace_context_names(workspace_name, limit=3):
    """Get context names for the current workspace only, limited to specified count"""
    context_path = os.path.join(get_cns_path(), "cns", "memory", "context")
    
    if not os.path.exists(context_path):
        return []
    
    context_files = glob.glob(os.path.join(context_path, "*.md"))
    workspace_contexts = []  # (display_name, timestamp, file_path)
    
    for context_file in context_files:
        filename = os.path.basename(context_file).replace('.md', '')
        
        # Extract context name and timestamp from filename
        context_name = None
        timestamp = None
        
        if filename.startswith('context-') and filename.count('-') >= 4:
            # Old format: context-YYYY-MM-DD-HHMMSS-workspace.md
            parts = filename.split('-')
            if len(parts) >= 5:
                context_name = '-'.join(parts[4:])  # Everything after timestamp
                timestamp = '-'.join(parts[1:4]) + '-' + parts[3]  # YYYY-MM-DD-HHMMSS
        else:
            # New format: [context-name]-YYYY-MM-DD-HHMMSS.md
            import re
            match = re.search(r'^(.+?)-(\d{4}-\d{2}-\d{2}-\d{6})$', filename)
            if match:
                context_name = match.group(1)
                timestamp = match.group(2)
        
        # Check if this context belongs to the current workspace
        if context_name and timestamp:
            # For old format, context_name already contains workspace
            # For new format, check if context file content matches workspace
            belongs_to_workspace = False
            
            if filename.startswith('context-') and workspace_name in context_name:
                # Old format - workspace is part of context name
                belongs_to_workspace = True
            elif not filename.startswith('context-'):
                # New format - check file content for workspace
                try:
                    with open(context_file, 'r') as f:
                        content = f.read()
                        if f'**Current Workspace**: {workspace_name}' in content:
                            belongs_to_workspace = True
                except:
                    # If we can't read the file, include it anyway for new format with workspace name
                    if workspace_name in context_name:
                        belongs_to_workspace = True
            
            if belongs_to_workspace:
                # Create display name with timestamp for clarity
                time_part = timestamp.replace('-', '/')[0:10] + ' ' + timestamp[-6:-4] + ':' + timestamp[-4:-2] + ':' + timestamp[-2:]
                display_name = f"{context_name} ({time_part})"
                workspace_contexts.append((display_name, timestamp, context_file))
    
    # Sort by timestamp (newest first) and limit to specified count
    workspace_contexts.sort(key=lambda x: x[1], reverse=True)
    
    return [display_name for display_name, timestamp, file_path in workspace_contexts[:limit]]

def get_all_workspaces_from_contexts():
    """Get all unique workspace names from existing context files"""
    context_path = os.path.join(get_cns_path(), "cns", "memory", "context")
    
    if not os.path.exists(context_path):
        return []
    
    context_files = glob.glob(os.path.join(context_path, "*.md"))
    workspaces = set()
    
    for context_file in context_files:
        filename = os.path.basename(context_file).replace('.md', '')
        
        if filename.startswith('context-') and filename.count('-') >= 4:
            # Old format: context-YYYY-MM-DD-HHMMSS-workspace.md
            parts = filename.split('-')
            if len(parts) >= 5:
                workspace_name = '-'.join(parts[4:])  # Everything after timestamp
                workspaces.add(workspace_name)
        else:
            # New format: check file content for workspace
            try:
                with open(context_file, 'r') as f:
                    content = f.read()
                    lines = content.split('\n')
                    for line in lines[:20]:
                        if '**Current Workspace**:' in line:
                            workspace_name = line.split(':', 1)[1].strip()
                            if workspace_name and workspace_name != 'unknown':
                                workspaces.add(workspace_name)
                            break
            except:
                pass
    
    # Sort workspaces, putting common ones first
    workspace_list = sorted(list(workspaces))
    
    # Prioritize common workspace patterns
    priority_workspaces = []
    other_workspaces = []
    
    for ws in workspace_list:
        if any(pattern in ws.lower() for pattern in ['atlassian', 'consent', 'pgm']):
            priority_workspaces.append(ws)
        else:
            other_workspaces.append(ws)
    
    return priority_workspaces + other_workspaces

def update_workspace_tracking(workspace_name):
    """Update the workspace tracking file with confirmed workspace"""
    tracking_file = os.path.join(get_cns_path(), 'current-workspace.txt')
    try:
        with open(tracking_file, 'w') as f:
            f.write(workspace_name)
    except Exception as e:
        print(f"Warning: Could not update workspace tracking: {e}")

def create_session_context(context_name):
    """Create a new context file with the given context name"""
    from datetime import datetime
    
    # Generate timestamp for context filename  
    timestamp = datetime.now().strftime("%Y-%m-%d-%H%M%S")
    context_filename = f"{context_name}-{timestamp}.md"
    
    # Determine the actual working directory (not .codelassian)
    working_dir = os.environ.get('WORKSPACE_FOLDER') or os.environ.get('VSCODE_CWD')
    current_workspace = get_current_workspace()
    if not working_dir:
        # Try to reconstruct from workspace name
        user_home = os.path.expanduser('~')
        repos_path = os.path.join(user_home, 'Repos', current_workspace)
        if os.path.exists(repos_path):
            working_dir = repos_path
        else:
            working_dir = os.getcwd()
    
    # Create context file path
    context_path = os.path.join(get_cns_path(), "cns", "memory", "context")
    os.makedirs(context_path, exist_ok=True)
    context_file_path = os.path.join(context_path, context_filename)
    
    # Create initial context content
    context_content = f"""# Context Session: {context_name} - {timestamp}

## Session Overview
- **Start Time**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
- **Working Directory**: {working_dir}
- **Current Workspace**: {current_workspace}
- **Context Name**: {context_name}
- **Context File**: {context_filename}

## Session Status
- **CNS Initialization**: Completed
- **Context Creation**: Manual (after user context restoration decision)
- **Ready for**: User requests and task execution

## Session Activities
- Context file created after context restoration decision
- Ready to track user requests, actions taken, and outcomes

## Next Steps
- Await user direction
- Track all activities in this context file
- Update throughout session for continuity
"""
    
    # Write context file
    try:
        with open(context_file_path, 'w') as f:
            f.write(context_content)
        
        # Update current context tracking file
        tracking_file = os.path.join(get_cns_path(), 'current-context.txt')
        try:
            with open(tracking_file, 'w') as f:
                f.write(context_name)
        except:
            pass  # Non-critical
        
        return context_filename, context_name
    except Exception as e:
        print(f"Warning: Could not create context file: {e}")
        return None, context_name

def display_startup_sequence():
    """Display the full Central Neural System startup sequence"""
    
    print("🧠 CENTRAL NEURAL SYSTEM LOADING...")
    print("   1. 🔧 Initializing CNS session...")
    print("   2. 📖 Loading methodology from AGENTS.md")
    print("   3. 🧠 Loading recent learnings and memory patterns")
    print("   4. 🎯 Applying CNS architecture patterns")
    print("   5. ⚡ Activating reflex system and quality checks")
    print("   6. 📝 Creating session context file...")
    print()
    print("   ✅ CNS SESSION INITIALIZED SUCCESSFULLY")
    print()
    
    # Load methodology from AGENTS.md
    agents_path = os.path.join(get_cns_path(), "AGENTS.md")
    methodology_content = ""
    methodology_size = 0
    
    if os.path.exists(agents_path):
        with open(agents_path, 'r') as f:
            methodology_content = f.read()
            methodology_size = len(methodology_content)
    
    # Load Prime Principles from CNS brain
    prime_principles_path = os.path.join(get_cns_path(), "cns", "brain", "prime-principles.md")
    prime_principles = []
    principles_size = 0
    
    if os.path.exists(prime_principles_path):
        with open(prime_principles_path, 'r') as f:
            principles_content = f.read()
            principles_size = len(principles_content)
            
        # Parse prime principles with details
        lines = principles_content.split('\n')
        current_principle = None
        
        for line in lines:
            if line.startswith('### ') and '. ' in line:
                # New principle heading
                if current_principle:
                    prime_principles.append(current_principle)
                
                title = line.replace('### ', '').strip()
                current_principle = {
                    'title': title,
                    'details': []
                }
            elif current_principle and line.strip().startswith('- ') and not line.startswith('**'):
                # Principle detail (bullet point that's not metadata)
                detail = line.strip()[2:].strip()  # Remove "- " prefix
                current_principle['details'].append(detail)
            elif line.strip() == "---" and current_principle:
                # End of principle section
                prime_principles.append(current_principle)
                current_principle = None
        
        # Don't forget the last principle if no final ---
        if current_principle:
            prime_principles.append(current_principle)
    
    # Load User Patterns from CNS brain
    user_patterns_path = os.path.join(get_cns_path(), "cns", "brain", "user-patterns.md")
    user_patterns_loaded = False
    user_patterns_size = 0
    
    if os.path.exists(user_patterns_path):
        with open(user_patterns_path, 'r') as f:
            user_patterns_content = f.read()
            user_patterns_size = len(user_patterns_content)
            user_patterns_loaded = True
    
    print("📚 METHODOLOGY LOADED:")
    print(f"   1. From: AGENTS.md ({methodology_size} chars)")
    print(f"   2. Prime Principles: {len(prime_principles)} loaded from CNS brain ({principles_size} chars)")
    if user_patterns_loaded:
        print(f"   3. User Patterns: Loaded from CNS brain ({user_patterns_size} chars)")
        print("   4. Memory System: Episodic, Semantic, Procedural, Context")
        print("   5. Reflex System: Triggers, Error Handling, Quality Checks")
        print("   6. Learning Cycles: 6-point reflection, Pattern recognition")
    else:
        print("   3. User Patterns: Not found (using defaults)")
        print("   4. Memory System: Episodic, Semantic, Procedural, Context")
        print("   5. Reflex System: Triggers, Error Handling, Quality Checks")
        print("   6. Learning Cycles: 6-point reflection, Pattern recognition")
    print()
    
    if prime_principles:
        print("🎯 PRIME PRINCIPLES ACTIVE:")
        for i, principle in enumerate(prime_principles, 1):
            if isinstance(principle, dict):
                # Extract title after the number
                title_parts = principle['title'].split('.', 1)
                title = title_parts[1].strip() if len(title_parts) > 1 else principle['title']
                print(f"   {i}. {title}")
                
                # Show ALL details verbatim
                if principle['details']:
                    for j, detail in enumerate(principle['details'], 1):
                        print(f"      {j}. {detail}")
            else:
                # Fallback for old string format
                principle_title = principle.split('.', 1)[1].strip() if '. ' in principle else principle
                print(f"   {i}. {principle_title}")
            print()
    else:
        print("🎯 PRIME PRINCIPLES: Loading from CNS brain...")
    print()
    
    # Load and display recent learnings
    learnings = load_recent_learnings(5)
    print("🧠 RECENT LEARNINGS APPLICATION:")
    if learnings:
        print("These are the last 5 things I learned and how I plan to apply them:")
        for i, learning in enumerate(learnings, 1):
            # Extract date from filename (learning-YYYY-MM-DD-*)
            date = "Unknown"
            try:
                filename = learning['filename']
                if 'learning-' in filename:
                    date_part = filename.split('learning-')[1][:10]  # Extract YYYY-MM-DD
                    if len(date_part) == 10 and date_part.count('-') == 2:
                        date = date_part
            except:
                pass
                
            # Extract title from path
            title = "Learning"
            try:
                with open(learning['path'], 'r') as f:
                    first_line = f.readline().strip()
                    if first_line.startswith('# '):
                        title = first_line.replace('# ', '').strip()
                        # Remove "Learning: " prefix if present
                        if title.startswith('Learning: '):
                            title = title.replace('Learning: ', '')
                        # Remove date suffix if present
                        if ' - 20' in title:
                            title = title.split(' - 20')[0]
            except:
                pass
                
            # Get summary
            summary = get_learning_application(learning)
            
            print(f"   {i}. {date}: {title}")
            print(f"      {summary}")
    else:
        print("   📝 No previous learnings found - this is a fresh start!")
        print("   🧠 I will begin accumulating learnings from this session forward.")
    print()
    
    print("🎯 CNS ARCHITECTURE ACTIVE:")
    print("   1. Brain: Identity, Capabilities, Decision Framework, Collaboration")
    print("   2. Memory: Learning accumulation and pattern recognition")
    print("   3. Reflexes: Automatic quality assurance and error handling")
    print("   4. Integration: Prompt engineering and agent coordination")
    print()
    
    print()
    print("✅ CENTRAL NEURAL SYSTEM OPERATIONAL")
    print()
    
    # Clean up old context files (keep current + 2 previous per context name)
    cleanup_old_contexts(keep_per_context_name=3)
    
    # Get detected workspace
    current_workspace = get_current_workspace()
    
    # Get available repositories for user confirmation
    available_repos = []
    user_home = os.path.expanduser('~')
    repos_path = os.path.join(user_home, 'Repos')
    if os.path.exists(repos_path):
        try:
            dirs = [d for d in os.listdir(repos_path) 
                   if os.path.isdir(os.path.join(repos_path, d)) and not d.startswith('.')]
            # Sort alphabetically for consistency
            available_repos = sorted(dirs)
        except:
            pass
    
    # Get workspace-specific context names (max 3)
    workspace_contexts = get_workspace_context_names(current_workspace, limit=3)
    
    print("📝 SESSION CONTEXT:")
    print(f"   1. Current workspace: {current_workspace}")
    print("   2. Context file will be created AUTOMATICALLY")
    
    # Show available repositories for confirmation
    if available_repos:
        print(f"   3. Available repositories: {', '.join(available_repos[:10])}")
        if len(available_repos) > 10:
            print(f"      ...and {len(available_repos) - 10} more")
    
    if workspace_contexts:
        print("   4. Available contexts for this workspace:")
        for i, context_name in enumerate(workspace_contexts, 1):
            print(f"      {i}. {context_name}")
    else:
        print("   4. No previous contexts found for this workspace")
    
    print()
    
    # Show context restoration options
    if workspace_contexts:
        # Get details about the most recent context
        latest_context_display = workspace_contexts[0]  # This now includes timestamp
        
        # Find the actual latest file by scanning files directly
        context_path = os.path.join(get_cns_path(), "cns", "memory", "context")
        workspace_files = []
        
        for context_file in glob.glob(os.path.join(context_path, "*.md")):
            try:
                with open(context_file, 'r') as f:
                    content = f.read()
                    if f'**Current Workspace**: {current_workspace}' in content:
                        # Get file modification time
                        mod_time = os.path.getmtime(context_file)
                        workspace_files.append((context_file, mod_time))
            except:
                pass
        
        # Sort by modification time, newest first
        workspace_files.sort(key=lambda x: x[1], reverse=True)
        latest_file = workspace_files[0][0] if workspace_files else None
        
        start_time = "unknown"
        activities_count = 0
        
        if latest_file:
            try:
                with open(latest_file, 'r') as f:
                    content = f.read()
                    lines = content.split('\n')
                    
                    # Extract session info - prefer Last Updated over Start Time
                    for line in lines[:20]:
                        if '**Last Updated**:' in line:
                            start_time = line.split(':', 1)[1].strip()
                            break
                        elif '**Start Time**:' in line:
                            start_time = line.split(':', 1)[1].strip()
                    
                    # Count activities
                    for line in lines:
                        if line.strip().startswith('- ✅') or line.strip().startswith('✅'):
                            activities_count += 1
            except:
                pass
        
        print("🔄 CONTEXT RESTORATION:")
        print(f"   1. Latest context: '{latest_context_display}'")
        print(f"   2. Last used: {start_time}")
        print(f"   3. Contains: {activities_count} completed activities")
        print()
        print("⚠️  WORKSPACE CONFIRMATION REQUIRED:")
        print(f"   Detected workspace: {current_workspace}")
        print("   Assistant will confirm workspace BEFORE context restoration")
        print()
        print("📝 CONTEXT OPTIONS (after workspace confirmation):")
        print("   1. Answer 'yes' to restore the latest context and continue previous work")
        print("   2. Answer 'no' to start fresh (assistant will ask for new context name)")
        print("   3. Provide specific context name to restore different context")
    else:
        print("⚠️  WORKSPACE CONFIRMATION REQUIRED:")
        print(f"   Detected workspace: {current_workspace}")
        print("   Assistant will confirm workspace BEFORE creating context")
        print()
        print("📝 FRESH START:")
        print("   No previous context files found for this workspace.")
        print("   Assistant will ask for a new context name to begin session tracking.")

def cleanup_old_contexts(keep_per_context_name=3):
    """Clean up old context files, keeping only the most recent N per context name"""
    context_path = os.path.join(get_cns_path(), "cns", "memory", "context")
    
    if not os.path.exists(context_path):
        return
    
    # Get all context files
    context_files = glob.glob(os.path.join(context_path, "*.md"))
    
    # Group context files by context name
    context_groups = {}
    
    for context_file in context_files:
        filename = os.path.basename(context_file).replace('.md', '')
        
        # Extract context name from filename
        context_name = "unknown"
        
        if filename.startswith('context-') and filename.count('-') >= 4:
            # Old format: context-YYYY-MM-DD-HHMMSS-workspace.md
            parts = filename.split('-')
            if len(parts) >= 5:
                context_name = '-'.join(parts[4:])  # Everything after timestamp
        else:
            # New format: [context-name]-YYYY-MM-DD-HHMMSS.md
            import re
            match = re.search(r'^(.+?)-(\d{4}-\d{2}-\d{2}-\d{6})$', filename)
            if match:
                context_name = match.group(1)
        
        if context_name not in context_groups:
            context_groups[context_name] = []
        context_groups[context_name].append(context_file)
    
    # Clean up old files for each context name
    total_deleted = 0
    for context_name, files in context_groups.items():
        if len(files) > keep_per_context_name:
            # Sort by filename (timestamp) and keep only the most recent N
            files.sort(reverse=True)  # Newest first
            files_to_delete = files[keep_per_context_name:]
            
            for file_to_delete in files_to_delete:
                try:
                    os.remove(file_to_delete)
                    total_deleted += 1
                except Exception as e:
                    print(f"Warning: Could not delete {os.path.basename(file_to_delete)}: {e}")
    
    if total_deleted > 0:
        print(f"🧹 Cleaned up {total_deleted} old context files (keeping {keep_per_context_name} per context name)")

def get_learning_application(learning):
    """Get application description for a learning entry - VERBATIM, NO TRUNCATION"""
    # Extract learning summary from episodic learning files
    try:
        with open(learning['path'], 'r') as f:
            content = f.read()
            lines = content.split('\n')
            
            # Look for ## Summary section first
            summary_content = ""
            in_summary = False
            
            for i, line in enumerate(lines):
                if line.strip() == '## Summary':
                    in_summary = True
                    continue
                elif in_summary:
                    if line.startswith('## ') and line.strip() != '## Summary':
                        # Hit next section, stop
                        break
                    elif line.strip():  # Non-empty line
                        summary_content += line.strip() + " "
            
            # Return full summary content verbatim (NO TRUNCATION)
            if summary_content:
                return summary_content.strip()
            
            # Second priority: Look for ## Learning Content section
            learning_content = ""
            in_learning_content = False
            
            for i, line in enumerate(lines):
                if line.strip() == '## Learning Content':
                    in_learning_content = True
                    continue
                elif in_learning_content:
                    if line.startswith('## ') and line.strip() != '## Learning Content':
                        # Hit next section, stop
                        break
                    elif line.strip():  # Non-empty line
                        learning_content += line.strip() + " "
            
            # Return full learning content verbatim (NO TRUNCATION)
            if learning_content:
                return learning_content.strip()
            
            # Third priority: Look for ## Context section
            context_content = ""
            in_context = False
            
            for i, line in enumerate(lines):
                if line.strip() == '## Context':
                    in_context = True
                    continue
                elif in_context:
                    if line.startswith('## ') and line.strip() != '## Context':
                        # Hit next section, stop
                        break
                    elif line.strip():  # Non-empty line
                        context_content += line.strip() + " "
            
            # Return full context content verbatim (NO TRUNCATION)
            if context_content:
                return context_content.strip()
            
            # Final fallback: Extract title and try to make it meaningful
            title = ""
            if lines and lines[0].startswith('# '):
                title = lines[0].replace('# ', '').strip()
                
                # Remove generic "Learning: " prefix and date suffix
                if title.startswith('Learning: '):
                    title = title.replace('Learning: ', '')
                if ' - 20' in title:
                    title = title.split(' - 20')[0]
                
                if title and title != "Critical Learning Captured":
                    return title
                
    except Exception as e:
        pass
    
    # Fallback to using the summary from learning loading
    summary = learning.get('summary', '')
    
    # If we have a meaningful summary that's not generic, use it verbatim
    if summary and not summary.startswith('Learning about') and len(summary) > 20:
        # Clean up and format the summary for display (but don't truncate)
        if summary.endswith('...'):
            summary = summary[:-3]
        return summary
    
    # Final fallback: use activity name in a more natural format
    activity = learning.get('activity', 'Unknown Learning').replace('-', ' ').title()
    return f"{activity}"

def run_user_pattern_learning():
    """Run user pattern learning after startup sequence"""
    try:
        import sys
        cns_brain_path = os.path.join(get_cns_path(), "cns", "brain")
        if cns_brain_path not in sys.path:
            sys.path.append(cns_brain_path)
        
        from user_pattern_learner import main as run_pattern_learning
        
        # Run user pattern learning - will only activate for new workspaces
        pattern_learning_result = run_pattern_learning()
        
        if pattern_learning_result:
            print("🧠 User patterns updated! Changes will be active in next CNS session.")
            print()
        
    except ImportError:
        # Pattern learning is optional - don't break startup if module unavailable
        pass
    except Exception as e:
        # Pattern learning is optional - don't break startup if it fails
        print(f"🤔 User pattern learning error: {e}")
        print()

if __name__ == "__main__":
    display_startup_sequence()
    
    # Run user pattern learning after the main startup sequence
    run_user_pattern_learning()