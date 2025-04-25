# 0x01. Lockboxes

## 📚 Description

This project is part of the ALX Interview preparation series. It focuses on algorithmic problem solving using Python.

You are given `n` number of locked boxes, each numbered from `0` to `n - 1`. Each box may contain keys to other boxes. The goal is to write a method that determines if all the boxes can be opened, starting from box 0 which is initially unlocked.

---

## 🔍 Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.4.3)
- Code must follow the `PEP 8` style guide (version 1.7.x)
- All files must be executable
- The first line of all files must be exactly `#!/usr/bin/python3`
- Each file should end with a new line
- A `README.md` file is mandatory

---

## 🚀 Function Prototype

```python
def canUnlockAll(boxes):
    """
    boxes: list of lists, each inner list contains keys to other boxes
    Returns: True if all boxes can be opened, else False
    """

