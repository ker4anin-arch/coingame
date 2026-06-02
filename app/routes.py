from flask import Blueprint, render_template

bp = Blueprint('main', __name__, template_folder='../templates')

MOCK_SKILLS = [
    {"name": "Маркетинг", "income": 500, "level": 1, "cost": 5000, "category": "brand", "icon": "fa-bullhorn"},
    {"name": "SEO", "income": 300, "level": 2, "cost": 3000, "category": "brand", "icon": "fa-search"},
    {"name": "MVP", "income": 800, "level": 1, "cost": 8000, "category": "product", "icon": "fa-rocket"},
    {"name": "Аналитика", "income": 600, "level": 3, "cost": 6000, "category": "product", "icon": "fa-chart-line"},
    {"name": "Спорт", "income": 200, "level": 1, "cost": 2000, "category": "health", "icon": "fa-dumbbell"},
    {"name": "Медитация", "income": 150, "level": 2, "cost": 1500, "category": "health", "icon": "fa-spa"},
    {"name": "Курсы", "income": 400, "level": 1, "cost": 4000, "category": "development", "icon": "fa-graduation-cap"},
    {"name": "Менторство", "income": 700, "level": 2, "cost": 7000, "category": "development", "icon": "fa-chalkboard-teacher"},
    {"name": "Инвестиции", "income": 1200, "level": 1, "cost": 12000, "category": "wealth", "icon": "fa-coins"},
    {"name": "Стартап", "income": 2000, "level": 1, "cost": 20000, "category": "wealth", "icon": "fa-chart-bar"},
]

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/skills')
def skills():
    return render_template('skills.html', skills=MOCK_SKILLS)

@bp.route('/friends')
def friends():
    return render_template('friends.html')

@bp.route('/tasks')
def tasks():
    return render_template('tasks.html')

@bp.route('/airdrop')
def airdrop():
    return render_template('airdrop.html')
