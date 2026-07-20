# Resume Design System

## Status

Approved standard for all role-specific and master resume DOCX/PDF exports. The reference implementation is `resumes/senior-backend/resume.docx` and `resumes/senior-backend/resume.pdf`.

## Layout

- Single-column, ATS-safe layout with all critical content in the document body.
- A4 page size; 0.55–0.70 inch margins.
- No sidebars, text boxes, columns, floating elements, complex tables, graphics, icons, or photos.
- Use intentional page breaks only between major sections. Keep headings with their following content and avoid split company headings.

## Typography and Color

- Preferred font: Aptos, then Calibri, then Arial.
- Name: 21–24 pt bold.
- Target title and section headings: 11.5–13 pt.
- Role/company lines: 10.5–11 pt.
- Body: 10–10.5 pt with compact 1.0–1.08 line spacing.
- Use dark body text and a dark-navy accent (`#1B375C`) for name, title, section headings, and thin divider lines.
- Use bold only for company names, role titles, skill labels, and supported metrics.

## Required Structure

1. Body-based contact header
2. Professional Summary
3. Career Highlights, where supported and useful
4. Technical Skills
5. Professional Experience
6. Selected Projects, only when it adds non-duplicative value
7. Education
8. Publications, only when space permits

## Output and Source Rules

- Markdown remains the editable content source; DOCX and PDF are generated artifacts.
- Use `scripts/build_designed_resume.py` for standard Markdown-driven exports.
- The Senior Backend resume uses its dedicated builder because its approved two-page composition includes curated highlights; it must retain this visual standard.
- Preserve role-specific output names as `resumes/<role>/resume.docx` and `resumes/<role>/resume.pdf`.
- Verify A4 size, page count, selectable PDF text, readable extraction order, no blank pages, and visual parity after each export.
