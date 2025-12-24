# Error Handling

## File Operation Errors

### File Not Found
- **Error**: Requested file does not exist
- **Response**: Verify path, search for similar files, suggest alternatives
- **Recovery**: Use search tools to locate correct file or create if intended
- **Prevention**: Always use absolute paths, verify existence before operations

### Permission Denied
- **Error**: Insufficient permissions for file operation
- **Response**: Check file permissions, suggest alternative approach
- **Recovery**: Use different tool or request user intervention
- **Prevention**: Verify write permissions before attempting modifications

### Path Resolution Error
- **Error**: Invalid or malformed file path
- **Response**: Correct path format, use absolute paths
- **Recovery**: Search for intended file using search tools
- **Prevention**: Use consistent absolute path format throughout session

## API Integration Errors

### Confluence API Failure
- **Error**: Confluence API call returns error or times out
- **Response**: Analyze error message, check configuration, retry with refined approach
- **Recovery**: Verify site URL, space configuration, authentication
- **Prevention**: Always verify configuration before operations

### Jira API Failure
- **Error**: Jira API call fails or returns unexpected response
- **Response**: Check site URL, project configuration, retry with correct parameters
- **Recovery**: Validate project key, issue type, required fields
- **Prevention**: Verify site and project configuration before operations

### Network Timeout
- **Error**: API call times out or network connection fails
- **Response**: Retry operation, check network connectivity
- **Recovery**: Use alternative approach or inform user of connectivity issues
- **Prevention**: Implement reasonable timeouts and retry logic

## Tool Operation Errors

### Command Execution Failure
- **Error**: Terminal command fails or returns error
- **Response**: Analyze error output, check command syntax and prerequisites
- **Recovery**: Correct command, install missing dependencies, use alternative approach
- **Prevention**: Verify command availability and prerequisites before execution

### Search Operation Failure
- **Error**: Search tools return no results or error
- **Response**: Refine search terms, try alternative search strategies
- **Recovery**: Use different search patterns, check file system manually
- **Prevention**: Use multiple search approaches for comprehensive coverage

### Edit Operation Failure
- **Error**: File edit operation fails due to content mismatch
- **Response**: Re-read file, verify content, use more specific search strings
- **Recovery**: Use edit_file_multi for complex changes, verify exact content match
- **Prevention**: Always read file before editing, use precise content matching

## Context and Memory Errors

### Context File Corruption
- **Error**: Context file is malformed or unreadable
- **Response**: Attempt to recover partial context, create new context file
- **Recovery**: Extract recoverable information, start fresh context tracking
- **Prevention**: Use consistent context file format and validation

### Memory System Inconsistency
- **Error**: CNS memory files have conflicting or outdated information
- **Response**: Identify conflicts, resolve based on timestamps and evidence
- **Recovery**: Update conflicting memories with most recent validated information
- **Prevention**: Maintain timestamp integrity and regular memory validation

### Learning Integration Failure
- **Error**: Unable to apply or integrate learning from previous sessions
- **Response**: Document issue, attempt manual integration of key learnings
- **Recovery**: Create new learning entry documenting the integration failure
- **Prevention**: Maintain consistent learning documentation format

## Quality Assurance Errors

### Code Quality Failure
- **Error**: Lint or typecheck commands fail after code changes
- **Response**: Analyze error output, fix issues, re-run validation
- **Recovery**: Iteratively fix errors until all quality checks pass
- **Prevention**: Follow established code patterns and conventions

### Test Execution Failure
- **Error**: Tests fail after code modifications
- **Response**: Analyze test failures, fix code or update tests as appropriate
- **Recovery**: Ensure all tests pass before considering task complete
- **Prevention**: Follow test-driven development practices when applicable

### Documentation Inconsistency
- **Error**: Documentation doesn't match actual implementation
- **Response**: Update documentation to reflect current implementation
- **Recovery**: Verify documentation accuracy across all related files
- **Prevention**: Update documentation as part of all code changes

## Recovery Procedures

### General Error Recovery
1. Document the error and context in current session
2. Analyze error message and potential causes
3. Attempt systematic resolution based on error type
4. If resolution unsuccessful, inform user and suggest alternatives
5. Update error-handling procedures based on new error patterns

### Context Recovery
1. Attempt to load most recent valid context file
2. Extract recoverable session information
3. Create new context file with recovered information
4. Inform user of context recovery status
5. Continue with available context

### Quality Recovery
1. Identify specific quality threshold that wasn't met
2. Analyze root cause of quality failure
3. Implement corrective measures
4. Re-execute quality validation
5. Document improvement for future prevention

**Last Updated**: 2025-10-23T14:15:00Z