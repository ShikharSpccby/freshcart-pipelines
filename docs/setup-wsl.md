# WSL Ubuntu setup

Run these commands in Ubuntu/WSL:

```bash
sudo apt update
sudo apt upgrade -y
sudo apt install -y git python3 python3-pip python3-venv python3-dev build-essential curl unzip tree
git --version
python3 --version
mkdir -p ~/freshcart-pipelines
cd ~/freshcart-pipelines
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip setuptools wheel
```

If `python3 --version` is not Python 3.12, do not change the system Python blindly. Confirm the Ubuntu release and available Python versions first.

After extracting the starter archive into this directory:

```bash
python -m pip install -r requirements.txt
cp .env.example .env
PYTHONPATH=. pytest -v
code .
```

If `code .` is unavailable, install/enable the VS Code WSL extension and reopen the folder using VS Code's **WSL: Open Folder** command.
