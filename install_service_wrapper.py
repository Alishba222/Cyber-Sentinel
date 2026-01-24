# install_service_wrapper.py - ROBUST VERSION
import os
import sys

# 1. Manually set the environment variable for Django to find the settings file.
# This is required for service execution and installation.
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'

# 2. Add the project root to the Python path.
# This ensures modules like 'config' can be found.
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

# 3. Add the configuration directory (parent of settings.py) to the path.
# This often resolves tricky 'config.settings' import issues.
config_dir = os.path.join(project_root, 'config')
if config_dir not in sys.path:
    sys.path.insert(0, config_dir)

# 4. Initialize Django (which will now use the env var and path additions)
import django
django.setup()

# 5. Import the service script after setup
try:
    import service.service_runner as service_script
except ImportError as e:
    print(f"Error importing service script: {e}")
    sys.exit(1)

# 6. Execute the service command handler, passing all command-line arguments.
# This includes the 'install' command.
# ... (code before main block)

# CRITICAL: Assuming your service class is named 'MLOpsCyberbullyingService' 
# and is defined in service.py
SERVICE_CLASS = service_script.AutoMLService # <-- VERIFY THIS NAME IN service.py

if __name__ == '__main__':
    # Import the utility function directly
    import win32serviceutil

    # Use the utility's handler function, passing the service class and command line args
    # This function handles the 'install' and 'start' commands.
    win32serviceutil.HandleCommandLine(SERVICE_CLASS)