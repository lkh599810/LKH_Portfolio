# 프로젝트 데이터 단일 원본: 메인 Projects 탭/카드와 /projects/<slug> 상세 페이지가 모두 이 파일을 읽는다.
# 텍스트는 T(ko, en)으로 한/영을 같이 적는다. 이미지 경로는 /static/images/ 기준 파일명.
# 상세 섹션 블록 타입: p, ul, figures, table, steps, stats, note, sub(하위 프로젝트)


def T(ko, en):
    return {"ko": ko, "en": en}


CATEGORIES = [
    {"key": "all", "label": T("전체", "All")},
    {"key": "service", "label": T("서비스 · 플랫폼", "Services · Platforms")},
    {"key": "research", "label": T("AI · Research", "AI · Research")},
]

TAGS = {
    "work": T("실무", "Work"),
    "personal": T("개인", "Personal"),
    "team": T("팀", "Team"),
    "research": T("연구", "Research"),
    "outsourced": T("외주", "Contract Development"),
}

TOSEL_WEB_STACK = "Python · Flask · MariaDB · Jinja2 · jQuery"


def fig(src, caption=None, alt=None, thumb=None):
    # thumb: 갤러리 하단 썸네일용 작은 정지 이미지 (애니메이션 원본을 썸네일로 받지 않게)
    return {"src": src, "caption": caption, "alt": alt or (caption["ko"] if caption else src), "thumb": thumb}


PROJECTS = [
    # ------------------------------------------------------------------ 서비스 · 플랫폼
    {
        "slug": "tosel-lab",
        "category": "service",
        "tags": ["work", "team"],
        "title": "TOSEL Lab Platform",
        "summary": T(
            "TOSEL 지정교육기관과 원생을 위한 영어 학습 콘텐츠 플랫폼. 메인 사이트와 4개 학습 콘텐츠의 DB 설계·백엔드 API 개발.",
            "English learning platform for TOSEL-designated academies. I designed the DB and built backend APIs for the main site and four learning contents.",
        ),
        "intro": T(
            "20여 년간 영어능력 인증시험을 운영해 온 TOSEL의 신규 학습 콘텐츠 플랫폼입니다. 2022년 8월 정식 출시된 상용 서비스로, 기획부터 개발·배포·운영까지 참여했습니다.",
            "TOSEL's new learning content platform, built on 20 years of running an English proficiency test. It launched commercially in August 2022, and I worked on it from planning through development, deployment, and operations.",
        ),
        "stack": ["Python", "Flask", "MariaDB", "JWT", "jQuery", "Jinja2", "OpenCV", "pytesseract"],
        "cover": "TOSEL_LAB_Banner.png",
        "hero": "tosel_lab_platform_image.png",
        "period": T("2022.03 ~ 2022.06 개발 · 2022.08 출시 후 운영", "Built 2022.03–2022.06 · operated after the 2022.08 launch"),
        "role": T("백엔드 개발 · 기획 · DB 설계", "Backend development · planning · DB design"),
        "team": "Backend 2 · Frontend 1 · Designer 1",
        "org": T("(주) 에듀토셀", "Edutosel Co., Ltd."),
        "sections": [
            {
                "id": "background",
                "title": T("배경 · 요구사항", "Background & requirements"),
                "blocks": [
                    {"ul": T(
                        [
                            "전국 학원 중 심사를 통과한 곳을 <span class=\"highlight\">TOSEL Lab 지정교육기관</span>으로 선정하고, 해당 기관 원생에게 진단 데이터·처방·학습 콘텐츠를 제공하는 서비스.",
                            "기존 TOSEL 시험 사이트는 모든 기능이 한 곳에 몰린 Monolithic 구조여서, 신규 학습 서비스를 그대로 붙이기 어려웠음.",
                            "심사를 통과한 기관만 이용할 수 있어야 하고, 원장·강사·학생 등 <span class=\"highlight\">14종의 사용자 유형</span>별 권한이 달라야 했음.",
                        ],
                        [
                            "Academies that pass a screening become <span class=\"highlight\">designated TOSEL Lab institutions</span>; their students receive diagnostic data, prescriptions, and learning content.",
                            "The existing TOSEL test site was a monolith with every feature in one place, so new learning services could not simply be attached to it.",
                            "Only screened institutions could use the service, and permissions had to differ across <span class=\"highlight\">14 user types</span> such as directors, teachers, and students.",
                        ],
                    )},
                ],
            },
            {
                "id": "architecture",
                "title": T("아키텍처", "Architecture"),
                "blocks": [
                    {"p": T(
                        "기존 시험 사이트 리뉴얼까지 고려해 <span class=\"highlight\">TOSEL Lab 메인 사이트 + 4개 디지털 콘텐츠</span>를 각각 독립 서비스로 두는 Microservices 구조로 설계했습니다. 사용자 인증은 별도 SSO 서비스가 담당하고, 서비스 간 데이터는 S2S REST API로 주고받습니다.",
                        "Planning ahead for the renewal of the old test site, I designed a microservices layout: <span class=\"highlight\">the TOSEL Lab main site plus four digital contents</span>, each as its own service. A separate SSO service handles authentication, and services exchange data through S2S REST APIs.",
                    )},
                    {"steps": [
                        T("사용자 (기관 · 학생)", "User (institution · student)"),
                        T("TOSEL SSO · JWT 쿠키", "TOSEL SSO · JWT cookie"),
                        T("메인 사이트 (권한별 화면)", "Main site (per-role views)"),
                        T("콘텐츠 서비스 4종", "Four content services"),
                        T("S2S REST API · MariaDB", "S2S REST API · MariaDB"),
                    ]},
                    {"ul": T(
                        [
                            "프론트엔드 서버와 API 서버가 서로 다른 서브도메인에서 동작 — Cross-Origin 요청을 처리하도록 <span class=\"highlight\">CORS 허용 정책</span>을 설정하고 API를 연동.",
                            "JWT 기반 토큰으로 사용자 접근 권한을 확인하고, 기관·사용자 유형별로 접근 가능한 기능을 분리.",
                        ],
                        [
                            "The frontend and API servers ran on different subdomains, so I configured a <span class=\"highlight\">CORS allow policy</span> for cross-origin requests and wired up the APIs.",
                            "JWT-based tokens check access rights, and available features are split by institution and user type.",
                        ],
                    )},
                ],
            },
            {
                "id": "features",
                "title": T("세부 서비스", "Sub-projects"),
                "blocks": [
                    {"sub": {
                        "title": "TOSEL Lab Main Website",
                        "meta": T("2022.03 ~ 2022.06 · Backend 2, Frontend 1, Designer 1", "2022.03–2022.06 · Backend 2, Frontend 1, Designer 1"),
                        "blocks": [
                            {"ul": T(
                                [
                                    "지정교육기관과 원생이 학습 콘텐츠를 이용하는 공식 홈페이지.",
                                    "프로젝트 기획, 유저 플로우 설계, DB 설계, 기능 API·S2S REST API 개발.",
                                    "14종 사용자 유형에 따른 DB 설계와 JWT 기반 권한 관리 API 개발.",
                                ],
                                [
                                    "The official site where designated institutions and their students use learning content.",
                                    "Project planning, user flow design, DB design, feature APIs and S2S REST APIs.",
                                    "DB design for 14 user types and JWT-based permission management APIs.",
                                ],
                            )},
                            {"figures": [
                                fig("TOSEL_LAB_Banner.png", T("메인 화면", "Main page")),
                                fig("tosel_lab_detail3.png", T("진단 및 학습 흐름 안내", "Diagnosis and learning flow")),
                                fig("tosel_lab_detail_4.png", T("서비스 상세 화면", "Service detail")),
                                fig("tosel_lab_detail5.png", T("원생 등록 (엑셀 일괄 업로드)", "Student registration (Excel bulk upload)")),
                                fig("tosel_lab_detail_6.png", T("마이페이지 · 학습 현황", "My page · learning progress")),
                                fig("tosel_lab_detail7.png", T("마이페이지 · 콘텐츠 바로가기", "My page · content shortcuts")),
                                fig("tosel_lab_detail8.png", T("Voca 학습 결과 목록", "Voca results list")),
                                fig("tosel_lab_detail2.png", T("메인 사이트와 콘텐츠 서비스 구조 스케치", "Sketch of the main site and content services")),
                            ]},
                        ],
                    }},
                    {"sub": {
                        "title": "Monthly Test",
                        "meta": T("2022.05 ~ 2022.06 · Backend 2, Frontend 1, Designer 1", "2022.05–2022.06 · Backend 2, Frontend 1, Designer 1"),
                        "blocks": [
                            {"ul": T(
                                [
                                    "지정교육기관 원생이 매월 응시하는 월별고사 콘텐츠.",
                                    "시험 프로세스 기획, 다양한 문항 형태·리소스에 대응하는 문항 DB 설계, 문항 레이아웃과 타이머 설계.",
                                ],
                                [
                                    "A monthly exam taken by students of designated institutions.",
                                    "Planned the exam flow, designed a question DB for varied formats and resources, and built question layouts and the timer.",
                                ],
                            )},
                            {"figures": [
                                fig("monthly_start.png", T("시험 시작 화면", "Exam start")),
                                fig("monthly_listening.png", T("Listening 문항", "Listening section")),
                                fig("monthly_reading.png", T("Reading 문항", "Reading section")),
                                fig("monthly_detail_receive.png", T("시험 접수 화면", "Exam registration")),
                            ]},
                        ],
                    }},
                    {"sub": {
                        "title": T("Monthly Test · 성적 처리", "Monthly Test · score processing"),
                        "meta": T("2022.05 ~ 2022.06 · Backend 2", "2022.05–2022.06 · Backend 2"),
                        "blocks": [
                            {"ul": T(
                                [
                                    "학교·지역·학원별 평균과 응시자 선택 답안을 추적하기 쉽도록 성적 DB를 기획·설계.",
                                    "오프라인 응시 대응을 위해 여러 업체와 협의해 자체 프로그램에 맞는 OMR을 제작.",
                                    "<span class=\"highlight\">OCR로 OMR 데이터 로딩 → 오답 정정 → 엑셀 변환 → 자동화 스크립트로 성적 DB 적재</span> 흐름을 정립.",
                                ],
                                [
                                    "Designed the score DB so school, region, and academy averages and each taker's chosen answers are easy to track.",
                                    "Worked with vendors to produce OMR sheets that fit our program for offline takers.",
                                    "Set up the flow <span class=\"highlight\">OMR data via OCR → error correction → Excel → automation script into the score DB</span>.",
                                ],
                            )},
                        ],
                    }},
                    {"sub": {
                        "title": T("Monthly Test · 성적표", "Monthly Test · score report"),
                        "meta": T("2022.05.23 ~ 2022.06.01 · Backend 1, Frontend 1", "2022.05.23–2022.06.01 · Backend 1, Frontend 1"),
                        "blocks": [
                            {"ul": T(
                                [
                                    "진단·처방을 위해 지역·학교·학원별 평균과 미국 학생 독서 지수(AR/Lexile) 비교표를 포함하도록 기획.",
                                    "평균 비교·AR/Lexile 산출 알고리즘, 개인/전체 평균 성적 DB와 데이터 로딩 로직 구현.",
                                    "짧은 일정 때문에 퍼블리싱·프론트엔드 일부도 맡아 chart.js로 시각화.",
                                ],
                                [
                                    "Included region, school, and academy averages plus an AR/Lexile comparison for diagnosis and prescription.",
                                    "Built the average-comparison and AR/Lexile algorithms, the individual/overall score DB, and data loading.",
                                    "The schedule was tight, so I also took part of the publishing/frontend work and charted results with chart.js.",
                                ],
                            )},
                            {"figures": [
                                fig("monthly_grade_full.png", T("성적표 전체", "Full score report")),
                                fig("monthly_gradecard1.png", T("성적표 1면", "Score report, page 1")),
                                fig("monthly_gradecard2.png", T("성적표 2면", "Score report, page 2")),
                                fig("monthly_sixgrade.png", T("영역별 성적", "Scores by section")),
                                fig("monthly_check.png", T("원생 성적 확인 목록", "Student score list")),
                            ]},
                        ],
                    }},
                    {"sub": {
                        "title": "Placement Test",
                        "meta": T("2022.04 ~ 2022.05 · Backend 2, Frontend 1, Designer 1", "2022.04–2022.05 · Backend 2, Frontend 1, Designer 1"),
                        "blocks": [
                            {"ul": T(
                                [
                                    "학원 신규 원생의 학습 레벨을 평가하는 반 배치고사.",
                                    "응시자의 답에 따라 다음 문항 난이도가 달라지는 <span class=\"highlight\">Adaptive Test</span>로 기획.",
                                    "출제된 문항의 정답 여부를 통계화해 분야별 레벨을 정하는 분류 알고리즘과 문항 출제 알고리즘 구현.",
                                ],
                                [
                                    "A placement test that finds the right level for new academy students.",
                                    "Planned as an <span class=\"highlight\">adaptive test</span>: the next question's difficulty depends on the previous answers.",
                                    "Built the question selection algorithm and a classification step that turns results into a level per skill area.",
                                ],
                            )},
                            {"figures": [
                                fig("placement_intro.png", T("서비스 소개", "Service overview")),
                                fig("placement_start.png", T("시작 화면", "Start")),
                                fig("placement_info.png", T("응시 안내", "Test information")),
                                fig("placement_listening.png", T("Listening 문항", "Listening section")),
                                fig("placemnet_reading.png", T("Reading 문항", "Reading section")),
                                fig("placement_weakness.png", T("취약 영역 결과", "Weak-area result")),
                                fig("placement_review.png", T("문항 화면 (도표·이미지 지문)", "Questions with charts and images")),
                                fig("placement_done.png", T("응시 완료 · 결과 요약", "Finished · result summary")),
                            ]},
                        ],
                    }},
                    {"sub": {
                        "title": "Daily Study (Self Study)",
                        "meta": T("2022.05 ~ 2022.06 · Backend 2, Frontend 1, Designer 1", "2022.05–2022.06 · Backend 2, Frontend 1, Designer 1"),
                        "blocks": [
                            {"ul": T(
                                [
                                    "매일 문제를 풀며 자기주도 학습 습관을 기르는 일일 학습 콘텐츠.",
                                    "주 단위 문제 제공, 풀이 중 중간 저장, 원장·학생 양쪽의 오답 확인 기능 구현.",
                                    "레벨·카테고리별 문항 DB와 학생 로그 DB 설계, 원장이 원생 학습 현황을 보는 S2S API 구축.",
                                ],
                                [
                                    "A daily study content that builds self-directed study habits.",
                                    "Weekly question sets, mid-session save, and wrong-answer review for both students and directors.",
                                    "Designed question DBs by level and category plus a student log DB, and built the S2S API that shows directors their students' progress.",
                                ],
                            )},
                            {"figures": [
                                fig("daily_start.png", T("학습 시작", "Start")),
                                fig("daily_1.png", T("문제 풀이 · 빈칸 완성", "Solving · fill in the blank")),
                                fig("daily_2.png", T("문제 풀이", "Solving questions")),
                                fig("daily_3.png", T("문제 풀이 · 실용문 독해", "Solving · practical reading")),
                                fig("daily_4.png", T("문제 풀이 · 게시문 독해", "Solving · notice reading")),
                                fig("daily_finish.png", T("학습 완료", "Finished")),
                            ]},
                        ],
                    }},
                    {"sub": {
                        "title": "Voca Quiz",
                        "meta": T("2022.05.23 ~ 2022.06.01 · Backend 2, Frontend 1, Designer 1", "2022.05.23–2022.06.01 · Backend 2, Frontend 1, Designer 1"),
                        "blocks": [
                            {"ul": T(
                                [
                                    "원생의 단어 학습을 위한 단어 퀴즈 콘텐츠.",
                                    "랜덤 문항 출제 알고리즘과 문항·풀이 DB 설계.",
                                    "본인 정답률과 전체 정답률을 함께 쓰는 개인별 오답노트 알고리즘 설계.",
                                    "단어 길이에 따라 달라지는 레이아웃을 프론트엔드와 함께 설계.",
                                ],
                                [
                                    "A vocabulary quiz content for students.",
                                    "Designed the random question algorithm and the question/attempt DB.",
                                    "Designed a personal wrong-answer note algorithm that uses both personal and overall accuracy.",
                                    "Worked with the frontend on layouts that adapt to word length.",
                                ],
                            )},
                            {"figures": [
                                fig("voca_start.png", T("퀴즈 시작", "Quiz start")),
                                fig("voca_1.png", T("레벨 선택", "Level select")),
                                fig("voca_2.png", T("문항 화면", "Question")),
                                fig("voca_3.png", T("문제 세트 선택", "Question set select")),
                                fig("voca_4.png", T("제한 시간 문항", "Timed question")),
                                fig("voca_finish.png", T("결과 화면", "Result")),
                            ]},
                        ],
                    }},
                ],
            },
            {
                "id": "problems",
                "title": T("문제 해결", "Problem solving"),
                "blocks": [
                    {"ul": T(
                        [
                            "<strong>서브도메인 간 API 호출</strong> — 프론트와 API 서버가 다른 서브도메인에 있어 브라우저 요청이 차단됨. 허용 Origin을 명시한 CORS 정책과 쿠키 기반 인증을 함께 맞춰 해결.",
                            "<strong>온라인/오프라인으로 나뉜 성적 처리</strong> — 오프라인 OMR 답안을 OCR(OpenCV, pytesseract)로 읽고, 오답 정정 후 엑셀로 변환해 스크립트로 DB에 적재하는 흐름을 만들어 수작업을 줄임.",
                            "<strong>사용자 유형별 권한</strong> — 14종 사용자 유형을 DB에서 구분하고 JWT 토큰으로 접근 범위를 검사하도록 권한 관리 API를 설계.",
                        ],
                        [
                            "<strong>API calls across subdomains</strong> — the browser blocked requests because the frontend and API lived on different subdomains. Solved with a CORS policy listing allowed origins, aligned with cookie-based auth.",
                            "<strong>Score processing split between online and offline</strong> — read offline OMR answers with OCR (OpenCV, pytesseract), corrected errors, converted to Excel, and loaded them into the DB with a script, cutting manual work.",
                            "<strong>Permissions per user type</strong> — distinguished 14 user types in the DB and designed permission APIs that check access scope from JWT tokens.",
                        ],
                    )},
                ],
            },
            {
                "id": "role",
                "title": T("담당 역할", "My role"),
                "blocks": [
                    {"ul": T(
                        [
                            "서비스 초기 기획부터 개발, 협업, 런칭까지 참여.",
                            "메인 사이트와 4개 콘텐츠의 DB 설계, 기능 API와 S2S REST API 개발.",
                            "성적 처리 자동화 스크립트, 문항 출제·오답노트 알고리즘 구현.",
                        ],
                        [
                            "Took part from initial planning through development, collaboration, and launch.",
                            "DB design, feature APIs, and S2S REST APIs for the main site and the four contents.",
                            "Score processing automation scripts and question selection / wrong-answer note algorithms.",
                        ],
                    )},
                ],
            },
            {
                "id": "results",
                "title": T("성과", "Results"),
                "blocks": [
                    {"ul": T(
                        [
                            "2022년 8월 정식 출시, 전국 지정교육기관과 원생을 대상으로 운영된 상용 서비스.",
                            "메인 사이트 1개와 학습 콘텐츠 4종(Monthly Test, Placement Test, Daily Study, Voca Quiz)을 독립 서비스로 구성.",
                        ],
                        [
                            "Launched in August 2022 as a commercial service for designated institutions and students nationwide.",
                            "Built one main site and four learning contents (Monthly Test, Placement Test, Daily Study, Voca Quiz) as independent services.",
                        ],
                    )},
                ],
            },
        ],
        "links": [],
    },
    {
        "slug": "kanglish",
        "category": "service",
        "tags": ["personal"],
        "title": "Kanglish",
        "summary": T(
            "단어 학습, 빈칸 문제 풀이, 오답노트를 제공하는 영어 학습 PWA. FastAPI·Next.js로 직접 만들어 홈랩 Kubernetes에서 운영 중.",
            "An English learning PWA with vocabulary study, fill-in-the-blank quizzes, and review notes. Built with FastAPI and Next.js and deployed on my homelab Kubernetes.",
        ),
        "intro": T(
            "TOEIC 단어장 프로젝트로 시작해 Kanglish로 이어진 개인 서비스입니다. 단어·문제 콘텐츠는 모든 사용자가 공유하고, 풀이 기록과 오답노트만 사용자별로 분리합니다.",
            "A personal service that started as a TOEIC vocabulary project and became Kanglish. Words and questions are shared by everyone; attempts and review notes are kept per user.",
        ),
        "stack": ["FastAPI", "Next.js", "TypeScript", "SQLAlchemy", "Alembic", "SQLite", "Tailwind CSS", "Docker"],
        "cover": None,
        "cover_note": "Vocabulary · Quiz · Review",
        "period": T("2026.07 ~ 운영 중", "2026.07 – running"),
        "role": T("기획 · 백엔드 · 프론트엔드 · 배포 (개인)", "Planning · backend · frontend · deployment (solo)"),
        "team": T("개인 프로젝트", "Solo project"),
        "sections": [
            {
                "id": "background",
                "title": T("요구사항", "Requirements"),
                "blocks": [
                    {"ul": T(
                        [
                            "단어 외우기(단어·발음·뜻·예문)와 빈칸 채우기 객관식 문제 풀이, 틀린 문제를 다시 보는 오답노트.",
                            "여러 사람이 각자 계정으로 사용 — 콘텐츠는 공유, 학습 기록만 사용자별 분리.",
                            "웹과 앱을 따로 만들지 않고, 하나의 코드베이스로 데스크톱과 모바일을 지원하며 홈 화면에 설치할 수 있는 PWA.",
                        ],
                        [
                            "Vocabulary study (word, pronunciation, meaning, example), fill-in-the-blank multiple-choice questions, and a review note for wrong answers.",
                            "Multiple users with their own accounts — content is shared, only study records are per user.",
                            "One codebase for desktop and mobile, installable to the home screen as a PWA instead of separate web and native apps.",
                        ],
                    )},
                ],
            },
            {
                "id": "architecture",
                "title": T("시스템 설계", "System design"),
                "blocks": [
                    {"steps": [
                        T("Next.js PWA (TypeScript · Tailwind)", "Next.js PWA (TypeScript · Tailwind)"),
                        T("REST /api/v1", "REST /api/v1"),
                        T("FastAPI", "FastAPI"),
                        T("SQLAlchemy 2.x · Alembic", "SQLAlchemy 2.x · Alembic"),
                        T("SQLite", "SQLite"),
                    ]},
                    {"ul": T(
                        [
                            "백엔드·프론트엔드 이미지를 GitHub Actions에서 빌드해 GHCR에 올리고, Argo CD가 홈랩 k3s에 배포.",
                            "서비스워커는 프로덕션 빌드에서만 등록. 정적 화면은 network-first + 캐시 폴백, <span class=\"highlight\">/api/ 응답은 캐시하지 않음</span> — 계정 정보와 오답노트가 다른 사용자에게 재사용되지 않도록.",
                            "초기 데이터는 엑셀(TOEIC 단어 1,455개)에서 import했고, 이후 <span class=\"highlight\">DB를 원본(source of truth)으로 전환</span>. importer는 최초 부트스트랩 전용으로 제한.",
                        ],
                        [
                            "GitHub Actions builds backend and frontend images and pushes them to GHCR; Argo CD deploys them to the homelab k3s cluster.",
                            "The service worker registers only in production builds. Static screens use network-first with cache fallback, and <span class=\"highlight\">/api/ responses are never cached</span> so account data and review notes are not reused across users.",
                            "Initial data was imported from Excel (1,455 TOEIC words); later <span class=\"highlight\">the DB became the source of truth</span> and the importer was limited to the first bootstrap.",
                        ],
                    )},
                ],
            },
            {
                "id": "db",
                "title": T("DB 설계", "Database design"),
                "blocks": [
                    {"p": T(
                        "문제는 <code>questions → question_blanks → question_options</code>로 나누고, 정답은 <code>question_answers</code>에 둡니다. 애플리케이션 검증에 기대지 않고 DB 제약으로 잘못된 데이터를 막는 데 집중했습니다.",
                        "Questions are split into <code>questions → question_blanks → question_options</code>, with answers in <code>question_answers</code>. The focus was on rejecting bad data with DB constraints rather than relying on application checks.",
                    )},
                    {"ul": T(
                        [
                            "<code>question_answers</code>의 PK를 <code>blank_id</code>로 두어, 한 빈칸에 정답이 둘 이상 들어가는 것을 DB 차원에서 차단.",
                            "복합 FK <code>(question_option_id, blank_id) → question_options(id, blank_id)</code>로 \"정답은 반드시 그 빈칸의 보기\"를 강제. 2빈칸 문제에서 다른 빈칸의 보기를 정답으로 넣으면 SQLite가 거부하며, 테스트로 검증.",
                            "오답노트 테이블을 따로 만들지 않고 <code>question_attempts</code> 하나에서 오답노트·정답률·복습 우선순위를 파생.",
                            "다의어(approval, bear 등 10종) 때문에 <code>word</code>에 UNIQUE를 두지 않음.",
                        ],
                        [
                            "<code>question_answers</code> uses <code>blank_id</code> as its primary key, so a blank can never have two answers.",
                            "A composite FK <code>(question_option_id, blank_id) → question_options(id, blank_id)</code> enforces that an answer must be one of that blank's options. Pointing a two-blank question's answer at the other blank's option is rejected by SQLite, and tests cover it.",
                            "No separate review-note table: review notes, accuracy, and review priority are all derived from <code>question_attempts</code>.",
                            "<code>word</code> has no UNIQUE constraint because of polysemous words (10 cases such as approval and bear).",
                        ],
                    )},
                ],
            },
            {
                "id": "features",
                "title": T("주요 기능", "Key features"),
                "blocks": [
                    {"ul": T(
                        [
                            "단어장과 단어 북마크, 빈칸 객관식 문제 풀이와 채점.",
                            "오답노트 두 화면 — 문제·내 답·정답을 함께 보는 노트, 정답을 가리고 다시 푸는 재풀이.",
                            "회원가입(이메일 인증 코드)·로그인·로그아웃·비밀번호 재설정.",
                            "관리자 화면에서 단어와 문제를 추가·수정·삭제. 쓰기 API는 관리자 권한 라우터에만 등록.",
                        ],
                        [
                            "Vocabulary list with bookmarks, fill-in-the-blank questions with grading.",
                            "Two review screens — a note showing the question, my answer, and the correct answer, and a retry mode that hides the answer.",
                            "Sign-up with an email verification code, login, logout, and password reset.",
                            "An admin screen to create, edit, and delete words and questions; write APIs live only on an admin-only router.",
                        ],
                    )},
                    {"table": {
                        "head": [T("테이블", "Table"), T("행 수", "Rows")],
                        "rows": [
                            ["vocabularies", "1,456"],
                            ["questions", "103"],
                            ["question_blanks", "104"],
                            ["question_options", "415"],
                        ],
                        "caption": T("프로젝트 문서(2026-10-30) 기준 콘텐츠 규모", "Content size per the project docs (2026-10-30)"),
                    }},
                ],
            },
            {
                "id": "problems",
                "title": T("문제 해결", "Problem solving"),
                "blocks": [
                    {"ul": T(
                        [
                            "<strong>DB가 원본이 된 뒤의 데이터 보호</strong> — 계정과 학습 기록은 DB에만 있어 복구할 곳이 없음. 서버 실행 중 24시간마다 백업하고 최근 7개를 보관. 실행 중 파일을 그냥 복사하면 쓰기 중간 페이지가 섞일 수 있어 <span class=\"highlight\">SQLite 온라인 백업 API</span>를 사용.",
                            "<strong>문제 수정과 풀이 기록</strong> — 수정은 문구·정답만 허용해 보기 id를 유지하고, 빈칸·보기 개수 변경은 거부. 풀이 기록이 있는 문제 삭제는 409로 막고 <code>?force=true</code>를 요구.",
                            "<strong>인증</strong> — 비밀번호는 scrypt로 해싱, 토큰은 HttpOnly/SameSite 쿠키로 전달하고 DB에는 SHA-256 해시만 저장. 상태를 바꾸는 요청은 허용된 Origin만 받고 API 응답은 no-store.",
                            "<strong>정답 노출 방지</strong> — 재풀이 화면은 정답이 포함된 오답노트 응답 대신 문제 목록 API를 사용.",
                        ],
                        [
                            "<strong>Protecting data once the DB is the source</strong> — accounts and study records exist only in the DB. The server takes a backup every 24 hours and keeps the last seven, using the <span class=\"highlight\">SQLite online backup API</span> because copying the file mid-write can mix pages.",
                            "<strong>Editing questions vs. attempt history</strong> — edits may change only text and the correct answer so option ids stay stable; changing blank or option counts is rejected. Deleting an answered question returns 409 unless <code>?force=true</code> is passed.",
                            "<strong>Authentication</strong> — passwords hashed with scrypt; tokens sent as HttpOnly/SameSite cookies with only their SHA-256 stored. State-changing requests must come from allowed origins, and API responses are no-store.",
                            "<strong>Not leaking answers</strong> — the retry screen loads questions from the question API instead of the review-note response, which contains answers.",
                        ],
                    )},
                ],
            },
            {
                "id": "results",
                "title": T("운영 · 검증", "Operations & testing"),
                "blocks": [
                    {"ul": T(
                        [
                            "<code>kanglish.leekanghyun.co.kr</code>에서 운영 중이며, 홈랩의 Argo CD에서 Synced/Healthy 상태 확인 (2026-11-01).",
                            "인증·권한·마이그레이션·엑셀 import를 포함한 pytest 테스트 함수 176개, 프론트엔드 node 테스트.",
                        ],
                        [
                            "Running at <code>kanglish.leekanghyun.co.kr</code>; Argo CD on the homelab reported Synced/Healthy (2026-11-01).",
                            "176 pytest test functions covering auth, permissions, migrations, and Excel import, plus frontend node tests.",
                        ],
                    )},
                ],
            },
            {
                "id": "limits",
                "title": T("한계 · 개선", "Limits & next steps"),
                "blocks": [
                    {"ul": T(
                        [
                            "SQLite WAL 모드가 아직 꺼져 있어, 동시 사용자가 늘면 쓰기 중 읽기가 막힐 수 있음.",
                            "백업 사본이 원본과 같은 디스크에 있어 기기 장애는 막지 못함 — 외부 복사는 미결정.",
                            "단어 학습 기록(vocabulary_reviews)과 앱 내 엑셀 import/export는 계획 단계.",
                        ],
                        [
                            "SQLite WAL mode is not enabled yet, so reads can block during writes as concurrent users grow.",
                            "Backups sit on the same disk as the database, so they do not protect against device failure — off-site copies are undecided.",
                            "Vocabulary review history (vocabulary_reviews) and in-app Excel import/export are still planned.",
                        ],
                    )},
                ],
            },
        ],
        "links": [
            {"label": T("서비스", "Live service"), "url": "https://kanglish.leekanghyun.co.kr/"},
        ],
    },
    {
        "slug": "homelab",
        "category": "service",
        "tags": ["personal"],
        "title": T("홈랩 구축 및 서비스 인프라 운영", "Homelab & Service Infrastructure"),
        "summary": T(
            "미니PC 한 대에 Proxmox·k3s·Caddy를 올리고 Argo CD GitOps로 포트폴리오·Kanglish·AlignFit을 직접 배포·운영하는 셀프 호스팅 환경.",
            "A self-hosted setup on one mini PC: Proxmox, k3s, and Caddy, with Argo CD GitOps deploying and running this portfolio, Kanglish, and AlignFit.",
        ),
        "intro": T(
            "Intel N100 미니PC의 Proxmox VE 위에 Caddy 리버스 프록시(LXC)와 단일 노드 Kubernetes(k3s, VM)를 분리해 두고, Traefik Gateway API와 Argo CD로 개인 서비스 3개를 배포·운영합니다.",
            "On an Intel N100 mini PC running Proxmox VE, a Caddy reverse proxy (LXC) and a single-node Kubernetes cluster (k3s, VM) are kept separate, and three personal services are deployed and run with the Traefik Gateway API and Argo CD.",
        ),
        "stack": ["Proxmox VE", "k3s", "Caddy", "Traefik", "Gateway API", "Argo CD", "GitHub Actions", "GHCR", "Docker"],
        "cover": "projects/homelab-architecture.svg",
        "hero": None,
        "period": T("2026.03 ~ 운영 중", "2026.03 – running"),
        "role": T("설계 · 구축 · 운영 (개인)", "Design · build · operations (solo)"),
        "team": T("개인 프로젝트", "Solo project"),
        "sections": [
            {
                "id": "goals",
                "title": T("설계 목표", "Goals"),
                "blocks": [
                    {"ul": T(
                        [
                            "물리 서버 한 대에서 여러 애플리케이션을 격리된 실행 환경으로 운영.",
                            "외부 HTTPS 요청을 하나의 진입 경로로 받고, 도메인별로 Kubernetes Service에 전달.",
                            "소스 코드 → 컨테이너 이미지 → Kubernetes 배포 명세를 연결해 GitHub Push만으로 배포.",
                            "공용 Gateway 설정과 서비스별 배포 설정을 서로 다른 Git 저장소에서 관리.",
                        ],
                        [
                            "Run several applications in isolated environments on a single physical server.",
                            "Accept external HTTPS through one entry point and route each domain to its Kubernetes Service.",
                            "Link source code → container image → Kubernetes manifest so a GitHub push is enough to deploy.",
                            "Manage the shared Gateway and each service's deployment config in separate Git repositories.",
                        ],
                    )},
                ],
            },
            {
                "id": "architecture",
                "title": T("인프라 아키텍처", "Infrastructure architecture"),
                "blocks": [
                    {"figures": [fig(
                        "projects/homelab-architecture.svg",
                        T("현재 운영 구조. 실선은 사용자 요청, 점선은 배포·설정 흐름", "Current production layout. Solid lines are user traffic, dashed lines are delivery and config"),
                        "Homelab architecture: Caddy LXC and k3s VM on Proxmox, Traefik Gateway routing to Portfolio, Kanglish, AlignFit, with GitHub Actions, GHCR and Argo CD",
                    )], "wide": True},
                    {"table": {
                        "head": [T("계층", "Layer"), T("구성요소", "Component"), T("역할", "Role")],
                        "rows": [
                            [T("하드웨어", "Hardware"), "Intel N100 Mini PC", T("개인 서비스용 물리 호스트", "Physical host for personal services")],
                            [T("가상화", "Virtualization"), "Proxmox VE", T("LXC · VM 호스팅", "Hosts LXC and VM")],
                            [T("진입점 · TLS", "Ingress · TLS"), "Gateway LXC + Caddy", T("외부 HTTPS 수신, TLS 종료, 리버스 프록시", "Receives HTTPS, terminates TLS, reverse proxy")],
                            [T("오케스트레이션", "Orchestration"), "Ubuntu VM + k3s", T("단일 노드 Kubernetes", "Single-node Kubernetes")],
                            [T("클러스터 라우팅", "In-cluster routing"), "Traefik · Gateway API", T("NodePort 30080, HTTPRoute로 Host/Path 매칭", "NodePort 30080, Host/Path matching via HTTPRoute")],
                            ["GitOps", "Argo CD", T("Git의 매니페스트를 클러스터와 동기화 (Application 4개)", "Syncs Git manifests to the cluster (4 Applications)")],
                            ["CI · Image", "GitHub Actions + GHCR", T("테스트, 이미지 빌드·게시, 배포 태그 갱신", "Tests, image build/push, manifest tag update")],
                        ],
                    }},
                ],
            },
            {
                "id": "routing",
                "title": T("요청 라우팅", "Request routing"),
                "blocks": [
                    {"p": T(
                        "Caddy는 세 서비스의 HTTPS 요청을 모두 하나의 Traefik NodePort <code>30080</code>으로 넘깁니다. Traefik은 Gateway API 리소스에 따라 Host와 Path를 매칭해 Service를 고릅니다. 새 서비스는 NodePort를 추가하지 않고 서비스 저장소에 HTTPRoute를 추가하는 방식으로 붙입니다.",
                        "Caddy forwards HTTPS for all three services to a single Traefik NodePort, <code>30080</code>. Traefik matches Host and Path from Gateway API resources to pick the Service. A new service is added by putting an HTTPRoute in its own repository, not by opening another NodePort.",
                    )},
                    {"table": {
                        "head": [T("도메인", "Domain"), "HTTPRoute", T("백엔드", "Backend")],
                        "rows": [
                            ["introduce.leekanghyun.co.kr", "default/portfolio-route", "Service portfolio :80 → Pod :5001"],
                            ["kanglish.leekanghyun.co.kr", T("Kanglish Route (default)", "Kanglish route (default)"), T("Kanglish Service → Pod", "Kanglish Service → Pod")],
                            ["alignfit-api.leekanghyun.co.kr", "alignfit/alignfit", "Service alignfit-api :8000 → Pod :8000"],
                        ],
                    }},
                ],
            },
            {
                "id": "gitops",
                "title": T("CI/CD · GitOps", "CI/CD & GitOps"),
                "blocks": [
                    {"steps": [
                        T("git push (main)", "git push (main)"),
                        T("GitHub Actions · 테스트 · 이미지 빌드", "GitHub Actions · test · image build"),
                        T("GHCR · image:commit SHA", "GHCR · image:commit SHA"),
                        T("k3s/*.yaml 이미지 태그 커밋", "Commit image tag in k3s/*.yaml"),
                        T("Argo CD Sync", "Argo CD sync"),
                        T("Deployment 롤아웃", "Deployment rollout"),
                    ]},
                    {"ul": T(
                        [
                            "<span class=\"highlight\">공용 리소스와 서비스 리소스를 분리</span> — GatewayClass·Gateway는 private 저장소 <code>homelab-infra</code>에서 관리하고 Argo CD에서 수동 Sync. 각 서비스 저장소는 자신의 Deployment·Service·HTTPRoute만 관리하고 Auto Sync.",
                            "공용 Gateway에는 <code>Prune=false</code>, <code>Delete=false</code>를 걸어 앱 쪽 변경이 공용 진입점을 지우지 않도록 보호.",
                            "<code>:latest</code>가 아니라 커밋 SHA 태그를 매니페스트에 기록해 어떤 코드가 배포됐는지 추적 가능하게 함.",
                            "이 포트폴리오 저장소도 같은 흐름 — <code>k3s/**</code>만 바뀐 커밋은 이미지 재빌드를 건너뛰고, 태그 갱신 커밋에는 <code>[skip ci]</code>를 붙여 루프를 막음.",
                        ],
                        [
                            "<span class=\"highlight\">Shared vs. per-service resources</span> — GatewayClass and Gateway live in the private <code>homelab-infra</code> repo with manual sync in Argo CD. Each service repo owns only its Deployment, Service, and HTTPRoute, with auto sync.",
                            "The shared Gateway carries <code>Prune=false</code> and <code>Delete=false</code> so app-side changes cannot remove the shared entry point.",
                            "Manifests record commit-SHA image tags instead of <code>:latest</code>, so the deployed code is traceable.",
                            "This portfolio repo uses the same flow — commits touching only <code>k3s/**</code> skip the image rebuild, and tag-bump commits carry <code>[skip ci]</code> to avoid loops.",
                        ],
                    )},
                ],
            },
            {
                "id": "problems",
                "title": T("트러블슈팅", "Troubleshooting"),
                "blocks": [
                    {"ul": T(
                        [
                            "<strong>NodePort에서 Gateway API로 이전</strong> — AlignFit은 처음에 NodePort 30081로 따로 노출했으나, Traefik Gateway + HTTPRoute 구조로 옮기고 비상용 롤백 매니페스트를 남김.",
                            "<strong>Gateway 소유권 분리</strong> — 포트폴리오 저장소에 있던 공용 Gateway 정의를 <code>homelab-infra</code>로 옮겨, 한 서비스의 변경이 다른 서비스 라우팅에 영향을 주지 않게 함.",
                            "<strong>역할 분리</strong> — 외부 TLS는 Caddy(LXC), 서비스별 HTTP 라우팅은 Traefik(k3s)이 담당하도록 나눠 장애 범위와 설정 위치를 구분.",
                        ],
                        [
                            "<strong>From NodePort to Gateway API</strong> — AlignFit was first exposed on its own NodePort 30081; it moved to Traefik Gateway + HTTPRoute, with an emergency rollback manifest kept.",
                            "<strong>Separating Gateway ownership</strong> — the shared Gateway definition moved from this portfolio repo to <code>homelab-infra</code>, so one service's change cannot affect another's routing.",
                            "<strong>Clear responsibilities</strong> — external TLS stays in Caddy (LXC) and per-service HTTP routing in Traefik (k3s), separating failure domains and config locations.",
                        ],
                    )},
                ],
            },
            {
                "id": "results",
                "title": T("운영 검증 (2026-11-01)", "Verification (2026-11-01)"),
                "blocks": [
                    {"stats": [
                        {"value": "3", "label": T("운영 중인 서비스", "Services running")},
                        {"value": "4", "label": T("Argo CD Application (Synced/Healthy)", "Argo CD Applications (Synced/Healthy)")},
                        {"value": "200", "label": T("세 도메인 HTTPS 응답", "HTTPS status on all three domains")},
                    ]},
                    {"note": T(
                        "위 결과는 인프라 연결과 준비 상태를 확인한 것입니다. 부하 테스트, 장애 복구 성능, 모든 앱의 E2E 테스트까지 검증한 것은 아닙니다.",
                        "These checks confirm connectivity and readiness only. Load testing, failure recovery, and end-to-end tests for every app were not part of this verification.",
                    )},
                ],
            },
            {
                "id": "limits",
                "title": T("한계 · 개선", "Limits & next steps"),
                "blocks": [
                    {"ul": T(
                        [
                            "단일 노드 구성이라 고가용성(HA)이나 무중단 배포를 보장하지 않음.",
                            "모니터링·로그 수집 스택은 아직 없음 — 장애 감지는 수동 확인에 의존.",
                            "공유기 포트포워딩·DNS 등 네트워크 경계 구성은 문서화가 더 필요.",
                        ],
                        [
                            "A single node, so no high availability or zero-downtime guarantee.",
                            "No monitoring or log collection stack yet — failure detection relies on manual checks.",
                            "Network edge setup (router port forwarding, DNS) needs more documentation.",
                        ],
                    )},
                ],
            },
        ],
        "links": [
            {"label": T("배포 매니페스트 (이 저장소)", "Manifests (this repo)"), "url": "https://github.com/lkh599810/LKH_Portfolio/tree/main/k3s"},
        ],
    },
    {
        "slug": "tosel-sso",
        "category": "service",
        "parent": "tosel-lab",
        "tags": ["work", "team"],
        "title": "TOSEL SSO",
        "summary": T(
            "TOSEL 서비스들의 학습-평가-분석 사이클을 잇는 통합 유저 관리 서비스. JWT 쿠키 발급, S2S REST API 담당.",
            "An integrated user service linking the learn-assess-analyze cycle across TOSEL services. I handled JWT cookie issuing and the S2S REST APIs.",
        ),
        "intro": T(
            "TOSEL Lab과 콘텐츠 서비스들이 한 번의 로그인으로 사용자 정보와 데이터 접근 권한을 공유하도록 만든 SSO 서비스입니다.",
            "An SSO service that lets TOSEL Lab and its content services share user identity and data access rights from a single login.",
        ),
        "stack": ["Python", "Flask", "JWT", "CORS", "MariaDB"],
        "cover": "sso_image.png",
        "cover_fit": "contain",
        "hero": "sso_image.png",
        "period": "2022.04 ~ 2022.05",
        "role": T("백엔드 개발 (S2S API)", "Backend development (S2S APIs)"),
        "team": "Backend 2",
        "org": T("(주) 에듀토셀", "Edutosel Co., Ltd."),
        "sections": [
            {
                "id": "design",
                "title": T("설계", "Design"),
                "blocks": [
                    {"ul": T(
                        [
                            "SSO 서버가 JWT 쿠키를 발급해 로그인 여부와 데이터 접근 권한을 관리. 다른 서브도메인 서비스와 연계하기 위해 CORS 기반으로 개발.",
                            "<strong>refresh-token</strong> — 로그인 상태 유지용, 만료 전 주기적으로 갱신.",
                            "<strong>access-token</strong> — refresh-token으로 발급, 지정된 권한 범위 안에서만 데이터 요청, 연장 불가.",
                        ],
                        [
                            "The SSO server issues JWT cookies to manage login state and data access; built on CORS to work with services on other subdomains.",
                            "<strong>refresh-token</strong> — keeps the login alive and is renewed before it expires.",
                            "<strong>access-token</strong> — issued from the refresh-token, grants access only within its scope, cannot be extended.",
                        ],
                    )},
                    {"steps": [
                        T("로그인", "Login"),
                        T("refresh-token 발급 (쿠키)", "Issue refresh-token (cookie)"),
                        T("access-token 발급", "Issue access-token"),
                        T("서비스별 권한 범위 내 요청", "Scoped requests per service"),
                    ]},
                ],
            },
            {
                "id": "role",
                "title": T("담당 역할", "My role"),
                "blocks": [
                    {"ul": T(
                        ["서비스 간 사용자 정보를 제공하는 S2S REST API 구축."],
                        ["Built the S2S REST APIs that serve user information between services."],
                    )},
                ],
            },
            {
                "id": "lessons",
                "title": T("배운 점", "Lessons"),
                "blocks": [
                    {"p": T(
                        "통합 회원 DB는 모든 서비스가 공통으로 쓰는 회원 정보를 먼저 파악한 뒤 설계해야 한다는 점을 체감했습니다.",
                        "I learned that an integrated member DB has to start from the member data every service shares.",
                    )},
                ],
            },
        ],
        "links": [],
    },
    {
        "slug": "tosel-refactoring",
        "category": "service",
        "parent": "tosel-lab",
        "tags": ["work", "team"],
        "title": "Business Model Refactoring",
        "summary": T(
            "10년간 유지보수만 이어 온 TOSEL 시험 사이트 분석, 시험·학습 서비스를 Microservices 구조로 재설계.",
            "Analyzed a TOSEL test site maintained for a decade and redesigned test and learning services as microservices.",
        ),
        "intro": T(
            "TOSEL Business Process Model을 Microservices Architecture 기반으로 재설계한 프로젝트입니다. TOSEL Lab 개발과 같은 기간에 진행했습니다.",
            "A redesign of TOSEL's business process model on a microservices architecture, carried out alongside TOSEL Lab.",
        ),
        "stack": ["Microservices", "DB Modeling", "ERD", "REST API"],
        "cover": "refactor_modeling2.png",
        "hero": "refactor_modeling2.png",
        "period": "2022.03 ~ 2022.06",
        "role": T("기획 · 리팩토링 설계 참여", "Planning · refactoring design"),
        "team": "Backend 2 · Frontend 1 · Designer 1",
        "org": T("(주) 에듀토셀", "Edutosel Co., Ltd."),
        "sections": [
            {
                "id": "background",
                "title": T("배경", "Background"),
                "blocks": [
                    {"ul": T(
                        [
                            "기존 TOSEL 웹사이트는 시험 접수·변경·성적 확인을 제공하는 응시자 중심 플랫폼.",
                            "포스트 코로나 시기 영어 학습 콘텐츠 사업(TOSEL Lab)을 새로 시작하며 서비스 확장이 필요.",
                            "기존 사이트에 확장 서비스를 붙이기엔 구조적 문제가 많았음.",
                        ],
                        [
                            "The old TOSEL website was a test-taker platform for registration, changes, and score checks.",
                            "Post-COVID, TOSEL started a learning content business (TOSEL Lab) and needed to expand.",
                            "The old site had too many structural problems to extend.",
                        ],
                    )},
                ],
            },
            {
                "id": "problems",
                "title": T("문제 정의", "Problem"),
                "blocks": [
                    {"ul": T(
                        [
                            "<strong>노후화된 코드</strong> — 10년간 유지보수만 진행, 낮은 JDK 버전으로 HTTPS 기반 API 호출 불가.",
                            "<strong>정규화되지 않은 DB</strong> — 임시로 덧붙인 구조로 중복·쓰레기 데이터가 쌓여 무결성 미보장.",
                            "<strong>서비스 혼재</strong> — 대상 사용자가 다른 서비스가 Monolithic 구조에 섞여 사용·관리(Admin/ERP)가 어려움.",
                        ],
                        [
                            "<strong>Outdated code</strong> — only maintained for 10 years; an old JDK blocked HTTPS-based API calls.",
                            "<strong>Unnormalized DB</strong> — ad-hoc structures piled up duplicate and garbage data, breaking integrity.",
                            "<strong>Mixed services</strong> — services for different users were tangled in a monolith, hard to use and manage (Admin/ERP).",
                        ],
                    )},
                    {"figures": [
                        fig("refactor_oldtosel_ppt1.png", T("기존 Monolithic 구조", "Old monolithic structure")),
                        fig("refactor_oldtosel_site.png", T("기존 TOSEL 사이트", "Old TOSEL site")),
                        fig("refactor_oldtosel_site2.png", T("기존 TOSEL 사이트 · 시험 레벨 안내", "Old TOSEL site · test levels")),
                        fig("refactoring_erd1.png", T("기존 DB 분석 ERD", "ERD of the old DB")),
                        fig("refactor_modeling2.png", T("재설계한 비즈니스 프로세스 모델", "Redesigned business process model")),
                        fig("refactoring_erd3.png", T("재설계 ERD", "Redesigned ERD")),
                    ]},
                ],
            },
            {
                "id": "solution",
                "title": T("해결 · 역할", "Solution & role"),
                "blocks": [
                    {"ul": T(
                        [
                            "기존 시험 사이트 전면 리뉴얼과 신규 학습 콘텐츠 사이트를 Microservices Architecture로 설계.",
                            "TOSEL Lab과 같은 기간에 진행하며 기획·리팩토링 계획 전반에 참여.",
                            "기존 구조의 한계를 분석하고, 서비스 경계를 나누는 아키텍처 설계를 경험.",
                        ],
                        [
                            "Designed the full renewal of the test site and the new learning sites on a microservices architecture.",
                            "Ran alongside TOSEL Lab; took part in all planning and refactoring decisions.",
                            "Analyzed the old structure's limits and practiced drawing service boundaries.",
                        ],
                    )},
                ],
            },
        ],
        "links": [],
    },
    {
        "slug": "tosel-book-mall",
        "category": "service",
        "parent": "tosel-lab",
        "tags": ["work", "team"],
        "title": T("TOSEL 교재몰 (SCM)", "TOSEL Book Mall (SCM)"),
        "summary": T(
            "공급망관리시스템(SCM)과 쇼핑몰 역할을 함께 하는 교재몰. 교재 DB, 유저별 권한 관리, S2S API 설계·개발.",
            "A book mall that works as both a supply chain system and an online shop. I designed the book DB, per-user permissions, and S2S APIs.",
        ),
        "intro": T(
            "전화·팩스·이메일로 흩어져 있던 교재 주문과 엑셀 수기 재고 관리를 하나로 묶은 TOSEL 교재몰입니다.",
            "The TOSEL book mall, consolidating textbook orders that arrived by phone, fax, and email, and stock tracked by hand in Excel.",
        ),
        "stack": ["DB Design", "REST API", "Web · Mobile"],
        "cover": "mall_main.png",
        "hero": "mall_main.png",
        "period": "2022.01 ~ 2022.04",
        "role": T("기획 · DB 설계 · 백엔드", "Planning · DB design · backend"),
        "team": "Backend 2 · Frontend 1 · Designer 1",
        "org": T("(주) 에듀토셀", "Edutosel Co., Ltd."),
        "sections": [
            {
                "id": "requirements",
                "title": T("요구사항 · SCM 선택", "Requirements · why SCM"),
                "blocks": [
                    {"ul": T(
                        [
                            "초판·증쇄·개정·재고 상태 등 교재 특성상 현황 관리와 추적이 필요.",
                            "일반회원·지역본부·총판 등 4종 사용자별로 기능과 화면이 달라야 함.",
                            "총판·지역본부는 주문 규모가 커서 증쇄 여부 판단이 필요.",
                            "전화·팩스·이메일·메신저로 제각각이던 주문 방식을 통합할 필요.",
                            "엑셀 수기 관리로 금액·재고 불일치가 잦아 자동화가 필요.",
                        ],
                        [
                            "Textbooks need tracking of editions, reprints, revisions, and stock status.",
                            "Four user types (general members, regional offices, distributors, etc.) need different features and views.",
                            "Distributors and regional offices order in bulk, so reprint decisions are needed.",
                            "Orders arrived by phone, fax, email, and messenger and needed one channel.",
                            "Manual Excel tracking caused price and stock mismatches; automation was needed.",
                        ],
                    )},
                ],
            },
            {
                "id": "design",
                "title": T("설계 · 구현", "Design & implementation"),
                "blocks": [
                    {"ul": T(
                        [
                            "웹/모바일 대응, 프로젝트 기획·유저 플로우·와이어프레임 설계.",
                            "<span class=\"highlight\">교재 DB 설계, 유저별 권한 관리 시스템, S2S API</span>, 메인·상세 페이지 구축.",
                        ],
                        [
                            "Web and mobile support; project planning, user flows, and wireframes.",
                            "<span class=\"highlight\">Book DB, per-user permission system, S2S APIs</span>, main and detail pages.",
                        ],
                    )},
                    {"figures": [
                        fig("mall_main.png", T("메인 화면", "Main page")),
                        fig("mall_user_category.png", T("사용자 유형 정의", "User types")),
                        fig("mall_wireframe.png", T("와이어프레임", "Wireframe")),
                        fig("mall_admin_wireframe.png", T("관리자 와이어프레임", "Admin wireframe")),
                        fig("mall_bookdetail.png", T("교재 상세 화면", "Book detail")),
                        fig("mall_detail.png", T("카테고리별 교재 목록", "Books by category")),
                    ]},
                ],
            },
            {
                "id": "lessons",
                "title": T("배운 점", "Lessons"),
                "blocks": [
                    {"p": T(
                        "기존 사업 구조를 빠르게 파악해 필요한 기능을 정의하고 개발하는 경험을 했습니다.",
                        "I practiced learning an existing business quickly and turning it into a feature list.",
                    )},
                ],
            },
        ],
        "links": [],
    },
    {
        "slug": "nexell-renewal",
        "category": "service",
        "tags": ["outsourced"],
        "title": T("넥셀시스템 웹사이트 리뉴얼", "Nexel System Website Renewal"),
        "summary": T(
            "노후화된 기업 웹사이트를 전면 리뉴얼한 외주 프로젝트. 레이아웃 재정비, PHP 레거시 리팩토링, 응답 속도 개선 담당.",
            "Contract development renewing an aging corporate website: layout overhaul, legacy PHP refactoring, and faster responses.",
        ),
        "intro": T(
            "넥셀시스템 주식회사의 기업 웹사이트를 리뉴얼한 외주 프로젝트입니다.",
            "A freelance project to renew Nexel System's corporate website.",
        ),
        "stack": ["PHP", "JavaScript", "HTML/CSS"],
        "cover": "nexell_new.png",
        "hero": "nexell_new.png",
        "period": "2025.02 ~ 2025.06",
        "role": T("웹 개발 (외주)", "Web development (freelance)"),
        "team": T("외주", "Contract Development"),
        "sections": [
            {
                "id": "work",
                "title": T("주요 업무", "Key work"),
                "blocks": [
                    {"ul": T(
                        [
                            "기존 웹사이트 전체 레이아웃 재정비 및 신규 페이지 구축.",
                            "디자인 요소와 인터랙션을 개선해 UI/UX 정리.",
                            "노후 DB를 분석하고 <span class=\"highlight\">Front-end 기반 정적 데이터 처리 구조</span>로 재설계.",
                            "PHP 레거시 서버 코드 리팩토링 — 불필요한 의존성 제거, 코드 모듈화, 로직 재구성.",
                            "경량화와 최적화로 <span class=\"highlight\">웹사이트 응답 속도 개선</span>.",
                        ],
                        [
                            "Reorganized the entire site layout and built new pages.",
                            "Cleaned up UI/UX by improving design elements and interactions.",
                            "Analyzed the aging DB and redesigned it as a <span class=\"highlight\">front-end based static data structure</span>.",
                            "Refactored legacy PHP code — removed unneeded dependencies, modularized code, restructured logic.",
                            "<span class=\"highlight\">Faster responses</span> through lightweighting and optimization.",
                        ],
                    )},
                ],
            },
            {
                "id": "result",
                "title": T("리뉴얼 전 / 후", "Before / after"),
                "blocks": [
                    {"figures": [
                        fig("nexell_old.png", T("리뉴얼 전", "Before")),
                        fig("nexell_new.png", T("리뉴얼 후", "After")),
                    ], "wide": True},
                ],
            },
        ],
        "links": [],
    },
    {
        "slug": "sarangmoa",
        "category": "service",
        "tags": ["personal"],
        "title": T("연세 사랑모아", "Yonsei SarangMoa"),
        "summary": T(
            "연세대 구성원이 안 쓰는 물품을 기부하고 판매 수익금으로 나눔을 실천하는 웹 플랫폼. 권한 등급과 기부 물품 상태 워크플로 설계.",
            "A web platform where Yonsei members donate unused items and proceeds go to good causes. I designed role levels and the donated-item workflow.",
        ),
        "intro": T(
            "학생·교직원이 기부한 물품을 저렴하게 판매하고, 수익금은 교내외 봉사단체와 프로젝트 지원에 쓰는 교내 기부·나눔 플랫폼입니다.",
            "A campus donation platform: items donated by students and staff are sold cheaply, and proceeds support volunteer groups and projects.",
        ),
        "stack": ["Django", "SQLite", "jQuery", "AJAX"],
        "cover": "sarangmoa_category.jpg",
        "hero": "sarangmoa_category.jpg",
        "period": "2024.11 ~ 2024.12",
        "role": T("웹 개발", "Web development"),
        "team": T("개인 프로젝트", "Solo project"),
        "sections": [
            {
                "id": "service",
                "title": T("서비스", "Service"),
                "blocks": [
                    {"ul": T(
                        [
                            "기부 물품 판매, 수익금으로 봉사단체·프로젝트 지원.",
                            "기부자에게 <span class=\"highlight\">마일리지</span>를 적립해 이벤트 상품으로 교환.",
                            "자원봉사자 모집, 봉사점수·봉사활동 확인서 발급.",
                        ],
                        [
                            "Sells donated items; proceeds support volunteer groups and projects.",
                            "Donors earn <span class=\"highlight\">mileage</span> to exchange for event rewards.",
                            "Recruits volunteers and issues volunteer points and certificates.",
                        ],
                    )},
                ],
            },
            {
                "id": "features",
                "title": T("주요 구현", "Key features"),
                "blocks": [
                    {"ul": T(
                        [
                            "세션 기반 로그인·회원가입, 재학증명서 이미지 업로드로 가입 인증.",
                            "<span class=\"highlight\">권한 등급별 접근 제어</span> — 미승인·승인 회원·관리자 3단계. 재학증명서 검증 후 관리자 승인을 받은 회원만 구매 가능, 관리자 메뉴는 관리자에게만 노출.",
                            "<span class=\"highlight\">기부 물품 상태 워크플로</span> — 신청 → 승인/반려 → 판매 완료 → 삭제. 승인·반려를 취소하면 신청 상태로 되돌리는 관리자 검수 프로세스.",
                            "카테고리별 상품 조회와 페이지네이션 JSON API (AJAX 연동).",
                            "결제 처리 — 구매 내역 저장과 판매 완료 상태 변경, 마일리지 잔액 검증 후 차감하는 이벤트 응모.",
                            "공지사항·이벤트·좋은 사례 게시물 CRUD, 마이페이지 구매·기부 내역, 봉사활동 확인서 페이지.",
                        ],
                        [
                            "Session-based login and sign-up, verified with an uploaded enrollment certificate image.",
                            "<span class=\"highlight\">Role-based access</span> — three levels (pending, approved member, admin). Only members verified and approved by an admin can buy; admin menus show only to admins.",
                            "<span class=\"highlight\">Donated item workflow</span> — requested → approved/rejected → sold → deleted, with an admin review that can roll decisions back to requested.",
                            "JSON API for category-filtered, paginated listings (via AJAX).",
                            "Payment handling — saves purchases and marks items sold; event entry checks and deducts mileage.",
                            "CRUD for notices, events, and good-example posts; my page with purchase/donation history; volunteer certificate page.",
                        ],
                    )},
                    {"figures": [
                        fig("sarangmoa_category.jpg", T("카테고리별 기부 물품", "Donated items by category")),
                        fig("sarangmoa_service.jpg", T("기부 서비스 페이지", "Donation service page")),
                        fig("sarangmoa_detail.jpg", T("물품 상세", "Item detail")),
                        fig("sarangmoa_mypage.jpg", T("마이페이지", "My page")),
                        fig("sarangmoa_payment.jpg", T("결제 수단 선택", "Payment method selection")),
                        fig("sarangmoa_apply.jpg", T("기부 신청서", "Donation application form")),
                        fig("sarangmoa_admin.jpg", T("관리자 승인 화면", "Admin approval")),
                        fig("sarangmoa_manage_events.jpg", T("이벤트 관리", "Event management")),
                        fig("sarangmoa_faq.jpg", T("FAQ", "FAQ")),
                        fig("sarangmoa_certificate.jpg", T("봉사활동 확인서", "Volunteer certificate")),
                        fig("sarangmoa_signup.jpg", T("재학증명서 업로드 회원가입", "Sign-up with enrollment certificate upload")),
                    ]},
                ],
            },
        ],
        "links": [
            {"label": "GitHub", "url": "https://github.com/lkh599810/Yonsei_SarangMoa"},
        ],
    },
    {
        "slug": "card24",
        "category": "service",
        "tags": ["team"],
        "title": "CARD 24",
        "summary": T(
            "사용자 조건에 맞는 카드와 카드사를 추천하는 웹사이트. Spring Boot로 만든 첫 팀 프로젝트, AWS EC2·RDS 배포.",
            "A website that recommends cards and issuers for each user's conditions. My first team project, built with Spring Boot and deployed on AWS EC2/RDS.",
        ),
        "intro": T(
            "웹 개발을 배운 뒤 처음 진행한 팀 프로젝트입니다. 메타데이터 기반으로 사용자 조건별 카드·카드사를 추천합니다.",
            "My first team project after learning web development: metadata-based card and issuer recommendations for each user.",
        ),
        "stack": ["Java", "Spring Boot", "Spring Security", "OAuth2", "MariaDB", "AWS EC2/RDS"],
        "cover": "card8.png",
        "hero": "card8.png",
        "period": "2021.05 ~ 2021.06",
        "role": T("웹 개발", "Web development"),
        "team": T("2명", "2 people"),
        "sections": [
            {
                "id": "implementation",
                "title": T("구현", "Implementation"),
                "blocks": [
                    {"ul": T(
                        [
                            "Spring Boot MVC 2 패턴, Spring Security로 HTTP 보안, OAuth2 로그인 (Monolithic 구조).",
                            "메타데이터 기반 <span class=\"highlight\">사용자 조건별 카드·카드사 추천 알고리즘</span>, 혜택별 비교, 문의 게시판.",
                            "AWS EC2 배포 (RDS-MariaDB).",
                        ],
                        [
                            "Spring Boot MVC 2, HTTP security with Spring Security, OAuth2 login (monolith).",
                            "Metadata-based <span class=\"highlight\">card/issuer recommendation algorithm</span>, benefit comparison, inquiry board.",
                            "Deployed on AWS EC2 (RDS-MariaDB).",
                        ],
                    )},
                    {"figures": [
                        fig("card8.png", T("개발 배경과 소개", "Background and overview")),
                        fig("card4.png", T("프로젝트 일정", "Project schedule")),
                        fig("card5.png", T("DB 정의서", "DB definition")),
                        fig("card9.png", T("홈페이지 구조", "Site structure")),
                        fig("card10.png", T("사용자/관리자 로그인 · OAuth2", "User/admin login · OAuth2")),
                        fig("card11.png", T("카드 차트 · 비교함 담기", "Card chart · add to comparison")),
                        fig("card12.png", T("연령·성별·혜택 조건 검색", "Search by age, gender, benefit")),
                        fig("card13.png", T("문의 게시판 · 글쓰기/수정/삭제", "Q&A board · write, edit, delete")),
                        fig("card14.png", T("문의 게시판 · 내 작성글", "Q&A board · my posts")),
                        fig("card15.png", T("관리자 · 카드/카드사, 게시판 답글 관리", "Admin · cards, issuers, board replies")),
                        fig("card16.png", T("관리자 · 조건 검색 결과 목록", "Admin · search result list")),
                    ]},
                ],
            },
            {
                "id": "lessons",
                "title": T("트러블슈팅", "Troubleshooting"),
                "blocks": [
                    {"ul": T(
                        [
                            "MVC 2 패턴과 어노테이션 개념이 낯설어 협업 인계에 부담이 컸음.",
                            "콘솔 CRUD 게시판, JavaFX 키오스크 등 MVC 미니 프로젝트로 따로 연습해 극복하고 프로젝트를 완수.",
                        ],
                        [
                            "The MVC 2 pattern and annotations were new, and handing work off to a teammate felt heavy.",
                            "Practiced with MVC mini projects (console CRUD board, JavaFX kiosk) on my own and finished the project.",
                        ],
                    )},
                ],
            },
        ],
        "links": [
            {"label": "GitHub", "url": "https://github.com/lkh599810/CARD24_Project"},
            {"label": T("시연 영상", "Demo video"), "url": "https://www.youtube.com/watch?v=iGtQYibdWVs"},
        ],
    },
    # ------------------------------------------------------------------ AI 엔지니어링
    {
        "slug": "alignfit",
        "category": "service",
        "tags": ["personal"],
        "title": "AlignFit",
        "summary": T(
            "사진으로 자세 정렬을 분석하고 운동 영상을 평가해 홈케어 운동을 추천하는 앱. Android · FastAPI · MediaPipe · PyTorch.",
            "An app that analyzes posture from photos and evaluates exercise videos to recommend home-care exercises. Android, FastAPI, MediaPipe, PyTorch.",
        ),
        "intro": T(
            "Android 앱이 사진·영상을 올리면 FastAPI 백엔드가 MediaPipe로 포즈 랜드마크를 뽑아 정렬 상태를 분석하거나, 학습한 MLP로 동작 품질과 운동 종류를 판별합니다. 의료기기가 아니며 진단을 하지 않습니다.",
            "The Android app uploads a photo or video; the FastAPI backend extracts pose landmarks with MediaPipe to analyze alignment, or uses trained MLPs to judge movement quality and exercise type. It is not a medical device and does not diagnose.",
        ),
        "stack": ["Kotlin", "Jetpack Compose", "FastAPI", "MediaPipe", "PyTorch", "OpenCV", "SQLite", "Docker"],
        "cover": "projects/alignfit-banner-og.webp",
        "hero": "projects/alignfit-banner.webp",
        "hero_mobile": "projects/alignfit-banner-og.webp",
        "period": "2026.05 ~",
        "role": T("앱 · 백엔드 · 모델 학습 · 배포", "App · backend · model training · deployment"),
        "team": T("개인 프로젝트 (모바일프로그래밍 · 지능형멀티미디어시스템)", "Solo project (Mobile Programming · Intelligent Multimedia Systems)"),
        "sections": [
            {
                "id": "problem",
                "title": T("문제 정의", "Problem"),
                "blocks": [
                    {"p": T(
                        "통증 부위와 자세 사진만으로 어깨·골반 높이 차이 같은 정렬 상태를 확인하고, 운동 영상을 올리면 동작이 올바른지와 어떤 운동인지 판별해 집에서 할 수 있는 운동을 추천하는 것이 목표였습니다.",
                        "The goal: from pain areas and a posture photo, show alignment issues such as shoulder or hip height differences; from an exercise video, judge whether the movement is correct and which exercise it is, then recommend home exercises.",
                    )},
                ],
            },
            {
                "id": "screens",
                "title": T("앱 화면", "App screens"),
                "blocks": [
                    {"p": T(
                        "불편한 부위 선택 → 전신 사진 분석 → 결과 확인 → 상담 메모 · 맞춤 운동 → 움직임 평가 순서로 이어집니다.",
                        "Pick where it hurts → full-body photo analysis → result → consultation memo and exercises → movement evaluation.",
                    )},
                    {"portrait": True, "figures": [
                        fig("projects/alignfit-flow.webp", T("전체 흐름", "Full flow"), thumb="projects/alignfit-flow-thumb.webp"),
                        fig("projects/alignfit-home.webp", T("홈", "Home")),
                        fig("projects/alignfit-pain.webp", T("불편한 부위 선택", "Choose where it hurts")),
                        fig("projects/alignfit-body-map.webp", T("바디맵으로 부위 확인", "Body map")),
                        fig("projects/alignfit-photo-selected.webp", T("전신 사진 업로드", "Upload a full-body photo")),
                        fig("projects/alignfit-result-1.webp", T("자세 분석 결과", "Posture analysis result")),
                        fig("projects/alignfit-result-2.webp", T("통증 부위와 함께 본 해석", "Reading the result with pain areas")),
                        fig("projects/alignfit-result-3.webp", T("측정값 · 부위별 상세", "Measurements by body part")),
                        fig("projects/alignfit-consult-1.webp", T("상담 메모", "Consultation memo")),
                        fig("projects/alignfit-consult-2.webp", T("상담 때 함께 정리할 내용", "What to bring to a consultation")),
                        fig("projects/alignfit-exercise-1.webp", T("부위별 맞춤 운동 추천", "Exercises by body area")),
                        fig("projects/alignfit-exercise-2.webp", T("운동 방법 안내", "Exercise guide")),
                        fig("projects/alignfit-evaluate.webp", T("움직임 평가 (영상 업로드)", "Movement evaluation (video upload)")),
                    ]},
                ],
            },
            {
                "id": "exercises",
                "title": T("추천 운동 동작", "Exercise library"),
                "blocks": [
                    {"p": T(
                        "분석 결과에 따라 추천되는 운동 19종. 목·어깨 → 허리·코어 → 하체 순서.",
                        "The 19 exercises the app recommends from the analysis, ordered neck and shoulders → back and core → lower body.",
                    )},
                    {"figures": [
                        fig("projects/alignfit-ex/chin-tuck.webp", T("턱 당기기", "Chin tuck"), thumb="projects/alignfit-ex/chin-tuck-thumb.webp"),
                        fig("projects/alignfit-ex/neck-side-stretch.webp", T("목 옆 스트레칭", "Neck side stretch"), thumb="projects/alignfit-ex/neck-side-stretch-thumb.webp"),
                        fig("projects/alignfit-ex/scapular-retraction.webp", T("견갑 모으기", "Scapular retraction"), thumb="projects/alignfit-ex/scapular-retraction-thumb.webp"),
                        fig("projects/alignfit-ex/wall-angel.webp", T("월 엔젤", "Wall angel"), thumb="projects/alignfit-ex/wall-angel-thumb.webp"),
                        fig("projects/alignfit-ex/pec-stretch.webp", T("가슴 스트레칭", "Pec stretch"), thumb="projects/alignfit-ex/pec-stretch-thumb.webp"),
                        fig("projects/alignfit-ex/thoracic-extension.webp", T("흉추 신전", "Thoracic extension"), thumb="projects/alignfit-ex/thoracic-extension-thumb.webp"),
                        fig("projects/alignfit-ex/cat-camel.webp", T("고양이-낙타", "Cat-camel"), thumb="projects/alignfit-ex/cat-camel-thumb.webp"),
                        fig("projects/alignfit-ex/pelvic-tilt.webp", T("골반 기울이기", "Pelvic tilt"), thumb="projects/alignfit-ex/pelvic-tilt-thumb.webp"),
                        fig("projects/alignfit-ex/dead-bug.webp", T("데드버그", "Dead bug"), thumb="projects/alignfit-ex/dead-bug-thumb.webp"),
                        fig("projects/alignfit-ex/bird-dog.webp", T("버드독", "Bird dog"), thumb="projects/alignfit-ex/bird-dog-thumb.webp"),
                        fig("projects/alignfit-ex/side-plank.webp", T("사이드 플랭크", "Side plank"), thumb="projects/alignfit-ex/side-plank-thumb.webp"),
                        fig("projects/alignfit-ex/glute-bridge.webp", T("엉덩이 들기 (글루트 브릿지)", "Glute bridge"), thumb="projects/alignfit-ex/glute-bridge-thumb.webp"),
                        fig("projects/alignfit-ex/hip-flexor-stretch.webp", T("고관절 굴곡근 스트레칭", "Hip flexor stretch"), thumb="projects/alignfit-ex/hip-flexor-stretch-thumb.webp"),
                        fig("projects/alignfit-ex/hamstring-stretch.webp", T("햄스트링 스트레칭", "Hamstring stretch"), thumb="projects/alignfit-ex/hamstring-stretch-thumb.webp"),
                        fig("projects/alignfit-ex/quad-strengthening.webp", T("허벅지 앞 근육 강화", "Quad strengthening"), thumb="projects/alignfit-ex/quad-strengthening-thumb.webp"),
                        fig("projects/alignfit-ex/clamshell.webp", T("클램쉘", "Clamshell"), thumb="projects/alignfit-ex/clamshell-thumb.webp"),
                        fig("projects/alignfit-ex/calf-stretch.webp", T("종아리 스트레칭", "Calf stretch"), thumb="projects/alignfit-ex/calf-stretch-thumb.webp"),
                        fig("projects/alignfit-ex/ankle-mobility.webp", T("발목 가동성", "Ankle mobility"), thumb="projects/alignfit-ex/ankle-mobility-thumb.webp"),
                        fig("projects/alignfit-ex/single-leg-balance.webp", T("한 발 서기", "Single-leg balance"), thumb="projects/alignfit-ex/single-leg-balance-thumb.webp"),
                    ]},
                ],
            },
            {
                "id": "architecture",
                "title": T("아키텍처 · 데이터 흐름", "Architecture & data flow"),
                "blocks": [
                    {"steps": [
                        T("Android 앱 (Compose · Retrofit)", "Android app (Compose · Retrofit)"),
                        T("HTTPS · multipart 업로드", "HTTPS · multipart upload"),
                        T("FastAPI (k3s)", "FastAPI (k3s)"),
                        T("MediaPipe 랜드마크 33개", "MediaPipe, 33 landmarks"),
                        T("분석 · 추론 · 추천 DB", "Analysis · inference · recommendation DB"),
                        T("JSON 결과 + 주석 이미지", "JSON result + annotated image"),
                    ]},
                    {"table": {
                        "head": [T("엔드포인트", "Endpoint"), T("입력", "Input"), T("처리", "Processing")],
                        "rows": [
                            ["POST /analyze/image", T("JPEG/PNG ≤ 20MB", "JPEG/PNG ≤ 20MB"), T("포즈 랜드마크 → 규칙 기반 정렬 분석 (어깨·골반·머리·몸통 중심선·발 방향) → 팁 + 주석 이미지", "Pose landmarks → rule-based alignment (shoulder, hip, head, trunk line, feet) → tips + annotated image")],
                            ["POST /predict", T("영상 ≤ 100MB, ≤ 60초", "Video ≤ 100MB, ≤ 60 s"), T("2프레임마다 PoseLandmarker → 69차원 특징 → MLP 2개 (동작 품질, 운동 9종) → SQLite 추천", "PoseLandmarker every 2nd frame → 69-d features → two MLPs (quality, 9 exercises) → SQLite recommendations")],
                            ["GET /health", "–", T("서버·영상 모델 로드 상태", "Server and video model status")],
                        ],
                    }},
                ],
            },
            {
                "id": "ai",
                "title": T("AI 활용", "AI usage"),
                "blocks": [
                    {"ul": T(
                        [
                            "<strong>사진 분석</strong> — 학습 모델 없이 MediaPipe 랜드마크 좌표로 기울기·중심 편차·각도를 계산하고, 임계값(예: 몸통 기울기 3°/7°, 발 방향 차이 8°/15°)으로 정도를 구분. 랜드마크 가시성이 낮으면 해당 항목을 판단하지 않음.",
                            "<strong>영상 평가</strong> — 관절 각도 15개의 평균·표준편차·범위·최댓값과 좌우 대칭 특징 9개로 69차원 벡터를 만들고, PyTorch MLP 두 개가 동작 품질(정상/비정상)과 운동 종류(9종)를 분류.",
                            "운영 추론 코드는 연구용 특징 추출기를 그대로 옮긴 독립 모듈로, 연구 코드(<code>src/</code>)를 import하지 않음.",
                            "<code>torch.load</code>는 pickle을 해제하므로, 모델 파일을 읽기 전에 SHA256 체크섬을 검증해 신뢰된 파일만 로드.",
                        ],
                        [
                            "<strong>Photo analysis</strong> — no trained model: slopes, center offsets, and angles from MediaPipe landmarks, graded by thresholds (e.g. trunk tilt 3°/7°, foot direction 8°/15°). Items with low landmark visibility are not judged.",
                            "<strong>Video evaluation</strong> — a 69-d vector from the mean/std/range/max of 15 joint angles plus 9 left-right symmetry features; two PyTorch MLPs classify movement quality (correct/incorrect) and exercise type (9 classes).",
                            "Production inference is a standalone port of the research feature extractor and never imports the research code (<code>src/</code>).",
                            "<code>torch.load</code> unpickles, so model files are checked against SHA256 sums before loading.",
                        ],
                    )},
                ],
            },
            {
                "id": "results",
                "title": T("테스트 · 결과", "Testing & results"),
                "blocks": [
                    {"p": T(
                        "MobiPhysio 데이터셋(24명, 534개 시퀀스)을 피험자 단위로 train/val/test 분할해, 같은 사람이 학습과 평가에 동시에 들어가지 않도록 했습니다. 지표는 클래스 불균형을 고려해 macro-F1을 기준으로 봤습니다.",
                        "The MobiPhysio dataset (24 subjects, 534 sequences) was split by subject into train/val/test so no person appears in both training and evaluation. Macro-F1 is the headline metric because of class imbalance.",
                    )},
                    {"table": {
                        "head": [T("과제", "Task"), "Majority", "Nearest centroid", T("MLP (배포)", "MLP (deployed)")],
                        "rows": [
                            [T("동작 품질 (2클래스)", "Movement quality (2 classes)"), "0.33", "0.61", "<strong>0.70</strong>"],
                            [T("운동 종류 (9클래스)", "Exercise type (9 classes)"), "0.03", "0.74", "<strong>0.88</strong>"],
                        ],
                        "caption": T("피험자 단위 held-out test set의 macro-F1", "Macro-F1 on the subject-wise held-out test set"),
                    }},
                    {"ul": T(
                        [
                            "GitHub Actions에서 pytest API 계약 테스트·모델 체크섬 검증 → 이미지 빌드 → 컨테이너 smoke test → GHCR 게시 → 매니페스트 갱신 순으로 실행.",
                            "운영 도메인 <code>/health</code> HTTP 200 확인 (2026-11-01).",
                        ],
                        [
                            "GitHub Actions runs pytest API contract tests and model checksum checks → image build → container smoke test → GHCR push → manifest bump.",
                            "Production <code>/health</code> returned HTTP 200 (2026-11-01).",
                        ],
                    )},
                ],
            },
            {
                "id": "limits",
                "title": T("한계", "Limitations"),
                "blocks": [
                    {"ul": T(
                        [
                            "학습한 영상 모델 가중치는 데이터 라이선스 문제로 공개 이미지에 포함하지 않아, 현재 운영 서버의 <code>/predict</code>는 503을 반환할 수 있음. 사진 분석(<code>/analyze/image</code>)은 동작.",
                            "MobiPhysio에는 프레임별 원시 시퀀스가 없어 요약 특징 기반 MLP만 평가했고, 시계열 1D-CNN은 이 데이터에 적용하지 못함.",
                            "동작 품질 macro-F1 0.70은 실사용 판정에 충분한 수준이라고 보기 어려움. 결과는 교육용 참고 정보로만 제공.",
                        ],
                        [
                            "Trained video weights are not in the public image because of data licensing, so production <code>/predict</code> may return 503. Photo analysis (<code>/analyze/image</code>) works.",
                            "MobiPhysio has no raw per-frame sequences, so only summary-feature MLPs were evaluated; a temporal 1D-CNN could not be applied to it.",
                            "A movement-quality macro-F1 of 0.70 is not enough for real-world judgment; results are shown as educational reference only.",
                        ],
                    )},
                ],
            },
        ],
        "links": [
            {"label": "GitHub", "url": "https://github.com/lkh599810/AlignFit"},
            {"label": T("API 문서 (Swagger)", "API docs (Swagger)"), "url": "https://alignfit-api.leekanghyun.co.kr/docs"},
        ],
    },
    {
        "slug": "llm-routing",
        "category": "research",
        "tags": ["personal"],
        "title": "Cost-Aware Efficient Routing",
        "summary": T(
            "LLM 코드 리뷰 하네스 앞에 Laya decision model 라우터를 붙여 커밋마다 필요한 검사만 호출. API 비용 40.4~42.1% 절감.",
            "Put a Laya decision-model router in front of an LLM code-review harness and measured a 40.4–42.1% API cost drop when only the needed checks run per commit.",
        ),
        "intro": T(
            "커밋마다 일관성(CA)·보안(VA)·형식(FA) 리뷰어를 항상 고성능 모델로 전부 부르는 대신, 라우터가 필요한 검사와 모델 크기를 고르게 했을 때 비용·호출 수·판정 성능·시간이 어떻게 달라지는지 비교한 실험입니다.",
            "Instead of always calling consistency (CA), security (VA), and format (FA) reviewers on a strong model for every commit, a router picks the checks and model size; the experiment compares cost, calls, accuracy, and time.",
        ),
        "stack": ["Python", "Claude API", "Laya", "Structured Output"],
        "cover": "laya_structure.jpg",
        "hero": "laya_structure.jpg",
        "period": "2026",
        "role": T("설계 · 구현 · 라벨링 · 분석", "Design · implementation · labeling · analysis"),
        "team": T("개인 실험", "Solo experiment"),
        "sections": [
            {
                "id": "problem",
                "title": T("문제 정의", "Problem"),
                "blocks": [
                    {"p": T(
                        "CodeAgent(EMNLP 2024)의 CA·VA·FA 리뷰 과제를 참고해 단순한 리뷰 하네스를 만들었습니다. 모든 커밋에 세 리뷰어를 strong 모델로 호출하면 비용과 시간이 커서, 하네스 앞단에 의사결정 단계를 두어 커밋별로 필요한 검사만 고르도록 했습니다.",
                        "Based on the CA/VA/FA review tasks from CodeAgent (EMNLP 2024), I built a simple review harness. Calling all three reviewers on a strong model for every commit is costly and slow, so a decision step in front of the harness picks only the checks each commit needs.",
                    )},
                ],
            },
            {
                "id": "architecture",
                "title": T("아키텍처 · 처리 흐름", "Architecture & flow"),
                "blocks": [
                    {"steps": [
                        T("커밋 (메시지 · diff · 문맥)", "Commit (message · diff · context)"),
                        T("라우터: VA·FA 필요 여부", "Router: VA/FA needed?"),
                        T("줄 수 규칙: small / strong", "Line rule: small / strong"),
                        T("리뷰어 호출 (CA 항상 + 선택된 VA·FA)", "Call reviewers (CA always + chosen VA/FA)"),
                        T("구조화 출력 → 채점", "Structured output → scoring"),
                    ]},
                    {"ul": T(
                        [
                            "<span class=\"highlight\">Laya decision model</span>이 로컬 CPU에서 보안·형식 검토 필요 여부를 판단 — 라우터 자체의 외부 API 비용은 없음.",
                            "보수적 규칙: \"불필요\" 판단의 confidence가 0.7 미만이면 검사를 실행.",
                            "모델 선택은 변경 줄 수 기준(5줄 이하 small, 6줄 이상 strong). Laya의 complexity 출력은 로그용으로만 사용.",
                            "라우터 칸만 바꿔 끼우는 구조로 all · rule · laya_v1 · laya_v2 · small_llm 5개 조건을 같은 인터페이스로 비교.",
                        ],
                        [
                            "The <span class=\"highlight\">Laya decision model</span> runs on local CPU to decide whether security/format checks are needed — the router adds no external API cost.",
                            "Conservative rule: if a \"not needed\" answer has confidence below 0.7, the check runs anyway.",
                            "Model tier by lines changed (≤5 small, ≥6 strong). Laya's complexity output is logged only.",
                            "A swappable router slot compares five conditions — all, rule, laya_v1, laya_v2, small_llm — through one interface.",
                        ],
                    )},
                    {"figures": [fig("laya_setup.jpg", T("실험 구성", "Experiment setup"))]},
                ],
            },
            {
                "id": "method",
                "title": T("실험 설계", "Experiment design"),
                "blocks": [
                    {"ul": T(
                        [
                            "Zenodo 공개 데이터의 커밋 40개를 직접 라벨링 (CA 불일치 12개 — 자연 7, 합성 5 / 보안 검토 대상 9개).",
                            "40개 × 검사 3종 × 모델 2종 = <span class=\"highlight\">리뷰 답안 240개를 한 번만 생성해 캐시</span>하고, 라우터 판단도 캐시 — LLM 출력의 비결정성과 무관하게 재실행 시 같은 결과(결과 파일 md5 동일 확인).",
                            "지표: API 비용, 리뷰어 호출 수, 토큰, CA 정답률·F1, 보안 검토 배정 누락, 순차/병렬 가정 처리 시간.",
                        ],
                        [
                            "Hand-labeled 40 commits from a public Zenodo dataset (12 CA mismatches — 7 natural, 5 synthetic / 9 security-relevant).",
                            "40 × 3 checks × 2 models = <span class=\"highlight\">240 review outputs generated once and cached</span>, along with router decisions — reruns give identical results regardless of LLM non-determinism (output md5 matched).",
                            "Metrics: API cost, reviewer calls, tokens, CA accuracy/F1, missed security assignments, and sequential/parallel time estimates.",
                        ],
                    )},
                ],
            },
            {
                "id": "results",
                "title": T("결과", "Results"),
                "blocks": [
                    {"stats": [
                        {"value": "40.4–42.1%", "label": T("API 비용 절감 (Laya v1·v2)", "API cost reduction (Laya v1/v2)")},
                        {"value": "14.2–18.3%", "label": T("리뷰어 호출 감소", "Fewer reviewer calls")},
                        {"value": "0 / 9", "label": T("보안 검토 배정 누락", "Missed security assignments")},
                    ]},
                    {"table": {
                        "head": [T("조건", "Condition"), T("리뷰어 호출", "Calls"), T("API 비용", "API cost"), T("절감률", "Saving"), T("CA 정답률", "CA accuracy"), T("VA 누락", "VA missed"), T("순차 시간", "Seq. time")],
                        "rows": [
                            ["all", "120", "$0.5534", "–", "97.5%", "0/9", "6.42s"],
                            ["rule", "68", "$0.1817", "67.2%", "92.5%", "2/9", "3.32s"],
                            ["<strong>laya_v1</strong>", "98", "$0.3203", "42.1%", "92.5%", "0/9", "9.48s"],
                            ["<strong>laya_v2</strong>", "103", "$0.3296", "40.4%", "92.5%", "0/9", "9.95s"],
                            ["small_llm", "67", "$0.1744", "68.5%", "92.5%", "0/9", "4.85s"],
                        ],
                        "caption": T("TAU 0.7, 커밋 40개. 비용은 저장된 토큰에 단가를 적용한 조건별 합계", "TAU 0.7, 40 commits. Cost is per-condition, from stored tokens and unit prices"),
                    }},
                    {"figures": [
                        fig("laya_cost.jpg", T("조건별 API 비용 (축 0부터)", "API cost by condition (axis from 0)")),
                        fig("laya_table.jpg", T("전체 결과표", "Full results table")),
                    ]},
                ],
            },
            {
                "id": "limits",
                "title": T("해석 · 한계", "Interpretation & limits"),
                "blocks": [
                    {"ul": T(
                        [
                            "성과의 범위는 API 비용 절감. CA 정답률은 97.5% → 92.5%로 낮아졌고, CPU 순차 처리 시간 추정치는 6.42초 → 9.48초로 늘어남.",
                            "이 실험에서 최저 비용은 작은 LLM 라우터(small_llm)였음. Laya 구성은 기준선 대비 절감을 보였지만 가장 싼 방법은 아님.",
                            "모델 선택 규칙과 호출 생략을 함께 적용한 결과로, Laya만의 기여를 분리 측정하지 않음. 데이터 40개, 반복 실험 없음.",
                            "\"VA 누락 0/9\"는 보안 리뷰어를 모두 배정했다는 뜻이지 실제 취약점 검출률을 뜻하지 않음.",
                            "각 리뷰어는 단발 LLM 호출. 다단계 에이전트 루프나 그래프 기반 워크플로는 구현 범위에 포함하지 않음.",
                        ],
                        [
                            "The result is about API cost. CA accuracy fell from 97.5% to 92.5%, and the CPU sequential time estimate rose from 6.42 s to 9.48 s.",
                            "The cheapest condition here was the small LLM router (small_llm). Laya saved cost versus the baseline but was not the cheapest option.",
                            "Model-tier rules and skipped calls were applied together, so Laya's own contribution was not isolated. 40 samples, no repeated runs.",
                            "\"VA missed 0/9\" means every security-relevant commit got a security reviewer, not a vulnerability detection rate.",
                            "Each reviewer is a single LLM call. Multi-step agent loops and graph-based workflows were out of scope.",
                        ],
                    )},
                ],
            },
        ],
        "links": [
            {"label": T("참고 논문 코드 (CodeAgent)", "Reference code (CodeAgent)"), "url": "https://github.com/Daniel4SE/codeagent"},
            {"label": T("데이터 (Zenodo)", "Dataset (Zenodo)"), "url": "https://zenodo.org/records/10607925"},
        ],
    },
    # ------------------------------------------------------------------ 데이터 · 연구
    {
        "slug": "talkiebridge",
        "category": "research",
        "tags": ["team", "personal"],
        "title": "TalkieBridge",
        "summary": T(
            "1931년 이전 텍스트로만 학습된 Talkie-1930에게 현대 용어를 기능 설명으로 바꿔 물으면 응답이 나아지는지 검증한 팀 실험.",
            "A team experiment testing whether Talkie-1930, trained only on pre-1931 text, answers better when modern terms are rewritten as functional descriptions.",
        ),
        "intro": T(
            "시대적 지식 격차가 LLM 응답 품질에 미치는 영향을 다룬 기계학습개론 팀 프로젝트입니다. 모델을 재학습시키지 않고, 질문(입력)을 전처리하는 방식의 효과만 평가했습니다.",
            "An Intro to Machine Learning team project on how a time-bound knowledge gap affects LLM answers. The model was not retrained; only the effect of preprocessing the input question was evaluated.",
        ),
        "stack": ["Python", "OpenAI API", "Talkie-1930", "LLM-as-a-Judge", "McNemar · Binomial test"],
        "cover": "talkie_structure.jpg",
        "hero": "talkie_structure.jpg",
        "period": "2026.05",
        "role": T("기획 참여 · 테스트/평가 설계 · 결과 분석", "Planning · test & evaluation design · result analysis"),
        "team": T("팀 프로젝트 (기계학습개론)", "Team project (Intro to Machine Learning)"),
        "sections": [
            {
                "id": "question",
                "title": T("배경 · 문제 정의", "Background & question"),
                "blocks": [
                    {"p": T(
                        "Talkie에게 GPS의 쓸모를 물으면 GPS를 눈으로 보는 방향 계기처럼 설명합니다. 질문은 이해했지만 단어를 모르는 상황입니다. 현대 용어가 들어간 질문에 엉뚱하게 답할 때, 추론을 못 한 것인지 단어를 몰라서인지 구분되지 않는다는 점이 출발점이었습니다.",
                        "Asked what GPS is useful for, Talkie describes a direction instrument you look at — it understood the question but not the word. When a modern question gets an odd answer, you cannot tell whether reasoning failed or the word was unknown. That was the starting point.",
                    )},
                    {"note": T(
                        "<strong>가설</strong> — 현대 용어를 1930년에도 있던 말로 기능을 풀어 쓰면(GPS → \"멀리 있는 송신기의 신호 시간을 비교해 위치를 추정하는 방법\"), 모델이 이미 아는 지식을 조합해 더 나은 답을 낼 것이다.",
                        "<strong>Hypothesis</strong> — if a modern term is spelled out by its function in words that existed in 1930 (GPS → \"compares timed signals from distant transmitters to estimate position\"), the model can combine what it already knows and answer better.",
                    )},
                ],
            },
            {
                "id": "method",
                "title": T("실험 설계", "Experiment design"),
                "blocks": [
                    {"steps": [
                        T("용어 탐지 (사전 141개 표현)", "Term detection (141-entry dictionary)"),
                        T("기능 설명 연결 (100개)", "Map to description (100 entries)"),
                        T("문장 재작성 (\"this method\")", "Rewrite (\"this method\")"),
                        T("검증 (용어 잔존 · 정답 누출 · 길이)", "Validate (leftover terms · answer leak · length)"),
                        T("Talkie-1930 질의", "Query Talkie-1930"),
                    ]},
                    {"p": T(
                        "원문(raw)과만 비교하면 좋아졌는지는 알아도 왜 좋아졌는지는 모릅니다. 그래서 다른 원인을 하나씩 떼어 낸 대조 조건을 같은 100문항(6개 분야)에 함께 적용했습니다.",
                        "Comparing only with the raw question shows whether it got better, not why. So control conditions that remove one cause at a time were run on the same 100 questions (6 domains).",
                    )},
                    {"table": {
                        "head": [T("조건", "Condition"), T("내용", "What it isolates")],
                        "rows": [
                            ["raw", T("원래 질문", "Original question")],
                            ["rule_only", T("사전 설명만 붙이는 단순 치환", "Plain dictionary substitution")],
                            ["length_controlled", T("용어만 지우고 의미 없는 단어로 길이를 맞춤 (평균 13 → 34단어 효과 분리)", "Term removed and padded to the same length (isolates the 13 → 34 word increase)")],
                            ["proposed", T("전체 파이프라인", "Full pipeline")],
                            ["proposed_no_validator", T("검증기를 뺀 파이프라인", "Pipeline without the validator")],
                        ],
                    }},
                    {"figures": [
                        fig("projects/talkie-demo-rewrite.webp", T("데모: 용어 탐지와 재작성", "Demo: term detection and rewrite")),
                        fig("talkie_example.jpg", T("질문 변환 예시 · GPS 문항", "Rewrite example · GPS question")),
                    ]},
                ],
            },
            {
                "id": "metrics",
                "title": T("데이터 · 평가 지표", "Data & metrics"),
                "blocks": [
                    {"ul": T(
                        [
                            "<strong>객관식</strong> — 100문항 × 5조건 = 500건, 정확도와 무효 응답률, McNemar 검정.",
                            "<strong>서술형</strong> — \"1~2문장으로 원리를 설명하라\". 같은 문항의 두 답을 <span class=\"highlight\">LLM-as-a-Judge</span>가 비교 (조건명 숨김, A/B 순서 섞음), 400쌍, 이항 검정.",
                            "Talkie 웹 API가 부하 시 응답을 거부해 초기 자동화에서 정확도가 0으로 나옴 — 수집 실패와 무효 응답을 분리 기록하고 재시도·응답 캐시·프롬프트 해시 검증을 추가해 500건이 모두 올바른 프롬프트의 응답인지 확인.",
                        ],
                        [
                            "<strong>Multiple choice</strong> — 100 questions × 5 conditions = 500 calls; accuracy, invalid-answer rate, McNemar test.",
                            "<strong>Open-ended</strong> — \"explain the principle in 1–2 sentences\". An <span class=\"highlight\">LLM judge</span> compares two answers to the same question (condition names hidden, A/B order shuffled); 400 pairs, binomial test.",
                            "The Talkie web API rejected requests under load and early automated runs showed 0% accuracy — collection failures were logged apart from invalid answers, and retries, a response cache, and prompt hashes confirmed all 500 responses matched the right prompt.",
                        ],
                    )},
                ],
            },
            {
                "id": "results",
                "title": T("결과", "Results"),
                "blocks": [
                    {"stats": [
                        {"value": "79–18–3", "label": T("서술형: Proposed vs Raw (승–패–무)", "Open-ended: proposed vs raw (W–L–T)")},
                        {"value": "21% → 19%", "label": T("객관식 정확도: Raw → Proposed", "MCQ accuracy: raw → proposed")},
                        {"value": "45–51–4", "label": T("서술형: Proposed vs 단순 치환", "Open-ended: proposed vs rule_only")},
                    ]},
                    {"ul": T(
                        [
                            "객관식은 개선되지 않음 — raw 21%, proposed 19% (p=0.77). 다섯 조건 모두 19~24%로 무작위 기준 25% 아래, 보기 대신 문장으로 답해 채점이 안 된 경우도 12~22%.",
                            "서술형에서는 proposed가 raw에 79승 18패 3무, 길이 대조군에 88승 11패 1무 (이항 검정 p&lt;0.001) — 길이만으로는 좋아지지 않음.",
                            "단순 사전 치환과는 45승 51패 4무 (p=0.61)로 차이 없음 — 효과는 오토인코더나 검증기보다 <span class=\"highlight\">용어를 기능으로 풀어 쓰는 것 자체</span>에서 나온 것으로 판단.",
                        ],
                        [
                            "No multiple-choice gain — raw 21%, proposed 19% (p=0.77). All five conditions scored 19–24%, below the 25% random baseline, and 12–22% of answers were sentences that could not be graded.",
                            "Open-ended: proposed beat raw 79–18 (3 ties) and the length control 88–11 (1 tie) (binomial p&lt;0.001) — length alone did not help.",
                            "Against plain dictionary substitution: 45–51 (4 ties, p=0.61), no difference — the gain comes from <span class=\"highlight\">spelling out the function itself</span>, not from the autoencoder or validator.",
                        ],
                    )},
                    {"figures": [
                        fig("talkie_judge.jpg", T("서술형 블라인드 비교 결과", "Blind open-ended comparison")),
                        fig("talkie_mcq.jpg", T("객관식 4지선다 정확도", "Multiple-choice accuracy")),
                    ]},
                ],
            },
            {
                "id": "limits",
                "title": T("해석 · 한계", "Interpretation & limits"),
                "blocks": [
                    {"ul": T(
                        [
                            "모델 자체를 바꾸지 않고 입력 표현만 재구성해 지식 격차의 일부를 완화할 가능성을 관찰한 실험.",
                            "순수 추론 능력이 입증되었거나 지식 부족과 추론 부족이 완전히 분리되었다고 볼 수 없음.",
                            "서술형 결과는 정답률이 아니라 평가 모델의 상대 판단 — 사람 평가와의 교차 확인이 남은 과제.",
                            "단순 규칙 기반 변환보다 낫다는 근거는 확인되지 않음.",
                        ],
                        [
                            "The experiment observed that restructuring only the input, without changing the model, may ease part of the knowledge gap.",
                            "It does not prove pure reasoning ability or fully separate missing knowledge from missing reasoning.",
                            "Open-ended results are relative judgments by an evaluator model, not accuracy — cross-checking with human ratings remains.",
                            "No evidence that it beats a simple rule-based substitution.",
                        ],
                    )},
                ],
            },
            {
                "id": "role",
                "title": T("담당 역할", "My role"),
                "blocks": [
                    {"p": T(
                        "팀 프로젝트에서 주제 기획에 참여했고, 대조 조건 구성과 객관식·서술형 평가 방식 등 <span class=\"highlight\">테스트·평가 설계</span>와 결과 분석을 중심으로 맡았습니다.",
                        "In this team project I took part in planning, and focused on <span class=\"highlight\">test and evaluation design</span> — control conditions, multiple-choice and open-ended evaluation — and on result analysis.",
                    )},
                ],
            },
        ],
        "links": [],
    },
    {
        "slug": "semen-quality-environment",
        "category": "research",
        "tags": ["research"],
        "title": T("정자질 및 환경인자 관계 분석", "Semen Quality vs. Environmental Factors"),
        "summary": T(
            "2018~2024 정액검사 데이터와 대기오염·기상 요인의 연관성을 회귀·트리 모델과 반복측정 모델로 비교 분석한 RAISE Lab 연구.",
            "RAISE Lab research relating 2018–2024 semen test data to air pollution and weather, comparing regression, tree, and repeated-measures models.",
        ),
        "intro": T(
            "연세대학교 미래캠퍼스 RAISE Lab 학부연구생으로 참여한 연구입니다. 정액검사 결과(정액량, 정자 수, 운동성 등)와 대기환경 인자 간의 연관성을 분석했습니다.",
            "Research done as an undergraduate researcher at RAISE Lab, Yonsei University Mirae Campus, relating semen test results (volume, count, motility, etc.) to environmental factors.",
        ),
        "stack": ["Python", "R", "XGBoost", "GPBoost", "Optuna", "SHAP", "GEE · GLMM · LMM"],
        "cover": "raise_xgboost_dashboard.png",
        "hero": "raise_xgboost_dashboard.png",
        "period": T("2025.09 ~ 진행 중", "2025.09 – ongoing"),
        "role": T("데이터셋 구축 · 모델링 · 분석", "Dataset building · modeling · analysis"),
        "team": T("RAISE Lab 학부연구생", "RAISE Lab undergraduate researcher"),
        "sections": [
            {
                "id": "question",
                "title": T("배경 · 문제 정의", "Background & question"),
                "blocks": [
                    {"p": T(
                        "대기오염과 기상 요인이 남성 생식건강 지표와 관련이 있는지를 실제 검사 데이터로 확인하는 것이 목표입니다. 같은 환자가 여러 번 검사를 받은 반복측정 데이터라 관측치가 독립이 아니라는 점을 분석 설계의 핵심 조건으로 두었습니다.",
                        "The goal is to check with real test data whether air pollution and weather relate to male reproductive health markers. Many patients were tested more than once, so observations are not independent — a core constraint in the analysis design.",
                    )},
                ],
            },
            {
                "id": "data",
                "title": T("데이터 · 실험 설계", "Data & design"),
                "blocks": [
                    {"ul": T(
                        [
                            "2018~2024 정액검사 데이터와 대기오염·기상 요인을 결합해 데이터셋 구축 — 2,672건, 환자 1,287명.",
                            "타깃 6종: 정액량(vol), 정자 수(count), 농도(sm), 운동성(motility), 총 정자 수(tsc), 총 운동 정자 수(tmsc). 분포가 치우친 vol·count·tsc·tmsc는 log1p 변환.",
                            "특징: 환경인자 + 나이 + 계절 더미. COVID-19 기간 주효과와 환경인자×COVID 상호작용을 넣은 split 모델을 별도로 비교.",
                        ],
                        [
                            "Built a dataset joining 2018–2024 semen tests with air pollution and weather — 2,672 tests from 1,287 patients.",
                            "Six targets: volume, count, concentration (sm), motility, total sperm count (tsc), total motile count (tmsc). Skewed vol/count/tsc/tmsc were log1p-transformed.",
                            "Features: environmental factors + age + season dummies. A separate split model adds a COVID-19 period effect and environment × COVID interactions.",
                        ],
                    )},
                    {"figures": [fig("raise_env_corr.png", T("환경인자 간 상관관계", "Correlation among environmental factors"))]},
                ],
            },
            {
                "id": "method",
                "title": T("방법론", "Methods"),
                "blocks": [
                    {"ul": T(
                        [
                            "OLS, Ridge, Lasso, Decision Tree, Random Forest, XGBoost, GPBoost를 교차검증으로 비교하고 Optuna로 타깃별 하이퍼파라미터를 탐색.",
                            "SHAP으로 변수 중요도를 확인.",
                            "반복측정 모델링: GEE, GLMM, LMM과 GPBoost, BiMM의 예측 성능 비교. 환자 ID 랜덤효과, 나이, 계절, COVID-19를 교란변수로 보정 (R, Python).",
                            "GPBoost는 환자 ID를 그룹으로 하는 GroupKFold(3-fold)로 평가해, 같은 환자가 학습·검증에 동시에 들어가지 않도록 함.",
                        ],
                        [
                            "Compared OLS, Ridge, Lasso, Decision Tree, Random Forest, XGBoost, and GPBoost with cross-validation, tuning each target with Optuna.",
                            "Checked feature importance with SHAP.",
                            "Repeated-measures modeling: compared GEE, GLMM, LMM, GPBoost, and BiMM, adjusting for patient-ID random effects, age, season, and COVID-19 (R, Python).",
                            "GPBoost was evaluated with GroupKFold (3-fold) by patient ID so no patient appears in both training and validation.",
                        ],
                    )},
                ],
            },
            {
                "id": "results",
                "title": T("결과", "Results"),
                "blocks": [
                    {"table": {
                        "head": [T("모델", "Model"), T("교차검증", "CV"), T("평균 CV R²", "Mean CV R²"), T("최고 타깃 CV R²", "Best target CV R²")],
                        "rows": [
                            ["XGBoost", "5-fold KFold", "0.123", "0.141 ~ 0.148"],
                            [T("GPBoost (환자 ID 랜덤효과)", "GPBoost (patient-ID random effect)"), "GroupKFold by ID", "0.042 ~ 0.047", "0.063 ~ 0.074"],
                        ],
                        "caption": T("Optuna 최적 파라미터 기준, 특징 구성(combined/split)·표준화 여부별 범위", "With Optuna-best parameters; ranges across feature sets (combined/split) and scaling"),
                    }},
                    {"ul": T(
                        [
                            "환경인자·나이·계절로 설명되는 정액 지표의 변동은 작음 (CV R² 0.04~0.15).",
                            "환자 단위로 분할한 평가에서 R²가 더 낮게 나옴. 두 결과는 모델과 분할 방식이 함께 달라 직접 비교할 수는 없지만, 반복측정 구조를 무시한 평가는 성능을 높게 보이게 할 수 있다는 점을 확인하는 근거로 삼음.",
                        ],
                        [
                            "Environment, age, and season explain only a small share of variation in semen markers (CV R² 0.04–0.15).",
                            "Patient-wise evaluation gave lower R². Model and split both differ, so the numbers are not directly comparable, but it supports the point that ignoring repeated measures can make performance look better than it is.",
                        ],
                    )},
                    {"figures": [
                        fig("raise_xgboost_dashboard.png", T("XGBoost Optuna 대시보드", "XGBoost Optuna dashboard")),
                        fig("raise_gpboost_dashboard.png", T("GPBoost Optuna 대시보드 (환자 ID 랜덤효과)", "GPBoost Optuna dashboard (patient-ID random effect)")),
                    ]},
                ],
            },
            {
                "id": "limits",
                "title": T("해석 · 한계", "Interpretation & limits"),
                "blocks": [
                    {"ul": T(
                        [
                            "관측 데이터 기반의 연관성 분석으로, 환경인자가 정액 지표를 변화시킨다는 인과관계를 주장하지 않음.",
                            "지역 대기 측정값을 개인 노출로 사용해 실제 개인 노출과 차이가 있을 수 있음.",
                            "연구 진행 중으로, 반복측정 모델 결과와 해석은 계속 보완 중.",
                        ],
                        [
                            "An association analysis on observational data; it does not claim environmental factors cause changes in semen markers.",
                            "Regional air measurements stand in for personal exposure, which may differ.",
                            "The study is ongoing; repeated-measures results and interpretation are still being refined.",
                        ],
                    )},
                ],
            },
        ],
        "links": [],
    },
    {
        "slug": "gynecologic-disease-environment",
        "category": "research",
        "tags": ["research"],
        "title": T("부인과질환 및 환경인자 관계 분석", "Gynecologic Disease vs. Environmental Factors"),
        "summary": T(
            "HIRA·NHIS 의료 통계로 자궁내막증·자궁근종·다낭성난소증후군과 대기환경 인자의 연관성을 음이항 회귀로 분석.",
            "Used HIRA/NHIS statistics and negative binomial regression to study links between endometriosis, fibroids, PCOS, and air quality.",
        ),
        "intro": T(
            "부인과질환 3종(자궁내막증, 자궁근종, 다낭성난소증후군)의 시도별 환자 수와 환경인자의 관계를 분석했습니다. RAISE Lab 헬스케어 요청 과제로 진행했습니다.",
            "Analyzed regional patient counts for three gynecologic diseases (endometriosis, uterine fibroids, PCOS) against environmental factors, as a RAISE Lab healthcare request.",
        ),
        "stack": ["Python", "R", "Negative Binomial Regression", "Cluster-Robust SE", "HIRA · NHIS · KOSIS"],
        "cover": "raise_analysis_logic.png",
        "hero": "raise_analysis_logic.png",
        "period": "2026.04",
        "role": T("데이터 전처리 · 모델링 · 결과 해석", "Preprocessing · modeling · interpretation"),
        "team": T("RAISE Lab 학부연구생", "RAISE Lab undergraduate researcher"),
        "sections": [
            {
                "id": "data",
                "title": T("데이터", "Data"),
                "blocks": [
                    {"ul": T(
                        [
                            "질환: 자궁근종·다낭성난소증후군은 HIRA(보건의료빅데이터개방시스템) 국민관심질병통계, 자궁내막증은 NHIS(국민건강보험 빅데이터) 질병통계. 3종을 시도별로 병합.",
                            "인구: KOSIS 2020~2024 시도별 여성 인구 — 모델의 offset으로 사용.",
                            "환경인자 8종: 타깃 연도(2020~2024)마다 과거 4개년 누적평균을 계산해 사용.",
                        ],
                        [
                            "Diseases: fibroids and PCOS from HIRA public disease statistics, endometriosis from NHIS statistics, merged by province.",
                            "Population: KOSIS 2020–2024 female population by province, used as the model offset.",
                            "Eight environmental factors: for each target year (2020–2024), the mean of the previous four years.",
                        ],
                    )},
                    {"note": T(
                        "환경인자 간 상관 확인 결과 PM10–PM2.5는 매우 강한 양의 상관, NO2–O3는 강한 음의 상관(-0.76)이 있었습니다. 다중공선성을 피하려고 환경인자는 한 번에 하나씩 모델에 넣었습니다.",
                        "Checking correlations first: PM10–PM2.5 were very strongly positive and NO2–O3 strongly negative (-0.76). To avoid multicollinearity, each factor entered the model on its own.",
                    )},
                ],
            },
            {
                "id": "method",
                "title": T("모델", "Model"),
                "blocks": [
                    {"p": T(
                        "<code>ln(E(Y_it)) = β0 + β1·D_it(Med) + β2·D_it(High) + Σ γ_t·I(Year=t) + ln(Pop_it)</code>",
                        "<code>ln(E(Y_it)) = β0 + β1·D_it(Med) + β2·D_it(High) + Σ γ_t·I(Year=t) + ln(Pop_it)</code>",
                    )},
                    {"ul": T(
                        [
                            "<strong>음이항 회귀</strong> — 과대산포가 있는 환자 수(count) 데이터에 사용, 지역·연도별 여성 인구를 offset으로 넣어 발생률로 해석.",
                            "<strong>환경인자 범주화</strong> — 임계점 효과를 보기 위해 3분위(하위·중위·상위 33%)로 나누고 하위(Low)를 기준군으로 설정.",
                            "<strong>연도 고정효과</strong> — 연도를 명목형 변수로 넣어 연도별 전체 환자 수준 차이를 통제.",
                            "<strong>Cluster-robust SE</strong> — 같은 지역의 반복 관측은 독립이 아니므로 지역을 군집으로 표준오차를 다시 계산(Sandwich).",
                            "결과는 회귀계수에 exp를 취한 상대위험도(RR)로 해석.",
                        ],
                        [
                            "<strong>Negative binomial regression</strong> — for overdispersed patient counts, with female population as the offset so results read as rates.",
                            "<strong>Categorized exposure</strong> — tertiles (bottom, middle, top 33%) to look for threshold effects, with Low as the reference.",
                            "<strong>Year fixed effects</strong> — year as a nominal variable to absorb year-level differences.",
                            "<strong>Cluster-robust SE</strong> — repeated observations within a province are not independent, so standard errors are clustered by province (sandwich).",
                            "Coefficients are reported as rate ratios (RR = exp(β)).",
                        ],
                    )},
                    {"figures": [
                        fig("raise_nb_model.png", T("음이항 회귀 모델 정의", "Negative binomial model")),
                        fig("raise_nb_result.png", T("환경인자별 분석 결과표", "Results by environmental factor")),
                    ]},
                ],
            },
            {
                "id": "results",
                "title": T("결과", "Results"),
                "blocks": [
                    {"table": {
                        "head": [T("환경인자", "Factor"), T("자궁내막증", "Endometriosis"), T("자궁근종", "Fibroids"), T("다낭성난소증후군", "PCOS")],
                        "rows": [
                            ["NO2", "Med 1.489 · High 1.834", "Med 1.488 · High 1.509", "High 1.688"],
                            ["O3", "High 0.618", "High 0.748", "Med 0.689"],
                            [T("평균기온", "Temperature"), "High 1.388", "High 1.441", T("유의한 차이 없음", "No significant difference")],
                            [T("평균습도", "Humidity"), "Med 0.765 · High 0.658", "Med 0.785 · High 0.712", T("유의한 차이 없음", "No significant difference")],
                        ],
                        "caption": T("Low 대비 유의한 상대위험도(RR)만 표시", "Only significant rate ratios vs. Low are shown"),
                    }},
                    {"ul": T(
                        [
                            "NO2와 O3는 세 질환 모두에서 유의한 연관을 보였고, 기온·습도는 자궁근종·자궁내막증과 유의한 연관을 보임.",
                            "O3의 RR&lt;1은 O3가 질병을 줄인다는 의미로 읽기 어려움 — 도심의 NO2가 O3를 소모하는 대기화학적 역상관(-0.76)이 반영된 결과로 추정.",
                        ],
                        [
                            "NO2 and O3 showed significant associations for all three diseases; temperature and humidity did for fibroids and endometriosis.",
                            "O3's RR below 1 should not be read as O3 reducing disease — it likely reflects the atmospheric inverse relation in which urban NO2 consumes O3 (-0.76).",
                        ],
                    )},
                ],
            },
            {
                "id": "limits",
                "title": T("해석 · 한계", "Interpretation & limits"),
                "blocks": [
                    {"note": T(
                        "이 결과는 지역 단위 통계의 <strong>상관관계</strong>이며, 환경인자가 질환을 일으킨다는 인과관계를 뜻하지 않습니다.",
                        "These are <strong>associations</strong> in regional statistics; they do not show that environmental factors cause the diseases.",
                    )},
                    {"ul": T(
                        [
                            "<strong>생태학적 오류 가능성</strong> — 개인이 실제로 노출된 농도가 아니라 지역 연평균 누적값을 사용.",
                            "<strong>작은 표본</strong> — 5개년 × 16개 시도로 전체 관측 수가 제한적.",
                            "질환별 데이터 출처(HIRA, NHIS)가 달라 집계 기준 차이가 있을 수 있음.",
                        ],
                        [
                            "<strong>Ecological fallacy</strong> — uses regional cumulative averages, not each person's actual exposure.",
                            "<strong>Small sample</strong> — 5 years × 16 provinces limits the number of observations.",
                            "Disease data come from different sources (HIRA, NHIS), which may differ in counting rules.",
                        ],
                    )},
                ],
            },
        ],
        "links": [],
    },
]

PROJECTS_BY_SLUG = {p["slug"]: p for p in PROJECTS}

# 하위 프로젝트("parent" 지정)는 목록에서 상위 프로젝트 카드 안에 묶고, 상세 페이지 순서도 상위 바로 뒤에 둔다
CHILDREN = {}
for _p in PROJECTS:
    if _p.get("parent"):
        CHILDREN.setdefault(_p["parent"], []).append(_p)
TOP_PROJECTS = [p for p in PROJECTS if not p.get("parent")]
PROJECTS[:] = [q for p in TOP_PROJECTS for q in [p] + CHILDREN.get(p["slug"], [])]


def category_counts():
    counts = {c["key"]: 0 for c in CATEGORIES}
    counts["all"] = len(TOP_PROJECTS)
    for p in TOP_PROJECTS:
        counts[p["category"]] += 1
    return counts


def category_label(key):
    return next(c["label"] for c in CATEGORIES if c["key"] == key)
