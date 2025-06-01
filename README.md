# SonicBoom - YouTube MP3 Downloader

## Overview
SonicBoom is a simple GUI application that allows you to download audio from YouTube videos as MP3 files. It provides an easy-to-use interface where you can paste a YouTube URL, select an output folder, and download the audio with a single click. The application is built with Python using `tkinter` for the GUI and `yt-dlp` for downloading YouTube audio. It has been packaged into a standalone `.exe` file for Windows users, with `ffmpeg.exe` included for audio conversion.

## Features
- Download YouTube video audio as MP3 files.
- Simple GUI built with `tkinter`.
- Select an output folder for downloaded MP3 files.
- Packaged as a standalone `.exe` for easy usage on Windows without requiring Python.
- Includes `ffmpeg.exe` for audio conversion, so no external installation is needed.

## Prerequisites
- **For the `.exe` Version**:
  - No additional software is required. The `.exe` file includes all dependencies, including `ffmpeg.exe`.
  - A stable internet connection is needed to download YouTube audio.
- **For the Python Script (`SonicBoom.py`)**:
  - Python 3.6 or later.
  - Required Python packages: `yt-dlp`.
  - `ffmpeg.exe` must be placed in the same directory as `SonicBoom.py`.

## Installation

### Using the `.exe` File
1. Download the `SonicBoom.exe` file from the [releases](https://github.com/Nischayabeniwal/SonicBoom-yt-audio-downloader) section of this repository.
2. Place `SonicBoom.exe` in a folder of your choice.
3. Double-click `SonicBoom.exe` to launch the application.
   - Note: Some antivirus software may flag the `.exe` as suspicious due to its network activity. Add an exception to allow it to run.

### Running the Python Script
1. Clone or download this repository:
   ```bash
   git clone https://github.com/Nischayabeniwal/SonicBoom-yt-audio-downloader
   cd SonicBoom
   ```
2. Install the required Python package:
   ```bash
   pip install yt-dlp
   ```
3. Ensure `ffmpeg.exe` is in the same folder as `SonicBoom.py`. The script expects `ffmpeg.exe` to be in the same directory.
4. Run the script:
   ```bash
   python SonicBoom.py
   ```

## Usage
1. Launch the application:
   - Double-click `SonicBoom.exe` (if using the `.exe`).
   - Or run `python SonicBoom.py` (if using the Python script).
2. A GUI window will appear.
3. **Enter a YouTube URL**:
   - Copy the URL of a YouTube video (e.g., `https://www.youtube.com/watch?v=2ydCvkxuNm4`) and paste it into the "YouTube URL" field.
4. **Select an Output Folder**:
   - Click the "Browse" button to choose a folder where the MP3 file will be saved.
5. **Download the MP3**:
   - Click the "Download MP3" button.
   - The status label will show "Downloading... Please wait."
   - Upon completion, the status label will change to "Download completed!" and a success message will pop up.
   - If the download fails, an error message will be displayed.

## Files in the Repository
- `SonicBoom.py`: The main Python script for the application.
- `SonicBoom.exe`: The standalone executable for Windows, bundled with all dependencies.
- `ffmpeg.exe`: The FFmpeg binary required for audio conversion, included for convenience.
- `README.md`: This documentation file.

## Building the `.exe` Yourself
If you want to rebuild the `.exe` from `SonicBoom.py`, follow these steps:
1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```
2. Ensure `ffmpeg.exe` is in the same folder as `SonicBoom.py`.
3. Run PyInstaller to create the `.exe`:
   ```bash
   pyinstaller --onefile --add-data "ffmpeg.exe;." SonicBoom.py
   ```
4. The `SonicBoom.exe` file will be created in the `dist` folder.

## Troubleshooting
- **Antivirus Blocking**:
  - If your antivirus blocks `SonicBoom.exe`, add an exception to allow it to run. The application uses `yt-dlp` to download audio, which may trigger network activity warnings.
- **Download Fails**:
  - Ensure you have a stable internet connection.
  - Check if the YouTube URL is valid and the video is accessible (not region-locked or private).
  - If using the Python script, ensure `yt-dlp` is installed and up-to-date:
    ```bash
    pip install --upgrade yt-dlp
    ```
- **FFmpeg Not Found**:
  - The `.exe` includes `ffmpeg.exe`, but if you’re running the Python script, ensure `ffmpeg.exe` is in the same folder as `SonicBoom.py`.

## Contributing
Contributions are welcome! If you’d like to contribute:
1. Fork this repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit them (`git commit -m "Add your feature"`).
4. Push to your branch (`git push origin feature/your-feature`).
5. Open a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Built with [yt-dlp](https://github.com/yt-dlp/yt-dlp) for YouTube audio downloading.
- Uses [FFmpeg](https://ffmpeg.org/) for audio conversion.
- Created by [Your Name] on June 1, 2025.