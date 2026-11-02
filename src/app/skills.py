# 기술 스택 단일 원본: 이력서 카드와 Skills 섹션이 같이 읽는다.
# 아이콘이 있는 기술만 SKILL_ICONS에 등록 (/static/images/ 기준)

SKILLS = [
    ("Languages", ["Java", "Python", "JavaScript", "TypeScript", "C", "C++", "PHP", "SQL", "Kotlin"]),
    ("Frontend", ["HTML5", "CSS3", "React", "Next.js", "jQuery", "AJAX", "Hugo"]),
    ("Backend", ["Spring", "Spring Boot", "Node.js", "Flask", "FastAPI", "NestJS", "Django", "JSP", "Java Servlet",
                 "SQLAlchemy", "Alembic"]),
    ("Database & Cache", ["MySQL", "MariaDB", "SQLite", "PostgreSQL", "Redis"]),
    ("Messaging & Streaming", ["Redis Streams", "RabbitMQ", "Apache Kafka"]),
    ("Cloud / AWS", ["AWS", "EC2", "VPC", "ALB", "Auto Scaling", "RDS", "ECS Fargate", "ECR", "CloudWatch"]),
    ("DevOps / CI/CD", ["Docker", "Kubernetes", "k3s", "Argo CD", "Jenkins", "GitHub Actions", "GHCR", "Terraform"]),
    ("Infrastructure", ["Proxmox VE", "LXC", "Caddy", "Nginx", "Traefik", "Kubernetes Gateway API"]),
    ("OS / Network", ["Linux", "Ubuntu", "Debian", "CentOS", "Windows Server", "SSH", "Tailscale", "Cloudflare",
                      "Cloudflare Tunnel", "Reverse Proxy", "CORS"]),
    ("Testing / Tools", ["Git", "GitHub", "Playwright", "pytest", "Google Colab", "Obsidian"]),
    ("AI / ML", ["PyTorch", "scikit-learn", "XGBoost", "GPBoost", "Linear Regression", "Ridge", "Lasso",
                 "Random Forest", "Decision Tree", "CNN", "RNN", "LSTM", "Attention", "Transformer"]),
    ("LLM / Agentic Systems", ["Efficient LLM Routing", "Multi-Agent Systems", "LLM-as-a-Judge",
                               "Harness Engineering (Prompt / Context / Loop / Graph Engineering)",
                               "System-1 Decision Models (Jev, Laya)", "Model Cascading", "Confidence-based Routing",
                               "Cost-Aware Inference", "Tool Routing"]),
]

SKILL_ICONS = {
    "Java": "java.png", "Python": "python_image.png", "JavaScript": "js_image.png",
    "HTML5": "html_image.png", "CSS3": "css_image.png", "React": "react_image.svg", "jQuery": "jQuery_image.png",
    "JSP": "jsp_image.png", "Spring": "spring_image.png", "Spring Boot": "springboot_image.png", "Flask": "flask.png",
    "FastAPI": "fastapi_image.svg", "Django": "django_image.svg", "MySQL": "mysql.png", "MariaDB": "mariadb.png",
    "Docker": "docker.png", "Kubernetes": "kubernetes_image.svg", "Jenkins": "jenkins.png", "AWS": "aws.png",
    "Git": "git.png", "GitHub": "github.png",
}

SKILL_TOTAL = sum(len(items) for _, items in SKILLS)
