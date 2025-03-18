# BPMN Translator MCP for Cursor AI

A Model Context Protocol (MCP) component for Cursor AI that translates BPMN diagrams into human-readable descriptions and user stories.

## Features

- Translate BPMN diagrams into clear, human-readable process descriptions
- Generate user stories from BPMN processes
- Support for various BPMN elements:
  - Events (start, end, intermediate, timer)
  - Tasks and Activities
  - Sequence Flows
  - Participants and Lanes
  - Documentation

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### As a Command Line Tool

```bash
python -m bpmn_translator translate path/to/your/diagram.bpmn
```

### As an MCP Component

The BPMN Translator provides two main functions through its MCP interface:

1. `translate_bpmn`:
```python
from bpmn_translator.mcp_adapter import MCPBPMNTranslator

# Translate BPMN content
result = MCPBPMNTranslator.translate_bpmn(
    bpmn_content="<your BPMN XML content>",
    output_format="both"  # Options: "description", "user_stories", "both"
)

# Access results
if "description" in result:
    print(result["description"])
if "user_stories" in result:
    print(result["user_stories"])
```

2. `generate_user_stories`:
```python
from bpmn_translator.mcp_adapter import MCPBPMNTranslator

# Generate user stories for specific roles
stories = MCPBPMNTranslator.generate_user_stories(
    bpmn_content="<your BPMN XML content>",
    roles=["Business Customer", "System Administrator"]  # Optional
)

# Access user stories
print(stories["user_stories"])
```

## Input Format

The component accepts BPMN 2.0 XML files. Example structure:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<bpmn:definitions xmlns:bpmn="http://www.omg.org/spec/BPMN/20100524/MODEL">
  <bpmn:process id="Process_1">
    <bpmn:startEvent id="StartEvent_1" name="Start">
      <bpmn:outgoing>Flow_1</bpmn:outgoing>
    </bpmn:startEvent>
    <!-- ... more BPMN elements ... -->
  </bpmn:process>
</bpmn:definitions>
```

## Output Format

### Process Description

The process description provides a hierarchical view of the process flow:

```
The process can start in these ways:

Path:
- Start Process
  - First Task
    - Second Task
      - End Process
```

### User Stories

User stories are generated in the format:
```
As a [role], I want to [action] so that [benefit]
```

## Error Handling

The component includes robust error handling:

- `BPMNTranslatorError`: Base exception class
- `BPMNParsingError`: Raised when there's an error parsing the BPMN file

## Testing

Run the test suite:

```bash
pytest tests/
```

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

MIT License - see LICENSE file for details