# Wish List

Born out of the livid frustration with managing my [PyQuest](https://github.com/Python3-Training/PyQuest) and Cookpedia data files, this project presently contains two core modules:

## 🚀 Real-World Backup Support
1. **TempFile** (`tempfile.py`):
   
A fully integrated backup and file lifecycle strategy that secures files and preserves metadata before destructive data transitions.

## 🚀 Real-World JSON Support
2. **Juman** (`juman.py`):
   
A human-centric JSON handler that unpacks and normalizes multi-line plain old text strings (POTS) into clean, visually aligned layouts across Mac (`\r`), Windows (`\r\n`), and POSIX (`\n`) newline formats.

## 🚀 Why?

Because the mission of this **Wish9000** package is to share the wish 'grants' herein 🧞 of:

🪄**File Wish 1100:** "I wish I could backup a file that keeps the file time & status."

🪄**File Wish 1101:** "I wish I could tell if there are any backup files."

🪄**File Wish 1102:** "I wish I could tell how many backup files there are."

🪄**File Wish 1103:** "I wish I could delete all of my backup files."

🪄**JSON Wish 1200:** "I wish I could use JSON to easily edit multi-line TEXT."

🪄**JSON Wish 1201:** "I wish I could stop worrying about newlines on Windows."

🪄**JSON Wish 1202:** "I wish I could I had an robust & automatic data backup."

🪄**JSON Wish 1203:** "I wish I could manage any data backups at the command line."

These above now supported by this [TOTAL PYTHONEERING](https://ko-fi.com/randallnagy) 🤠 Project. 🔮

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

- **Author / Publisher:**
  [TOTAL PYTHONEERING](https://ko-fi.com/randallnagy)
- **Project Link:**
  [Wish9000](https://github.com/TotalPythoneering/Wish9000)

