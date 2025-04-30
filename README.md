
# 🔍 Edge Detection Live from Webcam

This project streams live video from the webcam and applies various edge detection filters using OpenCV.

---

## 📸 Project Idea

The program captures live frames from the device's camera (internal or USB) and allows real-time application of different edge detection filters such as:
- Sobel X/Y
- Gradient Magnitude
- Laplacian
- Sobel + Threshold (Bonus)
- Gaussian Smoothing (with adjustable sigma)

---

## 🧪 Technologies Used

- Python 3.8+
- OpenCV
- NumPy
- Git + GitHub for version control

---

## 🖥️ How to Run

```bash
python main.py
```

A window will open displaying the live video feed from the webcam.

---

## 🎮 Keyboard Controls

| Key | Function |
|----|----------|
| `o` | Show original frame |
| `x` | Apply Sobel filter in X direction |
| `y` | Apply Sobel filter in Y direction |
| `m` | Display Gradient Magnitude |
| `s` | Apply Sobel + Threshold |
| `l` | Apply Laplacian of Gaussian |
| `+` | Increase Gaussian Blur sigma |
| `-` | Decrease Gaussian Blur sigma |
| `q` | Quit the program |

---

## 📁 Project Structure

```
com_vision_1/
│
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── edge_detector/
│   ├── __init__.py
│   └── edge_detector_app.py
│
├── camera_detection/
│   ├── __init__.py
│   └── find_working_camera.py
│
├── venv/  ← Virtual Environment (excluded from GitHub)
```

---

## ⚙️ Installation Steps

1. Make sure you have Python and Git installed.
2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate the environment:

```bash
# On CMD
venv\Scripts\activate

# On PowerShell
venv\Scripts\Activate.ps1
```

4. Install the dependencies:

```bash
pip install -r requirements.txt
```

5. Run the program:

```bash
python main.py
```

---

## ✅ Features

- Works with internal or external webcams.
- Applies multiple real-time edge detection filters.
- Clean and organized code using OOP principles.

---

## 🔮 Future Improvements

- Add GUI using Tkinter or PyQt.
- Support for video recording and snapshot capturing.
- Enhance filter control via sliders.

---

## 📬 Developer

Created by: [Mohamed Ahmed Abu Zamil]  
GitHub: [https://github.com/MohamedAbuZamil](https://github.com/MohamedAbuZamil)

---

## ⚙️ Quick Dependency Installation

```bash
pip install -r requirements.txt
```

---
