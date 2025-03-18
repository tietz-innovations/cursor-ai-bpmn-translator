import pytest
import os
from bpmn_translator.translator import BPMNTranslator, BPMNTranslatorError, BPMNParsingError

# Sample BPMN XML for testing
SAMPLE_BPMN = '''<?xml version="1.0" encoding="UTF-8"?>
<bpmn:definitions xmlns:bpmn="http://www.omg.org/spec/BPMN/20100524/MODEL">
  <bpmn:process id="Process_1">
    <bpmn:startEvent id="StartEvent_1" name="Start">
      <bpmn:outgoing>Flow_1</bpmn:outgoing>
    </bpmn:startEvent>
    <bpmn:task id="Task_1" name="First Task">
      <bpmn:incoming>Flow_1</bpmn:incoming>
      <bpmn:outgoing>Flow_2</bpmn:outgoing>
      <bpmn:documentation>This is the first task</bpmn:documentation>
    </bpmn:task>
    <bpmn:endEvent id="EndEvent_1" name="End">
      <bpmn:incoming>Flow_2</bpmn:incoming>
    </bpmn:endEvent>
    <bpmn:sequenceFlow id="Flow_1" sourceRef="StartEvent_1" targetRef="Task_1" />
    <bpmn:sequenceFlow id="Flow_2" sourceRef="Task_1" targetRef="EndEvent_1" />
  </bpmn:process>
</bpmn:definitions>'''

@pytest.fixture
def sample_bpmn_file(tmp_path):
    """Create a temporary BPMN file for testing."""
    bpmn_file = tmp_path / "test.bpmn"
    bpmn_file.write_text(SAMPLE_BPMN)
    return str(bpmn_file)

def test_translator_initialization(sample_bpmn_file):
    """Test that the translator initializes correctly with a valid BPMN file."""
    translator = BPMNTranslator(sample_bpmn_file)
    assert translator.bpmn_graph is not None
    assert translator.xml_root is not None

def test_translator_invalid_file():
    """Test that the translator raises an error with an invalid file."""
    with pytest.raises(BPMNParsingError):
        BPMNTranslator("nonexistent.bpmn")

def test_get_node_data(sample_bpmn_file):
    """Test that node data is retrieved correctly."""
    translator = BPMNTranslator(sample_bpmn_file)
    node_data = translator._get_node_data("Task_1")
    
    assert node_data["id"] == "Task_1"
    assert node_data["name"] == "First Task"
    assert node_data["documentation"] == "This is the first task"

def test_generate_description(sample_bpmn_file):
    """Test that process description is generated correctly."""
    translator = BPMNTranslator(sample_bpmn_file)
    description = translator.generate_description()
    
    assert "Start" in description
    assert "First Task" in description
    assert "End" in description

def test_generate_user_stories(sample_bpmn_file):
    """Test that user stories are generated correctly."""
    translator = BPMNTranslator(sample_bpmn_file)
    stories = translator.generate_user_stories()
    
    # Since our sample BPMN doesn't have explicit roles, it should return an empty dict
    assert isinstance(stories, dict)

def test_translate_file_static_method(sample_bpmn_file):
    """Test the static translate_file method."""
    description = BPMNTranslator.translate_file(sample_bpmn_file)
    assert isinstance(description, str)
    assert "First Task" in description