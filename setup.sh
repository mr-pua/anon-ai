#!/usr/bin/env bash

# ------------------------------------------------------------------
#  ANONAI CLI Setup - Spinners & Structure
# ------------------------------------------------------------------

# Stylish formatting
BOLD=$(tput bold)
RESET=$(tput sgr0)
RED=$(tput setaf 1)
GREEN=$(tput setaf 2)
CYAN=$(tput setaf 6)
MAGENTA=$(tput setaf 5)
YELLOW=$(tput setaf 3)

# 1-second spinner with task message
spinner() {
  local msg=$1
  echo -ne "  ${CYAN}⏳${RESET} ${YELLOW}${msg}${RESET}"
  sleep 1
  echo -ne "\r  ${GREEN}✓${RESET} ${YELLOW}${msg}${RESET}    \r"
}

# Show folder structure
show_structure() {
  echo -e "\n${MAGENTA}📁 Project Structure:${RESET}"
  tree -L 2 -I "__pycache__|*.pyc" 2>/dev/null || find . -maxdepth 2 -type d | sed -e "s/[^-][^\/]*\//  │ /g" -e "s/│ \([^ ]\)/│─ \1/"
}

# Killer banner
show_banner() {
  clear
  echo -e "${CYAN}"
  cat << "EOF"
 ▄▄▄·  ▐ ▄        ▐ ▄      ▄▄▄· ▪  
▐█ ▀█ •█▌▐█▪     •█▌▐█    ▐█ ▀█ ██ 
▄█▀▀█ ▐█▐▐▌ ▄█▀▄ ▐█▐▐▌    ▄█▀▀█ ▐█·
▐█ ▪▐▌██▐█▌▐█▌.▐▌██▐█▌    ▐█ ▪▐▌▐█▌
 ▀  ▀ ▀▀ █▪ ▀█▄▀▪▀▀ █▪     ▀  ▀ ▀▀▀
                        by : Mr. Pua
EOF
  echo -e "${RESET}"
  printf "%b" "${MAGENTA}╭───────────────────────────────────────╮\n"
  printf "%b" "│ ${BOLD}${YELLOW}⚡  AnonAI CLI Setup Wizard  ${RESET}${MAGENTA}│\n"
  printf "%b" "╰───────────────────────────────────────╯${RESET}\n\n"
}

# Main setup
run_setup() {
  spinner "Checking Python environment"
  python3 --version >/dev/null 2>&1 || {
    echo -e "\n${RED}✗ Python3 required!${RESET}"
    exit 1
  }

  spinner "Installing dependencies"
  pip3 install -r requirements.txt >/dev/null 2>&1

  spinner "Setting executable permissions"
  chmod +x src/cli.py

  spinner "Verifying folder structure"
  show_structure
}

# Post-install
show_instructions() {
  cat << EOF

${BOLD}${GREEN}✅ Setup Complete!${RESET}

${CYAN}First Steps:${RESET}
1. Set your API key:
   ${MAGENTA}echo 'export OPENROUTER_API_KEY="your_key"' >> ~/.bashrc${RESET}
   ${MAGENTA}source ~/.bashrc${RESET}

2. Run the CLI:
   ${YELLOW}./src/cli.py${RESET}

${BOLD}Key Commands:${RESET}
  /help    Show all commands
  /model   Change AI model
  /clear   Reset conversation

${CYAN}└──────────────────────────────────────┘${RESET}
${BOLD}Enjoy your AI-powered terminal! 🚀${RESET}
EOF
}

# Execute
show_banner
run_setup
show_instructions