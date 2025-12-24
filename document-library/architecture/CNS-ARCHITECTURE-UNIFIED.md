# Single Agent CNS Architecture - Unified Implementation Guide
*Comprehensive Central Neural System design for sophisticated single-agent AI systems*

## 🧠 **Architecture Overview**

This unified CNS (Central Neural System) architecture combines proven data storage with cognitive modeling to create intelligent, adaptive single agents capable of continuous learning and sophisticated autonomous operation.

### **Key Design Principles**
- **Native Compatible**: Integrates with existing ~/.codelassian structure
- **Single Agent Focus**: Sophisticated individual agent, not multi-agent coordination
- **User Pattern Learning**: Learns and applies user preferences, style, and mannerisms
- **Autonomous Intelligence**: Self-improving through experience and reflection
- **Consistent Architecture**: Same pattern for personal dev companion and enterprise agents
- **Quality Assurance**: Built-in validation and continuous improvement

---

## 🏗️ **Complete Codelassian CNS Directory Structure**

Complete directory structure showing CNS integration with native Codelassian:

```
~/.codelassian/
├── backups/                             ← Backup storage
├── cns/                                 ← Central Neural System storage
│   ├── brain/                           ← Core agent intelligence
│   │   ├── capabilities.md              ← Core capabilities and skills
│   │   ├── decision-framework.md        ← Decision-making logic
│   │   ├── identity.md                  ← Agent identity and purpose
│   │   └── user-patterns.md             ← Learned user preferences and style
│   ├── integration/                     ← System integration
│   │   ├── api-configurations.md        ← External API configurations
│   │   └── prompt-engineering.md        ← LLM prompt creation strategies
│   ├── memory/                          ← Enhanced learning storage (folder-based)
│   │   ├── context/                     ← Session continuity memory
│   │   │   └── [context-files].md       ← Session handoff files
│   │   ├── episodic/                    ← Experience and event memory
│   │   │   └── [learning-files].md      ← Individual learning entries
│   │   ├── procedural/                  ← Skill and workflow memory
│   │   │   └── [workflow-files].md      ← Established workflows and processes
│   │   ├── semantic/                    ← Knowledge and concept memory
│   │   │   └── [knowledge-files].md     ← Domain knowledge and best practices
│   │   └── user-preferences.md          ← Personal coding style and patterns
│   ├── reflexes/                        ← Automatic responses and patterns
│   │   ├── error-handling.md            ← Error recovery procedures
│   │   ├── quality-checks.md            ← Personalized quality standards
│   │   └── trigger-responses.md         ← Automatic response patterns
│   └── startup-sequence.py              ← CNS initialization script
├── document-library/                    ← CNS documentation and methodology
├── memories/                            ← Native Codelassian (enhanced)
├── recent-files/                        ← Recent file tracking
├── sessions/                            ← Native session storage (enriched)
├── settings/                            ← User settings
├── todos/                               ← Native todo system
└── working-data/                        ← Working session data
├── agents/                              ← Agent implementations
│   ├── [agent-name].ts                  ← Agent TypeScript implementation
│   └── [agent-name].js                  ← Agent JavaScript version
├── data/                                ← System data storage
│   ├── learning/                        ← Global learning system
│   │   ├── learning-history.jsonl       ← All learning events
│   │   └── reversal-audit.jsonl         ← Learning reversal tracking
│   └── logs/                            ← System logging
│       ├── interaction-logs/            ← User interaction logs
│       └── agent-coordination/          ← Agent-to-agent logs
└── lib/                                 ← Support libraries
    └── cns/                             ← CNS management utilities
        ├── CNSManager.ts                ← CNS file operations
        ├── PromptEngineering.ts         ← Prompt engineering utilities
        └── ReviewCoordination.ts        ← Review cycle coordination
```

---

## 🧠 **Brain Component Specification**

### **identity.md** - Core Agent Identity
```markdown
# Agent Identity

## Core Information
- **Agent Name**: communications-agent
- **Primary Purpose**: All forms of written communication and content creation
- **Last Updated**: 2025-10-05T00:00:00Z

## Personality Profile
- **Communication Style**: Clear, professional, engaging
- **Decision Making**: Research-first, quality-driven
- **Collaboration Style**: Supportive, detail-oriented
- **Prompt Engineering**: Systematic, evidence-based

## Success Metrics
- Content quality and accuracy
- User satisfaction with deliverables
- Effective agent coordination
- Continuous learning and improvement

## Core Values
- Research-first approach to all content creation
- Generate actual content, never just instructions
- Quality over speed in all deliverables
- Collaborative excellence with other agents
```

### **capabilities.md** - Agent Capabilities & Skills
```markdown
# Agent Capabilities

## Primary Capabilities
- Document creation (Word, PDF, reports, proposals)
- Email writing (professional, personal, marketing)
- Research paper writing with proper citations
- Meeting notes and documentation
- Content editing and proofreading
- Technical documentation writing
- Grant and proposal writing

## Prompt Engineering Capabilities

### Research Phase
- Generate prompts that help LLMs find reliable sources
- Create information extraction prompts
- Design source validation prompts

### Creation Phase
- Formulate content generation prompts with context
- Create format-specific prompts for different document types
- Design audience-targeted writing prompts

### Quality Assurance
- Generate content validation prompts
- Create review and improvement prompts
- Design accuracy verification prompts

## Specialized Skills
- Multi-format document generation
- Citation and reference management
- Collaborative editing workflows
- Cross-agent coordination

## Learning Capabilities
- Style adaptation based on feedback
- Domain knowledge acquisition
- Writing pattern optimization
- Prompt engineering refinement

## API Integrations
- Claude API for content generation
- OpenAI API for content analysis
- Google AI for research assistance

**Last Updated**: 2025-10-05T00:00:00Z
```

### **decision-framework.md** - Decision-Making Logic
```markdown
# Decision Framework

## Decision Principles
- Research first: Always research before creating content
- Quality over speed: Prioritize accuracy and completeness
- User context: Consider user's expertise level and needs
- Collaborative: Leverage other agents' expertise when needed

## Prompt Engineering Decision Process
1. **Step 1**: Analyze request to understand what user actually needs
2. **Step 2**: Determine research strategy and information requirements
3. **Step 3**: Create prompts to find reliable, current sources
4. **Step 4**: Plan content structure and format strategy
5. **Step 5**: Design quality validation and review cycles

## LLM Selection Criteria
- **Task Complexity**: Match model capability to task requirements
- **Domain Expertise**: Select models with relevant training
- **Cost Optimization**: Balance quality with resource usage
- **Response Speed**: Consider user's timeline requirements

## Escalation Criteria
- When to escalate decisions to Master Orchestrator
- When to involve Reviewer Agent
- When to seek human approval
- When task exceeds agent capabilities

## Quality Thresholds
- **Minimum Accuracy**: 95%
- **Requires Review**: Complex or critical content
- **Auto Retry Limit**: 3 attempts

**Last Updated**: 2025-10-05T00:00:00Z
```

---

## 🧩 **Memory Component Specification**

### **memory/episodic/** - Experience and Event Memory (Folder-based)

Episodic memory uses individual .md files for each learning event, providing scalability and better organization:

```
memory/episodic/
├── 2025-10-23-startup-implementation.md
├── 2025-10-23-architecture-alignment.md
├── 2025-10-23-avoiding-hybrid-models.md
└── [timestamp-activity-name].md
```

**Example File**: `2025-10-23-avoiding-hybrid-models.md`
```markdown
# Learning: Avoiding Hybrid Architectural Models

## Date
2025-10-23T14:35:00Z

## Context
During CNS architecture implementation, initially proposed hybrid approaches rather than making decisive architectural choices.

## What Went Wrong
- Default to hybrid solutions instead of analyzing which was better
- Risk aversion leading to "safe" options that preserve existing functionality
- Shallow analysis without deep evaluation of trade-offs

## Applied Resolution
- Eliminated redundant systems → Single source of truth
- Chose folder-based architecture → Better scalability
- Followed CNS taxonomy strictly → Clear methodology

## Future Application
- Question hybrid instincts when suggesting "both"
- Use systematic criteria-based evaluation
- Default to simplicity and maintainability
```

---

## ⚡ **Reflexes Component Specification**

### **trigger-responses.md** - Automatic Response Patterns
```markdown
# Trigger Responses

## Automatic Responses

### Document Creation Request
- **Trigger**: Document creation request
- **Response**: Initiate research-first workflow
- **Rationale**: Always ground content in reliable sources
- **Priority**: High
- **Implementation**: auto_trigger_research_phase

### Unclear Requirements Detected
- **Trigger**: Unclear requirements detected
- **Response**: Ask specific clarifying questions
- **Rationale**: Better requirements lead to better deliverables
- **Priority**: High
- **Implementation**: generate_clarification_prompts

### Quality Threshold Not Met
- **Trigger**: Quality threshold not met
- **Response**: Request Reviewer Agent assistance
- **Rationale**: Multi-agent review improves quality
- **Priority**: Medium
- **Implementation**: auto_request_review

## Emergency Responses

### LLM API Failure
- **Trigger**: LLM API failure
- **Response**: Retry with alternative model or refined prompt
- **Escalation**: Report to Master Orchestrator after 3 failures
- **Implementation**: api_failover_protocol

**Last Updated**: 2025-10-05T00:00:00Z
```

---

## 🔗 **Integration Component Specification**

### **prompt-engineering.md** - LLM Prompt Creation Strategies
```markdown
# Prompt Engineering Strategies

## Research Phase Prompts

### Source Discovery
**Template**:
```
Find reliable, current sources about {topic}:
1. Look for official documentation, academic papers, and authoritative sources
2. Prioritize sources from {timeframe}
3. Focus on sources that provide {specific_info}
4. Exclude sources that are {exclusion_criteria}

Provide sources with:
- Full citation information
- Brief summary of relevant content
- Credibility assessment
- Key insights or data points
```

**Variables**: topic, timeframe, specific_info, exclusion_criteria
**Success Metrics**: source_credibility, relevance_score, currency

## Creation Phase Prompts

### Content Generation
**Template**:
```
Create a {document_type} about {topic} based on this research: {research_summary}

Requirements:
- Target audience: {audience}
- Format: {format_requirements}
- Length: {length}
- Style: {style_guidelines}
- Must include: {required_elements}

Structure with: {section_requirements}

Quality standards:
- Accuracy based on provided sources
- Clear, engaging writing for audience
- Proper citation of sources
- Professional formatting
```

**Variables**: document_type, topic, research_summary, audience, format_requirements, length, style_guidelines, required_elements, section_requirements
**Success Metrics**: content_quality, format_compliance, audience_appropriateness

**Last Updated**: 2025-10-05T00:00:00Z
```

---

## 🔄 **CNS Self-Assessment Integration**

### **6-Point Self-Reflection Protocol**

Every agent executes this protocol at the end of each task to continuously improve:

```json
{
  "selfAssessmentProtocol": {
    "frequency": "after_each_task",
    "components": [
      {
        "question": "What has gone right?",
        "action": "Update brain/decision-framework.md and memory/episodic.md",
        "purpose": "Reinforce successful behaviors and decision patterns"
      },
      {
        "question": "What did I do wrong?",
        "action": "Update memory/episodic.md failed_attempts and reflexes/error-handling.md",
        "purpose": "Implement preventive measures and improved processes"
      },
      {
        "question": "What feedback did I receive?",
        "action": "Update memory/semantic.md best_practices and brain/collaboration-protocols.md",
        "purpose": "Integrate feedback into future decision-making"
      },
      {
        "question": "What new capabilities do I need?",
        "action": "Update brain/capabilities.md and memory/semantic.md domain_knowledge",
        "purpose": "Communicate capability gaps to Project Coordinator"
      },
      {
        "question": "What other roles could I play?",
        "action": "Update brain/collaboration-protocols.md and memory/procedural.md workflows",
        "purpose": "Identify expansion opportunities"
      },
      {
        "question": "What should I stop doing?",
        "action": "Update reflexes/trigger-responses.md and memory/procedural.md workflows",
        "purpose": "Eliminate ineffective or counterproductive behaviors"
      }
    ]
  }
}
```

---

## 🚀 **Implementation Guidelines**

### **Critical Implementation Requirements**

#### **1. Content Generation, Not Instructions**
```typescript
// ✅ CORRECT: Generate actual content using LLM
const researchPrompt = this.cns.promptEngineering.createResearchPrompt(userRequest);
const sources = await this.llmCall(researchPrompt);
const contentPrompt = this.cns.promptEngineering.createContentPrompt(userRequest, sources);
const result = await this.llmCall(contentPrompt);

// ❌ WRONG: Generate instructions for creating content
const instructions = "Here are prompts you could use to create content...";
```

#### **2. CNS Integration Requirements**
```typescript
// Always update CNS after task completion
await this.updateCNS({
  memory: { 
    episodic: { successfulPatterns: newPattern },
    semantic: { bestPractices: refinedPractice }
  },
  reflexes: { triggerResponses: improvedResponse }
});

// Execute self-assessment protocol
await this.executeSelfAssessment(taskContext, outcomes);
```

#### **3. Two-Phase Workflow Implementation**
```typescript
// Phase 1: Research
const researchResults = await this.executeResearchPhase(userRequest);

// Phase 2: Creation  
const content = await this.executeCreationPhase(userRequest, researchResults);

// Phase 3: Quality Assurance
const finalDeliverable = await this.executeQualityPhase(content, requirements);
```

---

## 📊 **Implementation Status & Roadmap**

### **✅ Ready for Implementation**
- Complete CNS file structure and specifications
- Agent coordination protocols
- Quality assurance framework
- Self-assessment and learning protocols
- Prompt engineering strategies

### **🚧 Implementation Priority**
1. **CNS Manager Library** - File operations and data management
2. **Base Agent Class** - Common CNS integration functionality  
3. **Communications Agent** - First complete agent implementation
4. **Master Orchestrator** - Multi-agent coordination
5. **Reviewer Agent** - Quality assurance validation

### **⏳ Future Enhancements**
- Advanced learning pattern recognition
- Predictive agent capability matching
- Real-time performance monitoring
- Advanced collaboration optimization

---

*This unified CNS architecture provides the complete cognitive framework for implementing the Atlassian Agent Team, combining proven JSON-based storage with comprehensive cognitive modeling for intelligent, adaptive, and continuously learning agents.*