"""Build the designed Senior Backend Engineer resume without changing canonical sources."""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "resumes" / "senior-backend"
DOCX_OUT = OUTPUT_DIR / "resume.docx"
PDF_OUT = OUTPUT_DIR / "resume.pdf"

NAVY = RGBColor(27, 55, 92)
CHARCOAL = RGBColor(35, 39, 45)
MUTED = RGBColor(82, 88, 96)


def set_cell_margins(cell, top=0, start=0, bottom=0, end=0):
    tc = cell._tc
    tc_pr = tc.get_or_add_tcPr()
    tc_mar = tc_pr.first_child_found_in("w:tcMar")
    if tc_mar is None:
        tc_mar = OxmlElement("w:tcMar")
        tc_pr.append(tc_mar)
    for side, value in (("top", top), ("start", start), ("bottom", bottom), ("end", end)):
        node = tc_mar.find(qn(f"w:{side}"))
        if node is None:
            node = OxmlElement(f"w:{side}")
            tc_mar.append(node)
        node.set(qn("w:w"), str(value))
        node.set(qn("w:type"), "dxa")


def shade_cell(cell, fill: str):
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:fill"), fill)
    tc_pr.append(shd)


def prevent_row_split(row):
    tr_pr = row._tr.get_or_add_trPr()
    cant_split = OxmlElement("w:cantSplit")
    tr_pr.append(cant_split)


def add_hyperlink(paragraph, text: str, url: str, *, color="1B375C"):
    part = paragraph.part
    relationship_id = part.relate_to(url, "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink", is_external=True)
    hyperlink = OxmlElement("w:hyperlink")
    hyperlink.set(qn("r:id"), relationship_id)
    run = OxmlElement("w:r")
    properties = OxmlElement("w:rPr")
    color_node = OxmlElement("w:color")
    color_node.set(qn("w:val"), color)
    properties.append(color_node)
    underline = OxmlElement("w:u")
    underline.set(qn("w:val"), "single")
    properties.append(underline)
    run.append(properties)
    text_node = OxmlElement("w:t")
    text_node.text = text
    run.append(text_node)
    hyperlink.append(run)
    paragraph._p.append(hyperlink)


def set_bottom_border(paragraph, color="1B375C"):
    p_pr = paragraph._p.get_or_add_pPr()
    borders = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), "8")
    bottom.set(qn("w:space"), "5")
    bottom.set(qn("w:color"), color)
    borders.append(bottom)
    p_pr.append(borders)


def set_keep(paragraph, *, with_next=False, together=False):
    p_pr = paragraph._p.get_or_add_pPr()
    if with_next:
        p_pr.append(OxmlElement("w:keepNext"))
    if together:
        p_pr.append(OxmlElement("w:keepLines"))


def add_run(paragraph, text, *, bold=False, size=None, color=None):
    run = paragraph.add_run(text)
    run.bold = bold
    if size:
        run.font.size = Pt(size)
    if color:
        run.font.color.rgb = color
    return run


def configure_document() -> Document:
    document = Document()
    section = document.sections[0]
    section.page_width = Inches(8.2677)
    section.page_height = Inches(11.6929)
    section.top_margin = Inches(0.55)
    section.bottom_margin = Inches(0.55)
    section.left_margin = Inches(0.62)
    section.right_margin = Inches(0.62)
    section.header_distance = Inches(0.25)
    section.footer_distance = Inches(0.25)

    styles = document.styles
    normal = styles["Normal"]
    normal.font.name = "Arial"
    normal._element.rPr.rFonts.set(qn("w:eastAsia"), "Arial")
    normal.font.size = Pt(10)
    normal.font.color.rgb = CHARCOAL
    normal.paragraph_format.space_after = Pt(0)
    normal.paragraph_format.line_spacing = 1.03

    for name, size, color in (("Resume Section", 11.3, NAVY), ("Resume Role", 10.3, CHARCOAL)):
        style = styles.add_style(name, WD_STYLE_TYPE.PARAGRAPH)
        style.font.name = "Arial"
        style._element.rPr.rFonts.set(qn("w:eastAsia"), "Arial")
        style.font.size = Pt(size)
        style.font.bold = True
        style.font.color.rgb = color

    return document


def section_heading(document: Document, text: str):
    paragraph = document.add_paragraph(style="Resume Section")
    paragraph.paragraph_format.space_before = Pt(7)
    paragraph.paragraph_format.space_after = Pt(3)
    paragraph.add_run(text.upper())
    set_bottom_border(paragraph)
    set_keep(paragraph, with_next=True)
    return paragraph


def bullet(document: Document, text: str):
    paragraph = document.add_paragraph(style="Normal")
    paragraph.style = document.styles["Normal"]
    paragraph.paragraph_format.left_indent = Inches(0.17)
    paragraph.paragraph_format.first_line_indent = Inches(-0.13)
    paragraph.paragraph_format.space_after = Pt(1.8)
    paragraph.paragraph_format.line_spacing = 1.02
    add_run(paragraph, "•  ", color=NAVY)
    add_run(paragraph, text)
    set_keep(paragraph, together=True)
    return paragraph


def add_experience(document: Document, company: str, location: str, role: str, dates: str, bullets: list[str]):
    heading = document.add_paragraph(style="Resume Role")
    heading.paragraph_format.space_before = Pt(4.5)
    heading.paragraph_format.space_after = Pt(0.4)
    add_run(heading, company, bold=True)
    add_run(heading, f"  |  {location}", color=MUTED)
    set_keep(heading, with_next=True)

    details = document.add_paragraph()
    details.paragraph_format.space_after = Pt(1.5)
    add_run(details, role, bold=True, size=9.7)
    add_run(details, f"  |  {dates}", size=9.7, color=MUTED)
    set_keep(details, with_next=True)

    for item in bullets:
        bullet(document, item)


def build_docx(output: Path):
    document = configure_document()

    name = document.add_paragraph()
    name.alignment = WD_ALIGN_PARAGRAPH.CENTER
    name.paragraph_format.space_after = Pt(1)
    add_run(name, "Sadman Sobhan", bold=True, size=22, color=NAVY)

    title = document.add_paragraph()
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    title.paragraph_format.space_after = Pt(2)
    add_run(title, "Senior Backend Engineer  |  Java  |  Spring Boot  |  PostgreSQL  |  Distributed Systems", bold=True, size=11.4, color=NAVY)

    contact = document.add_paragraph()
    contact.alignment = WD_ALIGN_PARAGRAPH.CENTER
    contact.paragraph_format.space_after = Pt(0)
    add_run(contact, "Dhaka, Bangladesh  |  +8801912070224  |  ", size=9.4, color=MUTED)
    add_hyperlink(contact, "imran110219@gmail.com", "mailto:imran110219@gmail.com")

    links = document.add_paragraph()
    links.alignment = WD_ALIGN_PARAGRAPH.CENTER
    links.paragraph_format.space_after = Pt(3)
    add_hyperlink(links, "linkedin.com/in/sadmansobhan", "https://www.linkedin.com/in/sadmansobhan")
    add_run(links, "  |  ", size=9.4, color=MUTED)
    add_hyperlink(links, "sadmansobhan.com", "https://www.sadmansobhan.com")
    set_bottom_border(links)

    section_heading(document, "Professional Summary")
    summary = document.add_paragraph()
    summary.paragraph_format.space_after = Pt(1)
    summary.paragraph_format.line_spacing = 1.03
    add_run(summary, "Senior Software Engineer with 9+ years of experience delivering secure, scalable backend systems across government, education, healthcare, and enterprise domains. Specializes in Java, Spring Boot, PostgreSQL, distributed systems, API design, and performance optimization, with hands-on technical leadership from planning through production delivery.")

    section_heading(document, "Career Highlights")
    highlights = [
        "Backend team lead contributing to grooming, planning, implementation guidance, and code reviews within a 30-person development team",
        "Designed and delivered Java and Spring Boot services across a microservices architecture of nearly 20 running services",
        "Helped deliver an internal election-management platform supporting 50,000 users alongside a public-facing application",
        "Reduced exam-management system response time by 30% through Redis caching and backend performance improvements",
        "Supported production workflows used by 2,500+ administrators, 1,000 invigilators, and 1,000 examinees, including payments for nearly 30,000 students",
        "Contributed to the National Electronic Government Procurement System, supporting enterprise workflows, data integrity, and privacy",
    ]
    for item in highlights:
        bullet(document, item)

    section_heading(document, "Technical Skills")
    skills = [
        ("Languages", "Java, SQL, C#"),
        ("Backend", "Spring Boot, Hibernate, REST APIs, Microservices, Backend Architecture"),
        ("Data & Performance", "PostgreSQL, SQL Server, Redis, Database Modeling, Query Optimization"),
        ("Security & Platform", "Keycloak, Authentication, Authorization, Kubernetes, Data Integrity"),
        ("Delivery", "Agile Development, Requirements Analysis, Deployment, Code Review, Mentoring"),
    ]
    for label, value in skills:
        paragraph = document.add_paragraph()
        paragraph.paragraph_format.space_after = Pt(1)
        paragraph.paragraph_format.line_spacing = 1.0
        add_run(paragraph, f"{label}: ", bold=True, size=9.5, color=NAVY)
        add_run(paragraph, value, size=9.5)
        set_keep(paragraph, together=True)

    document.add_page_break()
    section_heading(document, "Professional Experience")
    add_experience(document, "Penta Global Ltd.", "Dhaka, Bangladesh", "Senior Software Engineer", "August 2023 – Present", [
        "Serve as backend team lead for an Election Management System, guiding grooming, planning, implementation, and code reviews within a 30-person development team",
        "Design and implement secure, scalable Java, Spring Boot, Hibernate, and REST API services across a microservices architecture of nearly 20 running services",
        "Help deliver an internal system supporting 50,000 users alongside a public-facing application that does not require authentication",
        "Support Kubernetes deployments to the organization’s self-managed data center and digitized election-result workflows formerly dependent on paperwork and physical result delivery",
    ])
    add_experience(document, "Dynamic Solution Innovators Ltd.", "Dhaka, Bangladesh", "Software Engineer", "January 2022 – July 2023", [
        "Led development of an exam management system using Java, Spring Boot, PostgreSQL, Flutter, and Crystal Reports; analyzed requirements and designed its database schema",
        "Reduced system response time by 30% through Redis caching and backend performance improvements",
        "Built a real-time administrator dashboard that contributed to a 40% increase in system usage and user satisfaction",
        "Deployed a production system used by 2,500+ administrators, 1,000 invigilators, and 1,000 examinees; supported registration and payment management for nearly 30,000 students",
    ])
    add_experience(document, "Dohatec New Media", "Dhaka, Bangladesh", "Java Software Engineer", "October 2016 – December 2021", [
        "Implemented features and resolved defects for the National Electronic Government Procurement System while preserving data privacy and integrity",
        "Contributed to large-file upload capabilities, relational data modeling, and enterprise workflow features; helped drive an 80% increase in user engagement over six months",
    ])
    add_experience(document, "Jaliks Soft IT Limited", "Khulna, Bangladesh", ".NET Developer", "February 2016 – June 2016", [
        "Implemented features and resolved defects for a large-scale education application using ASP.NET, C#, and SQL Server",
    ])

    section_heading(document, "Education")
    education = document.add_paragraph()
    education.paragraph_format.space_after = Pt(0)
    add_run(education, "Bachelor of Science in Computer Science and Engineering", bold=True, size=9.8)
    add_run(education, "  |  Khulna University  |  2011 – 2016", size=9.8, color=MUTED)
    set_keep(education, together=True)

    section_heading(document, "Publications")
    for publication in (
        "Temporal Relation Extraction using Apriori Algorithm",
        "An Effective Attendance Monitoring System with Fraud Prevention Technique for Educational Institutions",
    ):
        publication_paragraph = document.add_paragraph()
        publication_paragraph.paragraph_format.space_after = Pt(1)
        publication_paragraph.paragraph_format.line_spacing = 1.0
        add_run(publication_paragraph, publication, size=9.2)
        set_keep(publication_paragraph, together=True)

    document.save(output)


def export_pdf(docx: Path, pdf: Path):
    libreoffice = shutil.which("libreoffice") or shutil.which("soffice")
    if not libreoffice:
        raise RuntimeError("LibreOffice is required to export the PDF.")
    temporary = OUTPUT_DIR / ".pdf-export"
    temporary.mkdir(exist_ok=True)
    profile = Path("/tmp/career-resume-libreoffice-profile")
    profile.mkdir(exist_ok=True)
    subprocess.run([
        libreoffice,
        f"-env:UserInstallation={profile.as_uri()}",
        "--headless",
        "--convert-to",
        "pdf",
        "--outdir",
        str(temporary),
        str(docx),
    ], check=True)
    generated = temporary / f"{docx.stem}.pdf"
    generated.replace(pdf)
    temporary.rmdir()


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    build_docx(DOCX_OUT)
    export_pdf(DOCX_OUT, PDF_OUT)
    print(DOCX_OUT)
    print(PDF_OUT)


if __name__ == "__main__":
    main()
