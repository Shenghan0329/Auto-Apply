# Auto Apply Job Boards

Automatically apply to jobs based on your preferences through command line interface.

## How to Use

1. Run the application
2. Enter your desired position type when prompted
3. Enter your preferred job category when prompted
4. The app will automatically apply to matching positions for you

## Current Status

* **Supported Job Boards:** shixiseng.com
* **Expansion:** Actively adding support for additional job boards

## Setup

1. **Create `.env` file** in the project root directory:
   ```env
   DRIVER_LOCATION="path/to/your/chromedriver"
   PROFILE_LOCATION="path/to/your/chrome/profile"
   ```
2. **Find your Chrome profile and driver location:**
   * Use a Chrome profile with job board auth sessions
   * Open Chrome and go to `chrome://version/`
   * Copy the "Profile Path" value to `PROFILE_LOCATION`
   * Set the path to `DRIVER_LOCATION`

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py

# Follow the command line prompts to set your preferences
```

*Note: Ensure you have configured your .env file before running the application.*
