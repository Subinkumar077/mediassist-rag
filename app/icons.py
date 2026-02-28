"""
Inline SVG icon constants used throughout the UI.

All icons are Material Design style, rendered as inline SVG strings so they
work inside st.markdown(unsafe_allow_html=True) blocks without any external
dependencies.
"""

ICON_HEART = (
    '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" '
    'xmlns="http://www.w3.org/2000/svg">'
    '<path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 '
    "2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 "
    "14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 "
    '11.54L12 21.35z" fill="#0e7490"/></svg>'
)

ICON_STETHOSCOPE = (
    '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" '
    'xmlns="http://www.w3.org/2000/svg">'
    '<path d="M19 8c0-3.31-2.69-6-6-6h-2C7.69 2 5 4.69 5 8v5c0 '
    "2.76 2.24 5 5 5h1v2c0 1.1.9 2 2 2s2-.9 2-2v-2h1c2.76 0 "
    '5-2.24 5-5V8zm-2 5c0 1.66-1.34 3-3 3h-4c-1.66 0-3-1.34-3-3V8'
    'c0-2.21 1.79-4 4-4h2c2.21 0 4 1.79 4 4v5z" fill="#0e7490"/>'
    '<circle cx="12" cy="10" r="2" fill="#0e7490"/></svg>'
)

ICON_DRUG = (
    '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" '
    'xmlns="http://www.w3.org/2000/svg">'
    '<path d="M4.22 11.29l5.07-5.07c1.95-1.95 5.12-1.95 7.07 '
    "0s1.95 5.12 0 7.07l-5.07 5.07c-1.95 1.95-5.12 1.95-7.07 "
    "0s-1.95-5.12 0-7.07zm1.41 1.42c-1.17 1.17-1.17 3.07 0 "
    "4.24s3.07 1.17 4.24 0L12 14.83 7.76 10.6l-2.12 2.12zm8.49"
    "-5.07c-1.17-1.17-3.07-1.17-4.24 0L7.76 9.76l4.24 4.24 "
    '2.12-2.12c1.17-1.17 1.17-3.07 0-4.24z" fill="#475569"/></svg>'
)

ICON_STEPS = (
    '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" '
    'xmlns="http://www.w3.org/2000/svg">'
    '<path d="M3 13h2v-2H3v2zm0 4h2v-2H3v2zm0-8h2V7H3v2zm4 '
    '4h14v-2H7v2zm0 4h14v-2H7v2zM7 7v2h14V7H7z" fill="#475569"/>'
    "</svg>"
)

ICON_FLAG = (
    '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" '
    'xmlns="http://www.w3.org/2000/svg">'
    '<path d="M14.4 6L14 4H5v17h2v-7h5.6l.4 2h7V6h-5.6z" '
    'fill="#dc2626"/></svg>'
)

ICON_CHECK = (
    '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" '
    'xmlns="http://www.w3.org/2000/svg">'
    '<path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 '
    "10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59"
    '-7.59L19 8l-9 9z" fill="#16a34a"/></svg>'
)

ICON_SOURCE = (
    '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" '
    'xmlns="http://www.w3.org/2000/svg">'
    '<path d="M18 2H6c-1.1 0-2 .9-2 2v16c0 1.1.9 2 2 2h12c1.1 '
    "0 2-.9 2-2V4c0-1.1-.9-2-2-2zM6 4h5v8l-2.5-1.5L6 12V4z\" "
    'fill="#64748b"/></svg>'
)

ICON_SHIELD = (
    '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" '
    'xmlns="http://www.w3.org/2000/svg">'
    '<path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 '
    "9-6.45 9-12V5l-9-4zm0 10.99h7c-.53 4.12-3.28 7.79-7 "
    '8.94V12H5V6.3l7-3.11v8.8z" fill="#94a3b8"/></svg>'
)

ICON_PULSE = (
    '<svg width="60" height="24" viewBox="0 0 120 40" fill="none" '
    'xmlns="http://www.w3.org/2000/svg">'
    '<polyline points="0,20 20,20 30,5 40,35 50,15 60,25 70,20 120,20" '
    'stroke="#0e7490" stroke-width="2" fill="none" stroke-linecap="round" '
    'stroke-linejoin="round" opacity="0.4"/></svg>'
)
