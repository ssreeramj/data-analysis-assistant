"""This is an automatically generated file. Do not modify it.

This file was generated using `langgraph-gen` version 0.0.3.
To regenerate this file, run `langgraph-gen` with the source `yaml` file as an argument.

Usage:

1. Add the generated file to your project.
2. Create a new agent using the stub.

Below is a sample implementation of the generated stub:

```python
from typing_extensions import TypedDict

from stub import CustomAgent

class SomeState(TypedDict):
    # define your attributes here
    foo: str

# Define stand-alone functions
def generate_pandas_code(state: SomeState) -> dict:
    print("In node: generate_pandas_code")
    return {
        # Add your state update logic here
    }


def check_pandas_code(state: SomeState) -> dict:
    print("In node: check_pandas_code")
    return {
        # Add your state update logic here
    }


def generate_final_answer(state: SomeState) -> dict:
    print("In node: generate_final_answer")
    return {
        # Add your state update logic here
    }


def generate_viz_code(state: SomeState) -> dict:
    print("In node: generate_viz_code")
    return {
        # Add your state update logic here
    }


def check_viz_code(state: SomeState) -> dict:
    print("In node: check_viz_code")
    return {
        # Add your state update logic here
    }


def pandas_code_cond(state: SomeState) -> str:
    print("In condition: pandas_code_cond")
    raise NotImplementedError("Implement me.")


def viz_code_cond(state: SomeState) -> str:
    print("In condition: viz_code_cond")
    raise NotImplementedError("Implement me.")


agent = CustomAgent(
    state_schema=SomeState,
    impl=[
        ("generate_pandas_code", generate_pandas_code),
        ("check_pandas_code", check_pandas_code),
        ("generate_final_answer", generate_final_answer),
        ("generate_viz_code", generate_viz_code),
        ("check_viz_code", check_viz_code),
        ("pandas_code_cond", pandas_code_cond),
        ("viz_code_cond", viz_code_cond),
    ]
)

compiled_agent = agent.compile()

print(compiled_agent.invoke({"foo": "bar"}))
"""

from typing import Callable, Any, Optional, Type

from langgraph.constants import START, END
from langgraph.graph import StateGraph


def CustomAgent(
    *,
    state_schema: Optional[Type[Any]] = None,
    config_schema: Optional[Type[Any]] = None,
    input: Optional[Type[Any]] = None,
    output: Optional[Type[Any]] = None,
    impl: list[tuple[str, Callable]],
) -> StateGraph:
    """Create the state graph for CustomAgent."""
    # Declare the state graph
    builder = StateGraph(
        state_schema, config_schema=config_schema, input=input, output=output
    )

    nodes_by_name = {name: imp for name, imp in impl}

    all_names = set(nodes_by_name)

    expected_implementations = {
        "generate_pandas_code",
        "check_pandas_code",
        "generate_final_answer",
        "generate_viz_code",
        "check_viz_code",
        "pandas_code_cond",
        "viz_code_cond",
    }

    missing_nodes = expected_implementations - all_names
    if missing_nodes:
        raise ValueError(f"Missing implementations for: {missing_nodes}")

    extra_nodes = all_names - expected_implementations

    if extra_nodes:
        raise ValueError(
            f"Extra implementations for: {extra_nodes}. Please regenerate the stub."
        )

    # Add nodes
    builder.add_node("generate_pandas_code", nodes_by_name["generate_pandas_code"])
    builder.add_node("check_pandas_code", nodes_by_name["check_pandas_code"])
    builder.add_node("generate_final_answer", nodes_by_name["generate_final_answer"])
    builder.add_node("generate_viz_code", nodes_by_name["generate_viz_code"])
    builder.add_node("check_viz_code", nodes_by_name["check_viz_code"])

    # Add edges
    builder.add_edge(START, "generate_pandas_code")
    builder.add_edge("generate_pandas_code", "check_pandas_code")
    builder.add_edge("generate_viz_code", "check_viz_code")
    builder.add_edge("generate_final_answer", "generate_viz_code")
    builder.add_conditional_edges(
        "check_pandas_code",
        nodes_by_name["pandas_code_cond"],
        [
            "generate_pandas_code",
            "generate_final_answer",
        ],
    )
    builder.add_conditional_edges(
        "check_viz_code",
        nodes_by_name["viz_code_cond"],
        [
            "generate_viz_code",
            END,
        ],
    )
    return builder
