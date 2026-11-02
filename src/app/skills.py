# 기술 스택 단일 원본 (메인 Skills 섹션).
# "프로젝트에 사용" 강조는 손으로 고르지 않고, projects.py의 stack과 이력서 연구 경력에 실제로 나온 기술만 자동으로 표시한다.
from .projects import PROJECTS

# 원래 분야별 목록 (사용자가 정리한 표 그대로)
_LANGUAGES = ["Java", "Python", "JavaScript", "TypeScript", "C", "C++", "PHP", "SQL", "Kotlin"]
_FRONTEND = ["HTML5", "CSS3", "React", "Next.js", "jQuery", "AJAX", "Hugo"]
_BACKEND = ["Spring", "Spring Boot", "Node.js", "Flask", "FastAPI", "NestJS", "Django", "JSP", "Java Servlet",
            "SQLAlchemy", "Alembic"]
_DATABASE = ["MySQL", "MariaDB", "SQLite", "PostgreSQL", "Redis"]
_MESSAGING = ["Redis Streams", "RabbitMQ", "Apache Kafka"]
_CLOUD = ["AWS", "EC2", "VPC", "ALB", "Auto Scaling", "RDS", "ECS Fargate", "ECR", "CloudWatch"]
_DEVOPS = ["Docker", "Kubernetes", "k3s", "Argo CD", "Jenkins", "GitHub Actions", "GHCR", "Terraform"]
_INFRA = ["Proxmox VE", "LXC", "Caddy", "Nginx", "Traefik", "Kubernetes Gateway API"]
_OS_NETWORK = ["Linux", "Ubuntu", "Debian", "CentOS", "Windows Server", "SSH", "Tailscale", "Cloudflare",
               "Cloudflare Tunnel", "Reverse Proxy", "CORS"]
_TOOLS = ["Git", "GitHub", "Playwright", "pytest", "Google Colab", "Obsidian"]
_AI_ML = ["PyTorch", "scikit-learn", "XGBoost", "GPBoost", "Linear Regression", "Ridge", "Lasso", "Random Forest",
          "Decision Tree", "CNN", "RNN", "LSTM", "Attention", "Transformer"]
_LLM = ["Efficient LLM Routing", "Multi-Agent Systems", "LLM-as-a-Judge",
        "Harness Engineering (Prompt / Context / Loop / Graph Engineering)", "System-1 Decision Models (Jev, Laya)",
        "Model Cascading", "Confidence-based Routing", "Cost-Aware Inference", "Tool Routing"]

# 화면에 보여줄 묶음: (제목, [(소분류, 기술 목록)])
SKILL_GROUPS = [
    ("Languages & Backend", [("Languages", _LANGUAGES), ("Backend", _BACKEND)]),
    ("Database & Messaging", [("Database & Cache", _DATABASE), ("Messaging & Streaming", _MESSAGING)]),
    ("Infrastructure / DevOps", [("DevOps / CI/CD", _DEVOPS), ("Infrastructure", _INFRA), ("Cloud / AWS", _CLOUD),
                                 ("OS / Network", _OS_NETWORK)]),
    ("AI / ML", [("AI / ML", _AI_ML)]),
    ("LLM / Agent Engineering", [("LLM / Agentic Systems", _LLM)]),
    ("Frontend & Tools", [("Frontend", _FRONTEND), ("Testing / Tools", _TOOLS)]),
]

# 프로젝트 stack 표기 → 기술 이름 (표기가 다른 경우만)
_ALIASES = {
    "aws ec2/rds": ["AWS", "EC2", "RDS"],
    "html/css": ["HTML5", "CSS3"],
    "gateway api": ["Kubernetes Gateway API"],
    "k3s": ["k3s", "Kubernetes"],
    "laya": ["Efficient LLM Routing", "System-1 Decision Models (Jev, Laya)"],
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

SKILL_ICONS = {
    "Java": "java.png", "Python": "python_image.png", "JavaScript": "js_image.png",
    "HTML5": "html_image.png", "CSS3": "css_image.png", "React": "react_image.svg", "jQuery": "jQuery_image.png",
    "JSP": "jsp_image.png", "Spring": "spring_image.png", "Spring Boot": "springboot_image.png", "Flask": "flask.png",
    "FastAPI": "fastapi_image.svg", "Django": "django_image.svg", "MySQL": "mysql.png", "MariaDB": "mariadb.png",
    "Docker": "docker.png", "Kubernetes": "kubernetes_image.svg", "Jenkins": "jenkins.png", "AWS": "aws.png",
    "Git": "git.png", "GitHub": "github.png",
}

if __name__ == "__main__":
    assert SKILL_TOTAL == 98, SKILL_TOTAL
    assert is_used("Flask") and is_used("Kubernetes") and not is_used("Apache Kafka")
    print("ok", SKILL_TOTAL)
