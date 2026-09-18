# NEWP 🚀

**NEWP** is a smart CLI tool that eliminates repetitive project setup. It instantly creates structured, production-ready projects with dependencies installed, Git initialized, and best practices applied.

> ⚠️ **Note:** Currently optimized for **Windows**. macOS/Linux support coming soon.

---

## ⚡ Quick Start

Once installed, you can use **NEWP** in two ways:

### 1. Interactive Mode (Wizard)
Perfect for beginners or when you want to explore options.
```bash
newp
```
*Follow the on-screen questions to configure your project.*

### 2. Quick Mode (One-Liner)
For experts who know exactly what they want.
```bash
# Syntax: newp <project-name> <language> [framework] [git-flag]

# Create a Python FastAPI project with Git
newp my-app python fastapi yes

# Create a Python Flask project (No Git)
newp my-app python flask no

# Create a basic Python project (No framework, No Git)
newp my-app python
```

---

## 📦 Installation

### Option A: Install via Pip (Recommended)
Install the latest version directly from GitHub:
```bash
pip install git+https://github.com/ILATRACHE/newp.git
```

### Option B: Local Development Install
1. Clone the repository:
   ```bash
   git clone https://github.com/ILATRACHE/newp.git
   cd newp
   ```
2. Install in editable mode:
   ```bash
   pip install -e .
   ```

---

## ✨ Current Features

### 🐍 Python Projects
NEWP creates a complete Python environment including:
- ✅ **Virtual Environment** (`venv/`) automatically created and activated.
- ✅ **Git Repository** initialized (optional).
- ✅ **Smart Structure**: `src/`, `tests/`, `main.py`.
- ✅ **Dependencies**: `requirements.txt` generated and installed.
- ✅ **Clean Git**: Pre-configured `.gitignore` (ignores `venv/`, `__pycache__`, `.env`).

### 🛠 Supported Frameworks
| Framework | Packages Installed | Description |
| :--- | :--- | :--- |
| **FastAPI** | `fastapi`, `uvicorn` | Modern, high-performance web API framework. |
| **Flask** | `flask` | Lightweight and flexible micro-web framework. |
| **None** | *(Empty)* | Bare-bones structure for custom setups. |

---

## 📋 Requirements

Before using NEWP, ensure you have:
- **OS**: Windows (Tested on Windows 10/11)
- **Python**: Version 3.8 or higher
- **Git**: Installed and added to PATH

---

## 🗺️ Roadmap & Status

**Current Version:** `v0.1.1`

- [x] Interactive Wizard Mode
- [x] Quick Mode (CLI Arguments)
- [x] Python Support (FastAPI, Flask)
- [x] Auto-dependency installation
- [x] Smart `.gitignore` generation
- [ ] React / Node.js Support
- [ ] C++ / CMake Support
- [ ] macOS & Linux Support
- [ ] Custom Template Registry

---

## 🐛 Reporting Issues

Found a bug or have a feature request? Please open an issue on the [GitHub Issues](https://github.com/ILATRACHE/newp/issues) page.

---

**Built by [ILATRACHE](https://github.com/ILATRACHE)**
```