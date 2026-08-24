"""Configuraciones estáticas y diccionarios de datos de la aplicación."""

LANG_OPTIONS = {
    "🌐 Auto-detectar": None,
    "🇪🇸 Español":      "es",
    "🇺🇸 English":       "en",
    "🇫🇷 Français":      "fr",
    "🇧🇷 Português":     "pt",
    "🇩🇪 Deutsch":       "de",
    "🇮🇹 Italiano":      "it",
    "🇯🇵 日本語":         "ja",
    "🇨🇳 中文":           "zh",
}

MODEL_INFO = {
    "tiny":   ("~40 MB",  "Más rápido"),
    "base":   ("~150 MB", "Recomendado ✨"),
    "small":  ("~500 MB", "Mejor precisión"),
    "medium": ("~1.5 GB", "Alta precisión"),
}
