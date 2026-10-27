
# Open Source Project Health Analytics
## Development Log

This document records the actual development process, implementation progress, technical challenges, and lessons learned throughout the project.

## Project Overview

- **Project name:** Open Source Project Health Analytics
- **Project type:** Data Analytics
- **Tools:** SQL, Python, Power BI, GitHub REST API
- **Primary objective:** Analyze open-source repository health using data-driven metrics.
- **Status:** Initial setup

## Development History

### Session 1 — Project Initialization

**Objective:** Establish the project workspace and documentation structure.

**Actions completed:**
- Created the root project folder.
- Opened the project in Visual Studio Code.
- Created the following directories:
  - `data/`
  - `notebooks/`
  - `src/`
  - `sql/`
  - `powerbi/`
  - `docs/`
- Created the initial project files:
  - `README.md`
  - `.gitignore`
  - `requirements.txt`
- Created documentation files:
  - `DEVELOPMENT_LOG.md`
  - `TROUBLESHOOTING.md`
  - `DECISIONS.md`

**Results:**
- Initial workspace structure established.
- Documentation system created.

**Challenges encountered:**
- No technical errors have been reported so far.

**Lessons learned:**
- A clear directory structure improves maintainability.
- Development documentation should begin at project initialization.

**Next steps:**
- Configure the Python environment.
- Define project dependencies.
- Configure Git and verify the repository setup.
- Plan GitHub API data collection.

---

## Session Log Template

Use this template for each future working session.

### Session [Number] — [Date]

**Objective:**

**Actions performed:**

**Commands executed:**

**Expected results:**

**Actual results:**

**Errors or challenges:**

**Root cause:**

**Solution attempted:**

**Verification results:**

**Lessons learned:**

**Next steps:**

---

### Session 2 — Python Environment Setup

**Objective:**
Verify Python and pip, create an isolated Python environment, and configure Git ignore rules.

**Environment:**
- Operating system: Windows
- Terminal: PowerShell in VS Code
- Python version: 3.15.2
- pip version: 26.2.2
- Project directory: `C:\Users\Administrator\Downloads\Open-Source-Project-Health-Analytics`

**Actions performed:**
- Verified Python using `python --version`.
- Verified pip using `python -m pip --version`.
- Created the `.venv` virtual environment.
- Activated the virtual environment in PowerShell.
- Verified the active Python executable.
- Updated `.gitignore` to exclude the virtual environment, environment variables, and selected local data files.

**Verification evidence:**
- `python --version` returned `Python 3.15.2`.
- `python -m pip --version` returned pip 26.2.2.
- `sys.executable` resolved to `.venv\Scripts\python.exe`.
- The terminal displayed the `(.venv)` environment prefix.

**Issues encountered:**
- No technical errors were reported during these checks.

**Lessons learned:**
- Virtual environments isolate project dependencies.
- Git ignore rules help prevent accidental commits of local files and secrets.

**Next steps:**
- Verify package compatibility with the selected Python version.
- Install and test project dependencies.
- Begin Git repository setup and GitHub API integration.

### Dependency Compatibility Check

**Objective:**
Check whether the declared Python dependencies can be resolved before installation.

**Command executed:**
```powershell
python -m pip install --dry-run -r requirements.txt
```

**Actual result:**
- pip displayed a list of packages under `Would install`.
- No dependency-resolution error was included in the supplied output.
- The dry run did not perform the normal package installation.

**Conclusion:**
The dependency resolution check completed without a reported resolution error in the provided output. Runtime compatibility has not yet been verified.

**Next steps:**
- Install the dependencies inside `.venv`.
- Verify imports and package versions.
- Record any installation or runtime errors.
