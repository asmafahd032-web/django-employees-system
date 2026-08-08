from django import template

# تسجيل الفلاتر في جانغو
register = template.Library()

@register.filter(name='salary_badge')
def salary_badge(value):
    """
    فلتر خاص يحول رقم الراتب إلى شارة أنيقة
    """
    try:
        val = float(value)
        if val >= 10000:
            return "🔥 راتب مميز (VIP)"
        else:
            return "✨ راتب أساسي"
    except (ValueError, TypeError):
        return value


@register.filter(name='employee_role')
def employee_role(title):
    """
    فلتر خاص يعطي إيموجي مناسب للمسمى الوظيفي
    """
    title_str = str(title).lower()
    if 'engineer' in title_str or 'developer' in title_str:
        return f"💻 {title}"
    elif 'manager' in title_str:
        return f"👔 {title}"
    else:
        return f"👤 {title}"