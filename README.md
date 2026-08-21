# Wish9000
**MISSION:** 👉 Share the 'grants' 😏 supporting our TOTAL PYTHONEERING 🤠 Wish List. 🔮

This **Wish9000** package provides a robust, production-grade toolset designed to simplify local development, preserve data integrity, and bridge the gap between structured code and human readability. 

The suite contains two core modules:
1. **Juman** (`juman.py`): A human-centric JSON handler that unpacks and normalizes multi-line plain old text strings (POTS) into clean, visually aligned layouts across Mac (`\r`), Windows (`\r\n`), and POSIX (`\n`) newline formats.
2. **TempFile** (`tempfile.py`): A fully integrated backup and file lifecycle strategy that secures files and preserves metadata before destructive data transitions.

## 🚀 Features

### 📄 Juman (JSON for Humans)
- **Newline Normalization** - Automatically cleans up erratic cross-platform carriage returns (`\r\n`, `\r`) during data ingestion.
- **Visual Block Indentation** - Replaces unreadable escaped string newlines (`\n`) with beautiful, block-aligned physical space lines for easier git diffs and human editing.
- **Safe Evaluation** - Gracefully handles raw internal text sequences without tripping standard library json parsers.
- **Fail-Safe Processing** - Couples writing workflows directly with automated snapshot architecture.

### 🛡️ TempFile Strategy
- **Metadata Preservation** - Clones your vital assets into backups while retaining original system timestamps and permissions.
- **Collision Immunity** - Guarantees unique file generation by dynamically resolving duplicate name conflicts.
- **Directory Scrubbing** - Sweeps, counts, and systematically purges lifecycle-ended temp files with pinpoint accuracy.

## 📊 Visual Transformation Example

When standard JSON formatters write multi-line text strings, they escape the newlines into a single, hard-to-read line. **Juman** expands these escaped characters into physical, properly indented lines that humans can read and edit directly in any text editor.

### Standard JSON Output (Hard to read/edit)
```json
{
    "game_title": "PyQuest",
    "intro_dialogue": "Line 1: Welcome Hero!\nLine 2: Your adventure awaits.\nLine 3: Choose your path wisely."
}
```

### Juman Formatted Output (Human-readable Block Alignment)
```json
{
    "game_title": "PyQuest",
    "intro_dialogue": "Line 1: Welcome Hero!
    Line 2: Your adventure awaits.
    Line 3: Choose your path wisely."
}
```

## 🛠️ Tech Stack

- **Language:** Python 3 (built and verified with `python3`)
- **Core Modules:** `json`, `re`, `os`, `shutil`, `datetime`, `pathlib`

## 📦 Installation

Ensure your local development environment runs **Python 3.x**. 

1. **Download and unpack the .zip file, then:**
   ```bash
   cd wish9000
   ```

2. **Structure:**
   Keep `juman.py` and `tempfile.py` within the same package or directory path so `Juman` can resolve its automated tracking logic.

## 💡 Usage Examples

### Reading and Writing Human-Readable JSON Data

```python
from juman import Juman

config_file = "config/pyquest_data.json"
handler = Juman(config_file)

# 1. Read structural JSON safely regardless of native OS line endings
success, raw_data = handler.hread()
if success:
    print("Ingested structure successfully:", raw_data)
    
    # Modify data or insert text blocks with raw python newlines
    raw_data["intro_dialogue"] = "Line 1: Welcome Hero!\nLine 2: Your adventure awaits."

    # 2. Write it out cleanly. Auto-creates a backup file first!
    write_success, output_string = handler.hwrite(raw_data, auto_backup=True)
    if write_success:
        print("Data saved. Escaped newlines converted into formatted text blocks.")
```

### Manual Temp File Lifecycle Management

```python
from tempfile import TempFile

target_asset = "config/pyquest_data.json"

# Check active temp footprints or clear up directory spaces manually
if TempFile.has_backups(target_asset):
    total_temps = TempFile.count_backups(target_asset)
    print(f"Discovered {total_temps} tracking backups.")
    
    # Clear out files starting with ~ when workspace processing wraps up
    TempFile.cleanup(target_asset)
    print("Workspace cleaned.")
```

## 🤝 Contributing

1. **Fork** the Project
2. Create your **Feature Branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit** your Changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the Branch (`git push origin feature/AmazingFeature`)
5. Open a **Pull Request**

## 📄 License

Distributed under the **MIT License**. See the `LICENSE` file for details.

## ✉️ Contact

- **Author / Publisher:** TOTAL PYTHONEERING
- **Project Link:** [Wish9000](https://github.com/TotalPythoneering/Wish9000)

