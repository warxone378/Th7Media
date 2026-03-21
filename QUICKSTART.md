# 🚀 Quick Deploy to Render

## 1-Minute Setup

### Step 1: Push to GitHub
```bash
cd /mnt/okcomputer/output/th7media
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/th7media.git
git push -u origin main
```

### Step 2: Deploy on Render
1. Go to [dashboard.render.com](https://dashboard.render.com)
2. Click **"New +"** → **"Blueprint"**
3. Connect your GitHub repo
4. Click **"Apply"**

### Done! 🎉
Your site will be live at: `https://th7media.onrender.com`

---

## Files for Render

| File | Purpose |
|------|---------|
| `render.yaml` | Auto-deployment config |
| `wsgi.py` | Production entry point |
| `requirements.txt` | Python dependencies (+gunicorn) |

---

## Updating Your Site

```bash
git add .
git commit -m "Your changes"
git push origin main
```

Render auto-redeploys on every push!

---

## Troubleshooting

| Issue | Fix |
|-------|-----|
| Build fails | Check logs in Render Dashboard |
| 500 errors | Verify `SECRET_KEY` env var is set |
| Static files 404 | Clear browser cache (Ctrl+Shift+R) |

---

For detailed instructions, see [DEPLOY.md](./DEPLOY.md)
