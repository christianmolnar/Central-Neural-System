# Prompt Engineering Strategies

## Context-Aware Prompt Creation

### User Pattern Integration
- **Strategy**: Incorporate learned user preferences into all prompts
- **Implementation**: Reference user-patterns.md for communication style, coding preferences
- **Template Variables**: user_communication_style, preferred_code_patterns, quality_standards
- **Success Metrics**: Response alignment with user expectations

### Session Context Integration
- **Strategy**: Include relevant context from current and previous sessions
- **Implementation**: Reference current context file and relevant episodic memory
- **Template Variables**: session_context, previous_learnings, ongoing_tasks
- **Success Metrics**: Context continuity and task progression

## Task-Specific Prompt Engineering

### Code Analysis Prompts
**Template**:
```
Analyze this code considering the following context:
- User coding style: {user_style_preferences}
- Project patterns: {established_patterns}
- Quality requirements: {quality_standards}
- Current task: {task_context}

Code to analyze:
{code_content}

Focus on:
1. Alignment with established patterns
2. Quality and maintainability
3. Security considerations
4. Performance implications
```

**Variables**: user_style_preferences, established_patterns, quality_standards, task_context, code_content
**Success Metrics**: Accurate analysis, actionable recommendations

### Documentation Creation Prompts
**Template**:
```
Create documentation for {documentation_type} with these requirements:
- Audience: {target_audience}
- Style: {user_communication_preferences}
- Format: {format_requirements}
- Context: {project_context}

Content to document:
{content_to_document}

Structure requirements:
- Clear, concise sections
- Actionable information
- Follow established documentation patterns
- Include necessary technical details without verbosity
```

**Variables**: documentation_type, target_audience, user_communication_preferences, format_requirements, project_context, content_to_document
**Success Metrics**: Documentation clarity, completeness, user satisfaction

### Problem-Solving Prompts
**Template**:
```
Solve this problem using established methodology:
- Problem: {problem_description}
- Context: {problem_context}
- Constraints: {constraints}
- Success criteria: {success_criteria}
- Previous similar solutions: {episodic_patterns}

Apply these approaches:
1. Evidence-based analysis
2. Pattern recognition from previous successes
3. Quality-first implementation
4. User preference alignment

Provide solution with implementation steps.
```

**Variables**: problem_description, problem_context, constraints, success_criteria, episodic_patterns
**Success Metrics**: Solution effectiveness, implementation clarity

## Memory-Enhanced Prompt Strategies

### Episodic Memory Integration
- **Strategy**: Include relevant successful patterns from previous experiences
- **Implementation**: Query episodic.md for similar scenarios and successful outcomes
- **Prompt Enhancement**: Add "Based on previous successful pattern: {pattern_description}"
- **Success Metrics**: Higher success rate through pattern reuse

### Semantic Knowledge Application
- **Strategy**: Leverage accumulated domain knowledge in prompts
- **Implementation**: Reference semantic.md for relevant best practices and knowledge
- **Prompt Enhancement**: Include "Applying established knowledge: {relevant_knowledge}"
- **Success Metrics**: More informed and accurate responses

### Procedural Memory Integration
- **Strategy**: Follow established workflows and procedures in prompts
- **Implementation**: Reference procedural.md for relevant workflow steps
- **Prompt Enhancement**: Structure prompts to follow proven procedural patterns
- **Success Metrics**: Consistent workflow execution and quality

## Quality-Assured Prompt Engineering

### Validation Prompt Templates
**Template**:
```
Validate this {output_type} against these criteria:
- Technical accuracy: {accuracy_requirements}
- User preference alignment: {user_preferences}
- Quality standards: {quality_thresholds}
- Methodology compliance: {golden_rules_applicable}

Output to validate:
{output_to_validate}

Provide:
1. Validation results for each criterion
2. Specific issues identified
3. Recommended improvements
4. Overall quality assessment
```

**Variables**: output_type, accuracy_requirements, user_preferences, quality_thresholds, golden_rules_applicable, output_to_validate
**Success Metrics**: Accurate validation, actionable feedback

### Error Analysis Prompts
**Template**:
```
Analyze this error and provide resolution:
- Error: {error_description}
- Context: {error_context}
- Previous similar errors: {error_patterns}
- Available resources: {available_tools}

Analysis requirements:
1. Root cause identification
2. Step-by-step resolution
3. Prevention measures
4. Learning integration for future

Provide comprehensive error resolution plan.
```

**Variables**: error_description, error_context, error_patterns, available_tools
**Success Metrics**: Effective error resolution, prevention measures

## Adaptive Prompt Refinement

### Success Pattern Recognition
- **Process**: Analyze successful prompt outcomes and extract effective patterns
- **Documentation**: Update episodic.md with successful prompt strategies
- **Application**: Incorporate successful patterns into future prompts
- **Metrics**: Improved success rate over time

### Failure Pattern Learning
- **Process**: Analyze unsuccessful prompts and identify improvement opportunities
- **Documentation**: Record failures and improvements in episodic.md
- **Application**: Avoid failed patterns and apply learned improvements
- **Metrics**: Reduced error rate and improved outcomes

### User Feedback Integration
- **Process**: Incorporate user feedback into prompt refinement
- **Documentation**: Update user-patterns.md with feedback-based preferences
- **Application**: Adjust prompt style and content based on user responses
- **Metrics**: Higher user satisfaction and preference alignment

## Integration-Specific Prompts

### API Integration Prompts
- **Focus**: Configuration validation, error handling, response processing
- **Context**: API-specific requirements and user configuration preferences
- **Quality**: Robust error handling and user communication

### File Operation Prompts
- **Focus**: Path validation, content accuracy, edit precision
- **Context**: Project structure and user file organization preferences
- **Quality**: Safe operations with proper validation

### Context Management Prompts
- **Focus**: Context continuity, session handoff, learning integration
- **Context**: Previous sessions and ongoing task context
- **Quality**: Comprehensive context maintenance and accurate handoff

**Last Updated**: 2025-10-23T14:15:00Z