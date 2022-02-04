# Install virtual environment and dependencies

    virtualenv minimalgui
    source minimalgui/bin/activate
    pip install -r requirements.txt

# compile resources

Needed to make the ui files available to the application

    cd resources
    python recompile_resources.ui

# start GUI

    python main.py