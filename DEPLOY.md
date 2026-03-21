# Deploy Th7media to Render

This guide will walk you through deploying your Th7media Flask website to Render's free tier.

## Prerequisites

- A [Render](https://render.com) account (free)
- A [GitHub](https://github.com) account (free)
- Your Th7media project files

---

## Step 1: Push to GitHub

### Option A: Create a New Repository

1. Go to [GitHub](https://github.com) and create a new repository named `th7media`
2. Don't initialize with README (we already have one)

### Option B: Push Existing Code

Open a terminal in your project folder:

```bash
# Navigate to your project
cd /mnt/okcomputer/output/th7media

# Initialize git repository
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit - Th7media portfolio website"

# Add remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/th7media.git

# Push to GitHub
git branch -M main
git push -u origin main
```

---

## Step 2: Deploy on Render

### Method 1: Using render.yaml (Blueprint - Recommended)

1. Go to [Render Dashboard](https://dashboard.render.com)

2. Click **"New +"** → **"Blueprint"**

3. Connect your GitHub account and select the `th7media` repository

4. Click **"Apply"** - Render will automatically:
   - Detect the `render.yaml` configuration
   - Create a new Web Service
   - Install dependencies
   - Deploy your application

5. Wait for deployment to complete (2-3 minutes)

6. Your site will be live at: `https://th7media.onrender.com`

### Method 2: Manual Web Service Setup

If Blueprint doesn't work, use this manual method:

1. Go to [Render Dashboard](https://dashboard.render.com)

2. Click **"New +"** → **"Web Service"**

3. Connect your GitHub repository

4. Configure the service:

   | Setting | Value |
   |---------|-------|
   | **Name** | `th7media` |
   | **Environment** | `Python 3` |
   | **Build Command** | `pip install -r requirements.txt` |
   | **Start Command** | `gunicorn wsgi:app` |
   | **Plan** | `Free` |

5. Click **"Advanced"** and add Environment Variables:

   | Key | Value |
   |-----|-------|
   | `PYTHON_VERSION` | `3.11.0` |
   | `FLASK_ENV` | `production` |
   | `SECRET_KEY` | *(click "Generate" to create a random key)* |

6. Click **"Create Web Service"**

7. Wait for deployment to complete

---

## Step 3: Verify Deployment

Once deployed, check these URLs:

- **Homepage**: `https://your-service-name.onrender.com`
- **Portfolio**: `https://your-service-name.onrender.com/portfolio`
- **Learning Lab**: `https://your-service-name.onrender.com/learning-lab`
- **Contact**: `https://your-service-name.onrender.com/contact`

---

## Step 4: Custom Domain (Optional)

1. In Render Dashboard, go to your service
2. Click **"Settings"** → **"Custom Domains"**
3. Add your domain (e.g., `th7media.com`)
4. Follow Render's DNS configuration instructions
5. Wait for SSL certificate to be issued (automatic)

---

## Updating Your Site

When you make changes:

```bash
# Make your changes to the code

# Commit and push
git add .
git commit -m "Update description"
git push origin main
```

Render will automatically redeploy your site!

---

## Troubleshooting

### Build Fails

**Check the build logs in Render Dashboard:**

1. Go to your service → **"Logs"** tab
2. Look for error messages

**Common fixes:**

```bash
# If dependencies fail, update requirements.txt
pip freeze > requirements.txt
```

### App Won't Start

**Check your start command:**
- Should be: `gunicorn wsgi:app`
- NOT: `python app.py`

**Check wsgi.py exists** and contains:
```python
from app import app
```

### Static Files Not Loading

Flask automatically serves static files. If they're not loading:

1. Check file paths in templates use `url_for('static', filename='...')`
2. Verify files exist in `static/` folder
3. Clear browser cache (Ctrl+Shift+R)

### 500 Errors

1. Check Render logs for Python errors
2. Verify `SECRET_KEY` environment variable is set
3. Make sure all templates are in the `templates/` folder

---

## Free Tier Limits

Render's free tier includes:

- **Web Services**: 1 free instance (sleeps after 15 min inactivity)
- **Bandwidth**: 100 GB/month
- **Build minutes**: 500 minutes/month
- **Disk**: 0.5 GB

**Note**: Free web services "sleep" after 15 minutes of inactivity. The first request after sleeping may take 30-60 seconds to wake up.

---

## Environment Variables Reference

| Variable | Required | Description |
|----------|----------|-------------|
| `SECRET_KEY` | ✅ Yes | Random string for session security |
| `FLASK_ENV` | ❌ No | `production` or `development` |
| `FLASK_DEBUG` | ❌ No | `0` (off) or `1` (on) |
| `PORT` | ❌ No | Auto-set by Render |

---

## Files for Render Deployment

These files are already configured in your project:

### `render.yaml`
Blueprint configuration for automatic deployment.

### `requirements.txt`
Python dependencies including `gunicorn` for production.

### `wsgi.py`
WSGI entry point that Gunicorn uses to run your app.

### `.gitignore`
Excludes unnecessary files from Git.

---

## Need Help?

- [Render Documentation](https://render.com/docs)
- [Flask Deployment Guide](https://flask.palletsprojects.com/en/3.0.x/deploying/)
- [Gunicorn Documentation](https://docs.gunicorn.org/)

---

## Next Steps

After deployment:

1. ✅ Update your social links in `app.py`
2. ✅ Add real project images to `static/images/`
3. ✅ Customize the content in templates
4. ✅ Set up a custom domain
5. ✅ Add Google Analytics for tracking

Happy deploying! 🚀
