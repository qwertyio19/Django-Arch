JAZZMIN_SETTINGS = {
    "show_sidebar": True,
    "navigation_expanded": True,

    "order_with_respect_to": [
        "base",
        "district",
        "administration",
        "kenesh",
        "news",
        "notifications",

        "base.footer",
        "base.cartmodel",
        "base.pagetitlesmodel",
        "base.headlinesmodel",
        "base.latestnews",
        "base.portal",

        "district.typetitle",
        "district.data",

        "administration.TypeAdministration",
        "administration.TitleAdministration",
        "administration.Management",
        "administration.Structure",
        "administration.Vacancy",
        "administration.AntiCorruptionMeasures",
        "administration.Report",

        "kenesh.CouncilSection",
        "kenesh.CouncilDocument",
        "kenesh.Deputies",
        "kenesh.Commission",

        "notifications.TypeNotification",
        "notifications.Notification",
    ],
}


JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": True,
    "brand_small_text": False,
    "brand_colour": "navbar-primary",
    "accent": "accent-primary",
    "navbar": "navbar-primary navbar-dark",
    "no_navbar_border": True,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": True,
    "sidebar_fixed": True,
    "sidebar": "sidebar-light-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": True,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": True,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": True,
    "theme": "default",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-outline-warning",
        "danger": "btn-outline-danger",
        "success": "btn-success"
    },
    "actions_sticky_top": False
}
