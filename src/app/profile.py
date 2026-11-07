# 프로필·경력 단일 원본 (메인 Experience 섹션). 내용은 기존 이력서 카드 문구 그대로, 영어는 직역.
from .projects import T

PROFILE = {
    "name": T("이강현", "Kanghyun Lee"),
    "role": "Backend Developer",
    "school": T("연세대학교 미래캠퍼스 · 컴퓨터공학", "Yonsei University Mirae Campus · Computer Engineering"),
    "photo": "증명사진_2023.jpg",
    "email": "lkh599810@naver.com",
    "links": [
        {"label": "GitHub", "url": "https://github.com/lkh599810"},
        {"label": "Blog", "url": "https://blog.naver.com/lkh599810"},
    ],
    "certs": [
        {"name": T("정보처리기사", "Engineer Information Processing"),
         "issuer": T("국가기술자격 · 한국산업인력공단", "National Technical Qualification · HRD Korea")},
        {"name": T("정보처리산업기사", "Industrial Engineer Information Processing"),
         "issuer": T("국가기술자격 · 한국산업인력공단", "National Technical Qualification · HRD Korea")},
        {"name": T("네트워크관리사 2급", "Network Administrator Level 2"),
         "issuer": T("국가공인 민간자격 · 한국정보통신자격협회", "Nationally Accredited Private Qualification · ICQA")},
    ],
    "language": {"name": "English · OPIc", "grade": "IH", "detail": "Intermediate High"},
}

# kind: work(실무) / research(연구). projects: 관련 상세 페이지 slug
EXPERIENCE = [
    {
        "kind": "work",
        "org": T("(주) 에듀토셀", "Edutosel Co., Ltd."),
        "period": "2021.10 ~ 2023.04",
        "items": T(
            [
                "AI 기반 영어 학습 콘텐츠 플랫폼 기획 및 백엔드 개발",
                "TOSEL Lab 메인 웹사이트 기획, DB 설계, 백엔드 개발",
                "TOSEL SSO 통합 로그인 및 마이크로서비스 간 S2S API 설계",
                "Monthly Test 성적 관리 서비스 DB 설계, 자동 채점 스크립트 구현, API 개발",
                "Self Study, Voca Quiz, Placement Test 콘텐츠 DB 설계 및 API 개발",
                "TOSEL 신규 SCM 시스템 및 Admin/ERP 기획, 프론트엔드/백엔드 개발",
            ],
            [
                "Planning and backend development of an AI-based English learning content platform",
                "TOSEL Lab main website: planning, DB design, backend development",
                "TOSEL SSO single sign-on and S2S API design between microservices",
                "Monthly Test score management: DB design, automated grading scripts, API development",
                "DB design and APIs for the Self Study, Voca Quiz, and Placement Test contents",
                "Planning and frontend/backend development of the new TOSEL SCM system and Admin/ERP",
            ],
        ),
        "projects": ["tosel-lab", "tosel-sso", "tosel-refactoring", "tosel-book-mall"],
    },
    {
        "kind": "work",
        "org": T("주식회사 앤서시스템", "Answer System Co., Ltd."),
        "period": "2023.05 ~ 2023.09",
        "items": T(
            [
                "소프트웨어 백신 유지보수 및 기술지원",
                "공공기관 고객사 환경별 백신 업데이트 및 프로그램 최적화",
                "내부망, 폐쇄망, 외부망 환경의 네트워크 및 서버 장애 대응",
                "Windows, Linux, CentOS 환경의 백신 관련 장애 대응 및 복구",
            ],
            [
                "Maintenance and technical support for antivirus software",
                "Antivirus updates and program tuning for each public-sector customer environment",
                "Network and server incident response on internal, closed, and external networks",
                "Antivirus-related incident response and recovery on Windows, Linux, and CentOS",
            ],
        ),
        "projects": [],
    },
    {
        "kind": "work",
        "org": T("넥셀시스템 주식회사 (외주)", "Nexel System Co., Ltd. (Outsourced)"),
        "period": "2025.02 ~ 2025.06",
        "items": T(
            [
                "기존 웹사이트 전체 레이아웃 재정비 및 신규 페이지 구축",
                "디자인 요소 및 인터랙션 개선을 통한 UI/UX 고도화",
                "노후 DB 분석 및 Front-end 기반 정적 데이터 처리 구조 재설계",
                "PHP 기반 레거시 서버 코드 리팩토링 및 응답 속도 개선",
            ],
            [
                "Reorganized the whole layout of the existing website and built new pages",
                "Improved the UI/UX through design elements and interactions",
                "Analyzed the aging DB and redesigned static data handling on the front end",
                "Refactored legacy PHP server code and improved response time",
            ],
        ),
        "projects": ["nexell-renewal"],
    },
    {
        "kind": "research",
        "org": T("연세대학교 미래캠퍼스 RAISE Lab (학부연구생)",
                 "RAISE Lab, Yonsei University Mirae Campus (Undergraduate Researcher)"),
        "period": T("2025.09 ~ 현재", "2025.09 ~ Present"),
        "items": T(
            [
                "의료·환경 데이터 기반 통계 분석 및 머신러닝 연구",
                "남성 생식건강–환경인자 연관성 분석: 2018~2024 정액검사 데이터와 대기오염·기상요인 연관성 분석, 데이터셋 구축",
                "OLS, Ridge, Lasso, Random Forest, XGBoost, GPBoost 모델 비교, Optuna 하이퍼파라미터 최적화, SHAP 변수 중요도 분석",
                "반복측정 의료데이터 모델링: GEE, GLMM, LMM 및 GPBoost, BiMM 기반 예측 성능 비교, 교란변수 보정 (R, Python)",
                "부인과질환–환경인자 연관성 분석: HIRA 건강보험 데이터 전처리, Negative Binomial Regression 발생률 모델링",
            ],
            [
                "Statistical analysis and machine learning research on medical and environmental data",
                "Male reproductive health and environmental factors: analyzed 2018–2024 semen test data against air pollution and weather, and built the dataset",
                "Compared OLS, Ridge, Lasso, Random Forest, XGBoost, and GPBoost; Optuna hyperparameter tuning; SHAP feature importance",
                "Repeated-measures medical data: compared GEE, GLMM, LMM with GPBoost and BiMM, with confounder adjustment (R, Python)",
                "Gynecologic disease and environmental factors: preprocessed HIRA health insurance data and modeled incidence with Negative Binomial Regression",
            ],
        ),
        "projects": ["semen-quality-environment", "gynecologic-disease-environment"],
    },
]
# 최신 경력이 위로 (period 앞 'YYYY.MM'으로 정렬, 실무·연구는 템플릿에서 따로 묶음)
EXPERIENCE.sort(key=lambda e: (e["period"]["ko"] if isinstance(e["period"], dict) else e["period"])[:7], reverse=True)

# 메인 Featured: 서로 다른 경험을 보여주는 대표 프로젝트 3개 (kind는 UI 라벨)
FEATURED = [
    {"slug": "tosel-lab", "kind": T("상용 서비스 개발 · 운영", "Commercial service · operations")},
    {"slug": "llm-routing", "kind": T("AI · LLM 엔지니어링", "AI · LLM engineering")},
    {"slug": "homelab", "kind": T("인프라 · 배포 자동화", "Infrastructure · deployment automation")},
]

# Hero 배포 파이프라인: 이 사이트의 실제 배포 과정 (.github/workflows, k3s/portfolio.yaml, 홈랩 문서 기준)
PIPELINE = [
    {"name": "git push", "summary": T("main 브랜치에 Push", "Push to main"),
     "code": "git push origin main",
     "note": T("k3s/ 경로만 바뀐 커밋은 빌드 제외 (paths-ignore)",
               "Commits touching only k3s/ skip the build (paths-ignore)")},
    {"name": "GitHub Actions", "summary": T("Docker 이미지 빌드", "Build the Docker image"),
     "code": "docker/build-push-action@v6",
     "note": T("커밋 SHA · latest 두 태그로 이미지 빌드",
               "Image build tagged with the commit SHA and latest")},
    {"name": "GHCR", "summary": T("이미지 저장 · 태그 갱신", "Store image · bump tag"),
     "code": "ghcr.io/lkh599810/lkh-portfolio:<sha>",
     "note": T("봇이 k3s/portfolio.yaml 이미지 태그를 새 SHA로 갱신 후 커밋 ([skip ci])",
               "Bot bumps the image tag in k3s/portfolio.yaml to the new SHA and commits ([skip ci])")},
    {"name": "Argo CD", "summary": T("Git → 클러스터 동기화", "Sync Git to the cluster"),
     "code": "k3s/portfolio.yaml",
     "note": T("Git의 매니페스트 기준으로 클러스터 상태 동기화",
               "Cluster state synced to the manifest in Git")},
    {"name": "k3s", "summary": T("Pod 교체 · 서비스 반영", "Roll out the Pod"),
     "code": "Service portfolio :80 → Pod :5001",
     "note": T("Caddy → Traefik Gateway(HTTPRoute) → introduce.leekanghyun.co.kr",
               "Caddy → Traefik Gateway (HTTPRoute) → introduce.leekanghyun.co.kr")},
]
