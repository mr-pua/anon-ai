# 🌟 AnonAI CLI - Ultimate OpenRouter Interface

![AnonAI CLI Demo](demo.gif) *(Replace with actual demo gif)*

The most powerful command-line interface for OpenRouter.ai, featuring:
- 🚀 Multi-model support
- 💬 Interactive chat with typing effects
- 🔄 Model switching mid-conversation
- 🎨 Beautiful terminal formatting
- 🔒 Privacy-focused design

## 📦 Installation

### Linux/macOS (Bash)
```bash
curl -sSL https://raw.githubusercontent.com/yourusername/anonai-cli/main/setup.sh | bash

Windows (PowerShell)
powershell

irm https://raw.githubusercontent.com/yourusername/anonai-cli/main/setup.ps1 | iex

Manual Installation
Prerequisites

    Python 3.8+

    pip package manager

Step-by-Step

    Clone the repository
    bash

git clone https://github.com/yourusername/anonai-cli.git
cd anonai-cli

Install dependencies
bash

# Linux/macOS
python3 -m pip install -r requirements.txt

# Windows
py -m pip install -r requirements.txt

Set your API key
bash

# Linux/macOS
export OPENROUTER_API_KEY='your_key_here'

# Windows (Powershell)
$env:OPENROUTER_API_KEY='your_key_here'

# Windows (CMD)
set OPENROUTER_API_KEY=your_key_here

Run the CLI
bash

    # Linux/macOS
    python3 src/cli.py

    # Windows
    py src/cli.py

🛠️ Configuration
Custom Models

Edit models.txt to add your preferred models:

nvidia/llama-3.3-nemotron-super-49b-v1:free
meta-llama/llama-3-70b-instruct
openai/gpt-4

Persistent API Key (Optional)

Add to your shell configuration file (~/.bashrc, ~/.zshrc, or ~/.profile):
bash

export OPENROUTER_API_KEY='your_key_here'

🎮 Usage
bash

python3 src/cli.py

Available Commands
Command	Description
/help	Show all commands
/exit	Quit the program
/model	Change AI model
/clear	Clear conversation history
/history	Show conversation history
/new	Start new conversation
/creator	Show creator info
/version	Show version information
🌐 Supported Platforms
OS	Tested Versions	Notes
Ubuntu	20.04 LTS, 22.04 LTS	Native support
Debian	10, 11	
macOS	Monterey (12), Ventura (13)	Requires Xcode tools
Windows	10, 11	PowerShell required
Arch Linux	Latest	
Fedora	36, 37	
🔧 Troubleshooting

Q: Getting ModuleNotFoundError?
bash

# Reinstall requirements
python3 -m pip install --force-reinstall -r requirements.txt

Q: API key not working?
bash

# Verify key is set
echo $OPENROUTER_API_KEY  # Linux/macOS
echo %OPENROUTER_API_KEY% # Windows CMD

📜 License

MIT License - See LICENSE
🙏 Attribution

This project uses the OpenRouter API
