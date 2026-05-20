#!/bin/bash

# ─────────────────────────────────────────
# STEP 1 — Install dependencies
# ─────────────────────────────────────────
pip install requests python-dotenv

# ─────────────────────────────────────────
# STEP 2 — Test the bot locally
# ─────────────────────────────────────────
export $(cat .env | xargs)
python send_announcement.py

# ─────────────────────────────────────────
# STEP 3 — Push to GitHub (run once)
# Replace YOUR_GITHUB_USERNAME and YOUR_REPO_NAME
# ─────────────────────────────────────────

# Initialize git
git init

# Create folder structure for GitHub Actions
mkdir -p .github/workflows
cp announce.yml .github/workflows/announce.yml

# Create .gitignore so .env is never uploaded
echo ".env" > .gitignore

# Commit files
git add send_announcement.py .github/workflows/announce.yml .gitignore
git commit -m "Add Friday food announcement bot"

# Connect to your GitHub repo (create the repo on github.com first)
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main

# ─────────────────────────────────────────
# STEP 4 — Add secrets on GitHub
# Go to: https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME/settings/secrets/actions
# Add these two secrets:
#   TELEGRAM_BOT_TOKEN  →  your bot token
#   TELEGRAM_CHAT_ID    →  your chat id
# ─────────────────────────────────────────

echo "✅ Done! Bot will now run every Friday automatically."
