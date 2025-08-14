# 🔌 API Documentation

## Overview

This document provides comprehensive documentation for the Gesture Control System API. The system is built around the core `HandDetection` class which provides all hand tracking and gesture recognition functionality.

## Table of Contents

- [HandDetection Class](#handdetection-class)
- [Method Reference](#method-reference)
- [Data Structures](#data-structures)
- [Constants and Configuration](#constants-and-configuration)
- [Error Handling](#error-handling)
- [Usage Examples](#usage-examples)
- [Integration Guide](#integration-guide)

## HandDetection Class

The `HandDetection` class is the core component that handles all hand tracking functionality using MediaPipe.

### Constructor

```python
class HandDetection:
    def __init__(self, min_detection_confidence=0.5)
```

**Parameters:**
- `min_detection_confidence` (float, optional): Minimum confidence threshold for hand detection. Range: 0.0 to 1.0. Default: 0.5

**Returns:**
- `HandDetection` instance

**Example:**
```python
import Hand_detection_module as hdm

# Initialize with default confidence
detector = hdm.HandDetection()

# Initialize with custom confidence
detector = hdm.HandDetection(min_detection_confidence=0.7)
```

## Method Reference

### findHand()

Detects and optionally draws hand landmarks on the input frame.

```python
def findHand(self, frame, flag=True)
```

**Parameters:**
- `frame` (numpy.ndarray): Input image frame from camera or video
- `flag` (bool, optional): Whether to draw hand landmarks and connections. Default: True

**Returns:**
- `numpy.ndarray`: Processed frame with optional hand landmarks drawn

**Example:**
```python
import cv2

cap = cv2.VideoCapture(0)
detector = hdm.HandDetection()

while True:
    ret, frame = cap.read()
    
    # Detect hands and draw landmarks
    frame = detector.findHand(frame, flag=True)
    
    # Detect hands without drawing
    frame = detector.findHand(frame, flag=False)
    
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
```

### findPosition()

Extracts hand landmark positions from the detected hand.

```python
def findPosition(self, frame, handno=0, draw=True)
```

**Parameters:**
- `frame` (numpy.ndarray): Input image frame
- `handno` (int, optional): Hand index to process (0 for first hand, 1 for second). Default: 0
- `draw` (bool, optional): Whether to draw landmark points. Default: True

**Returns:**
- `list`: List of landmark data in format `[[id, x, y], ...]` where:
  - `id` (int): Landmark ID (0-20)
  - `x` (int): X-coordinate in pixels
  - `y` (int): Y-coordinate in pixels

**Hand Landmark IDs:**
```
0: WRIST
1-4: THUMB (1:CMC, 2:MCP, 3:IP, 4:TIP)
5-8: INDEX_FINGER (5:MCP, 6:PIP, 7:DIP, 8:TIP)
9-12: MIDDLE_FINGER (9:MCP, 10:PIP, 11:DIP, 12:TIP)
13-16: RING_FINGER (13:MCP, 14:PIP, 15:DIP, 16:TIP)
17-20: PINKY (17:MCP, 18:PIP, 19:DIP, 20:TIP)
```

**Example:**
```python
frame = detector.findHand(frame)
landmarks = detector.findPosition(frame, handno=0, draw=False)

if landmarks:
    # Get thumb tip position
    thumb_tip = landmarks[4]  # [id, x, y]
    thumb_x, thumb_y = thumb_tip[1], thumb_tip[2]
    
    # Get index finger tip position
    index_tip = landmarks[8]
    index_x, index_y = index_tip[1], index_tip[2]
    
    print(f"Thumb: ({thumb_x}, {thumb_y})")
    print(f"Index: ({index_x}, {index_y})")
```

### findDistance()

Calculates the distance between two hand landmarks.

```python
def findDistance(self, frame, point1, point2, draw=True)
```

**Parameters:**
- `frame` (numpy.ndarray): Input image frame
- `point1` (int): First landmark ID (0-20)
- `point2` (int): Second landmark ID (0-20)
- `draw` (bool, optional): Whether to draw distance visualization. Default: True

**Returns:**
- `tuple`: `(distance, frame, center_x, center_y)` where:
  - `distance` (float): Euclidean distance between the two points
  - `frame` (numpy.ndarray): Frame with optional distance visualization
  - `center_x` (int): X-coordinate of the midpoint
  - `center_y` (int): Y-coordinate of the midpoint

**Example:**
```python
# Calculate distance between thumb tip (4) and index finger tip (8)
distance, frame, cx, cy = detector.findDistance(frame, 4, 8, draw=True)

if distance is not None:
    print(f"Distance: {distance:.2f} pixels")
    print(f"Midpoint: ({cx}, {cy})")
    
    # Use distance for gesture recognition
    if distance < 30:
        print("Pinch gesture detected!")
```

### handUp()

Determines which fingers are extended (up) or folded (down).

```python
def handUp(self, frame)
```

**Parameters:**
- `frame` (numpy.ndarray): Input image frame

**Returns:**
- `list`: Binary list indicating finger states `[thumb, index, middle, ring, pinky]` where:
  - `1`: Finger is extended (up)
  - `0`: Finger is folded (down)

**Example:**
```python
finger_status = detector.handUp(frame)

if finger_status:
    thumb, index, middle, ring, pinky = finger_status
    
    # Count extended fingers
    fingers_up = sum(finger_status)
    print(f"Fingers up: {fingers_up}")
    
    # Detect specific gestures
    if finger_status == [0, 1, 0, 0, 0]:
        print("Pointing gesture (index finger only)")
    elif finger_status == [0, 1, 1, 0, 0]:
        print("Peace sign (index and middle)")
    elif finger_status == [1, 1, 1, 1, 1]:
        print("Open palm (all fingers)")
```

## Data Structures

### Landmark List Format

```python
landmarks = [
    [0, x0, y0],   # WRIST
    [1, x1, y1],   # THUMB_CMC
    [2, x2, y2],   # THUMB_MCP
    [3, x3, y3],   # THUMB_IP
    [4, x4, y4],   # THUMB_TIP
    # ... continues for all 21 landmarks
    [20, x20, y20] # PINKY_TIP
]
```

### Finger Status Format

```python
finger_status = [thumb, index, middle, ring, pinky]
# Example: [1, 1, 0, 0, 0] = thumb and index extended
```

## Constants and Configuration

### Default Values

```python
# Detection confidence
MIN_DETECTION_CONFIDENCE = 0.5

# Camera settings
DEFAULT_WIDTH = 640
DEFAULT_HEIGHT = 480

# Distance thresholds
CLICK_THRESHOLD = 30      # pixels
PINCH_THRESHOLD = 45      # pixels
MIN_DISTANCE = 50         # pixels
MAX_DISTANCE = 300        # pixels

# Smoothing factor
MOUSE_SMOOTHING = 8

# Frame boundary
FRAME_REDUCTION = 100     # pixels
```

### Color Constants

```python
# BGR color values
RED = (0, 0, 255)
GREEN = (0, 255, 0)
BLUE = (255, 0, 0)
MAGENTA = (255, 0, 255)
CYAN = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
```

## Error Handling

### Common Error Scenarios

```python
import cv2
import Hand_detection_module as hdm

detector = hdm.HandDetection()

try:
    # Camera initialization error
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise RuntimeError("Cannot access camera")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Warning: Failed to capture frame")
            continue
            
        # Hand detection
        frame = detector.findHand(frame)
        landmarks = detector.findPosition(frame)
        
        # Check if hand detected
        if not landmarks:
            print("No hand detected")
            continue
            
        # Safe landmark access
        if len(landmarks) >= 21:
            thumb_tip = landmarks[4]
            index_tip = landmarks[8]
        else:
            print("Warning: Incomplete landmark detection")
            continue
            
except KeyboardInterrupt:
    print("Application terminated by user")
except Exception as e:
    print(f"Error: {e}")
finally:
    cap.release()
    cv2.destroyAllWindows()
```

### Best Practices

1. **Always check return values:**
```python
landmarks = detector.findPosition(frame)
if landmarks and len(landmarks) >= 21:
    # Safe to access landmarks
    process_landmarks(landmarks)
```

2. **Handle camera errors gracefully:**
```python
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Cannot access camera")
    exit(1)
```

3. **Use try-except for robust applications:**
```python
try:
    distance, frame, cx, cy = detector.findDistance(frame, 4, 8)
    if distance is not None:
        process_distance(distance)
except Exception as e:
    print(f"Distance calculation failed: {e}")
```

## Usage Examples

### Basic Hand Tracking

```python
import cv2
import Hand_detection_module as hdm

detector = hdm.HandDetection(min_detection_confidence=0.7)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
        
    # Detect and draw hands
    frame = detector.findHand(frame)
    
    # Get landmark positions
    landmarks = detector.findPosition(frame, draw=False)
    
    if landmarks:
        # Print thumb tip position
        thumb_tip = landmarks[4]
        print(f"Thumb tip: {thumb_tip}")
    
    cv2.imshow("Hand Tracking", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

### Gesture Recognition

```python
import cv2
import Hand_detection_module as hdm

detector = hdm.HandDetection()
cap = cv2.VideoCapture(0)

gesture_names = ["Fist", "Thumb", "Peace", "OK", "Stop"]

while True:
    ret, frame = cap.read()
    if not ret:
        break
        
    frame = detector.findHand(frame)
    fingers = detector.handUp(frame)
    
    if fingers:
        fingers_up = sum(fingers)
        
        # Simple gesture recognition
        if fingers_up == 0:
            gesture = "Fist"
        elif fingers == [1, 0, 0, 0, 0]:
            gesture = "Thumbs Up"
        elif fingers == [0, 1, 1, 0, 0]:
            gesture = "Peace Sign"
        elif fingers_up == 5:
            gesture = "Open Palm"
        else:
            gesture = f"{fingers_up} fingers up"
            
        cv2.putText(frame, gesture, (10, 50), 
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    cv2.imshow("Gesture Recognition", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

### Distance-Based Control

```python
import cv2
import numpy as np
import Hand_detection_module as hdm

detector = hdm.HandDetection()
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
        
    frame = detector.findHand(frame)
    
    # Calculate distance between thumb and index finger
    distance, frame, cx, cy = detector.findDistance(frame, 4, 8)
    
    if distance is not None:
        # Map distance to a value (e.g., volume, brightness)
        min_dist, max_dist = 20, 200
        control_value = np.interp(distance, [min_dist, max_dist], [0, 100])
        
        # Visual feedback
        cv2.putText(frame, f"Control: {int(control_value)}%", 
                   (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        # Change color based on distance
        if distance < 30:
            color = (0, 0, 255)  # Red - Close
        elif distance > 150:
            color = (0, 255, 0)  # Green - Far
        else:
            color = (255, 0, 255)  # Magenta - Medium
            
        cv2.circle(frame, (cx, cy), 15, color, -1)
    
    cv2.imshow("Distance Control", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

## Integration Guide

### Integrating with Existing Applications

```python
# your_app.py
import Hand_detection_module as hdm

class GestureController:
    def __init__(self):
        self.detector = hdm.HandDetection(min_detection_confidence=0.7)
        self.gesture_callbacks = {}
    
    def register_gesture(self, gesture_name, callback):
        """Register a callback for a specific gesture"""
        self.gesture_callbacks[gesture_name] = callback
    
    def process_frame(self, frame):
        """Process a single frame and trigger callbacks"""
        frame = self.detector.findHand(frame)
        fingers = self.detector.handUp(frame)
        
        if fingers:
            gesture = self.recognize_gesture(fingers)
            if gesture in self.gesture_callbacks:
                self.gesture_callbacks[gesture]()
        
        return frame
    
    def recognize_gesture(self, fingers):
        """Convert finger state to gesture name"""
        if fingers == [1, 0, 0, 0, 0]:
            return "thumbs_up"
        elif fingers == [0, 1, 1, 0, 0]:
            return "peace"
        elif sum(fingers) == 0:
            return "fist"
        elif sum(fingers) == 5:
            return "open_palm"
        return "unknown"

# Usage
def on_thumbs_up():
    print("Thumbs up detected!")

def on_peace():
    print("Peace sign detected!")

controller = GestureController()
controller.register_gesture("thumbs_up", on_thumbs_up)
controller.register_gesture("peace", on_peace)

# In your main loop
frame = controller.process_frame(frame)
```

### Threading for Performance

```python
import threading
import queue
import cv2
import Hand_detection_module as hdm

class ThreadedGestureDetector:
    def __init__(self):
        self.detector = hdm.HandDetection()
        self.frame_queue = queue.Queue(maxsize=2)
        self.result_queue = queue.Queue(maxsize=2)
        self.running = False
    
    def start(self):
        self.running = True
        self.thread = threading.Thread(target=self._process_frames)
        self.thread.start()
    
    def stop(self):
        self.running = False
        if hasattr(self, 'thread'):
            self.thread.join()
    
    def add_frame(self, frame):
        if not self.frame_queue.full():
            self.frame_queue.put(frame)
    
    def get_result(self):
        if not self.result_queue.empty():
            return self.result_queue.get()
        return None
    
    def _process_frames(self):
        while self.running:
            try:
                frame = self.frame_queue.get(timeout=0.1)
                
                # Process frame
                processed_frame = self.detector.findHand(frame)
                landmarks = self.detector.findPosition(frame, draw=False)
                fingers = self.detector.handUp(frame)
                
                result = {
                    'frame': processed_frame,
                    'landmarks': landmarks,
                    'fingers': fingers
                }
                
                if not self.result_queue.full():
                    self.result_queue.put(result)
                    
            except queue.Empty:
                continue
            except Exception as e:
                print(f"Processing error: {e}")

# Usage
detector = ThreadedGestureDetector()
detector.start()

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Add frame for processing
    detector.add_frame(frame.copy())
    
    # Get processed result
    result = detector.get_result()
    if result:
        cv2.imshow("Gesture Detection", result['frame'])
        if result['fingers']:
            print(f"Fingers: {result['fingers']}")
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

detector.stop()
cap.release()
cv2.destroyAllWindows()
```

## Performance Considerations

### Optimization Tips

1. **Reduce frame resolution** for better performance:
```python
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
```

2. **Skip frames** for real-time applications:
```python
frame_skip = 2
frame_count = 0

while True:
    ret, frame = cap.read()
    frame_count += 1
    
    if frame_count % frame_skip != 0:
        continue  # Skip processing this frame
        
    # Process frame
    frame = detector.findHand(frame)
```

3. **Process only when needed**:
```python
# Only process landmarks when hand is detected
frame = detector.findHand(frame, flag=False)
if detector.results.multi_hand_landmarks:
    landmarks = detector.findPosition(frame)
```

### Memory Management

```python
import gc

# Periodic garbage collection for long-running applications
frame_count = 0
while True:
    # ... process frames ...
    
    frame_count += 1
    if frame_count % 1000 == 0:  # Every 1000 frames
        gc.collect()
```