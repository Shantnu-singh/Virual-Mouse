# 🤝 Contributing to Gesture Control System

First off, thank you for considering contributing to the Gesture Control System! It's people like you that make this project such a great tool for the community.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Contribution Guidelines](#contribution-guidelines)
- [Style Guidelines](#style-guidelines)
- [Testing Guidelines](#testing-guidelines)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)
- [Issue Guidelines](#issue-guidelines)
- [Recognition](#recognition)

## 📜 Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

### Our Pledge

We are committed to making participation in this project a harassment-free experience for everyone, regardless of:

- Age, body size, disability, ethnicity, gender identity and expression
- Level of experience, nationality, personal appearance, race, religion
- Sexual identity and orientation

### Our Standards

**Positive behaviors include:**

- Using welcoming and inclusive language
- Being respectful of differing viewpoints and experiences
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

**Unacceptable behaviors include:**

- Harassment, trolling, insulting/derogatory comments
- Publishing others' private information without permission
- Other conduct which could reasonably be considered inappropriate

## 🚀 How Can I Contribute?

### 🐛 Reporting Bugs

Before creating bug reports, please check existing issues as you might find that the problem has already been reported. When creating a bug report, include as many details as possible:

**Bug Report Template:**

```markdown
**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

**Expected behavior**
A clear description of what you expected to happen.

**Screenshots/Videos**
If applicable, add screenshots or videos to help explain your problem.

**Environment:**
 - OS: [e.g. Windows 10, macOS 11.6, Ubuntu 20.04]
 - Python Version: [e.g. 3.8.10]
 - OpenCV Version: [e.g. 4.5.3]
 - Camera: [e.g. Built-in webcam, USB camera model]

**Additional context**
Add any other context about the problem here.
```

### 💡 Suggesting Enhancements

Enhancement suggestions are welcome! Please provide the following information:

**Feature Request Template:**

```markdown
**Is your feature request related to a problem?**
A clear description of what the problem is. Ex. I'm always frustrated when [...]

**Describe the solution you'd like**
A clear description of what you want to happen.

**Describe alternatives you've considered**
Alternative solutions or features you've considered.

**Additional context**
Add any other context, mockups, or examples about the feature request here.

**Implementation ideas**
If you have ideas about how this could be implemented, please share them.
```

### 🔧 Contributing Code

We love code contributions! Here's how you can help:

- **Bug fixes** - Fix reported issues
- **Feature implementations** - Add new gesture controls
- **Performance improvements** - Optimize existing code
- **Documentation** - Improve docs, add examples
- **Tests** - Add unit tests and integration tests

## 🏗️ Getting Started

### Prerequisites

- Python 3.8 or higher
- Git
- A webcam for testing
- Basic knowledge of computer vision concepts (helpful but not required)

### Development Environment

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/gesture-control-system.git
   cd gesture-control-system
   ```

3. **Add the original repository as upstream:**
   ```bash
   git remote add upstream https://github.com/ORIGINAL_OWNER/gesture-control-system.git
   ```

4. **Create a virtual environment:**
   ```bash
   python -m venv gesture_dev_env
   source gesture_dev_env/bin/activate  # On Windows: gesture_dev_env\Scripts\activate
   ```

5. **Install dependencies:**
   ```bash
   pip install -r requirements-dev.txt
   pip install -e .
   ```

## 🛠️ Development Setup

### Project Structure

```
gesture-control-system/
├── src/
│   ├── __init__.py
│   ├── Hand_detection_module.py    # Core detection module
│   ├── gesture_control.py          # Volume control
│   ├── virtual_mouse.py            # Mouse control
│   └── utils/                      # Utility functions
├── tests/
│   ├── __init__.py
│   ├── test_hand_detection.py      # Unit tests
│   ├── test_integration.py         # Integration tests
│   └── fixtures/                   # Test data
├── docs/                           # Documentation
├── examples/                       # Example usage
├── requirements.txt                # Production dependencies
├── requirements-dev.txt            # Development dependencies
├── setup.py                        # Package setup
└── pytest.ini                      # Test configuration
```

### Setting Up Pre-commit Hooks

Install pre-commit hooks to ensure code quality:

```bash
pip install pre-commit
pre-commit install
```

This will run automatic checks before each commit including:
- Code formatting with `black`
- Import sorting with `isort`
- Linting with `flake8`
- Type checking with `mypy`

## 📋 Contribution Guidelines

### Branch Naming Convention

Use descriptive branch names with the following prefixes:

- `feature/` - New features
- `bugfix/` - Bug fixes
- `hotfix/` - Critical bug fixes
- `docs/` - Documentation updates
- `refactor/` - Code refactoring
- `test/` - Adding or updating tests

**Examples:**
```bash
feature/multi-hand-detection
bugfix/camera-initialization-error
docs/api-documentation-update
refactor/hand-detection-performance
```

### Making Changes

1. **Create a new branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following the style guidelines

3. **Add tests** for new functionality

4. **Update documentation** if needed

5. **Test your changes:**
   ```bash
   pytest tests/
   python -m flake8 src/
   python -m black --check src/
   ```

6. **Commit your changes** following commit guidelines

7. **Push to your fork:**
   ```bash
   git push origin feature/your-feature-name
   ```

## 🎨 Style Guidelines

### Python Code Style

We follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) with some modifications:

**Formatting:**
- Line length: 88 characters (Black default)
- Use double quotes for strings
- Use trailing commas in multi-line structures

**Code Organization:**
```python
# Standard library imports
import os
import sys
import time
from typing import List, Optional, Tuple

# Third-party imports
import cv2
import numpy as np
import mediapipe as mp

# Local imports
from .utils import helper_functions
```

**Function Documentation:**
```python
def find_distance(self, frame: np.ndarray, point1: int, point2: int, draw: bool = True) -> Optional[Tuple[float, np.ndarray, int, int]]:
    """
    Calculate the distance between two hand landmarks.
    
    Args:
        frame: Input image frame
        point1: First landmark ID (0-20)
        point2: Second landmark ID (0-20) 
        draw: Whether to draw distance visualization
        
    Returns:
        Tuple of (distance, frame, center_x, center_y) or None if no hand detected
        
    Raises:
        ValueError: If point1 or point2 are invalid landmark IDs
        
    Example:
        >>> detector = HandDetection()
        >>> distance, frame, cx, cy = detector.find_distance(frame, 4, 8)
        >>> if distance and distance < 30:
        ...     print("Pinch gesture detected!")
    """
    # Implementation here
```

**Class Documentation:**
```python
class HandDetection:
    """
    A class for hand detection and gesture recognition using MediaPipe.
    
    This class provides methods for detecting hands, extracting landmark positions,
    calculating distances between landmarks, and recognizing basic gestures.
    
    Attributes:
        min_detection_confidence: Minimum confidence threshold for detection
        mpHands: MediaPipe hands solution
        hands: MediaPipe hands detector instance
        mpDraw: MediaPipe drawing utilities
        
    Example:
        >>> detector = HandDetection(min_detection_confidence=0.7)
        >>> frame = detector.find_hand(frame)
        >>> landmarks = detector.find_position(frame)
    """
```

### Variable Naming

```python
# Good examples
hand_landmarks = detector.find_position(frame)
detection_confidence = 0.7
frame_width, frame_height = 640, 480
is_hand_detected = len(landmarks) > 0

# Avoid
lmList = []  # Use descriptive names
x1, y1 = pos  # Use meaningful variable names
flag = True  # Use descriptive boolean names
```
