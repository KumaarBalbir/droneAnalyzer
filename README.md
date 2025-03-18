Still working on the project...

### To run the project:
1. Clone the repository

```bash
git clone https://github.com/KumaarBalbir/droneAnalyzer.git
```

2. Create a virtual environment in the root directory of the project
On Ubuntu or Debian based systems:
```bash
python3 -m venv <venv_name>
```
On Windows:
```bash
python -m venv <venv_name>
```
3. Activate your virtual environment:
On Ubuntu or Debian based systems:
```bash
source <venv_name>/bin/activate
```
On Windows:
```bash
<venv_name>\Scripts\activate
```

3. Install uv (a fast Python package manager that acts as a drop-in replacement for pip)
```bash
pip install uv
```
4. Install the project dependencies

```bash
uv pip install -r pyproject.toml
```

3. Run the project
```bash 
streamlit run main.py --server.port 5000
```

4. View the project in your browser
```bash
http://localhost:5000
```

