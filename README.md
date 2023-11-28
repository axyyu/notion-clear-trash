# notion-clear-trash

A simple script to clear the trash in your Notion workspace.

## How to Run the Script

### Prerequisites

- Python
- `pyenv` for Python version management (optional but recommended)
- A Notion account

### Setup

1. **Clone the Repository**
    ```bash
    git clone https://github.com/Renzodef/notion-clear-trash.git
    ```

2. **Install Python 3.10 (Recommended)**
    - If you don't have `pyenv`, install it from [pyenv](https://github.com/pyenv/pyenv#installation).
    - Install Python 3.10 using `pyenv`:
      ```bash
      pyenv install 3.10
      ```

3. **Create and Manage a Virtual Environment (Recommended)**
    - **Create a Virtual Environment:**
      ```bash
      python -m venv venv
      ```
    - **Activate the Virtual Environment:**
      - On Windows:
        ```bash
        .\venv\Scripts\activate
        ```
      - On Linux or MacOS:
        ```bash
        source venv/bin/activate
        ```
    - **Deactivate the Virtual Environment:**
      ```bash
      deactivate
      ```

4. **Install Requirements**
    ```bash
    pip install -r requirements.txt
    ```

5. **Setup Environment Variables**
    - Copy `.env.sample` to a new file named `.env`.
    - Fill in the `NOTION_AUTH_TOKEN` value in the `.env` file with your Notion Auth token (see below for instructions on how to retrieve this).

### How to Retrieve the Notion Auth Token (in Google Chrome Browser or similar)

1. Go to [Notion](https://www.notion.so).
2. Open developer tools (hit F12).
3. Navigate to the Application tab (may be hidden if the developer window is small).
4. Expand Cookies under the Storage section on the sidebar.
5. Click on 'https://www.notion.so' to view all the cookies.
6. Copy the value for the key 'token_v2'.

### Running the Script

1. Ensure you are in the script's directory and the virtual environment is active (if you followed the recommended steps above).
2. Run the script:
    ```bash
    python notion-clear-trash.py
    ```
