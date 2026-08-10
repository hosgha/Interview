#!/usr/bin/env python3
"""Create four completed server-request forms from the supplied PDF template."""

from pathlib import Path

import arabic_reshaper
import pymupdf
from bidi.algorithm import get_display


TEMPLATE = Path(
    "/home/ubuntu/.cursor/projects/workspace/uploads/serverrequest_7090.pdf"
)
OUTPUT = Path(__file__).with_name("serverrequest_4_servers.pdf")
FONT = "/usr/share/fonts/truetype/noto/NotoNaskhArabic-Regular.ttf"
FONT_BOLD = "/usr/share/fonts/truetype/noto/NotoNaskhArabic-Bold.ttf"

SERVERS = (
    {
        "name": "DB1",
        "cpu": "12 Core",
        "ram": "64 GB",
        "disk": "1 / 300 GB",
        "reason": "استقرار کلاستر پایگاه داده با دسترس پذیری بالا",
        "software": "DB Cluster, Backup Tools",
        "role": "Database",
        "application": "Clustered Database",
    },
    {
        "name": "DB2",
        "cpu": "12 Core",
        "ram": "64 GB",
        "disk": "1 / 300 GB",
        "reason": "استقرار کلاستر پایگاه داده با دسترس پذیری بالا",
        "software": "DB Cluster, Backup Tools",
        "role": "Database",
        "application": "Clustered Database",
    },
    {
        "name": "DB3",
        "cpu": "12 Core",
        "ram": "64 GB",
        "disk": "1 / 300 GB",
        "reason": "استقرار کلاستر پایگاه داده با دسترس پذیری بالا",
        "software": "DB Cluster, Backup Tools",
        "role": "Database",
        "application": "Clustered Database",
    },
    {
        "name": "Monitoring",
        "cpu": "8 Core",
        "ram": "32 GB",
        "disk": "1 / 300 GB",
        "reason": "استقرار سامانه مانیتورینگ و هشداردهی بلادرنگ",
        "software": "Prometheus, Alertmanager, Grafana",
        "role": "Monitoring",
        "application": "Observability Stack",
    },
)


def rtl(text: str) -> str:
    """Shape Persian text for correct visual display in a PDF text run."""
    return get_display(arabic_reshaper.reshape(text))


def add_text(
    page: pymupdf.Page,
    rect: tuple[float, float, float, float],
    text: str,
    *,
    size: float = 9,
    align: int = pymupdf.TEXT_ALIGN_LEFT,
    bold: bool = False,
) -> None:
    result = page.insert_textbox(
        pymupdf.Rect(rect),
        text,
        fontname="NotoNaskhBold" if bold else "NotoNaskh",
        fontfile=FONT_BOLD if bold else FONT,
        fontsize=size,
        color=(0.05, 0.05, 0.05),
        align=align,
        lineheight=1,
        overlay=True,
    )
    if result < 0:
        raise RuntimeError(f"Text does not fit in {rect}: {text!r}")


def fill_form(page: pymupdf.Page, server: dict[str, str]) -> None:
    add_text(page, (320, 130, 470, 149), server["name"], size=10, bold=True)

    # Mark "initial installation".
    page.draw_line((236.5, 133), (244.5, 141), color=(0, 0, 0), width=1.2)
    page.draw_line((244.5, 133), (236.5, 141), color=(0, 0, 0), width=1.2)

    add_text(
        page,
        (45, 176, 448, 195),
        rtl(server["reason"]),
        size=8.5,
        align=pymupdf.TEXT_ALIGN_RIGHT,
    )
    add_text(
        page,
        (45, 199, 288, 218),
        server["software"],
        size=8,
        align=pymupdf.TEXT_ALIGN_RIGHT,
    )
    add_text(page, (48, 218, 207, 237), server["cpu"], size=9, bold=True)
    add_text(
        page,
        (260, 242, 395, 262),
        server["disk"],
        size=9,
        align=pymupdf.TEXT_ALIGN_RIGHT,
        bold=True,
    )
    add_text(
        page,
        (355, 264, 466, 284),
        server["ram"],
        size=9,
        align=pymupdf.TEXT_ALIGN_RIGHT,
        bold=True,
    )
    add_text(
        page,
        (385, 307, 466, 326),
        "Ubuntu 22.04 LTS",
        size=6.5,
        align=pymupdf.TEXT_ALIGN_CENTER,
    )
    add_text(
        page,
        (340, 353, 422, 372),
        server["role"],
        size=7.5,
        align=pymupdf.TEXT_ALIGN_CENTER,
    )
    add_text(
        page,
        (45, 350, 154, 370),
        server["application"],
        size=7,
        align=pymupdf.TEXT_ALIGN_CENTER,
    )


def main() -> None:
    if not TEMPLATE.exists():
        raise FileNotFoundError(f"Template not found: {TEMPLATE}")

    template = pymupdf.open(TEMPLATE)
    output = pymupdf.open()

    for server in SERVERS:
        page = output.new_page(
            width=template[0].rect.width,
            height=template[0].rect.height,
        )
        page.show_pdf_page(page.rect, template, 0)
        fill_form(page, server)

    output.set_metadata(
        {
            "title": "Server Resource Requests - DB1, DB2, DB3, Monitoring",
            "subject": "Completed server request forms",
            "creator": "PyMuPDF",
        }
    )
    output.save(OUTPUT, garbage=4, deflate=True)
    output.close()
    template.close()
    print(OUTPUT)


if __name__ == "__main__":
    main()
