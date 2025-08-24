# 🤖 AI Webhook Reviewer

*It's GPT wrapper again...* but this time with more attitude! 🎭

## 🚨 What This Thing Does (For Now)

Welcome to yet another AI-powered code reviewer that pretends to know what it's doing! This bad boy is an **MVP version** that uses GPT to review code when you open a Pull Request and then adds feedback on it. Because apparently, we humans can't be trusted to write perfect code anymore. 😅

### Current Features 🎯
- 🎪 **GitHub Webhook Magic**: Listens to PR events like a nosy neighbor
- 🧠 **GPT-Powered Reviews**: Uses OpenAI's GPT to judge your code (harshly but fairly)
- 💬 **Automatic Comments**: Leaves helpful feedback directly on your PRs
- 🛡️ **Signature Verification**: Because security matters (even for our AI overlords)
- 📊 **Diff Analysis**: Reads your code changes and pretends to understand them

### The Grand Master Plan™ 🚀

In the **far future** (if I have a chance, time, and mood - yes, mood is a valid technical requirement), I might enhance this with:

🔮 **RAG Feature Implementation**:
- Instead of depending 100% on GPT (because even AI needs backup plans)
- The system will review based on specific rules from documentation
- A cron job will run every night to read rule documents and store them in a vector database
- Basically, we're teaching the AI to read the manual so you don't have to!

*Timeline: Somewhere between "when I have time" and "when I feel like it"* 📅

## 🛠️ Technical Stack (The Cool Stuff)

This project is built with modern, professional tools that sound impressive in meetings:

### Backend Framework
- **🚀 FastAPI**: Because life's too short for slow APIs
- **🐍 Python 3.12**: The latest and greatest snake version

### AI & Machine Learning
- **🤖 LangChain**: For chaining AI operations like a boss
- **🧠 OpenAI GPT**: The brain behind the operation (currently using gpt-5-nano)
- **💡 LangChain OpenAI Integration**: Making AI calls feel smooth

### GitHub Integration
- **🐙 PyGithub**: For talking to GitHub without crying
- **🔗 GitHub API**: The official way to annoy your repositories
- **🎣 GitHub Webhooks**: Real-time notifications (because waiting is for peasants)

### Configuration & Settings
- **⚙️ Pydantic Settings**: Type-safe configuration management
- **🔒 Environment Variables**: Keeping secrets actually secret

### HTTP & Networking
- **🌐 HTTPX**: Async HTTP client for the modern age
- **📡 FastAPI Standard**: All the HTTP goodness you need

## 🚀 Getting Started

### Prerequisites
- Python 3.12+ (older versions might work, but who has time to test that?)
- A GitHub repository to terrorize with reviews
- OpenAI API key (prepare your wallet)
- A sense of humor about AI feedback

### Installation

1. **Clone this masterpiece:**
   ```bash
   git clone https://github.com/BruceGoodGuy/ai-webhook-reviewer.git
   cd ai-webhook-reviewer
   ```

2. **Set up your virtual environment (because isolation is healthy):**
   ```bash
   python -m venv review
   source review/bin/activate  # On Windows: review\Scripts\activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure your secrets (shhh! 🤫):**
   Create a `.env` file in the root directory:
   ```env
   GITHUB_API=your_github_personal_access_token
   GITHUB_WEBHOOK_SECRET=your_webhook_secret
   OPEN_AI_API_KEY=your_openai_api_key
   ```

5. **Run the server:**
   ```bash
   uvicorn app.main:app --reload
   ```

### Setting Up GitHub Webhooks

1. Go to your repository settings
2. Navigate to Webhooks
3. Add a new webhook pointing to `your-server.com/webhook/`
4. Select "Pull requests" events
5. Set your secret (the same one in your `.env` file)
6. Watch the magic happen! ✨

## 📁 Project Structure

```
review/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI application entry point
│   ├── webhook.py       # Webhook endpoint handlers
│   ├── ai_chain.py      # GPT integration and prompt management
│   ├── services.py      # Business logic and data processing
│   ├── github_api.py    # GitHub API client wrapper
│   ├── config.py        # Configuration and settings
│   └── utils.py         # Utility functions and helpers
├── requirements.txt     # Python dependencies
└── README.md           # This beautiful documentation
```

## 🎭 How It Works (The Magic Behind the Curtain)

1. **🎣 Webhook Reception**: GitHub sends a webhook when PR events occur
2. **🔐 Signature Verification**: We verify it's really GitHub (trust but verify!)
3. **📥 Payload Processing**: Extract PR information and file changes
4. **🤖 AI Analysis**: Send the diff to GPT with a carefully crafted prompt
5. **💬 Comment Generation**: Parse AI feedback into GitHub-friendly comments
6. **📝 Review Submission**: Post the review directly to your PR

## 🎯 Supported Review Categories

The AI reviewer checks for:
- 🐛 **Bugs**: Logic errors and potential issues
- 🔒 **Security**: Vulnerabilities and security concerns
- ⚡ **Performance**: Optimization opportunities
- 🎨 **Style**: Code formatting and style violations
- 🔧 **Maintainability**: Code quality and readability
- 📚 **Documentation**: Missing or inadequate documentation

## 🚧 Current Limitations

- Only reviews PRs (because that's where the drama happens)
- Limited to 10,000 characters of diff (we're not reading War and Peace here)
- Depends entirely on GPT's mood swings
- No memory between reviews (each PR is a fresh start)

## 🔮 Future Enhancements (When Stars Align)

- **RAG Integration**: Custom rule-based reviews
- **Vector Database**: For storing coding standards
- **Cron Jobs**: Automated rule updates
- **Multiple AI Models**: Because variety is the spice of life
- **Custom Prompts**: Tailor the AI to your team's needs
- **Review Templates**: Standardized feedback formats

## 🤝 Contributing

Found a bug? Have a feature request? Want to roast my code?
1. Fork it
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request (and watch our AI judge your code! 😈)

## 📄 License

This project is licensed under the "Do Whatever You Want But Don't Blame Me" License. 
*(Actually, check the LICENSE file for real legal stuff)*

## ⚠️ Disclaimer

This AI reviewer might:
- Judge your code unfairly
- Miss obvious bugs while complaining about semicolons
- Become sentient and start a coding revolution
- Actually help improve your code quality (the most surprising outcome)

Use at your own risk, and remember: AI feedback is just another opinion, albeit a very expensive one! 💸

---

*Built with ❤️, ☕, and a healthy dose of sarcasm by developers who believe in automating code reviews so they can focus on more important things... like arguing about tabs vs spaces.*

**P.S.**: If this AI starts giving you relationship advice instead of code reviews, please file a bug report. We're still working on that feature. 🤖💕
