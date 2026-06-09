<h3 align="center">🛠️ dev-marketer</h3>

<div align="center">
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
  [![Language: Python](https://img.shields.io/badge/Language-Python-blue.svg)](https://python.org)
  [![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen.svg)](https://github.com/axentx/dev-marketer)
  [![Stars](https://img.shields.io/badge/Stars-⭐️⭐️⭐️⭐️⭐️-yellow.svg)](https://github.com/axentx/dev-marketer)
</div>

---

# 🚀 dev-marketer
**Power indie developers with automated growth marketing.** A growth automation platform tailored for indie developers to effectively market their products and reach their target audience.

## Why dev-marketer?
- **Effortless Marketing**: Automate your marketing campaigns with minimal setup and maximum impact
- **Audience Targeting**: Precisely identify and reach your ideal customer segments
- **Performance Analytics**: Track marketing ROI with comprehensive dashboards and insights
- **Built for Solopreneurs**: Designed specifically for indie developers with limited marketing resources
- **Time-Saving**: Automate repetitive tasks so you can focus on building great products
- **Growth-Focused**: Features engineered to accelerate user acquisition and retention

## Feature Overview
| Feature | Description |
|---------|-------------|
| Campaign Automation | Set up automated marketing sequences that run based on user behavior |
| Audience Segmentation | Create targeted user groups based on demographics and engagement |
| Multi-Channel Outreach | Engage users across email, social media, and other platforms |
| Performance Tracking | Monitor campaign effectiveness with real-time analytics |
| A/B Testing | Optimize your marketing with built-in experimentation tools |

## Tech Stack
- Python (primary language)
- FastAPI (web framework)
- PostgreSQL (database)
- Redis (caching)
- Docker (containerization)
- GitHub Actions (CI/CD)

## Project Structure
```
dev-marketer/
├── business/          # Business logic and core functionality
├── src/              # Source code and application modules
├── tests/            # Test suites and test utilities
├── README.md         # Project documentation
├── pyproject.toml    # Project configuration and dependencies
└── requirements.txt  # Python package requirements
```

## Getting Started
```bash
# Clone the repository
git clone https://github.com/axentx/dev-marketer.git
cd dev-marketer

# Install dependencies
pip install -r requirements.txt

# Run the application
python -m uvicorn src.main:app --reload
```

## Deploy
```bash
# Build Docker image
docker build -t dev-marketer .

# Run container
docker run -p 8000:8000 dev-marketer
```

## Status
Active development with recent focus on core marketing automation features. Last commit: fe780d9 - axentx-dev-bot: code-build cycle 20260609-025151-dev-mark

## Contributing
For contribution guidelines, please see [CONTRIBUTING.md](./CONTRIBUTING.md)

## License
This project is licensed under the MIT License.