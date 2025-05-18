#!/usr/bin/env python3
"""
 ▄▄▄·  ▐ ▄        ▐ ▄      ▄▄▄· ▪  
▐█ ▀█ •█▌▐█▪     •█▌▐█    ▐█ ▀█ ██ 
▄█▀▀█ ▐█▐▐▌ ▄█▀▄ ▐█▐▐▌    ▄█▀▀█ ▐█·
▐█ ▪▐▌██▐█▌▐█▌.▐▌██▐█▌    ▐█ ▪▐▌▐█▌
 ▀  ▀ ▀▀ █▪ ▀█▄▀▪▀▀ █▪     ▀  ▀ ▀▀▀
                        by : Mr. Pua
"""

import os
import sys
import json
import time
import readline
from typing import List, Dict, Optional
from dataclasses import dataclass
import requests

@dataclass
class CLITheme:
    """Terminal theme configuration"""
    primary: str = '\033[96m'  # Cyan
    secondary: str = '\033[95m'  # Magenta
    success: str = '\033[92m'  # Green
    warning: str = '\033[93m'  # Yellow
    error: str = '\033[91m'  # Red
    reset: str = '\033[0m'
    bold: str = '\033[1m'

class AnonAICLI:
    def __init__(self):
        self.theme = CLITheme()
        self.api_key = os.getenv("OPENROUTER_API_KEY")
        self.models = self._load_models()
        self.current_model = None
        self.conversation = []
        self.metadata = {
            'version': '2.0.0',
            'author': 'AnonAI Team',
            'github': 'https://github.com/yourusername/anonai-cli'
        }
        self.commands = {
            '/help': 'Show all commands',
            '/exit': 'Exit the program',
            '/clear': 'Reset conversation',
            '/model': 'Change AI model',
            '/history': 'View conversation',
            '/info': 'Show system info',
            '/new': 'Start fresh session'
        }

    def _load_models(self) -> Dict[str, str]:
        """Load available models with enhanced error handling"""
        try:
            with open('models.txt', 'r') as f:
                return {str(i): line.strip() 
                        for i, line in enumerate(f.readlines(), 1) 
                        if line.strip()}
        except FileNotFoundError:
            default_models = {
                '1': 'nvidia/llama-3.3-nemotron-super-49b-v1:free',
                '2': 'meta-llama/llama-4-maverick:free',
                '3': 'google/gemma-3-12b-it:free'
            }
            with open('models.txt', 'w') as f:
                f.writelines(f"{m}\n" for m in default_models.values())
            return default_models

    def _styled_text(self, text: str, style: str) -> str:
        """Apply styled formatting to text"""
        return f"{getattr(self.theme, style, '')}{text}{self.theme.reset}"

    def _clear_screen(self):
        """Clear terminal with cross-platform support"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def _show_banner(self):
        """Display animated banner"""
        self._clear_screen()
        print(self._styled_text(r"""
 ▄▄▄·  ▐ ▄        ▐ ▄      ▄▄▄· ▪  
▐█ ▀█ •█▌▐█▪     •█▌▐█    ▐█ ▀█ ██ 
▄█▀▀█ ▐█▐▐▌ ▄█▀▄ ▐█▐▐▌    ▄█▀▀█ ▐█·
▐█ ▪▐▌██▐█▌▐█▌.▐▌██▐█▌    ▐█ ▪▐▌▐█▌
 ▀  ▀ ▀▀ █▪ ▀█▄▀▪▀▀ █▪     ▀  ▀ ▀▀▀
                        by : Mr. Pua
""", 'primary'))
        print(self._styled_text("┌──────────────────────────────────────────────┐", 'secondary'))
        print(self._styled_text(f"│ {self.theme.bold}🚀  AI-Powered Terminal Interface v{self.metadata['version']}  │", 'secondary'))
        print(self._styled_text("└──────────────────────────────────────────────┘", 'secondary'))
        print()

    def _typing_effect(self, text: str, style: str = 'primary', speed: float = 0.015):
        """Enhanced typing animation with clean formatting"""
        text = text.replace('**', '').replace('`', '')
        for char in text:
            print(self._styled_text(char, style), end='', flush=True)
            time.sleep(speed)
        print()

    def _show_help(self):
        """Display formatted help menu"""
        help_text = "\n" + self._styled_text("Available Commands:", 'primary') + "\n"
        for cmd, desc in self.commands.items():
            help_text += f"  {self._styled_text(cmd, 'warning')}: {desc}\n"
        self._typing_effect(help_text, 'secondary')

    def _select_model(self) -> Optional[str]:
        """Interactive model selection with visual feedback"""
        self._clear_screen()
        print(self._styled_text("Available AI Models:", 'primary'))
        for num, model in self.models.items():
            print(f"  {self._styled_text(num, 'warning')}: {model}")
        
        while True:
            choice = input("\n" + self._styled_text("Select model (1-9): ", 'primary')).strip()
            if choice in self.models:
                return self.models[choice]
            print(self._styled_text("Invalid selection. Please try again.", 'error'))

    def _api_request(self, payload: Dict) -> Dict:
        """Enhanced API request handler"""
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": self.metadata['github']
        }

        try:
            response = requests.post(
                url="https://openrouter.ai/api/v1/chat/completions",
                headers=headers,
                json=payload,
                timeout=15
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            self._typing_effect(f"API Error: {str(e)}", 'error')
            return None

    def run(self):
        """Main application flow"""
        if not self.api_key:
            print(self._styled_text(
                "API Key Required!\n"
                "Set your OpenRouter API key first:\n"
                "export OPENROUTER_API_KEY='your_key_here'", 'error'))
            sys.exit(1)

        self.current_model = self._select_model()
        if not self.current_model:
            sys.exit(1)

        self._show_banner()

        while True:
            try:
                user_input = input(self._styled_text("\nYou: ", 'success')).strip()
                
                if not user_input:
                    continue
                    
                if user_input.startswith('/'):
                    if self._handle_command(user_input.lower()):
                        break
                    continue

                self.conversation.append({"role": "user", "content": user_input})
                
                response = self._api_request({
                    "model": self.current_model,
                    "messages": self.conversation[-10:]
                })

                if response:
                    try:
                        reply = response["choices"][0]["message"]["content"]
                        self._typing_effect(f"AI: {reply}", 'primary')
                        self.conversation.append({"role": "assistant", "content": reply})
                    except KeyError:
                        self._typing_effect("Error processing response", 'error')

            except (KeyboardInterrupt, EOFError):
                self._typing_effect("\nSession ended.", 'warning')
                break

    def _handle_command(self, command: str) -> bool:
        """Command processor with enhanced feedback"""
        if command == "/exit":
            self._typing_effect("Goodbye! Closing session...", 'warning')
            return True
        elif command == "/help":
            self._show_help()
        elif command == "/clear":
            self.conversation = []
            self._typing_effect("Conversation reset.", 'success')
        elif command == "/model":
            if new_model := self._select_model():
                self.current_model = new_model
                self._typing_effect(f"Model changed to: {self.current_model}", 'success')
        elif command == "/history":
            self._show_conversation()
        elif command == "/info":
            self._show_system_info()
        elif command == "/new":
            self.conversation = []
            self._typing_effect("New session started.", 'success')
        else:
            self._typing_effect("Unknown command. Type /help for options.", 'error')
        return False

    def _show_conversation(self):
        """Display conversation history with styling"""
        if not self.conversation:
            self._typing_effect("No conversation history yet.", 'warning')
            return

        print(self._styled_text("\nConversation History:", 'primary'))
        for i, msg in enumerate(self.conversation[-10:], 1):
            prefix = self._styled_text(f"{msg['role'].title()}:", 
                                     'success' if msg['role'] == 'user' else 'primary')
            print(f"  {i}. {prefix} {msg['content']}")

    def _show_system_info(self):
        """Display system information"""
        info = f"""
{self._styled_text("System Information:", 'primary')}
  {self._styled_text("Version:", 'warning')} {self.metadata['version']}
  {self._styled_text("Author:", 'warning')} {self.metadata['author']}
  {self._styled_text("Model:", 'warning')} {self.current_model}
  {self._styled_text("History:", 'warning')} {len(self.conversation)} messages
"""
        self._typing_effect(info, 'secondary')

if __name__ == "__main__":
    try:
        AnonAICLI().run()
    except Exception as e:
        print(f"\n{CLITheme().error}Critical Error: {e}{CLITheme().reset}")
        sys.exit(1)