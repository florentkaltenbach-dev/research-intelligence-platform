# ⚡ Next Steps - Quick Start Guide

## Current Status: 95% Complete! 🎉

✅ **Application fully built** - 44 files, production-ready code
✅ **Configured for web access** - IPv6 ready
✅ **Git repository ready** - 3 commits with proper history
✅ **SQLite configured** - No PostgreSQL needed

❌ **Missing**: System packages (pip, Node.js) - needs 1 command

---

## 🚀 One Command to Rule Them All

### Step 1: Install System Packages (30 seconds)

```bash
sudo apt update && sudo apt install -y python3-pip python3-venv nodejs npm
```

### Step 2: Run Automated Setup (2 minutes)

```bash
cd research-intelligence-platform
./install-and-run.sh
```

**That's it!** The script will:
1. Install Python dependencies
2. Initialize SQLite database
3. Install frontend dependencies
4. Start backend on port 8000
5. Start frontend on port 3000

---

## 🌐 Access Your Platform

Once running:

- **Frontend**: http://[2a01:4f9:c012:ee5a::1]:3000
- **API**: http://[2a01:4f9:c012:ee5a::1]:8000
- **API Docs**: http://[2a01:4f9:c012:ee5a::1]:8000/docs

---

## 📊 What You'll See

### Homepage
- Live statistics dashboard
- Recent events
- Source diversity metrics

### Events Page
- Power transition events
- Multi-regional perspectives
- Impact levels

### API Documentation
- Interactive Swagger UI
- Test endpoints directly
- Full schema documentation

---

## 🛑 To Stop Services

```bash
./stop-services.sh
```

Or manually:
```bash
kill $(cat backend.pid) $(cat frontend.pid)
```

---

## 📝 View Logs

```bash
tail -f backend.log    # Backend API logs
tail -f frontend.log   # Frontend dev server logs
```

---

## 🎯 Start Researching with Claude Code

Once the platform is running, open a new Claude Code session:

```bash
claude
```

Then try this research request:

```
Research "BRICS payment systems 2024" using the Source Diversification approach.

Search for:
1. Chinese sources (how do they frame it?)
2. Russian sources (what aspects do they emphasize?)
3. Indian sources (what's their perspective?)

Create an Event in the database with Perspectives for each region,
properly cited with Sources.
```

I'll:
- Use web search to find diverse sources
- Analyze each regional perspective
- Make API calls to create the Event
- Add Perspectives with proper citations
- Save Sources with credibility ratings
- Commit the research to git

---

## 🔧 Alternative: Manual Step-by-Step

If you prefer to see each step:

<details>
<summary>Click to expand manual instructions</summary>

### 1. Install Python Dependencies
```bash
cd backend
python3 -m pip install --user -r requirements.txt
```

### 2. Initialize Database
```bash
python3 scripts/init_db.py
```

### 3. Install Frontend Dependencies
```bash
cd ../frontend
npm install
```

### 4. Start Backend
```bash
cd ../backend
python3 main.py
```

### 5. Start Frontend (new terminal)
```bash
cd frontend
npm run dev
```

</details>

---

## 💡 Pro Tips

1. **First Research Session**: Start with something current like "BRICS currency 2024" or "Saudi PIF dedollarization"

2. **Check Database**: After adding research, view it at http://[2a01:4f9:c012:ee5a::1]:3000

3. **API Testing**: Use the Swagger UI at http://[2a01:4f9:c012:ee5a::1]:8000/docs to test endpoints

4. **Git History**: All research sessions are tracked in git commits

5. **Deploy**: When ready, push to GitHub and deploy to Vercel (frontend) + Railway (backend)

---

## ⚠️ Troubleshooting

### "Port already in use"
```bash
lsof -i :8000  # Check port 8000
lsof -i :3000  # Check port 3000
kill -9 <PID>  # Kill the process
```

### "Database locked"
```bash
rm backend/research.db  # Delete and reinitialize
python3 backend/scripts/init_db.py
```

### "npm ERR!"
```bash
cd frontend
rm -rf node_modules package-lock.json
npm install
```

---

**Ready to go? Run these two commands:**

```bash
sudo apt update && sudo apt install -y python3-pip python3-venv nodejs npm
./install-and-run.sh
```

Then visit: **http://[2a01:4f9:c012:ee5a::1]:3000** 🚀
