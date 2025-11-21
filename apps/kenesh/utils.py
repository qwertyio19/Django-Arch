# app/council/utils.py
import os
import mammoth
import pdfplumber
from django.utils.html import escape


def docx_to_html(file_path: str) -> str:
    with open(file_path, "rb") as docx_file:
        result = mammoth.convert_to_html(docx_file)
        html = result.value or ""
        return html


def pdf_to_html(file_path: str) -> str:
    paragraphs = []
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text() or ""
            if text.strip():
                escaped = escape(text).replace("\n", "<br/>")
                paragraphs.append(f"<p>{escaped}</p>")
    return "\n".join(paragraphs)


def file_to_html(file_field) -> str:
    """
    Файлдын кеңейтүүсүнө жараша HTML кылып чыгарат.
    """
    if not file_field:
        return ""

    path = file_field.path
    ext = os.path.splitext(path)[1].lower()

    try:
        if ext == ".docx":
            return docx_to_html(path)
        elif ext == ".pdf":
            return pdf_to_html(path)
        else:
            # запасной вариант: жөнөкөй текст файл
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                return f"<pre>{escape(f.read())}</pre>"
    except Exception:
        # Конвертация бузулса – сайтың кулап калбасын
        return ""
