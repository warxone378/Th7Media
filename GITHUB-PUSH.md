# Push Th7media to GitHub - Quick Guide

## Option 1: One-Command Script (Easiest)

```bash
cd /mnt/okcomputer/output/th7media
bash push-to-github.sh YOUR_GITHUB_USERNAME
```

**Example:**
```bash
bash push-to-github.sh johndoe
```

---

## Option 2: Manual Commands

### Step 1: Go to project folder
```bash
cd /mnt/okcomputer/output/th7media
```

### Step 2: Initialize Git
```bash
git init
```

### Step 3: Add all files
```bash
git add .
```

### Step 4: Commit
```bash
git commit -m "Initial commit"
```

### Step 5: Add GitHub remote
Replace `YOUR_USERNAME` with your GitHub username:

```bash
git remote add origin https://github.com/YOUR_USERNAME/th7media.git
```

### Step 6: Push
```bash
git branch -M main
git push -u origin main
```

---

## Option 3: GitHub CLI (Fastest if installed)

```bash
cd /mnt/okcomputer/output/th7media
gh repo create th7media --public --source=. --push
```

---

## Prerequisites

Before pushing, make sure:

1. **You have a GitHub account** → [Sign up](https://github.com/signup)

2. **Create an empty repository** on GitHub:
   - Go to [github.com/new](https://github.com/new)
   - Name: `th7media`
   - **Uncheck** "Add a README file"
   - Click "Create repository"

3. **Git is installed** (check with `git --version`)

---

## After Pushing

Your code will be at: `https://github.com/YOUR_USERNAME/th7media`

### Next: Deploy to Render

1. Go to [dashboard.render.com](https://dashboard.render.com)
2. Click **"New +"** → **"Blueprint"**
3. Connect your `th7media` repo
4. Click **"Apply"**

Done! 🎉 Your site will be live.

---

## Troubleshooting

### "Repository not found"
Create the repo on GitHub first (without README).

### "Permission denied"
Use a personal access token or SSH key.

### "fatal: not a git repository"
Run `git init` first.

### "failed to push some refs"
Pull first: `git pull origin main --rebase`

---

## Full Workflow Summary

```bash
# 1. Go to project
cd /mnt/okcomputer/output/th7media

# 2. Use the script
bash push-to-github.sh YOUR_USERNAME

# 3. Deploy on Render
# Go to: https://dashboard.render.com
```

That's it! 🚀
