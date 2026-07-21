# 🎯 Deployment Setup Complete — Quick Reference

## What We've Set Up For Render Deployment

### ✅ Configuration Files Created/Updated

| File | Purpose |
|------|---------|
| **render.yaml** | Render deployment config (build → migrate → collectstatic → gunicorn) |
| **config/settings/production.py** | PostgreSQL database URL parsing, HTTPS security, Gmail SMTP |
| **requirements.txt** | Added: `gunicorn`, `dj-database-url`, `psycopg2-binary` |
| **.env.example** | Updated with all production variables (DATABASE_URL, email, etc.) |
| **config/urls.py** | Added `/sitemap.xml` and `/robots.txt` routes |
| **accounts/sitemap_views.py** | Dynamic XML sitemap generation for SEO |
| **RENDER_DEPLOYMENT_GUIDE.md** | Complete step-by-step deployment walkthrough |

---

## 🚀 Quick Start: Deploy in 5 Steps

### 1️⃣ **Prepare Gmail** (5 min)
- Go to https://myaccount.google.com/apppasswords
- Generate App Password (Gmail → Your Device)
- Copy the 16-character password

### 2️⃣ **Push to GitHub** (2 min)
```bash
git add .
git commit -m "Setup: Render deployment + SEO sitemap"
git push origin main
```

### 3️⃣ **Create Render Account** (2 min)
- Visit https://render.com → Sign up with GitHub

### 4️⃣ **Deploy Web Service** (5 min)
- Dashboard → New Web Service
- Connect GitHub repo
- Set environment variables (DJANGO_SECRET_KEY, EMAIL_HOST_PASSWORD, etc.)
- Click Create

### 5️⃣ **Wait & Test** (5 min)
- Render builds automatically (2-5 min)
- Visit `https://your-app.onrender.com/accounts/login/`
- Check `/sitemap.xml` loads

**Total time: ~20 minutes to live production app** ⏱️

---

## 📋 Environment Variables Needed on Render

Copy-paste into Render Dashboard → Environment Variables:

```
DJANGO_SETTINGS_MODULE=config.settings.production
DJANGO_SECRET_KEY=<run: python manage.py shell, from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())>
ALLOWED_HOSTS=your-app.onrender.com,yourdomain.co.ke

EMAIL_HOST_USER=youremail@gmail.com
EMAIL_HOST_PASSWORD=<your 16-char Gmail App Password>
DEFAULT_FROM_EMAIL=noreply@yourdomain.co.ke

BASE_URL=https://your-app.onrender.com
PLATFORM_NAME=Mentify

PAYSTACK_SECRET_KEY=sk_live_xxx
PAYSTACK_PUBLIC_KEY=pk_live_xxx
GITHUB_TOKEN=ghp_xxx (optional)
GOOGLE_CLIENT_ID=xxx (optional)
```

---

## 🔧 How It Works: Render → Gunicorn → Django

```
┌──────────────────────────────────────────────────────────────┐
│ Render.com (Cloud Platform)                                  │
├──────────────────────────────────────────────────────────────┤
│                                                               │
│  BUILD PHASE (render.yaml buildCommand):                     │
│  ├─ pip install -r requirements.txt                          │
│  ├─ python manage.py migrate --noinput  (PostgreSQL)         │
│  └─ python manage.py collectstatic --noinput (WhiteNoise)    │
│                                                               │
│  RUN PHASE (render.yaml startCommand):                       │
│  └─ gunicorn config.wsgi:application --workers 3             │
│                                                               │
│  ┌─ PostgreSQL Database (auto-created)                       │
│  │  └─ DATABASE_URL → django.db.backends.postgresql          │
│  │                                                            │
│  └─ Static Files (served by WhiteNoise)                      │
│     └─ /static/ and /media/ paths                            │
│                                                               │
│  EMAIL: Gmail SMTP (config.settings.production)              │
│  └─ Guardian notifications, confirmations, etc.              │
│                                                               │
│  SEO: Dynamic Sitemap & robots.txt                           │
│  ├─ /sitemap.xml  (XML for Google)                           │
│  └─ /robots.txt   (crawler directives)                       │
│                                                               │
└──────────────────────────────────────────────────────────────┘
```

---

## 📊 Database Migration: MySQL → PostgreSQL

Your app switches from MySQL (local dev) to PostgreSQL (Render):

**Local dev (.env)**:
```
DJANGO_SETTINGS_MODULE=config.settings.development
DB_NAME=Mentify
DB_USER=root
DB_PASSWORD=...
```

**Render production (Dashboard Environment)**:
```
DJANGO_SETTINGS_MODULE=config.settings.production
DATABASE_URL=postgresql://user:pass@host:5432/db  (set by Render)
```

**Django handles both**: `production.py` uses `dj-database-url` to parse `DATABASE_URL` automatically.

---

## 🌍 SEO Setup Included

### Sitemap for Google
- **Endpoint**: `/sitemap.xml`
- **Updated automatically**: Includes latest pages with priority/frequency
- **Submit to**: https://search.google.com/search-console

### robots.txt for Crawlers
- **Endpoint**: `/robots.txt`
- **Directs to**: `/sitemap.xml`
- **Blocks**: `/admin/`, `/dashboard/admin*`

### To Get Indexed by Google:
1. Go to https://search.google.com/search-console
2. Add your domain
3. Verify (via Google Search Console)
4. Submit sitemap: `/sitemap.xml`
5. Wait 1-7 days for indexing

---

## 🔒 Security Features Enabled

✅ **HTTPS/SSL** (automatic by Render)  
✅ **HSTS** (force HTTPS, prevent downgrade)  
✅ **CSRF protection** (Django + cookies)  
✅ **Secure cookies** (HTTPS only, SameSite=Lax)  
✅ **X-Frame-Options** (clickjacking protection)  
✅ **X-Content-Type-Options** (MIME sniffing prevention)  

---

## 📧 Guardian Notification Emails

Your existing guardian linking workflow now works on production:

- **Guardian requests learner link** → Email sent to learner (via Gmail SMTP)
- **Learner accepts/rejects** → Email sent to guardian
- **Admin approves request** → Email sent to both parties
- **All emails use**: `DEFAULT_FROM_EMAIL` from env vars

---

## 🆘 Common Issues & Fixes

| Problem | Solution |
|---------|----------|
| **502 Bad Gateway** | Check logs → `python manage.py migrate` error; verify `DATABASE_URL` |
| **ModuleNotFoundError: dj_database_url** | Click **Manual Deploy** in dashboard to reinstall deps |
| **Emails not sending** | Verify `EMAIL_HOST_USER` and `EMAIL_HOST_PASSWORD` in env; check Gmail App Password is correct |
| **Static files return 404** | Run `python manage.py collectstatic --noinput` in Render shell |
| **ALLOWED_HOSTS error** | Update env var to include your Render domain |
| **Sitemap shows 404** | Ensure `accounts/sitemap_views.py` exists; check `config/urls.py` has sitemap route |

---

## 📝 Files Modified

```
✏️  config/settings/production.py          (PostgreSQL + HTTPS + Gmail)
✏️  requirements.txt                        (gunicorn + dj-database-url + psycopg2)
✏️  config/urls.py                         (sitemap + robots routes)
✏️  .env.example                            (production env vars)
✨ render.yaml                             (Render deployment config)
✨ accounts/sitemap_views.py              (dynamic sitemap + robots)
✨ RENDER_DEPLOYMENT_GUIDE.md             (detailed walkthrough)
```

---

## 🎯 Next Actions

1. **Read** [RENDER_DEPLOYMENT_GUIDE.md](./RENDER_DEPLOYMENT_GUIDE.md) for step-by-step instructions
2. **Generate** Django secret key (see guide Step 5)
3. **Get** Gmail App Password (see guide Step 1)
4. **Push** to GitHub
5. **Deploy** on Render
6. **Test** guardian workflow on production
7. **Register** sitemap with Google Search Console

---

## 💡 Pro Tips

- **Test locally first**: `DJANGO_SETTINGS_MODULE=config.settings.production python manage.py runserver`
- **Monitor logs**: Render dashboard → Logs tab (watch for errors in real-time)
- **Upgrade plan**: Free tier deletes DB after 90 days; upgrade to Standard for production
- **Custom domain**: Add DNS records for `yourdomain.co.ke` (see guide Step 8)
- **Email rate limits**: Gmail SMTP has limits; consider SendGrid or Mailgun for large deployments
- **Backups**: Enable automated PostgreSQL backups in Render settings

---

**You're all set! 🚀 Proceed to [RENDER_DEPLOYMENT_GUIDE.md](./RENDER_DEPLOYMENT_GUIDE.md) to start deploying.**
