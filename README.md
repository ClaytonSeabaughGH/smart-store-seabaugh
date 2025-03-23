# Smart Store Seabaugh

## Smart Sales Starter Files
Starter files to initialize the Smart Sales project.

## Project Setup Guide

### **1. Mac/Linux Setup**
Run all commands from a terminal in the root project folder.

#### **Step 1A - Create a Local Project Virtual Environment**
```sh
python3 -m venv .venv
```

#### **Step 1B - Activate the Virtual Environment**
```sh
source .venv/bin/activate
```

#### **Step 1C - Install Required Packages**
```sh
python3 -m pip install --upgrade -r requirements.txt
```

#### **Step 1D - Optional: Verify Virtual Environment Setup**
```sh
python3 -m datafun_venv_checker.venv_checker
```

#### **Step 1E - Run the Initial Project Script**
```sh
python3 scripts/data_prep.py
```

---

### **2. Windows Setup**
Run all commands from a PowerShell terminal in the root project folder.

#### **Step 2A - Create a Local Project Virtual Environment**
```powershell
py -m venv .venv
```

#### **Step 2B - Activate the Virtual Environment**
```powershell
.venv\Scripts\activate
```

#### **Step 2C - Install Required Packages**
```powershell
py -m pip install --upgrade -r requirements.txt
```

#### **Step 2D - Optional: Verify Virtual Environment Setup**
```powershell
py -m datafun_venv_checker.venv_checker
```

#### **Step 2E - Run the Initial Project Script**
```powershell
py scripts/data_prep.py
```

---

## **Initial Package List**
The following Python packages are required for this project:

- `pip`
- `loguru`
- `ipykernel`
- `jupyterlab`
- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`
- `plotly`
- `pyspark==4.0.0.dev1`
- `pyspark[sql]`
- `git+https://github.com/denisecase/datafun-venv-checker.git#egg=datafun_venv_checker`

---

## **Git Workflow**
After making changes, use the following commands to commit and push updates to GitHub:

```sh
git add .
git commit -m "Update README with commands"
git push
```

Modify the commit message to describe your changes appropriately. Keeping good commit messages is essential for collaboration and tracking changes effectively.

---

### **Markdown Preview**
To preview this `README.md` file in VS Code:
- Open the file.
- Press `Ctrl + Shift + V` (Windows/Linux) or `Cmd + Shift + V` (Mac).
- Alternatively, click the "Open Preview" button in the top-right corner.

---

## **Need Help?**
For issues or troubleshooting, reach out via discussion forums or the project repository.

Happy coding! 🚀

