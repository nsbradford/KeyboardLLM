import pytest
from langchain.agents import AgentType

from vimgpt.experimental.plan_and_execute import vimgpt_agent_plan_and_execute
from vimgpt.experimental.react import vimgpt_agent_react


# this agent is awful...
@pytest.mark.skip
def test_vimgpt_agent_plan_and_execute():
    result = vimgpt_agent_plan_and_execute(
        command="Write in the document the answer to: what is the capital of France?"
    )
    assert result.strip() == "The capital of France is Paris."

# this seems to work well, but langchain fails sometimes with 'Could not parse LLM output:'
@pytest.mark.skip
def test_vimgpt_agent_react():
    result = vimgpt_agent_react(
        command="Write in the document the answer to: what is the capital of France?",
        agent_type=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION
    )
    assert result.strip() == "The capital of France is Paris."

def test_vimgpt_agent_react_structured():
    result = vimgpt_agent_react(
        command="Write in the document the answer to: what is the capital of France? Just one word.",
        agent_type=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION
    )
    assert result.strip() == "Paris"
