"""Iconos SVG y banderas."""
import re
ICONS = {
 "wood": '<path d="M22 6C14 20 14 36 24 54M42 6c8 14 8 30-2 48M26 38l6 8 6-8"/><path d="M3 28h12m-4-4 4 4-4 4M61 28H49m4-4-4 4 4 4"/>',
 "fascia": '<path d="M10 54l14-14M40 24 54 10"/><circle cx="32" cy="32" r="7"/><circle cx="24" cy="40" r="5"/><circle cx="40" cy="24" r="5"/><path d="M6 36l-2 6M12 32l-3 5"/>',
 "cav": '<path d="M21 6C13 20 15 34 24 40l8 9 8-9c9-6 11-20 3-34"/><path d="M26 18v8M38 18v8" stroke-dasharray="3 3"/><path d="M3 24h11m-4-4 4 4-4 4M61 24H50m4-4-4 4 4 4"/>',
 "rf": '<circle cx="32" cy="32" r="4"/><path d="M24 24a12 12 0 0 0 0 16M40 24a12 12 0 0 1 0 16M17 17a22 22 0 0 0 0 30M47 17a22 22 0 0 1 0 30M10 10a32 32 0 0 0 0 44M54 10a32 32 0 0 1 0 44"/>',
 "lymph": '<path d="M22 6C12 20 10 28 10 36a12 12 0 0 0 24 0c0-8-2-16-12-30z"/><path d="M42 10c6 7 8 13 8 18"/><path d="M38 38c10 0 16 6 16 16-10 0-16-6-16-16z"/><path d="M16 38a6 6 0 0 0 5 6"/>',
 "lotus": '<path d="M32 54C18 52 8 42 6 28c10 0 20 6 26 16 6-10 16-16 26-16-2 14-12 24-26 26z"/><path d="M32 54C24 44 22 28 32 8c10 20 8 36 0 46z"/>',
 "massage": '<circle cx="14" cy="26" r="7"/><path d="M5 44c10-6 18-4 26-2s18 2 27-6M5 54c10-6 20-4 28-2s16 2 25-4M24 34c10 0 16 4 26 2"/><path d="M44 10c4 0 8 2 8 8-6 0-8-4-8-8z"/>',
 "lipo": '<rect x="10" y="44" width="44" height="9" rx="3"/><path d="M32 8v26M18 14l7 20M46 14l-7 20M7 26l17 10M57 26 40 36"/>',
 "cap": '<path d="M32 12 4 26l28 14 28-14z"/><path d="M16 33v12c0 4 8 8 16 8s16-4 16-8V33M60 26v16"/>',
 "chat": '<path d="M24 8C13 8 6 15 6 24c0 4 2 8 5 11l-2 9 9-4c2 .6 4 1 6 1 11 0 18-7 18-16S35 8 24 8z"/><path d="M44 22c9 1 14 7 14 14 0 4-2 7-5 10l1 8-8-4c-2 .5-3 .7-5 .7-6 0-11-3-13-8"/>',
 "gem": '<path d="M16 8h32l12 14-28 34L4 22z"/><path d="M4 22h56M24 22 32 56l8-34M24 22l-8-14M40 22l8-14M24 22l8-14 8 14"/>',
}

def svg(name, extra=""):
    return f'<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" {extra}>{ICONS[name]}</svg>'

ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 12h16m-6-6 6 6-6 6"/></svg>'
WA_ICON = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M17.47 14.38c-.3-.15-1.76-.87-2.03-.97-.27-.1-.47-.15-.67.15-.2.3-.77.97-.94 1.16-.17.2-.35.22-.65.07-.3-.15-1.26-.46-2.39-1.48-.88-.79-1.48-1.76-1.65-2.06-.17-.3-.02-.46.13-.6.13-.14.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.03-.52-.07-.15-.67-1.61-.92-2.21-.24-.58-.49-.5-.67-.51h-.57c-.2 0-.52.07-.79.37-.27.3-1.04 1.02-1.04 2.48s1.07 2.88 1.21 3.07c.15.2 2.1 3.2 5.08 4.49.71.3 1.26.49 1.69.63.71.23 1.36.2 1.87.12.57-.08 1.76-.72 2-1.41.25-.7.25-1.29.17-1.41-.07-.12-.27-.2-.57-.35m-5.42 7.4h-.01a9.87 9.87 0 0 1-5.03-1.38l-.36-.21-3.74.98 1-3.65-.24-.37a9.86 9.86 0 0 1-1.51-5.26c0-5.45 4.44-9.88 9.89-9.88 2.64 0 5.12 1.03 6.99 2.9a9.82 9.82 0 0 1 2.89 6.99c0 5.45-4.44 9.89-9.88 9.89m8.41-18.3A11.8 11.8 0 0 0 12.05 0C5.5 0 .16 5.34.16 11.89c0 2.1.55 4.14 1.59 5.95L.06 24l6.3-1.65a11.9 11.9 0 0 0 5.69 1.45h.01c6.55 0 11.89-5.34 11.89-11.89 0-3.18-1.24-6.17-3.48-8.41z"/></svg>'
FLAG_ES = '<svg viewBox="0 0 60 60" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><rect width="60" height="60" fill="#c60b1e"/><rect y="15" width="60" height="30" fill="#ffc400"/></svg>'
FLAG_EN = '<svg viewBox="0 0 60 60" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><rect width="60" height="60" fill="#012169"/><path d="M0 0 60 60M60 0 0 60" stroke="#fff" stroke-width="11"/><path d="M0 0 60 60M60 0 0 60" stroke="#c8102e" stroke-width="4"/><path d="M30 0v60M0 30h60" stroke="#fff" stroke-width="18"/><path d="M30 0v60M0 30h60" stroke="#c8102e" stroke-width="10"/></svg>'


CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>'
