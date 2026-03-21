#!/bin/bash
# Push Th7media to GitHub - One Command Deploy Script
# Usage: bash push-to-github.sh YOUR_GITHUB_USERNAME

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Check if username provided
if [ -z "$1" ]; then
    echo -e "${RED}Error: Please provide your GitHub username${NC}"
    echo -e "Usage: ${YELLOW}bash push-to-github.sh YOUR_GITHUB_USERNAME${NC}"
    exit 1
fi

GITHUB_USERNAME=$1
REPO_NAME="th7media"

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}  Th7media - GitHub Push Script${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo -e "${RED}Git is not installed. Please install git first.${NC}"
    exit 1
fi

# Navigate to project directory
cd "$(dirname "$0")"
PROJECT_DIR=$(pwd)
echo -e "${YELLOW}Project directory: ${PROJECT_DIR}${NC}"

# Initialize git if not already
echo -e "${BLUE}[1/6] Initializing Git repository...${NC}"
if [ -d ".git" ]; then
    echo -e "${GREEN}Git already initialized ✓${NC}"
else
    git init
    echo -e "${GREEN}Git initialized ✓${NC}"
fi

# Configure git (if not already set)
echo -e "${BLUE}[2/6] Checking Git configuration...${NC}"
if ! git config user.name &> /dev/null; then
    echo -e "${YELLOW}Please enter your Git name:${NC}"
    read GIT_NAME
    git config user.name "$GIT_NAME"
fi

if ! git config user.email &> /dev/null; then
    echo -e "${YELLOW}Please enter your Git email:${NC}"
    read GIT_EMAIL
    git config user.email "$GIT_EMAIL"
fi
echo -e "${GREEN}Git configured ✓${NC}"

# Add all files
echo -e "${BLUE}[3/6] Adding files to Git...${NC}"
git add .
echo -e "${GREEN}Files added ✓${NC}"

# Commit
echo -e "${BLUE}[4/6] Committing changes...${NC}"
git commit -m "Initial commit: Th7media portfolio website with Flask

Features:
- Portfolio showcase with project filtering
- Learning Lab with Python, HTML/CSS, JS tracks
- Progress tracking system
- Contact form
- Dark mode minimalist design
- Mobile responsive

Ready for Render deployment" || echo -e "${YELLOW}Nothing to commit (or commit already exists)${NC}"
echo -e "${GREEN}Committed ✓${NC}"

# Add remote
echo -e "${BLUE}[5/6] Setting up GitHub remote...${NC}"
REMOTE_URL="https://github.com/${GITHUB_USERNAME}/${REPO_NAME}.git"

# Remove existing remote if exists
git remote remove origin 2>/dev/null || true

git remote add origin "$REMOTE_URL"
echo -e "${GREEN}Remote added: ${REMOTE_URL} ✓${NC}"

# Push to GitHub
echo -e "${BLUE}[6/6] Pushing to GitHub...${NC}"
git branch -M main

# Try to push
if git push -u origin main; then
    echo ""
    echo -e "${GREEN}========================================${NC}"
    echo -e "${GREEN}  SUCCESS! 🎉${NC}"
    echo -e "${GREEN}========================================${NC}"
    echo ""
    echo -e "Your code is now on GitHub:"
    echo -e "${YELLOW}https://github.com/${GITHUB_USERNAME}/${REPO_NAME}${NC}"
    echo ""
    echo -e "${BLUE}Next step - Deploy to Render:${NC}"
    echo -e "1. Go to ${YELLOW}https://dashboard.render.com${NC}"
    echo -e "2. Click ${YELLOW}'New +' → 'Blueprint'${NC}"
    echo -e "3. Connect your ${REPO_NAME} repository"
    echo -e "4. Click ${YELLOW}'Apply'${NC}"
    echo ""
    echo -e "Your site will be live at: ${YELLOW}https://${REPO_NAME}.onrender.com${NC}"
    echo ""
else
    echo ""
    echo -e "${RED}========================================${NC}"
    echo -e "${RED}  PUSH FAILED${NC}"
    echo -e "${RED}========================================${NC}"
    echo ""
    echo -e "${YELLOW}Common fixes:${NC}"
    echo -e "1. Create the repository first on GitHub:"
    echo -e "   ${BLUE}https://github.com/new${NC}"
    echo -e "   Name it: ${REPO_NAME}"
    echo -e "   (Don't initialize with README)"
    echo ""
    echo -e "2. Or use GitHub CLI:"
    echo -e "   ${BLUE}gh repo create ${REPO_NAME} --public --source=. --push${NC}"
    echo ""
    echo -e "3. Check your credentials:"
    echo -e "   ${BLUE}git config --global user.name${NC}"
    echo -e "   ${BLUE}git config --global user.email${NC}"
    echo ""
fi
