# 🚀 EduAI Deployment Guide — Render + PostgreSQL + Gmail SMTP + Google SEO

This guide walks you through deploying EduAI to Render, a modern cloud platform (similar to Heroku but free tier available). By the end, your app will be live at `https://your-app.onrender.com`.

---

## 📋 Pre-Deployment Checklist

Before starting, you need:

- [x] **GitHub account** (Render deploys from GitHub)
- [x] **Render account** (free at https://render.com)
- [x] **Gmail account** (for SMTP email notifications)
- [x] **Domain name** (optional, but recommended for production)
- [x] **Your Django project with `render.yaml`** (already configured in this repo)

---

## 🔑 Step 1: Generate Gmail App Password for Email Notifications

Gmail requires an "App Password" for third-party apps (Django won't accept regular passwords via SMTP for security).

### Steps:

1. **Enable 2-Factor Authentication** (required for App Passwords):
   - Go to https://myaccount.google.com/security
   - Scroll to "2-Step Verification" → click **Enable**
   - Follow the prompts (you'll verify with phone)

2. **Generate App Password**:
   - Go to https://myaccount.google.com/apppasswords
   - Select **App**: Mail
   - Select **Device**: Windows Computer (or your OS)
   - Click **Generate**
   - Copy the 16-character password shown (looks like: `xxxx xxxx xxxx xxxx`)

3. **Save this password** — you'll paste it into Render dashboard in Step 5

**Example Gmail Setup**:
```
EMAIL_HOST_USER=youremail@gmail.com
EMAIL_HOST_PASSWORD=abcd efgh ijkl mnop  (16 chars, spaces included in display only)
```

---

## 📦 Step 2: Push Code to GitHub

Render deploys directly from GitHub, so your code must be on GitHub.

### If you DON'T have your code on GitHub yet:

1. **Create a new GitHub repository**:
   - Go to https://github.com/new
   - Name it `EduAI` (or similar)
   - Choose **Private** (recommended for security)
   - Click **Create repository**

2. **Push your code**:
   ```bash
   # From your project root (where manage.py is)
   git remote add origin https://github.com/YOUR_USERNAME/EduAI.git
   git branch -M main
   git push -u origin main
   ```

3. **Verify on GitHub**:
   - Go to https://github.com/YOUR_USERNAME/EduAI
   - You should see your files (including `render.yaml`, `requirements.txt`, `manage.py`)

---

## 🌐 Step 3: Create Render Account & Connect GitHub

1. **Sign up for free**:
   - Go to https://render.com
   - Click **Sign up**
   - Use GitHub to sign up (easiest option)
   - Authorize Render to access your GitHub account

2. **Your Render dashboard** should now show at https://dashboard.render.com

---

## 🗄️ Step 4: Create PostgreSQL Database on Render

Render auto-creates the PostgreSQL database from `render.yaml`, BUT you need to manually create it first or let Render create it during deployment. We'll let Render handle it.

### What you need to know:
- Render will create a PostgreSQL database
- Connection string: Render provides `DATABASE_URL` automatically to your app
- You don't configure anything here — it happens automatically

---

## 🔧 Step 5: Create Web Service on Render (with Environment Variables)

1. **Go to https://dashboard.render.com**

2. **Click "New +"** → **Web Service**

3. **Connect your GitHub repository**:
   - Click **Connect Account** (if not already connected)
   - Search for your repo name: `EduAI`
   - Click **Connect**

4. **Configure the service**:
   - **Name**: `eduai-api` (matches render.yaml)
   - **Region**: Choose closest to your users (e.g., `Oregon` for US/East Africa)
   - **Branch**: `main`
   - **Runtime**: `Python` (auto-detected)
   - **Build Command**: Leave empty (Render reads from `render.yaml`)
   - **Start Command**: Leave empty (Render reads from `render.yaml`)

5. **Add Environment Variables** — Click **Advanced** → **Environment Variables**:

   Add these variables (paste or type):

   ```
   DJANGO_SETTINGS_MODULE=config.settings.production
   DJANGO_SECRET_KEY=<generate-a-long-random-string>
   ALLOWED_HOSTS=<your-app>.onrender.com,www.yourdomain.co.ke
   
   EMAIL_HOST=smtp.gmail.com
   EMAIL_PORT=587
   EMAIL_HOST_USER=youremail@gmail.com
   EMAIL_HOST_PASSWORD=<paste-your-16-char-app-password>
   DEFAULT_FROM_EMAIL=noreply@yourdomain.co.ke
   
   PLATFORM_NAME=Mentify
   BASE_URL=https://<your-app>.onrender.com
   
   PAYSTACK_SECRET_KEY=<your-paystack-key>
   PAYSTACK_PUBLIC_KEY=<your-paystack-key>
   GITHUB_TOKEN=<optional>
   GOOGLE_CLIENT_ID=<optional>
   ```

   **How to generate `DJANGO_SECRET_KEY`**:
   - Open Python shell: `python`
   - Run: `from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())`
   - Copy the output string
   - Paste it into `DJANGO_SECRET_KEY` field

6. **Database** — Render auto-creates PostgreSQL, connection via `DATABASE_URL`

7. **Plan**: Select **Free** (if eligible) or **Standard** for production

8. **Click "Create Web Service"**

Render will start building immediately. **This takes 2-5 minutes.**

---

## ⏳ Step 6: Monitor Deployment

1. **Watch the build logs** — Render dashboard shows real-time logs
2. **You'll see**:
   ```
   Running build command: pip install -r requirements.txt && ...
   Running migrations...
   Collecting static files...
   Starting gunicorn...
   ```
3. **Wait for "Live"** — Dashboard shows green "Live" badge when deployed

### Common issues & solutions:

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError: No module named 'dj_database_url'` | Requirements already updated, but rebuild if needed: Dashboard → **Manual Deploy** |
| `ERROR: Migrations failed` | Database connection issue; check `DATABASE_URL` in env vars is set |
| `Static files not collecting` | Run manually: Dashboard → **Shell** → `python manage.py collectstatic --noinput` |
| `ALLOWED_HOSTS error` | Update env var `ALLOWED_HOSTS` to include your Render domain |

---

## 🌍 Step 7: Test Your Live App

1. **Get your Render URL**:
   - Dashboard shows: `https://eduai-api.onrender.com` (or similar)

2. **Test login page**:
   - Visit `https://eduai-api.onrender.com/accounts/login/`
   - Should show your login form (not 500 error)

3. **Test email** (optional):
   - Register a new account
   - Check that confirmation email arrives

4. **Check sitemap for SEO**:
   - Visit `https://eduai-api.onrender.com/sitemap.xml`
   - Should show XML with URLs

---

## 📍 Step 8: Connect Custom Domain (Optional but Recommended)

If you have a domain (e.g., `yourdomain.co.ke`):

1. **Go to Dashboard** → Click your service name
2. **Settings** → **Custom Domains**
3. **Add Domain**: `yourdomain.co.ke`
4. **Render gives you nameservers** — copy them
5. **Go to your domain registrar** (GoDaddy, Namecheap, etc.)
   - Update nameservers to Render's nameservers
   - Wait 1-24 hours for DNS to propagate

6. **Update your environment variables** on Render:
   - `ALLOWED_HOSTS=yourdomain.co.ke,www.yourdomain.co.ke`
   - `BASE_URL=https://yourdomain.co.ke`
   - Click **Save** (auto-redeploys)

---

## 🔐 Step 9: Register Sitemap with Google Search Console (SEO)

Getting your app indexed by Google:

1. **Go to https://search.google.com/search-console**

2. **Add Property**:
   - Enter URL: `https://yourdomain.co.ke` (or `https://eduai-api.onrender.com`)
   - Click **Continue**

3. **Verify ownership**:
   - Google shows options (HTML file upload, DNS record, etc.)
   - Choose **HTML file** → Download file
   - Place in `static/` folder on GitHub
   - Push to GitHub
   - Google will auto-fetch and verify

4. **Submit Sitemap**:
   - Left menu → **Sitemaps**
   - Add: `https://yourdomain.co.ke/sitemap.xml`
   - Click **Submit**
   - Google will crawl and index your pages

---

## 🛡️ Step 10: Set Up HTTPS (Automatic)

Render automatically provides SSL/TLS certificates (free, auto-renewing). Your site is already `https://` by default.

**Verify**:
- Visit your site — browser shows 🔒 lock icon
- Redirect: HTTP → HTTPS happens automatically

---

## 📊 Monitoring & Logs

Monitor your live app:

1. **Dashboard** → Click service name
2. **Logs** tab → See real-time activity
3. **Metrics** tab → CPU, RAM, bandwidth usage

### Example logs to watch for:
```
GET /accounts/login/ 200
POST /accounts/register/ 201
GET /sitemap.xml 200
Guardian link request email sent to user@example.com
```

---

## 🔄 Redeploying After Code Changes

After you make changes locally and push to GitHub:

1. **Push to GitHub**:
   ```bash
   git add .
   git commit -m "Fix: guardian dashboard UI"
   git push origin main
   ```

2. **Render auto-redeploys** (within 1 minute)
   - Dashboard shows new build running
   - Migrations run automatically

3. **Manual redeploy** (if needed):
   - Dashboard → **Manual Deploy** button

---

## ⚠️ Important Notes

### Database Persistence
- Render **free tier** deletes database after 90 days of inactivity
- **Standard tier** has persistent database
- Consider upgrading if you go live with users

### Email Sending
- Gmail SMTP works, but you may hit rate limits (100/hour)
- For production, consider **SendGrid** (free tier: 100/day) or **Mailgun**
- Update `EMAIL_BACKEND` and credentials in `production.py` if switching

### Static Files
- WhiteNoise handles static file serving
- Images, CSS, JS are cached and served fast
- User uploads (media files) go to GitHub (configured in your code)

### Backups
- Set up automated PostgreSQL backups:
  - Dashboard → Service Settings → **Backups** → Enable
  - Recommended: daily backups for production

---

## 🐛 Troubleshooting

### "502 Bad Gateway" after deploy
- Check logs: `python manage.py migrate` error
- Solution: Check `DATABASE_URL` env var is set correctly

### "ModuleNotFoundError: No module named 'dj_database_url'"
- You updated `requirements.txt` but Render didn't reinstall
- Fix: Dashboard → **Manual Deploy** → click Deploy

### Emails not sending
- Check: `EMAIL_HOST_USER` and `EMAIL_HOST_PASSWORD` are correct
- Test locally first: `python manage.py shell` → `send_mail(...)`
- Check spam folder (Gmail might flag test emails)

### Guardian links not working
- Check: `BASE_URL` env var matches your domain
- Test locally before deploying

### Site not in Google Search Console
- Wait 24-48 hours for initial crawl
- Submit sitemap manually: https://search.google.com/search-console

---

## 📝 Summary: What We've Set Up

✅ **render.yaml** — Deployment config with build/start commands  
✅ **production.py** — PostgreSQL + security headers + Gmail SMTP  
✅ **requirements.txt** — gunicorn + dj-database-url + psycopg2  
✅ **Sitemap API** — `/sitemap.xml` for Google indexing  
✅ **robots.txt** — `/robots.txt` for crawler directives  
✅ **.env.example** — Template for all production env vars  
✅ **Guardian linking** — Self-service + learner consent (from previous work)  
✅ **Email notifications** — Guardian requests/confirmations via Gmail  

---

## 🚀 You're Ready to Deploy!

**Next steps**:
1. Follow Step 1-5 above (Gmail password, GitHub, Render account, env vars)
2. Click "Create Web Service" and wait for deployment
3. Test your live site
4. Register sitemap with Google Search Console
5. (Optional) Connect custom domain

**If you hit any issues**, check the logs in Render dashboard or reply here with the error message.

Good luck! 🎉
