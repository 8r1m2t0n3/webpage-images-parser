# Images from DevTools Parser

Allows downloading all viewed images from a webpage using a HAR file from DevTools.

## Instructions

1. Open DevTools by pressing **F12**, then go to **Network -> Images**.
2. Refresh the webpage and scroll down to load all the required images.
3. Right-click on any image in DevTools, select **Copy -> Copy all as HAR**. This will copy the HAR file to your clipboard.
4. Create a file named `har.txt` in the same directory as `parser-script.py`, and paste the copied HAR data into this file.
5. Run `parser-script.py` from this directory.
6. All images will be saved to an **Images** folder within the same directory as the script.
