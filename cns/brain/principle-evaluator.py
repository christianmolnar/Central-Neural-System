#!/usr/bin/env python3
"""
Prime Principle Evaluation Framework
Analyzes learning patterns and evaluates principle validity
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

def load_prime_principles():
    """Load current prime principles from CNS brain"""
    principles_path = os.path.join(get_cns_path(), "cns", "brain", "prime-principles.md")
    
    if not os.path.exists(principles_path):
        return []
    
    with open(principles_path, 'r') as f:
        content = f.read()
    
    principles = []
    lines = content.split('\n')
    current_principle = None
    
    for line in lines:
        if line.startswith('### ') and '. ' in line:
            if current_principle:
                principles.append(current_principle)
            
            # Extract principle number and title
            title = line.replace('### ', '').strip()
            current_principle = {
                'title': title,
                'content': [],
                'validation_status': 'Unknown',
                'last_validated': None,
                'confidence': 'Unknown'
            }
        elif current_principle and line.strip():
            if line.startswith('**Validation Status**:'):
                current_principle['validation_status'] = line.split(':', 1)[1].strip()
            elif line.startswith('**Last Validated**:'):
                current_principle['last_validated'] = line.split(':', 1)[1].strip()
            elif line.startswith('**Confidence**:'):
                current_principle['confidence'] = line.split(':', 1)[1].strip()
            elif not line.startswith('**') and not line.strip() == '---':
                current_principle['content'].append(line.strip())
    
    if current_principle:
        principles.append(current_principle)
    
    return principles

def load_all_learnings(days_back=90):
    """Load all learning entries from the specified time period"""
    episodic_path = os.path.join(get_cns_path(), "cns", "memory", "episodic")
    
    if not os.path.exists(episodic_path):
        return []
    
    # Get cutoff date
    cutoff_date = datetime.now() - timedelta(days=days_back)
    
    learnings = []
    learning_files = glob.glob(os.path.join(episodic_path, "*.md"))
    
    for file_path in learning_files:
        try:
            # Check file modification time
            file_time = datetime.fromtimestamp(os.path.getmtime(file_path))
            if file_time < cutoff_date:
                continue
            
            with open(file_path, 'r') as f:
                content = f.read()
            
            filename = os.path.basename(file_path)
            
            # Extract learning metadata
            learning = {
                'filename': filename,
                'path': file_path,
                'content': content,
                'date': file_time,
                'activity': extract_activity_from_filename(filename),
                'patterns': extract_patterns_from_content(content),
                'principle_references': find_principle_references(content)
            }
            
            learnings.append(learning)
            
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            continue
    
    return sorted(learnings, key=lambda x: x['date'], reverse=True)

def extract_activity_from_filename(filename):
    """Extract activity name from learning filename"""
    if filename.startswith('learning-'):
        # Format: learning-YYYY-MM-DD-activity-name.md
        parts = filename.replace('.md', '').split('-')
        if len(parts) >= 4:
            return '-'.join(parts[4:])
    
    return filename.replace('.md', '').replace('-', ' ').title()

def extract_patterns_from_content(content):
    """Extract key patterns and insights from learning content"""
    patterns = []
    
    # Look for key sections
    lines = content.split('\n')
    current_section = None
    
    for line in lines:
        line = line.strip()
        
        if line.startswith('# ') or line.startswith('## '):
            current_section = line.replace('#', '').strip().lower()
        elif current_section in ['what went well', 'what didn\'t work', 'what to do differently', 'key learning']:
            if line.startswith('- ') or line.startswith('* '):
                patterns.append({
                    'section': current_section,
                    'insight': line[2:].strip(),
                    'type': classify_insight_type(line[2:].strip())
                })
    
    return patterns

def classify_insight_type(insight):
    """Classify the type of insight for pattern detection"""
    insight_lower = insight.lower()
    
    if any(word in insight_lower for word in ['interface', 'display', 'output', 'ui']):
        return 'interface'
    elif any(word in insight_lower for word in ['architecture', 'design', 'structure']):
        return 'architecture' 
    elif any(word in insight_lower for word in ['process', 'workflow', 'methodology']):
        return 'process'
    elif any(word in insight_lower for word in ['startup', 'initialization', 'loading']):
        return 'startup'
    elif any(word in insight_lower for word in ['context', 'memory', 'continuity']):
        return 'context'
    else:
        return 'general'

def find_principle_references(content):
    """Find references to principles in learning content"""
    references = []
    
    # Look for principle-related keywords
    principle_keywords = [
        'source control', 'ci', 'pr', 'merge',
        'change hygiene', 'commit', 'changelog', 
        'jira', 'confluence', 'integration',
        'methodology', 'documentation',
        'secrets', 'safety', 'security',
        'context continuity', 'session',
        'self-evaluation', 'learning'
    ]
    
    content_lower = content.lower()
    for keyword in principle_keywords:
        if keyword in content_lower:
            references.append(keyword)
    
    return references

def analyze_principle_validity(principles, learnings):
    """Analyze each principle's validity based on recent learnings"""
    evaluations = []
    
    for principle in principles:
        evaluation = {
            'principle': principle,
            'status': 'active',
            'confidence': 'high',
            'supporting_evidence': [],
            'contradicting_evidence': [],
            'proposed_changes': [],
            'last_referenced': None
        }
        
        # Analyze learnings for this principle
        for learning in learnings:
            if principle_mentioned_in_learning(principle, learning):
                evaluation['last_referenced'] = learning['date']
                
                # Check if learning supports or contradicts principle
                support_level = assess_learning_support(principle, learning)
                
                if support_level > 0:
                    evaluation['supporting_evidence'].append({
                        'learning': learning['filename'],
                        'evidence': extract_relevant_evidence(principle, learning),
                        'strength': support_level
                    })
                elif support_level < 0:
                    evaluation['contradicting_evidence'].append({
                        'learning': learning['filename'],
                        'evidence': extract_relevant_evidence(principle, learning),
                        'strength': abs(support_level)
                    })
        
        # Determine overall status
        if evaluation['contradicting_evidence']:
            evaluation['status'] = 'under_review'
            evaluation['confidence'] = 'medium'
        elif not evaluation['supporting_evidence'] and not evaluation['last_referenced']:
            evaluation['status'] = 'unused'
            evaluation['confidence'] = 'low'
        
        evaluations.append(evaluation)
    
    return evaluations

def principle_mentioned_in_learning(principle, learning):
    """Check if a principle is mentioned or relevant to a learning"""
    principle_text = ' '.join(principle['content']).lower()
    learning_text = learning['content'].lower()
    
    # Check for keyword overlap
    principle_keywords = extract_keywords(principle_text)
    
    for keyword in principle_keywords:
        if keyword in learning_text:
            return True
    
    return False

def extract_keywords(text):
    """Extract key terms from principle text"""
    # Simple keyword extraction - could be enhanced
    keywords = []
    
    # Common technical terms
    technical_terms = re.findall(r'\b[A-Z][A-Za-z]+\b', text)  # Capitalized words
    keywords.extend([term.lower() for term in technical_terms])
    
    # Important phrases
    important_phrases = ['source control', 'change hygiene', 'jira', 'confluence', 'secrets', 'documentation']
    for phrase in important_phrases:
        if phrase in text.lower():
            keywords.append(phrase)
    
    return list(set(keywords))

def assess_learning_support(principle, learning):
    """Assess how much a learning supports (+) or contradicts (-) a principle"""
    # This is a simplified assessment - could use ML/NLP for better analysis
    
    principle_text = ' '.join(principle['content']).lower()
    learning_text = learning['content'].lower()
    
    support_score = 0
    
    # Look for positive indicators
    positive_indicators = ['worked well', 'successful', 'improved', 'effective', 'better']
    negative_indicators = ['failed', 'didn\'t work', 'problem', 'issue', 'worse']
    
    for pattern in learning['patterns']:
        insight = pattern['insight'].lower()
        
        # Check if insight relates to this principle
        if any(keyword in insight for keyword in extract_keywords(principle_text)):
            if any(pos in insight for pos in positive_indicators):
                support_score += 1
            elif any(neg in insight for neg in negative_indicators):
                support_score -= 1
    
    return support_score

def extract_relevant_evidence(principle, learning):
    """Extract the specific evidence from learning that relates to principle"""
    evidence = []
    
    for pattern in learning['patterns']:
        insight = pattern['insight']
        
        # Check if this insight relates to the principle
        if any(keyword in insight.lower() for keyword in extract_keywords(' '.join(principle['content']))):
            evidence.append({
                'section': pattern['section'],
                'insight': insight,
                'type': pattern['type']
            })
    
    return evidence

def detect_new_principle_candidates(learnings):
    """Analyze learning patterns to identify potential new principles"""
    
    # Group patterns by type and frequency
    pattern_frequency = {}
    pattern_examples = {}
    
    for learning in learnings:
        for pattern in learning['patterns']:
            pattern_type = pattern['type']
            insight = pattern['insight']
            
            if pattern_type not in pattern_frequency:
                pattern_frequency[pattern_type] = 0
                pattern_examples[pattern_type] = []
            
            pattern_frequency[pattern_type] += 1
            pattern_examples[pattern_type].append({
                'insight': insight,
                'learning': learning['filename'],
                'date': learning['date']
            })
    
    # Identify patterns that appear frequently
    candidates = []
    
    for pattern_type, frequency in pattern_frequency.items():
        if frequency >= 5:  # Increased threshold for principle quality
            examples = pattern_examples[pattern_type]
            
            # Analyze the examples for commonalities
            common_themes = extract_common_themes(examples)
            
            if common_themes and passes_principle_quality_gates(pattern_type, frequency, examples):
                candidates.append({
                    'type': pattern_type,
                    'frequency': frequency,
                    'themes': common_themes,
                    'examples': examples[:3],  # Top 3 examples
                    'proposed_principle': generate_principle_proposal(pattern_type, common_themes),
                    'quality_score': calculate_principle_quality_score(pattern_type, frequency, examples)
                })
    
    # Sort by quality score and limit candidates
    candidates.sort(key=lambda x: x['quality_score'], reverse=True)
    return candidates[:3]  # Maximum 3 new principles per evaluation

def extract_common_themes(examples):
    """Extract common themes from a set of learning examples"""
    # Simplified theme extraction
    all_text = ' '.join([ex['insight'] for ex in examples]).lower()
    
    # Look for repeated concepts
    common_words = {}
    words = re.findall(r'\b\w{4,}\b', all_text)  # Words 4+ chars
    
    for word in words:
        if word not in ['that', 'this', 'with', 'from', 'they', 'were', 'been', 'have']:
            common_words[word] = common_words.get(word, 0) + 1
    
    # Return most frequent meaningful words
    themes = [word for word, count in common_words.items() if count >= 2]
    return themes[:5]  # Top 5 themes

def generate_principle_proposal(pattern_type, themes):
    """Generate a proposed principle based on pattern analysis"""
    
    theme_text = ', '.join(themes)
    
    proposals = {
        'interface': f"Interface Design and User Experience: Ensure clear, consistent interface patterns. Focus on {theme_text}.",
        'architecture': f"System Architecture: Maintain clean, scalable architecture principles. Consider {theme_text}.",
        'process': f"Process Optimization: Streamline workflows and methodologies. Emphasize {theme_text}.",
        'startup': f"System Initialization: Ensure reliable, comprehensive startup procedures. Include {theme_text}.",
        'context': f"Context Management: Maintain comprehensive context and continuity. Focus on {theme_text}.",
        'general': f"General Best Practice: Establish consistent patterns for {theme_text}."
    }
    
    return proposals.get(pattern_type, f"New principle needed for {pattern_type}: {theme_text}")

def passes_principle_quality_gates(pattern_type, frequency, examples):
    """Apply strict quality gates for principle candidacy"""
    
    # Quality Gate 1: Minimum frequency threshold
    if frequency < 5:
        return False
    
    # Quality Gate 2: Must span multiple learning sessions (not just one activity)
    unique_learnings = set(ex['learning'] for ex in examples)
    if len(unique_learnings) < 3:
        return False
    
    # Quality Gate 3: Must span reasonable time period
    dates = [ex['date'] for ex in examples if 'date' in ex]
    if len(dates) >= 2:
        from datetime import timedelta
        date_span = max(dates) - min(dates)
        if date_span < timedelta(days=7):  # Must span at least a week
            return False
    
    # Quality Gate 4: Must be fundamental enough (not too specific)
    insight_texts = [ex['insight'].lower() for ex in examples]
    
    # Reject if too specific to one technology/tool
    specific_tools = ['jira', 'confluence', 'bitbucket', 'vscode', 'python', 'javascript']
    tool_mentions = sum(1 for insight in insight_texts for tool in specific_tools if tool in insight)
    if tool_mentions / len(insight_texts) > 0.7:  # More than 70% tool-specific
        return False
    
    # Quality Gate 5: Must represent behavioral/process patterns, not just technical details
    behavioral_indicators = ['workflow', 'process', 'approach', 'method', 'pattern', 'practice', 'habit']
    behavioral_score = sum(1 for insight in insight_texts for indicator in behavioral_indicators if indicator in insight)
    if behavioral_score / len(insight_texts) < 0.3:  # Less than 30% behavioral
        return False
    
    return True

def calculate_principle_quality_score(pattern_type, frequency, examples):
    """Calculate quality score for principle candidates"""
    score = 0
    
    # Frequency component (max 25 points)
    score += min(frequency * 3, 25)
    
    # Diversity component (max 25 points) 
    unique_learnings = len(set(ex['learning'] for ex in examples))
    score += min(unique_learnings * 5, 25)
    
    # Fundamentalness component (max 25 points)
    insight_texts = [ex['insight'].lower() for ex in examples]
    fundamental_keywords = ['always', 'never', 'consistent', 'systematic', 'principle', 'standard', 'approach']
    fundamental_score = sum(1 for insight in insight_texts for keyword in fundamental_keywords if keyword in insight)
    score += min(fundamental_score * 8, 25)
    
    # Pattern strength component (max 25 points)
    theme_consistency = len(extract_common_themes(examples))
    score += min(theme_consistency * 3, 25)
    
    return score

def enforce_principle_limits(current_principles, new_candidates):
    """Enforce soft maximum of 15 principles with quality prioritization"""
    MAX_PRINCIPLES = 15
    WARN_THRESHOLD = 12
    
    current_count = len(current_principles)
    
    if current_count >= MAX_PRINCIPLES:
        print(f"⚠️  Maximum principle limit reached ({MAX_PRINCIPLES})")
        print("   Consider consolidating or deprecating existing principles before adding new ones")
        return []
    
    available_slots = MAX_PRINCIPLES - current_count
    
    if current_count >= WARN_THRESHOLD:
        print(f"⚠️  Approaching principle limit ({current_count}/{MAX_PRINCIPLES})")
        print("   New principles must meet higher quality standards")
        # Apply stricter quality filtering
        high_quality_candidates = [c for c in new_candidates if c.get('quality_score', 0) >= 80]
        return high_quality_candidates[:available_slots]
    
    return new_candidates[:available_slots]

def generate_evaluation_report(principles, learnings, evaluations, candidates):
    """Generate a comprehensive evaluation report"""
    
    report = []
    report.append("# Prime Principle Evaluation Report")
    report.append(f"**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report.append(f"**Analysis Period**: Last 90 days")
    report.append(f"**Learnings Analyzed**: {len(learnings)}")
    report.append("")
    
    # Summary
    active_count = len([e for e in evaluations if e['status'] == 'active'])
    review_count = len([e for e in evaluations if e['status'] == 'under_review'])
    unused_count = len([e for e in evaluations if e['status'] == 'unused'])
    
    report.append("## Executive Summary")
    report.append(f"- **Active Principles**: {active_count}")
    report.append(f"- **Under Review**: {review_count}")
    report.append(f"- **Unused/Stale**: {unused_count}")
    report.append(f"- **New Candidates**: {len(candidates)}")
    report.append("")
    
    # Individual principle evaluations
    report.append("## Principle Evaluations")
    report.append("")
    
    for evaluation in evaluations:
        principle = evaluation['principle']
        report.append(f"### {principle['title']}")
        report.append(f"**Status**: {evaluation['status'].replace('_', ' ').title()}")
        report.append(f"**Confidence**: {evaluation['confidence'].title()}")
        
        if evaluation['last_referenced']:
            report.append(f"**Last Referenced**: {evaluation['last_referenced'].strftime('%Y-%m-%d')}")
        else:
            report.append("**Last Referenced**: Not found in recent learnings")
        
        if evaluation['supporting_evidence']:
            report.append(f"**Supporting Evidence**: {len(evaluation['supporting_evidence'])} instances")
            for evidence in evaluation['supporting_evidence'][:2]:  # Top 2
                report.append(f"  - {evidence['learning']}: {evidence['evidence'][0]['insight'] if evidence['evidence'] else 'General support'}")
        
        if evaluation['contradicting_evidence']:
            report.append(f"**Contradicting Evidence**: {len(evaluation['contradicting_evidence'])} instances")
            for evidence in evaluation['contradicting_evidence']:
                report.append(f"  - {evidence['learning']}: {evidence['evidence'][0]['insight'] if evidence['evidence'] else 'General contradiction'}")
        
        report.append("")
    
    # New principle candidates
    if candidates:
        report.append("## New Principle Candidates")
        report.append("")
        
        for candidate in candidates:
            report.append(f"### Proposed: {candidate['type'].title()} Principle")
            report.append(f"**Frequency**: {candidate['frequency']} occurrences")
            report.append(f"**Themes**: {', '.join(candidate['themes'])}")
            report.append(f"**Proposed Text**: {candidate['proposed_principle']}")
            report.append("**Supporting Examples**:")
            for example in candidate['examples']:
                report.append(f"  - {example['learning']}: {example['insight']}")
            report.append("")
    
    # Recommendations
    report.append("## Recommendations")
    report.append("")
    
    if review_count > 0:
        report.append("### Principles Requiring Review")
        for evaluation in evaluations:
            if evaluation['status'] == 'under_review':
                report.append(f"- **{evaluation['principle']['title']}**: Review conflicting evidence and update if necessary")
    
    if unused_count > 0:
        report.append("### Unused Principles")
        for evaluation in evaluations:
            if evaluation['status'] == 'unused':
                report.append(f"- **{evaluation['principle']['title']}**: Consider deprecation or find opportunities to apply")
    
    if candidates:
        report.append("### New Principles to Consider")
        for candidate in candidates:
            report.append(f"- **{candidate['type'].title()}**: {candidate['proposed_principle']}")
    
    return '\n'.join(report)

def main():
    """Main evaluation function"""
    print("🔍 PRIME PRINCIPLE EVALUATION STARTING...")
    print()
    
    # Load data
    print("📚 Loading prime principles...")
    principles = load_prime_principles()
    print(f"   Loaded {len(principles)} principles")
    
    print("🧠 Loading recent learnings...")
    learnings = load_all_learnings(90)  # Last 90 days
    print(f"   Loaded {len(learnings)} learning entries")
    print()
    
    # Perform analysis
    print("🔍 Analyzing principle validity...")
    evaluations = analyze_principle_validity(principles, learnings)
    
    print("🔍 Detecting new principle candidates...")
    raw_candidates = detect_new_principle_candidates(learnings)
    
    # Apply quality gates and limits
    print("🚪 Applying quality gates and principle limits...")
    candidates = enforce_principle_limits(principles, raw_candidates)
    
    # Generate report
    print("📊 Generating evaluation report...")
    report = generate_evaluation_report(principles, learnings, evaluations, candidates)
    
    # Print report instead of saving to file
    print("✅ Evaluation complete! Results:")
    print()
    print(report)
    print()
    
    # Summary output
    print("📊 EVALUATION SUMMARY:")
    active_count = len([e for e in evaluations if e['status'] == 'active'])
    review_count = len([e for e in evaluations if e['status'] == 'under_review'])
    unused_count = len([e for e in evaluations if e['status'] == 'unused'])
    
    print(f"   ✅ Active: {active_count}")
    print(f"   ⚠️  Under Review: {review_count}")
    print(f"   💤 Unused: {unused_count}")
    print(f"   🆕 New Candidates: {len(candidates)}")
    
    if review_count > 0 or candidates:
        print()
        print("⚠️  USER ATTENTION REQUIRED:")
        if review_count > 0:
            print(f"   - {review_count} principles need review")
        if candidates:
            print(f"   - {len(candidates)} new principle candidates identified")
        print(f"   - Review the full report output above")

if __name__ == "__main__":
    main()