# CNS Refactor Plan - December 23, 2025

## Current State Issues

### 1. Path Inconsistencies ❌
- All Python scripts reference `~/.codelassian`
- Should be `~/.personal-cns`
- Affects: All 5 Python scripts

### 2. Context Management System ❌
- Scripts reference context update system
- User wants this removed (works with .md implementation plans instead)
- Affects: `startup-sequence.py`, `update-cns.py`

### 3. Installation Gaps ❌
- `install.sh` doesn't copy Python scripts to `~/.personal-cns/cns/`
- Scripts exist in repo but not deployed
- Users won't get automation capabilities

### 4. Integration Missing ❌
- `.github/copilot-instructions.md` doesn't mention Python scripts
- No guidance on when/how to use them
- CNS initialization is manual, not automated

## Python Scripts Inventory

### Core Scripts (5 total):

1. **`cns/startup-sequence.py`** (922 lines)
   - Purpose: CNS initialization, loads all brain/memory/reflexes
   - Issues: Context management code, wrong path
   - Keep: Brain loading, memory loading
   - Remove: Context file management

2. **`cns/process-learning.py`** (153 lines)
   - Purpose: Handles "Learn this:" commands
   - Issues: Wrong path, creates context files
   - Keep: Episodic memory creation
   - Remove: Context updates

3. **`cns/update-cns.py`** (513 lines)
   - Purpose: Comprehensive CNS maintenance
   - Issues: Heavy context management focus
   - Keep: Learning evaluation, memory consolidation
   - Remove: Context update functions

4. **`cns/brain/principle-evaluator.py`** (CURRENT FILE, working)
   - Purpose: Analyze learnings, propose principle updates
   - Issues: Wrong path only
   - Action: Fix path

5. **`cns/brain/user-pattern-learner.py`** (379 lines)
   - Purpose: Identify user patterns, update user-patterns.md
   - Issues: Wrong path, checks context files
   - Keep: Pattern analysis from learnings
   - Remove: Context file analysis

## Refactor Tasks

### Phase 1: Path Corrections ✅ COMPLETE
**Goal**: All scripts use `~/.personal-cns`

- [x] Replace `get_codelassian_path()` with `get_cns_path()` in all 5 scripts
- [x] Update return value to `~/.personal-cns`
- [x] Test each script independently

**Result**: All scripts now use `~/.personal-cns` - See docs/status/2025-12-23-PHASE-1-COMPLETE.md

### Phase 2: Remove Context Management ✅ COMPLETE
**Goal**: Scripts focus on learning, not context files

**See docs/status/2025-12-23-PHASE-2-COMPLETE.md for full details**

- [x] **process-learning.py**: Removed context file updates (~35 lines removed)
- [x] **user-pattern-learner.py**: Changed to analyze episodic learnings (~19 lines removed)
- [x] **update-cns.py**: Removed update_context() function and all calls (~43 lines removed)
- [x] **startup-sequence.py**: Complete rewrite to simplified version (~755 lines removed!)
  - Removed: Context management, workspace detection, restoration prompts
  - Kept: CNS status display only
  - Backup: startup-sequence-old.py created

**Total Impact**: ~852 lines of context code removed, scripts dramatically simplified

**Result**: All scripts now focus purely on learning and maintenance - See docs/status/2025-12-23-PHASE-2-COMPLETE.md

### Phase 3: Update Installation ✅ COMPLETE
**Goal**: Scripts deployed to user's CNS

**See docs/status/2025-12-23-PHASE-3-COMPLETE.md for full details**

- [x] Copy all 5 Python scripts to `~/.personal-cns/cns/` (via `cp -r cns`)
- [x] Make scripts executable with `chmod +x` (added to install.sh)
- [x] Create `~/.personal-cns/cns/brain/` subdirectory (handled by cp -r)
- [x] Copy principle-evaluator.py and user-pattern-learner.py there (handled by cp -r)
- [x] Create `reflex-state.json` template with initial state
- [x] Update success message to show deployed scripts

**Result**: install.sh now deploys all automation scripts with execute permissions - See docs/status/2025-12-23-PHASE-3-COMPLETE.md

### Phase 4: Integration Documentation 🔄
**Goal**: Clear guidance on CNS automation

**.github/copilot-instructions.md**:
- [ ] Remove: All context file management instructions
- [ ] Add: How CNS loads all files at startup (via startup-sequence.py concept)
- [ ] Add: "Learn this:" command triggers process-learning.py
- [ ] Add: Periodic maintenance with update-cns.py
- [ ] Clarify: Implementation plans in .md files provide persistence

**SETUP.md**:
- [ ] Update: Python scripts are included and deployed
- [ ] Add: Usage instructions for each script
- [ ] Add: How to run maintenance (`python3 ~/.personal-cns/cns/update-cns.py`)

**trigger-responses.md**:
- [ ] Fix: "Learn this:" trigger to use correct path
- [ ] Remove: Context update trigger
- [ ] Remove: References to `update-context.py`

### Phase 5: Simplify Initialization 🆕
**Goal**: CNS loads automatically without complex context management

**New Approach**:
- Copilot reads `.github/copilot-instructions.md` (automatic)
- Instructions tell it to load all CNS files from `~/.personal-cns/cns/`
- No Python script needed for initialization (Copilot does it natively)
- Python scripts are for maintenance/learning only

**What This Means**:
- `startup-sequence.py` → Not needed for initialization
- Can be repurposed for maintenance checks
- Or removed entirely if redundant

### Phase 6: Automated Reflex Triggers 🆕
**Goal**: CNS automatically executes maintenance scripts based on reflexes

**Trigger Types**:
1. **Event-Based** - When something significant happens
2. **Time-Based** - Periodic execution when overdue
3. **User-Commanded** - Explicit user request

#### Reflex Integration in trigger-responses.md

**New Triggers to Add**:

```markdown
### Learning Accumulation Trigger ⚙️ AUTOMATIC
- **Trigger**: 5+ new learning files created since last principle evaluation
- **Response**: Execute `python3 ~/.personal-cns/cns/brain/principle-evaluator.py`
- **Rationale**: Keep principles aligned with accumulated learnings
- **Priority**: Medium
- **Implementation**: Check episodic/ folder, count files newer than last evaluation
- **Frequency**: Minimum 7 days between runs

### User Pattern Evolution Trigger ⚙️ AUTOMATIC  
- **Trigger**: 10+ new learning entries since last pattern analysis
- **Response**: Execute `python3 ~/.personal-cns/cns/brain/user-pattern-learner.py`
- **Rationale**: Detect emerging user preferences and workflow patterns
- **Priority**: Medium
- **Implementation**: Check episodic/ folder, count files newer than last pattern update
- **Frequency**: Minimum 14 days between runs

### Explicit Learning Command ⚙️ USER-COMMANDED
- **Trigger**: User message starts with "Learn this:"
- **Response**: Execute `python3 ~/.personal-cns/cns/process-learning.py "[content]"`
- **Rationale**: Capture critical lessons immediately
- **Priority**: Critical
- **Implementation**: Extract content after "Learn this:", pass to script
- **Output**: Confirm learning captured and location

### CNS Maintenance Command ⚙️ USER-COMMANDED
- **Trigger**: User says "Run CNS maintenance" or "Update CNS"
- **Response**: Execute `python3 ~/.personal-cns/cns/update-cns.py`
- **Rationale**: Comprehensive CNS health check and optimization
- **Priority**: High
- **Implementation**: Run full maintenance: evaluate principles, analyze patterns, consolidate memory
- **Output**: Maintenance report with recommendations

### Stale Principles Detection ⚙️ TIME-BASED
- **Trigger**: 30+ days since last principle evaluation
- **Response**: Suggest running principle-evaluator.py
- **Rationale**: Ensure principles stay relevant and validated
- **Priority**: Low
- **Implementation**: Check last-evaluated date in prime-principles.md
- **Frequency**: Check monthly, suggest if stale

### Learning Capture Prompt ⚙️ EVENT-BASED
- **Trigger**: Significant task completed (3+ files changed, complex problem solved)
- **Response**: Ask: "Would you like me to capture learnings from this task?"
- **Rationale**: Don't miss valuable learning opportunities
- **Priority**: Medium
- **Implementation**: Detect completion of complex tasks
- **If Yes**: Prompt for key learnings, then run process-learning.py
```

#### Implementation in Copilot Instructions

Add to `.github/copilot-instructions.md`:

```markdown
## Automated Maintenance Reflexes

### When to Execute CNS Scripts

#### Automatic (I detect and suggest):
1. **Principle Evaluation**: When 5+ new learnings accumulated
   - Check: Count files in `~/.personal-cns/cns/memory/episodic/`
   - If triggered, ask: "I notice 5 new learnings. Run principle evaluation?"
   - If approved: `python3 ~/.personal-cns/cns/brain/principle-evaluator.py`

2. **Pattern Analysis**: When 10+ new learnings accumulated
   - Check: Count files since last pattern update
   - If triggered, ask: "Run user pattern analysis?"
   - If approved: `python3 ~/.personal-cns/cns/brain/user-pattern-learner.py`

3. **Stale Principles**: When 30+ days since last evaluation
   - Check: Last validated date in prime-principles.md
   - Suggest: "Principles haven't been evaluated in 30+ days. Run evaluation?"

#### User-Commanded:
1. **"Learn this: [content]"**
   - Immediately execute: `python3 ~/.personal-cns/cns/process-learning.py "[content]"`
   - Confirm: "✅ Learning captured in episodic memory"

2. **"Run CNS maintenance"** or **"Update CNS"**
   - Execute: `python3 ~/.personal-cns/cns/update-cns.py`
   - Display: Full maintenance report

3. **After complex task completion**
   - Ask: "Capture learnings from this task?"
   - If yes: Guide user through learning documentation

### Reflex Execution Flow

**Before executing any Python script**:
1. Verify script exists at expected path
2. Check Python3 is available
3. Execute with proper error handling
4. Display output to user
5. Update last-run timestamp (for time-based triggers)

**Error Handling**:
- If script not found: "CNS script missing. Run install.sh to set up."
- If Python error: Display error, suggest manual run
- Always inform user of script execution status
```

#### tracking State for Triggers

Create new file: `~/.personal-cns/cns/reflex-state.json`

```json
{
  "last_principle_evaluation": "2025-12-23T10:30:00",
  "last_pattern_analysis": "2025-12-20T14:15:00", 
  "last_maintenance_run": "2025-12-22T09:00:00",
  "learning_count_since_eval": 3,
  "learning_count_since_pattern": 7,
  "total_learnings": 15
}
```

**Update install.sh to create this file**:
```bash
# Create reflex state tracking file
cat > "$CNS_HOME/cns/reflex-state.json" << 'EOF'
{
  "last_principle_evaluation": null,
  "last_pattern_analysis": null,
  "last_maintenance_run": null,
  "learning_count_since_eval": 0,
  "learning_count_since_pattern": 0,
  "total_learnings": 0
}
EOF
```

#### Helper Functions in Copilot Instructions

Add to copilot-instructions.md:

```markdown
### CNS Reflex Helper Functions

When session starts or after completing tasks, check reflexes:

**Pseudo-code for reflex checking**:
```
function checkCNSReflexes():
  state = read ~/.personal-cns/cns/reflex-state.json
  episodic_files = count ~/.personal-cns/cns/memory/episodic/*.md
  
  # Update counts
  new_learnings = episodic_files - state.total_learnings
  state.learning_count_since_eval += new_learnings
  state.learning_count_since_pattern += new_learnings
  
  # Check triggers
  if state.learning_count_since_eval >= 5:
    if ask_user("Run principle evaluation?"):
      run principle-evaluator.py
      reset state.learning_count_since_eval
      
  if state.learning_count_since_pattern >= 10:
    if ask_user("Run pattern analysis?"):
      run user-pattern-learner.py
      reset state.learning_count_since_pattern
  
  if days_since(state.last_principle_evaluation) > 30:
    suggest "Principles are stale. Consider running evaluation."
  
  save state
```

**Simplified for actual implementation**:
- I check these conditions when appropriate
- I ask before executing (respect user control)
- I update state after execution
- I never execute without user awareness
```

### Phase 6 Tasks:

- [ ] Update `trigger-responses.md` with automated reflex triggers
- [ ] Add reflex checking instructions to `copilot-instructions.md`
- [ ] Create `reflex-state.json` template
- [ ] Update `install.sh` to create reflex-state.json
- [ ] Add state update logic to each Python script (update timestamps after run)
- [ ] Document reflex system in SETUP.md
- [ ] Test automated suggestions work correctly
- [ ] Test user-commanded execution works

### Benefits of Automated Reflexes:

✅ **Proactive**: CNS suggests maintenance before things get stale  
✅ **Non-intrusive**: Always asks permission before executing  
✅ **Intelligent**: Uses real metrics (learning counts, time elapsed)  
✅ **Transparent**: User sees when and why scripts run  
✅ **Maintainable**: State tracking prevents over-execution  
✅ **Extensible**: Easy to add new triggers as needed

## Implementation Order

1. **Phase 1: Path Corrections** (30 min)
   - Simple find/replace in all scripts
   - Test each script runs

2. **Phase 2: Remove Context Management** (1-2 hours)
   - Refactor each script
   - Test functionality preserved

3. **Phase 3: Update Installation** (30 min)
   - Modify install.sh to deploy scripts
   - Create reflex-state.json
   - Test installation process

4. **Phase 4: Documentation Updates** (30 min)
   - Update all docs
   - Remove context references

5. **Phase 5: Simplify Initialization** (30 min)
   - Update copilot-instructions.md
   - Remove startup-sequence dependency

6. **Phase 6: Automated Reflexes** (1 hour)
   - Add reflex triggers to trigger-responses.md
   - Update copilot-instructions.md with reflex logic
   - Add state updates to Python scripts
   - Test automated suggestions

7. **Phase 7: End-to-End Testing** (30 min)
   - Fresh install from install.sh
   - Verify all scripts deployed correctly
   - Test automated reflexes trigger
   - Verify learnings accumulate properly

## Success Criteria

✅ All Python scripts use `~/.personal-cns`  
✅ No context file management code  
✅ Scripts deployed by install.sh  
✅ reflex-state.json created and tracked  
✅ Documentation accurate and clear  
✅ CNS loads all files at chat startup  
✅ "Learn this:" creates episodic entries  
✅ Maintenance script runs successfully  
✅ User can see learnings in VS Code workspace  
✅ Automated reflexes suggest maintenance at right times  
✅ State tracking prevents over-execution  
✅ All triggers documented and functional
