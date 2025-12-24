#!/usr/bin/env python3
"""
User Pattern Learning System
Identifies user behavior patterns and proposes updates to user-patterns.md
"""

import os
import json
import glob
from datetime import datetime, timedelta
from pathlib import Path
import re

def get_cns_path():
    """Get the ~/.personal-cns directory path"""
    return os.path.expanduser("~/.personal-cns")

def is_new_workspace():
    """Detect if this is a new CNS installation with minimal learning history"""
    
    # Check if CNS was recently installed (within last 7 days)
    cns_path = os.path.join(get_cns_path(), "cns", "startup-sequence.py")
    if os.path.exists(cns_path):
        install_time = datetime.fromtimestamp(os.path.getctime(cns_path))
        if datetime.now() - install_time < timedelta(days=7):
            return True
    
    # Check if learning files are minimal (less than 3 files) 
    episodic_path = os.path.join(get_cns_path(), "cns", "memory", "episodic")
    if os.path.exists(episodic_path):
        learning_files = glob.glob(os.path.join(episodic_path, "*.md"))
        if len(learning_files) < 3:
            return True
    
    return False

def analyze_recent_interactions(days_back=7):
    """Analyze recent episodic learnings for user behavior patterns"""
    
    episodic_path = os.path.join(get_cns_path(), "cns", "memory", "episodic")
    if not os.path.exists(episodic_path):
        return []
    
    cutoff_date = datetime.now() - timedelta(days=days_back)
    patterns = []
    
    learning_files = glob.glob(os.path.join(episodic_path, "learning-*.md"))
    
    for file_path in learning_files:
        try:
            # Check file age
            file_time = datetime.fromtimestamp(os.path.getmtime(file_path))
            if file_time < cutoff_date:
                continue
            
            with open(file_path, 'r') as f:
                content = f.read()
            
            # Extract patterns from learning content
            detected_patterns = extract_patterns_from_learning(content, file_time)
            patterns.extend(detected_patterns)
            
        except Exception as e:
            print(f"Error analyzing {file_path}: {e}")
            continue
    
    return consolidate_patterns(patterns)

def extract_patterns_from_learning(content, timestamp):
    """Extract behavioral patterns from learning file content"""
    
    patterns = []
    lines = content.split('\n')
    
    # Pattern 1: Communication Style
    communication_indicators = {
        'concise': ['brief', 'short', 'concise', 'direct', 'minimal'],
        'detailed': ['detailed', 'comprehensive', 'thorough', 'complete'],
        'technical': ['technical', 'precise', 'specific', 'exact'],
        'collaborative': ['discuss', 'review', 'feedback', 'collaborate']
    }
    
    for style, indicators in communication_indicators.items():
        count = sum(1 for line in lines for indicator in indicators if indicator.lower() in line.lower())
        if count >= 3:  # Pattern threshold
            patterns.append({
                'category': 'communication',
                'pattern': f'prefers_{style}_communication',
                'confidence': min(count / 10.0, 1.0),
                'evidence': f"Used {style} communication indicators {count} times",
                'timestamp': timestamp
            })
    
    # Pattern 2: Workflow Preferences  
    workflow_patterns = {
        'step_by_step': r'step \d|first.*then|next.*step',
        'todo_driven': r'todo|task.*list|checklist',
        'testing_focused': r'test.*first|verify.*before|check.*that',
        'documentation_heavy': r'document.*this|add.*documentation|update.*docs'
    }
    
    content_lower = content.lower()
    for pattern_name, regex_pattern in workflow_patterns.items():
        matches = re.findall(regex_pattern, content_lower)
        if len(matches) >= 2:
            patterns.append({
                'category': 'workflow',
                'pattern': pattern_name,
                'confidence': min(len(matches) / 5.0, 1.0),
                'evidence': f"Found {len(matches)} instances of {pattern_name} behavior",
                'timestamp': timestamp
            })
    
    # Pattern 3: Quality Standards
    quality_indicators = {
        'high_standards': ['green.*test', 'lint.*check', 'verify.*quality', 'thorough.*review'],
        'security_conscious': ['secret', 'security', 'permission', 'auth'],
        'performance_aware': ['performance', 'optimize', 'efficient', 'fast']
    }
    
    for standard, indicators in quality_indicators.items():
        count = sum(1 for line in lines for indicator in indicators 
                   if re.search(indicator, line.lower()))
        if count >= 2:
            patterns.append({
                'category': 'quality',
                'pattern': standard,
                'confidence': min(count / 4.0, 1.0),
                'evidence': f"Demonstrated {standard} in {count} instances",
                'timestamp': timestamp
            })
    
    return patterns

def consolidate_patterns(patterns):
    """Consolidate similar patterns and calculate overall confidence"""
    
    consolidated = {}
    
    for pattern in patterns:
        key = f"{pattern['category']}_{pattern['pattern']}"
        
        if key not in consolidated:
            consolidated[key] = {
                'category': pattern['category'],
                'pattern': pattern['pattern'],
                'total_confidence': 0,
                'occurrences': 0,
                'evidence_list': [],
                'first_seen': pattern['timestamp'],
                'last_seen': pattern['timestamp']
            }
        
        cons = consolidated[key]
        cons['total_confidence'] += pattern['confidence']
        cons['occurrences'] += 1
        cons['evidence_list'].append(pattern['evidence'])
        cons['last_seen'] = max(cons['last_seen'], pattern['timestamp'])
    
    # Calculate final confidence scores and filter
    final_patterns = []
    for key, pattern in consolidated.items():
        avg_confidence = pattern['total_confidence'] / pattern['occurrences']
        
        # Only include patterns with reasonable confidence and frequency
        if avg_confidence >= 0.3 and pattern['occurrences'] >= 3:
            pattern['confidence'] = avg_confidence
            final_patterns.append(pattern)
    
    # Sort by confidence 
    final_patterns.sort(key=lambda x: x['confidence'], reverse=True)
    
    return final_patterns[:5]  # Top 5 most confident patterns

def generate_user_pattern_suggestions(patterns):
    """Generate specific user-patterns.md suggestions from detected patterns"""
    
    suggestions = []
    
    for pattern in patterns:
        category = pattern['category']
        pattern_type = pattern['pattern']
        confidence = pattern['confidence']
        
        if category == 'communication':
            if pattern_type == 'prefers_concise_communication':
                suggestions.append({
                    'section': 'Communication Preferences',
                    'suggested_addition': '- **Response Style**: Prefers concise, direct responses without verbose explanations',
                    'confidence': confidence,
                    'rationale': f"Detected concise communication preference with {confidence:.0%} confidence"
                })
            elif pattern_type == 'prefers_technical_communication':
                suggestions.append({
                    'section': 'Communication Preferences', 
                    'suggested_addition': '- **Technical Detail**: Prefers precise technical language and specific implementation details',
                    'confidence': confidence,
                    'rationale': f"Detected technical communication preference with {confidence:.0%} confidence"
                })
        
        elif category == 'workflow':
            if pattern_type == 'todo_driven':
                suggestions.append({
                    'section': 'Workflow Patterns',
                    'suggested_addition': '- **Task Management**: Strongly prefers structured todo lists and step-by-step tracking',
                    'confidence': confidence,
                    'rationale': f"Detected todo-driven workflow with {confidence:.0%} confidence"
                })
            elif pattern_type == 'testing_focused':
                suggestions.append({
                    'section': 'Workflow Patterns',
                    'suggested_addition': '- **Quality Assurance**: Always verify and test before proceeding to next steps',
                    'confidence': confidence,
                    'rationale': f"Detected testing-first approach with {confidence:.0%} confidence"
                })
        
        elif category == 'quality':
            if pattern_type == 'high_standards':
                suggestions.append({
                    'section': 'Project Preferences',
                    'suggested_addition': '- **Quality Gates**: Insists on green tests, lint checks, and thorough reviews',
                    'confidence': confidence,
                    'rationale': f"Detected high quality standards with {confidence:.0%} confidence"
                })
    
    return suggestions

def interactive_pattern_update(suggestions):
    """Interactive flow to get user feedback on pattern suggestions"""
    
    if not suggestions:
        return []
    
    print("\n🔍 CNS PATTERN RECOGNITION")
    print("=" * 50)
    print("I've analyzed your recent interactions and identified some behavioral patterns.")
    print("Would you like to review and add these to your CNS user patterns?\n")
    
    approved_updates = []
    
    for i, suggestion in enumerate(suggestions, 1):
        print(f"📋 Pattern {i}/{len(suggestions)}: {suggestion['section']}")
        print(f"   Suggested Addition: {suggestion['suggested_addition']}")
        print(f"   Confidence: {suggestion['confidence']:.0%}")
        print(f"   Rationale: {suggestion['rationale']}")
        print()
        
        while True:
            response = input("   Add this pattern? (y)es / (n)o / (e)dit / (s)kip all: ").lower().strip()
            
            if response in ['y', 'yes']:
                approved_updates.append(suggestion)
                print("   ✅ Pattern approved for addition\n")
                break
            elif response in ['n', 'no']:
                print("   ❌ Pattern discarded\n")
                break
            elif response in ['e', 'edit']:
                print("   Current suggestion:")
                print(f"   {suggestion['suggested_addition']}")
                new_text = input("   Enter your preferred version: ").strip()
                if new_text:
                    suggestion['suggested_addition'] = new_text
                    approved_updates.append(suggestion)
                    print("   ✅ Edited pattern approved\n")
                else:
                    print("   ❌ No text entered, pattern discarded\n")
                break
            elif response in ['s', 'skip', 'skip all']:
                print("   ⏭️  Skipping all remaining patterns\n")
                return approved_updates
            else:
                print("   Please enter 'y', 'n', 'e', or 's'")
    
    return approved_updates

def apply_pattern_updates(approved_updates):
    """Apply approved pattern updates to user-patterns.md"""
    
    if not approved_updates:
        return
    
    user_patterns_path = os.path.join(get_cns_path(), "cns", "brain", "user-patterns.md")
    
    if not os.path.exists(user_patterns_path):
        print("❌ user-patterns.md not found")
        return
    
    # Read current content
    with open(user_patterns_path, 'r') as f:
        content = f.read()
    
    # Apply updates section by section
    updated_content = content
    
    for update in approved_updates:
        section = update['section']
        addition = update['suggested_addition']
        
        # Find the section in the content
        section_pattern = f"## {section}"
        if section_pattern in updated_content:
            # Find the end of the section
            lines = updated_content.split('\n')
            section_start = -1
            
            for i, line in enumerate(lines):
                if line.strip() == section_pattern:
                    section_start = i
                    break
            
            if section_start != -1:
                # Find next section or end of content
                next_section = len(lines)
                for i in range(section_start + 1, len(lines)):
                    if lines[i].startswith('## ') and lines[i] != section_pattern:
                        next_section = i
                        break
                
                # Insert the new pattern
                lines.insert(next_section, addition)
                updated_content = '\n'.join(lines)
    
    # Update timestamp
    updated_content = re.sub(
        r'\*\*Last Updated\*\*:.*',
        f"**Last Updated**: {datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')}",
        updated_content
    )
    
    # Write back
    with open(user_patterns_path, 'w') as f:
        f.write(updated_content)
    
    print(f"✅ Updated user-patterns.md with {len(approved_updates)} new patterns")

def main():
    """Main user pattern learning function"""
    
    # Only run pattern learning if this appears to be a new workspace
    if not is_new_workspace():
        return False  # No new patterns detected
    
    print("🧠 Analyzing user behavior patterns...")
    
    # Analyze recent interactions
    patterns = analyze_recent_interactions(days_back=14)  # Look back 2 weeks for new workspaces
    
    if not patterns:
        return False  # No patterns detected
    
    # Generate suggestions
    suggestions = generate_user_pattern_suggestions(patterns)
    
    if not suggestions:
        return False  # No actionable suggestions
    
    # Interactive update process
    approved_updates = interactive_pattern_update(suggestions)
    
    if approved_updates:
        apply_pattern_updates(approved_updates)
        return True
    
    return False

if __name__ == "__main__":
    success = main()
    if success:
        print("🎉 User pattern learning completed successfully!")
    else:
        print("💭 No new user patterns detected at this time.")