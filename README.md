# KeyboardLLM
Prototype LLM agent tool for interacting with files via keystrokes.

## Why KeyboardLLM
There are two common options for using LLM agents to edit files:
1. **Rewrite the entire file**: reliable, but very expensive (in time and tokens), and for small changes/big files it is incredibly wasteful and difficult to interpret where the change was made.
2. **Make a patch**: using a patch format such as [UDF](https://en.wikipedia.org/wiki/Diff) can make edits much faster and more clearly, but is highly error-prone as the current generation of LLMs often make mistakes with line numbers, leading spaces, capitalization, etc.

**The Solution**: Instead of asking the agent to call a tool with the new contents, give the agent an "Editor" tool which drops into a sub-agent with appropriate context. The simulated editor shows the state of the editor in plaintext, takes individual keystrokes, and reflects updates. This can be conceptualized as individual keystrokes forming tools. The session ends when the agent invokes special save&exit command.

## Roadmap
1. Simulated Vim bindings directly (instead of re-creating functionality such as copy-paste, undo, etc.)

## Installation
...
