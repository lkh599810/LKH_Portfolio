# 기술 스택 단일 원본 (메인 Skills 섹션).
# "프로젝트에 사용" 강조는 손으로 고르지 않고, projects.py의 stack과 이력서 연구 경력에 실제로 나온 기술만 자동으로 표시한다.
from .projects import PROJECTS

# 분야별 목록. 각 목록 안에서 최신·핵심 기술을 앞에 둔다 (화면에 이 순서 그대로 표시)
_LANGUAGES = ["Python", "Java", "TypeScript", "JavaScript", "SQL", "Kotlin", "C", "C++", "PHP"]
_FRONTEND = ["React", "Next.js", "HTML5", "CSS3", "jQuery", "AJAX", "Hugo"]
_BACKEND = ["FastAPI", "Spring Boot", "Flask", "Spring", "Node.js", "NestJS", "Django", "SQLAlchemy", "Alembic",
            "JSP", "Java Servlet"]
_DATABASE = ["PostgreSQL", "MySQL", "Redis", "MariaDB", "SQLite"]
_MESSAGING = ["Redis Streams", "Apache Kafka", "RabbitMQ"]
_CLOUD = ["AWS", "EC2", "ECS Fargate", "ECR", "ALB", "Auto Scaling", "VPC", "RDS", "CloudWatch"]
_DEVOPS = ["Kubernetes", "k3s", "Argo CD", "GitHub Actions", "Docker", "GHCR", "Terraform", "Jenkins"]
_INFRA = ["Proxmox VE", "Traefik", "Kubernetes Gateway API", "Caddy", "Nginx", "LXC"]
_OS_NETWORK = ["Linux", "Ubuntu", "Debian", "Cloudflare Tunnel", "Tailscale", "Cloudflare", "SSH", "Reverse Proxy",
               "CORS", "CentOS", "Windows Server"]
_TOOLS = ["Git", "GitHub", "Playwright", "pytest", "Google Colab", "Obsidian"]
_AI_ML = ["PyTorch", "LLM", "Transformer", "Attention", "XGBoost", "GPBoost", "scikit-learn", "LSTM", "CNN", "RNN",
          "Random Forest", "Decision Tree", "Linear Regression", "Ridge", "Lasso"]
_LLM = ["Efficient LLM Routing", "Multi-Agent Systems", "LLM-as-a-Judge",
        "Harness Engineering (Prompt / Context / Loop / Graph Engineering)", "System-1 Decision Models (Jev, Laya)",
        "Model Cascading", "Confidence-based Routing", "Cost-Aware Inference", "Tool Routing"]

# 화면에 보여줄 묶음: (제목, [(소분류, 기술 목록)]). 묶음 순서도 핵심 → 최신 → 기타
SKILL_GROUPS = [
    ("Languages & Backend", [("Languages", _LANGUAGES), ("Backend", _BACKEND)]),
    ("Infrastructure / DevOps", [("DevOps / CI/CD", _DEVOPS), ("Infrastructure", _INFRA), ("Cloud / AWS", _CLOUD),
                                 ("OS / Network", _OS_NETWORK)]),
    ("LLM / Agent Engineering", [("LLM / Agentic Systems", _LLM)]),
    ("AI / ML", [("AI / ML", _AI_ML)]),
    ("Database & Messaging", [("Database & Cache", _DATABASE), ("Messaging & Streaming", _MESSAGING)]),
    ("Frontend & Tools", [("Frontend", _FRONTEND), ("Testing / Tools", _TOOLS)]),
]

# 프로젝트 stack 표기 → 기술 이름 (표기가 다른 경우만)
_ALIASES = {
    "aws ec2/rds": ["AWS", "EC2", "RDS"],
    "html/css": ["HTML5", "CSS3"],
    "gateway api": ["Kubernetes Gateway API"],
    "k3s": ["k3s", "Kubernetes"],
    "laya": ["Efficient LLM Routing", "System-1 Decision Models (Jev, Laya)"],
    "claude api": ["LLM"],
    "openai api": ["LLM"],
}
# 이력서 RAISE Lab 경력에 적힌 모델 비교 (OLS, Ridge, Lasso, Random Forest)
_RESEARCH_USED = ["Linear Regression", "Ridge", "Lasso", "Random Forest"]


def _used_in_projects():
    used = set(_RESEARCH_USED)
    for project in PROJECTS:
        for item in project["stack"]:
            key = item.lower()
            used.update(_ALIASES.get(key, []))
            used.add(key)
    return used


_USED = _used_in_projects()


def is_used(skill):
    return skill in _USED or skill.lower() in _USED


SKILL_TOTAL = sum(len(items) for _, subs in SKILL_GROUPS for _, items in subs)

# 접힌 상태에서 카드마다 보여줄 6개: 난도 높고 실무 깊이가 드러나는 기술
SKILL_CORE = {
    "Languages & Backend": ["Java", "Kotlin", "Python", "Spring Boot", "FastAPI", "NestJS"],
    "Infrastructure / DevOps": ["Kubernetes", "Argo CD", "Terraform", "Kubernetes Gateway API", "Proxmox VE",
                                "ECS Fargate"],
    "LLM / Agent Engineering": ["Multi-Agent Systems", "Efficient LLM Routing", "Model Cascading", "LLM-as-a-Judge",
                                "Confidence-based Routing", "Cost-Aware Inference"],
    "AI / ML": ["PyTorch", "LLM", "Transformer", "Attention", "XGBoost", "GPBoost"],
    "Database & Messaging": ["PostgreSQL", "Apache Kafka", "Redis Streams", "RabbitMQ", "Redis", "MySQL"],
    "Frontend & Tools": ["Next.js", "React", "Playwright", "pytest", "Git", "GitHub"],
}
SKILL_REST = SKILL_TOTAL - sum(len(v) for v in SKILL_CORE.values())

SKILL_ICONS = {
    "Java": "java.png", "Python": "python_image.png", "JavaScript": "js_image.png",
    "HTML5": "html_image.png", "CSS3": "css_image.png", "React": "react_image.svg", "jQuery": "jQuery_image.png",
    "JSP": "jsp_image.png", "Spring": "spring_image.png", "Spring Boot": "springboot_image.png", "Flask": "flask.png",
    "FastAPI": "fastapi_image.svg", "Django": "django_image.svg", "MySQL": "mysql.png", "MariaDB": "mariadb.png",
    "Docker": "docker.png", "Kubernetes": "kubernetes_image.svg", "Jenkins": "jenkins.png", "AWS": "aws.png",
    "Git": "git.png", "GitHub": "github.png",
}

if __name__ == "__main__":
    assert SKILL_TOTAL == 99, SKILL_TOTAL
    assert is_used("Flask") and is_used("Kubernetes") and not is_used("Apache Kafka")
    for title, subs in SKILL_GROUPS:
        every = [i for _, items in subs for i in items]
        assert len(SKILL_CORE[title]) == 6 and set(SKILL_CORE[title]) <= set(every), title
    print("ok", SKILL_TOTAL)
