# AI Coding Agent Instructions for UAS-Algoritma-Pemograman

## Project Overview
This is an educational Python project implementing Binary Search Tree (BST) operations and binary tree traversals with a Tkinter GUI. The project demonstrates recursive algorithms for tree insertion and three traversal methods (InOrder, PreOrder, PostOrder) in an interactive desktop application.

## Architecture
- **Node Class**: Represents individual tree nodes with `data` (int), `left`, and `right` child references
- **BinarySearchTree Class**: Manages tree operations using recursive algorithms
- **GUI Layer**: Tkinter-based interface for user interaction (input numbers, trigger traversals, display results)

## Key Coding Patterns
- **Recursive Implementation**: All tree operations use recursion with helper methods prefixed with `_`
- **Result Accumulation**: Traversal methods collect results in mutable lists passed to recursive helpers
- **Indonesian Documentation**: Code comments and documentation are in Indonesian (Bahasa Indonesia)
- **Simple Error Handling**: Basic try/except for input validation, using `tkinter.messagebox` for user alerts

## Development Workflow
- **Run Command**: `python index.py` (main entry point)
- **Dependencies**: Requires Tkinter (included with Python 3.x standard installation)
- **Testing**: Manual testing through GUI - insert values like `50, 30, 70, 20, 40, 60, 80` and verify traversals
- **Debugging**: Use print statements or GUI output label for intermediate results

## Important Files
- `index.py`: Complete implementation including BST logic, traversals, and Tkinter GUI
- `README.md`: Indonesian documentation with algorithm explanations and usage examples

## Code Examples
**Insert Pattern**:
```python
def insert(self, data):
    self.root = self._insert(self.root, data)

def _insert(self, root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = self._insert(root.left, data)
    elif data > root.data:
        root.right = self._insert(root.right, data)
    return root
```

**Traversal Pattern**:
```python
def inorder(self):
    result = []
    self._inorder(self.root, result)
    return result

def _inorder(self, root, result):
    if root:
        self._inorder(root.left, result)
        result.append(root.data)
        self._inorder(root.right, result)
```

## Guidelines
- Maintain recursive patterns for tree operations
- Use Indonesian for comments and user-facing strings
- Follow the established naming: public methods without `_`, private recursive helpers with `_`
- Keep GUI simple and educational-focused
- Validate numeric input and provide clear error messages