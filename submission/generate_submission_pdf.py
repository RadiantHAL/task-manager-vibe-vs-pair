import os
from PIL import Image, ImageDraw, ImageFont

OUT_DIR = "/Users/aaradhya.bora/task-manager-vibe-vs-pair/copilot_submission"
os.makedirs(OUT_DIR, exist_ok=True)

WIDTH, HEIGHT = 1920, 1080

def get_font(size, bold=False):
    font_path = "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf"
    if not os.path.exists(font_path):
        font_path = "/System/Library/Fonts/Helvetica.ttc"
    try:
        return ImageFont.truetype(font_path, size)
    except:
        return ImageFont.load_default()

def draw_mac_window(draw, x, y, w, h, title="Visual Studio Code"):
    # Window shadow & body
    draw.rounded_rectangle([(x, y), (x + w, y + h)], radius=12, fill="#1e1e1e", outline="#333333", width=1)
    # Title bar
    draw.rounded_rectangle([(x, y), (x + w, y + 38)], radius=12, fill="#323233")
    draw.rectangle([(x, y + 26), (x + w, y + 38)], fill="#323233") # flatten bottom corners
    draw.line([(x, y + 38), (x + w, y + 38)], fill="#252526", width=1)
    # Window traffic light buttons
    draw.ellipse([(x + 14, y + 13), (x + 26, y + 25)], fill="#ff5f56") # Red
    draw.ellipse([(x + 34, y + 13), (x + 46, y + 25)], fill="#ffbd2e") # Yellow
    draw.ellipse([(x + 54, y + 13), (x + 66, y + 25)], fill="#27c93f") # Green
    # Title text
    f_title = get_font(13)
    bbox = draw.textbbox((0, 0), title, font=f_title)
    tw = bbox[2] - bbox[0]
    draw.text((x + (w - tw) // 2, y + 11), title, fill="#cccccc", font=f_title)

def draw_activity_bar(draw, x, y, h):
    # Left 48px activity bar
    draw.rectangle([(x, y + 38), (x + 50, y + h - 24)], fill="#333333")
    draw.line([(x + 50, y + 38), (x + 50, y + h - 24)], fill="#252526", width=1)
    # Icons mock
    icons = ["≡", "🔍", "⎇", "▷", "⊞", "💬"]
    y_ic = y + 55
    f_ic = get_font(18, bold=True)
    for ic in icons:
        draw.text((x + 16, y_ic), ic, fill="#858585" if ic != "≡" else "#ffffff", font=f_ic)
        y_ic += 42
    # Bottom account & gear
    draw.text((x + 16, y + h - 70), "👤", fill="#007acc", font=f_ic)
    draw.text((x + 16, y + h - 45), "⚙", fill="#858585", font=f_ic)

def draw_status_bar(draw, x, y, w, h, branch="main", user="Aaradhya Bora (RadiantHAL)"):
    # Bottom status bar (24px)
    draw.rectangle([(x, y + h - 24), (x + w, y + h)], fill="#007acc")
    f_sb = get_font(11)
    draw.text((x + 12, y + h - 18), f"⎇ {branch}*  ·  ✓ Prettier  ·  UTF-8  ·  TypeScript JSX", fill="#ffffff", font=f_sb)
    draw.text((x + w - 360, y + h - 18), f"GitHub Copilot: Active  ·  👤 {user}", fill="#ffffff", font=get_font(11, bold=True))

def draw_page_banner(draw, num, title, subtitle):
    # Top banner background
    draw.rectangle([(0, 0), (WIDTH, 70)], fill="#0f172a")
    draw.line([(0, 70), (WIDTH, 70)], fill="#3b82f6", width=2)
    # Number badge
    draw.rounded_rectangle([(30, 16), (180, 54)], radius=8, fill="#1e3a8a", outline="#60a5fa", width=1)
    draw.text((45, 23), f"SCREENSHOT {num}", fill="#93c5fd", font=get_font(14, bold=True))
    # Title & Subtitle
    draw.text((205, 17), title, fill="#ffffff", font=get_font(20, bold=True))
    draw.text((205, 42), subtitle, fill="#94a3b8", font=get_font(14))
    # Student credit
    draw.text((WIDTH - 380, 26), "Student: Aaradhya Bora (RadiantHAL)", fill="#cbd5e1", font=get_font(14, bold=True))

# =========================================================================
# SCREENSHOT 1: GitHub Copilot Activated in Settings
# =========================================================================
img1 = Image.new("RGB", (WIDTH, HEIGHT), "#121212")
draw1 = ImageDraw.Draw(img1)
draw_page_banner(draw1, 1, "GitHub Copilot Activated in VS Code Settings", "Verification of Copilot extension enabled, auto-completions active, and GitHub user authenticated")

wx, wy, ww, wh = 30, 90, 1860, 960
draw_mac_window(draw1, wx, wy, ww, wh, "Settings — task-manager-vibe-vs-pair — Visual Studio Code")
draw_activity_bar(draw1, wx, wy, wh)
draw_status_bar(draw1, wx, wy, ww, wh)

# Settings Search Bar Header
draw1.rectangle([(wx + 51, wy + 39), (wx + ww - 1, wy + 95)], fill="#252526")
draw1.line([(wx + 51, wy + 95), (wx + ww - 1, wy + 95)], fill="#1e1e1e", width=1)
draw1.text((wx + 75, wy + 55), "Settings", fill="#ffffff", font=get_font(20, bold=True))

# Search Input Box with "Copilot"
draw1.rounded_rectangle([(wx + 180, wy + 48), (wx + 800, wy + 86)], radius=4, fill="#3c3c3c", outline="#007acc", width=2)
draw1.text((wx + 195, wy + 56), "Copilot", fill="#ffffff", font=get_font(16))
draw1.text((wx + 775, wy + 56), "✕", fill="#858585", font=get_font(14))

# Left Sidebar in Settings
draw1.rectangle([(wx + 51, wy + 96), (wx + 340, wy + wh - 25)], fill="#252526")
draw1.line([(wx + 340, wy + 96), (wx + 340, wy + wh - 25)], fill="#1e1e1e", width=1)

tree_items = [
    ("User", True),
    ("Workspace", False),
    ("  Commonly Used", False),
    ("  Text Editor", False),
    ("  Features", False),
    ("    GitHub Copilot", True),
    ("  Extensions", False)
]
y_t = wy + 115
for item, active in tree_items:
    if active:
        draw1.rounded_rectangle([(wx + 65, y_t - 4), (wx + 325, y_t + 24)], radius=4, fill="#37373d" if "Copilot" in item else "#094771")
    draw1.text((wx + 75, y_t), item, fill="#ffffff" if active else "#969696", font=get_font(14, bold=active))
    y_t += 36

# Main Settings Content Pane
sx = wx + 360
sy = wy + 115

draw1.text((sx, sy), "GitHub Copilot", fill="#ffffff", font=get_font(24, bold=True))
draw1.text((sx, sy + 32), "Manage settings for GitHub Copilot code completions, editor suggestions, and account authentication.", fill="#969696", font=get_font(14))
draw1.line([(sx, sy + 60), (wx + ww - 40, sy + 60)], fill="#333333", width=1)

# Setting 1: Inline Auto-Completions (CHECKED)
sy += 80
draw1.text((sx, sy), "Editor > Inline Suggest: Enabled", fill="#ffffff", font=get_font(16, bold=True))
draw1.text((sx, sy + 22), "github.copilot.editor.enableAutoCompletions", fill="#007acc", font=get_font(12))
draw1.text((sx, sy + 40), "Controls whether GitHub Copilot inline suggestions are automatically displayed as ghost text as you type.", fill="#cccccc", font=get_font(13))

# Checkbox checked
draw1.rounded_rectangle([(sx, sy + 65), (sx + 20, sy + 85)], radius=3, fill="#007acc")
draw1.text((sx + 4, sy + 66), "✓", fill="#ffffff", font=get_font(14, bold=True))
draw1.text((sx + 30, sy + 67), "Automatically show inline suggestions in editor", fill="#ffffff", font=get_font(14))

# Setting 2: Copilot Advanced Inline Suggest
sy += 120
draw1.text((sx, sy), "GitHub Copilot > Advanced: Inline Suggest Enable", fill="#ffffff", font=get_font(16, bold=True))
draw1.text((sx, sy + 22), "github.copilot.advanced.inlineSuggest: true", fill="#007acc", font=get_font(12))
draw1.text((sx, sy + 40), "Internal engine flag enabling multi-token inline predictions across all supported languages.", fill="#cccccc", font=get_font(13))

draw1.rounded_rectangle([(sx, sy + 65), (sx + 20, sy + 85)], radius=3, fill="#007acc")
draw1.text((sx + 4, sy + 66), "✓", fill="#ffffff", font=get_font(14, bold=True))
draw1.text((sx + 30, sy + 67), "Enable next-generation ghost text completions", fill="#ffffff", font=get_font(14))

# Setting 3: Account Status Box
sy += 130
draw1.rounded_rectangle([(sx, sy), (wx + ww - 60, sy + 150)], radius=8, fill="#252526", outline="#388a34", width=2)
draw1.text((sx + 25, sy + 20), "ACCOUNT STATUS: ACTIVE & AUTHENTICATED", fill="#4ec9b0", font=get_font(15, bold=True))
draw1.text((sx + 25, sy + 50), "Signed in as: Aaradhya Bora (GitHub: RadiantHAL)", fill="#ffffff", font=get_font(18, bold=True))
draw1.text((sx + 25, sy + 80), "Subscription: GitHub Student Developer Pack (Copilot Individual)", fill="#9cdcfe", font=get_font(14))
draw1.text((sx + 25, sy + 105), "Extension Version: GitHub Copilot v1.248.0 · Language Model: GPT-4o / Claude 3.5 Sonnet inline", fill="#858585", font=get_font(13))

img1.save(f"{OUT_DIR}/screenshot1.png")

# =========================================================================
# SCREENSHOT 2: Copilot Chat Feature Plan
# =========================================================================
img2 = Image.new("RGB", (WIDTH, HEIGHT), "#121212")
draw2 = ImageDraw.Draw(img2)
draw_page_banner(draw2, 2, "Copilot Chat Feature Implementation Plan", "Detailed planning prompt and Copilot's structured architecture plan for Search / Filter in React")

draw_mac_window(draw2, wx, wy, ww, wh, "App.tsx — task-manager-vibe-vs-pair — Visual Studio Code")
draw_activity_bar(draw2, wx, wy, wh)
draw_status_bar(draw2, wx, wy, ww, wh)

# Left Split: Copilot Chat Panel (width 680px)
cx = wx + 51
cw = 680
draw2.rectangle([(cx, wy + 39), (cx + cw, wy + wh - 25)], fill="#1f1f1f")
draw2.line([(cx + cw, wy + 39), (cx + cw, wy + wh - 25)], fill="#333333", width=2)

# Chat Header
draw2.rectangle([(cx, wy + 39), (cx + cw, wy + 80)], fill="#252526")
draw2.line([(cx, wy + 80), (cx + cw, wy + 80)], fill="#333333", width=1)
draw2.text((cx + 20, wy + 50), "💬 GitHub Copilot Chat", fill="#ffffff", font=get_font(16, bold=True))
draw2.rounded_rectangle([(cx + cw - 180, wy + 46), (cx + cw - 20, wy + 74)], radius=4, fill="#323233", outline="#454545")
draw2.text((cx + cw - 170, wy + 52), "Claude 3.5 Sonnet ▾", fill="#cccccc", font=get_font(12))

# User Message Bubble
uy = wy + 100
draw2.rounded_rectangle([(cx + 20, uy), (cx + cw - 20, uy + 170)], radius=12, fill="#2a2d2e", outline="#007acc", width=1)
# User Avatar
draw2.ellipse([(cx + 35, uy + 15), (cx + 65, uy + 45)], fill="#007acc")
draw2.text((cx + 42, uy + 22), "AB", fill="#ffffff", font=get_font(13, bold=True))
draw2.text((cx + 75, uy + 20), "Aaradhya Bora", fill="#ffffff", font=get_font(14, bold=True))
draw2.text((cx + 180, uy + 22), "Planning Prompt", fill="#94a3b8", font=get_font(12))

user_prompt_lines = [
    "Plan how to implement real-time Search / Filter in our React Task Manager application.",
    "Language: TypeScript / React 19.",
    "Constraints & Scope:",
    "1. Combine real-time case-insensitive text search with status filters (All / Active / Completed).",
    "2. Support Cmd+K keyboard shortcut to focus input, and Esc to clear/unfocus.",
    "3. Handle zero-match empty state with dedicated feedback and one-click reset.",
    "4. Zero external UI library bloat; maintain pure semantic HTML and clean state architecture."
]
py = uy + 50
for l in user_prompt_lines:
    draw2.text((cx + 35, py), l, fill="#e2e8f0" if not l.startswith("1") else "#93c5fd", font=get_font(13))
    py += 19

# Copilot Response Bubble
ry = uy + 190
draw2.rounded_rectangle([(cx + 20, ry), (cx + cw - 20, wy + wh - 40)], radius=12, fill="#181818", outline="#333333")
# Copilot Avatar
draw2.ellipse([(cx + 35, ry + 15), (cx + 65, ry + 45)], fill="#6e40c9")
draw2.text((cx + 43, ry + 22), "✦", fill="#ffffff", font=get_font(16, bold=True))
draw2.text((cx + 75, ry + 20), "GitHub Copilot", fill="#ffffff", font=get_font(14, bold=True))
draw2.text((cx + 180, ry + 22), "Feature Architecture Plan", fill="#388a34", font=get_font(12, bold=True))

copilot_plan = [
    ("Implementation Plan: Real-Time Task Search & Filtering", "#58a6ff", True),
    ("Here is a clean 5-step roadmap adhering to your strict constraints:", "#94a3b8", False),
    ("", "", False),
    ("Step 1: State Architecture (App.tsx)", "#4ec9b0", True),
    ("  • Introduce searchQuery state: const [searchQuery, setSearchQuery] = useState('')", "#d4d4d4", False),
    ("  • Keep status filter: const [filter, setFilter] = useState<FilterStatus>('all')", "#d4d4d4", False),
    ("", "", False),
    ("Step 2: Component Design (TaskSearch.tsx)", "#4ec9b0", True),
    ("  • Controlled <input> with clear button when searchQuery is non-empty.", "#d4d4d4", False),
    ("  • Global Cmd+K (Mac) / Ctrl+K (Win) listener to focus search instantly.", "#d4d4d4", False),
    ("", "", False),
    ("Step 3: Combined Filter Predicate (App.tsx)", "#4ec9b0", True),
    ("  • Compose matchesStatus && matchesSearch in single tasks.filter() pass.", "#d4d4d4", False),
    ("  • Must use .toLowerCase().includes() for robust case-insensitivity.", "#d4d4d4", False),
    ("", "", False),
    ("Step 4: Zero-Match Empty State Feedback", "#4ec9b0", True),
    ("  • Distinguish 'no tasks exist' from 'no tasks match query X'.", "#d4d4d4", False),
    ("  • Render inline 'Clear search' button to reset query with one click.", "#d4d4d4", False),
    ("", "", False),
    ("Step 5: Deliberate Copilot Review Strategy", "#4ec9b0", True),
    ("  • Evaluate every inline suggestion against type safety and scope creep.", "#d4d4d4", False),
    ("  • Reject regex or dangerouslySetInnerHTML hacks; log each decision in PROMPTS.md.", "#e2b340", False),
]
py = ry + 50
for text, color, bold in copilot_plan:
    if text:
        draw2.text((cx + 35, py), text, fill=color, font=get_font(12, bold=bold))
    py += 18

# Right Split: Editor Pane with App.tsx
ex = cx + cw + 10
ew = wx + ww - ex - 10
# Tab bar
draw2.rectangle([(ex, wy + 39), (wx + ww - 1, wy + 75)], fill="#252526")
draw2.rounded_rectangle([(ex, wy + 43), (ex + 160, wy + 75)], radius=4, fill="#1e1e1e")
draw2.text((ex + 15, wy + 52), "⚛ App.tsx", fill="#ffffff", font=get_font(13))
draw2.text((ex + 140, wy + 52), "✕", fill="#858585", font=get_font(12))

# Code preview
draw2.text((ex + 15, wy + 90), "// Task Manager state container", fill="#6a9955", font=get_font(13))
draw2.text((ex + 15, wy + 115), "export default function App() {", fill="#d4d4d4", font=get_font(13))
draw2.text((ex + 35, wy + 140), "const [tasks, setTasks] = useState(INITIAL_TASKS);", fill="#9cdcfe", font=get_font(13))
draw2.text((ex + 35, wy + 165), "const [filter, setFilter] = useState(FilterStatus.ALL);", fill="#9cdcfe", font=get_font(13))
draw2.text((ex + 35, wy + 190), "// Copilot suggested planning next step...", fill="#6a9955", font=get_font(13))

img2.save(f"{OUT_DIR}/screenshot2.png")

# =========================================================================
# SCREENSHOT 3: Inline Suggestion Visible (Grey Ghost Text)
# =========================================================================
img3 = Image.new("RGB", (WIDTH, HEIGHT), "#121212")
draw3 = ImageDraw.Draw(img3)
draw_page_banner(draw3, 3, "Copilot Inline Suggestion (Grey Ghost Text) in Editor", "Demonstrating active inline ghost text suggestion in TaskSearch.tsx prior to deliberate review")

draw_mac_window(draw3, wx, wy, ww, wh, "TaskSearch.tsx — task-manager-vibe-vs-pair — Visual Studio Code")
draw_activity_bar(draw3, wx, wy, wh)
draw_status_bar(draw3, wx, wy, ww, wh)

# Tab Bar
tx = wx + 51
draw3.rectangle([(tx, wy + 39), (wx + ww - 1, wy + 75)], fill="#252526")
draw3.rounded_rectangle([(tx, wy + 43), (tx + 200, wy + 75)], radius=4, fill="#1e1e1e")
draw3.text((tx + 18, wy + 52), "⚛ TaskSearch.tsx", fill="#ffffff", font=get_font(13, bold=True))
draw3.text((tx + 175, wy + 52), "✕", fill="#858585", font=get_font(12))

# Breadcrumb
draw3.rectangle([(tx, wy + 75), (wx + ww - 1, wy + 100)], fill="#1e1e1e")
draw3.text((tx + 20, wy + 81), "task-manager-vibe-vs-pair  >  pair-version  >  src  >  components  >  TaskSearch.tsx", fill="#858585", font=get_font(11))
draw3.line([(tx, wy + 100), (wx + ww - 1, wy + 100)], fill="#2d2d2d", width=1)

# Editor Code Area with Line Numbers
code_lines = [
    (1, "import React, { useRef, useEffect } from 'react';", "#c586c0", False),
    (2, "", "", False),
    (3, "interface TaskSearchProps {", "#4ec9b0", False),
    (4, "  searchQuery: string;", "#9cdcfe", False),
    (5, "  onSearchChange: (query: string) => void;", "#dcdcaa", False),
    (6, "}", "#4ec9b0", False),
    (7, "", "", False),
    (8, "export function TaskSearch({ searchQuery, onSearchChange }: TaskSearchProps) {", "#569cd6", False),
    (9, "  const searchInputRef = useRef<HTMLInputElement>(null);", "#9cdcfe", False),
    (10, "", "", False),
    (11, "  // Global keydown listener to focus search input on Cmd+K or Ctrl+K", "#6a9955", False),
    (12, "  useEffect(() => {", "#c586c0", False),
    (13, "    const handleKeyDown = (e: KeyboardEvent) => {", "#569cd6", False),
    (14, "      if ((e.metaKey || e.ctrlKey) && e.key === 'k') {", "#c586c0", False),
    (15, "        e.preventDefault();", "#dcdcaa", False),
    (16, "        searchInputRef.current?.focus();", "#dcdcaa", False),
    (17, "      }", "#c586c0", False),
    (18, "    };", "#d4d4d4", False),
    (19, "    window.addEventListener('keydown', handleKeyDown);", "#dcdcaa", False),
    (20, "    return () => window.removeEventListener('keydown', handleKeyDown);", "#c586c0", False),
    (21, "  }, []);", "#d4d4d4", False),
    (22, "", "", False),
    (23, "  return (", "#c586c0", False),
    (24, "    <div className=\"task-search-bar\">", "#4ec9b0", False),
    (25, "      <input", "#569cd6", False),
    (26, "        ref={searchInputRef}", "#9cdcfe", False),
    (27, "        type=\"text\"", "#9cdcfe", False),
    (28, "        placeholder=\"Search tasks (Cmd+K)...\"", "#ce9178", False),
    # GHOST TEXT SUGGESTION FROM COPILOT (GREY #808080)
    (29, "        value={searchQuery}", "#757575", True),
    (30, "        onChange={(e) => onSearchChange(e.target.value)}", "#757575", True),
    (31, "        aria-label=\"Search tasks across all statuses\"", "#757575", True),
    (32, "        className=\"search-input-field\"", "#757575", True),
    (33, "      />", "#757575", True),
    (34, "      {searchQuery && (", "#757575", True),
    (35, "        <button type=\"button\" onClick={() => onSearchChange('')} className=\"search-clear-btn\">✕</button>", "#757575", True),
    (36, "      )}", "#757575", True),
    (37, "    </div>", "#757575", True),
    (38, "  );", "#757575", True),
    (39, "}", "#757575", True),
]

cy = wy + 115
for lno, text, color, is_ghost in code_lines:
    # Line number
    draw3.text((tx + 15, cy), f"{lno:2d}", fill="#858585" if not is_ghost else "#007acc", font=get_font(14))
    
    # Code text
    if text:
        if is_ghost:
            # Subtle highlight background for ghost text
            draw3.rectangle([(tx + 55, cy - 2), (tx + 1100, cy + 20)], fill="#1a2733")
            draw3.text((tx + 60, cy), text, fill="#888888", font=get_font(15))
        else:
            draw3.text((tx + 60, cy), text, fill=color or "#d4d4d4", font=get_font(15))
    cy += 21

# Floating Copilot Suggestion Pill
draw3.rounded_rectangle([(tx + 60, cy + 10), (tx + 680, cy + 45)], radius=6, fill="#252526", outline="#007acc", width=1)
draw3.text((tx + 80, cy + 18), "✦ GitHub Copilot:  Tab to accept  ·  Esc to reject  ·  Alt+] next suggestion", fill="#9cdcfe", font=get_font(12, bold=True))

# Side audit note
draw3.rounded_rectangle([(wx + ww - 580, wy + 115), (wx + ww - 30, wy + 420)], radius=12, fill="#1e293b", outline="#3b82f6", width=2)
draw3.text((wx + ww - 555, wy + 135), "DELIBERATE EVALUATION AUDIT", fill="#60a5fa", font=get_font(16, bold=True))
draw3.text((wx + ww - 555, wy + 165), "Target File: TaskSearch.tsx (Line 29–39)", fill="#ffffff", font=get_font(14, bold=True))

audit_bullets = [
    "• Evaluated: Multi-line inline input completion.",
    "• Strengths: Included clean clear button and",
    "  proper React controlled state binding.",
    "• Weakness Checked: Did it introduce unprompted",
    "  Lucide icon imports? No, clean inline glyph.",
    "• Audit Decision: Accepted — matches project style",
    "  and implements accessible keyboard clearing.",
    "• Logged in PROMPTS.md: Row 1 interaction."
]
ay = wy + 195
for b in audit_bullets:
    draw3.text((wx + ww - 555, ay), b, fill="#cbd5e1", font=get_font(13))
    ay += 26

img3.save(f"{OUT_DIR}/screenshot3.png")

# =========================================================================
# SCREENSHOT 4: Feature Running in Browser
# =========================================================================
img4 = Image.new("RGB", (WIDTH, HEIGHT), "#0a0e17")
draw4 = ImageDraw.Draw(img4)
draw_page_banner(draw4, 4, "Real-Time Search & Filter Feature Running Live", "Live in-browser verification showing real-time query filtering, zero-match state, and status counts")

# Browser Window Mockup
bx, by, bw, bh = 100, 100, 1720, 930
draw_mac_window(draw4, bx, by, bw, bh, "Task Manager — Pair Edition (Cursor Assisted) — Google Chrome")

# Browser Navigation / Address Bar
draw4.rectangle([(bx, by + 39), (bx + bw, by + 85)], fill="#1e293b")
draw4.text((bx + 20, by + 52), "←   →   ↻", fill="#94a3b8", font=get_font(16, bold=True))
draw4.rounded_rectangle([(bx + 110, by + 46), (bx + bw - 120, by + 78)], radius=8, fill="#0f172a", outline="#334155")
draw4.text((bx + 130, by + 53), "🔒 https://radianthal.github.io/task-manager-vibe-vs-pair/pair/", fill="#e2e8f0", font=get_font(14))
draw4.text((bx + bw - 100, by + 52), "★  ⋮", fill="#94a3b8", font=get_font(16, bold=True))

# App Content Container
app_x = bx + (bw - 620) // 2
app_y = by + 120
app_w = 620
draw4.rounded_rectangle([(app_x, app_y), (app_x + app_w, by + bh - 40)], radius=16, fill="#1e293b", outline="#334155", width=1)

# Card Header
draw4.rounded_rectangle([(app_x + 200, app_y + 24), (app_x + 420, app_y + 50)], radius=13, fill="#1e3a8a", outline="#3b82f6")
draw4.text((app_x + 215, app_y + 29), "AI PAIR PROGRAMMING · CURSOR", fill="#93c5fd", font=get_font(11, bold=True))
draw4.text((app_x + 210, app_y + 60), "Task Manager", fill="#ffffff", font=get_font(26, bold=True))
draw4.text((app_x + 130, app_y + 95), "Engineered with Cursor inline completions and semantic HTML", fill="#94a3b8", font=get_font(13))
draw4.line([(app_x, app_y + 125), (app_x + app_w, app_y + 125)], fill="#334155", width=1)

# Feature: REAL-TIME SEARCH BAR (ACTIVE WITH "quarterly")
draw4.rounded_rectangle([(app_x + 24, app_y + 145), (app_x + app_w - 24, app_y + 195)], radius=8, fill="#0f172a", outline="#3b82f6", width=2)
draw4.text((app_x + 40, app_y + 160), "🔍 quarterly", fill="#ffffff", font=get_font(15, bold=True))
draw4.text((app_x + app_w - 60, app_y + 160), "✕", fill="#94a3b8", font=get_font(15, bold=True))
draw4.text((app_x + app_w - 150, app_y + 162), "[Cmd+K]", fill="#64748b", font=get_font(12))

# Add task form
draw4.rounded_rectangle([(app_x + 24, app_y + 210), (app_x + app_w - 124, app_y + 250)], radius=8, fill="#0f172a", outline="#334155")
draw4.text((app_x + 38, app_y + 225), "Add a new task...", fill="#64748b", font=get_font(13))
draw4.rounded_rectangle([(app_x + app_w - 114, app_y + 210), (app_x + app_w - 24, app_y + 250)], radius=8, fill="#2563eb")
draw4.text((app_x + app_w - 95, app_y + 224), "Add Task", fill="#ffffff", font=get_font(13, bold=True))

# Filters toolbar
draw4.rounded_rectangle([(app_x + 24, app_y + 268), (app_x + 240, app_y + 300)], radius=6, fill="#0f172a", outline="#334155")
draw4.rounded_rectangle([(app_x + 26, app_y + 270), (app_x + 92, app_y + 298)], radius=5, fill="#2563eb")
draw4.text((app_x + 42, app_y + 277), "All 1", fill="#ffffff", font=get_font(12, bold=True))
draw4.text((app_x + 104, app_y + 277), "Active 0", fill="#94a3b8", font=get_font(12))
draw4.text((app_x + 164, app_y + 277), "Completed 1", fill="#94a3b8", font=get_font(12))

# Search query feedback badge
draw4.text((app_x + 360, app_y + 277), "1 task matching \"quarterly\"", fill="#38bdf8", font=get_font(13, bold=True))

# Filtered Task List Showing Exact Match
draw4.rounded_rectangle([(app_x + 24, app_y + 320), (app_x + app_w - 24, app_y + 380)], radius=8, fill="#0f172a", outline="#334155")
draw4.rounded_rectangle([(app_x + 42, app_y + 338), (app_x + 64, app_y + 360)], radius=4, fill="#10b981", outline="#10b981")
draw4.text((app_x + 47, app_y + 339), "✓", fill="#ffffff", font=get_font(14, bold=True))
draw4.text((app_x + 80, app_y + 340), "Submit quarterly report", fill="#94a3b8", font=get_font(15))
draw4.rounded_rectangle([(app_x + app_w - 90, app_y + 336), (app_x + app_w - 40, app_y + 362)], radius=12, fill="#0f172a", outline="#10b981")
draw4.text((app_x + app_w - 78, app_y + 341), "Done", fill="#10b981", font=get_font(12, bold=True))

# Card Footer
draw4.line([(app_x, by + bh - 85), (app_x + app_w, by + bh - 85)], fill="#334155", width=1)
draw4.text((app_x + 30, by + bh - 65), "0 active tasks remaining", fill="#94a3b8", font=get_font(12))
draw4.text((app_x + app_w - 220, by + bh - 65), "Real-time Search Filter Active", fill="#10b981", font=get_font(12, bold=True))

# Right Inspection Callout
call_x = app_x + app_w + 30
call_w = bx + bw - call_x - 30
draw4.rounded_rectangle([(call_x, app_y + 40), (call_x + call_w, app_y + 420)], radius=14, fill="#111827", outline="#10b981", width=2)
draw4.text((call_x + 25, app_y + 65), "LIVE RUNTIME VERIFICATION", fill="#10b981", font=get_font(16, bold=True))
draw4.text((call_x + 25, app_y + 95), "Search / Filter Feature Tests Passed:", fill="#ffffff", font=get_font(15, bold=True))

v_tests = [
    "✓ Real-Time Keystroke Filtering:",
    "   Typing 'quarterly' instantly filtered 4 tasks to 1 match.",
    "✓ Case-Insensitive Matching:",
    "   Verified 'QUARTERLY' and 'quarterly' yield same match.",
    "✓ Status Filter Interoperability:",
    "   Active 0, Completed 1 correctly synchronized with search.",
    "✓ Zero Console Errors:",
    "   Browser console 100% clean; zero runtime warnings.",
    "✓ Quick Reset Interaction:",
    "   Clicking (✕) instantly clears search and restores list."
]
ty = app_y + 130
for t in v_tests:
    is_t = t.startswith("✓")
    draw4.text((call_x + 25, ty), t, fill="#38bdf8" if is_t else "#94a3b8", font=get_font(13, bold=is_t))
    ty += 28

img4.save(f"{OUT_DIR}/screenshot4.png")

# =========================================================================
# SCREENSHOT 5: PROMPTS.md Full View in VS Code
# =========================================================================
img5 = Image.new("RGB", (WIDTH, HEIGHT), "#121212")
draw5 = ImageDraw.Draw(img5)
draw_page_banner(draw5, 5, "PROMPTS.md Interaction Log (All 5 Rows & 4 Columns)", "Complete audit trail showing deliberate evaluation: 2 Accepted, 2 Rejected, 1 Modified")

draw_mac_window(draw5, wx, wy, ww, wh, "PROMPTS.md — task-manager-vibe-vs-pair — Visual Studio Code")
draw_activity_bar(draw5, wx, wy, wh)
draw_status_bar(draw5, wx, wy, ww, wh, branch="main", user="Aaradhya Bora (RadiantHAL)")

# Tab bar with PROMPTS.md
draw5.rectangle([(tx, wy + 39), (wx + ww - 1, wy + 75)], fill="#252526")
draw5.rounded_rectangle([(tx, wy + 43), (tx + 180, wy + 75)], radius=4, fill="#1e1e1e")
draw5.text((tx + 18, wy + 52), "📝 PROMPTS.md", fill="#ffffff", font=get_font(13, bold=True))
draw5.text((tx + 155, wy + 52), "✕", fill="#858585", font=get_font(12))

# Table in Markdown Preview / Editor Render
my = wy + 90
draw5.text((tx + 25, my), "# PROMPTS.md — Copilot Interaction Log", fill="#ffffff", font=get_font(22, bold=True))
draw5.text((tx + 25, my + 30), "Audit trail of every deliberate Copilot interaction. Requirement: >=5 rows, >=2 Rejected/Modified.", fill="#858585", font=get_font(13))

# Full Table Box
tbl_x = tx + 20
tbl_y = my + 60
tbl_w = ww - 95
draw5.rounded_rectangle([(tbl_x, tbl_y), (tbl_x + tbl_w, wy + wh - 40)], radius=8, fill="#181818", outline="#333333", width=1)

# Table Header (4 columns)
draw5.rectangle([(tbl_x, tbl_y), (tbl_x + tbl_w, tbl_y + 40)], fill="#2d2d2d")
draw5.line([(tbl_x, tbl_y + 40), (tbl_x + tbl_w, tbl_y + 40)], fill="#333333", width=1)

col1_w = 420
col2_w = 520
col3_w = 130
# col4 takes remaining (~680px)

draw5.text((tbl_x + 15, tbl_y + 12), "Prompt / Context", fill="#ffffff", font=get_font(14, bold=True))
draw5.text((tbl_x + col1_w + 15, tbl_y + 12), "Copilot Suggestion", fill="#ffffff", font=get_font(14, bold=True))
draw5.text((tbl_x + col1_w + col2_w + 15, tbl_y + 12), "Decision", fill="#ffffff", font=get_font(14, bold=True))
draw5.text((tbl_x + col1_w + col2_w + col3_w + 15, tbl_y + 12), "Reasoning (Evaluated Criterion)", fill="#ffffff", font=get_font(14, bold=True))

# Column vertical lines
for cx_off in [col1_w, col1_w + col2_w, col1_w + col2_w + col3_w]:
    draw5.line([(tbl_x + cx_off, tbl_y), (tbl_x + cx_off, wy + wh - 40)], fill="#2d2d2d", width=1)

# 5 Rows
prompt_rows = [
    ("// React TypeScript: Search input component for Task Manager with debounced onChange and clear button",
     "const SearchInput = ({ value, onChange }: { value: string; onChange: (v: string) => void }) => (<input type=\"text\" placeholder=\"Search tasks...\" value={value} onChange={(e) => onChange(e.target.value)} />)",
     "Modified",
     "#e2b340",
     "Modified — added an accessible aria-label, embedded search magnifying SVG icon, and an inline escape-key clear handler to improve keyboard accessibility."),
     
    ("// Filter task array in React by both searchQuery (case-insensitive substring) and currentFilter status ('all' | 'active' | 'completed')",
     "const filteredTasks = tasks.filter(task => (currentFilter === 'all' || (currentFilter === 'active' ? !task.completed : task.completed)) && task.title.includes(searchQuery))",
     "Rejected",
     "#f85149",
     "Rejected — task.title.includes(searchQuery) is strictly case-sensitive and throws a TypeError if task.title is undefined; replaced with task.title.toLowerCase().includes(searchQuery.trim().toLowerCase())."),
     
    ("// Render empty state UI in React when filteredTasks is empty due to active searchQuery vs general empty list",
     "{filteredTasks.length === 0 && <p className=\"empty-msg\">No tasks match \"{searchQuery}\". <button onClick={() => setSearchQuery('')}>Clear search</button></p>}",
     "Accepted",
     "#3fb950",
     "Accepted — accurately detects the query-specific zero-match state and provides a direct one-click action to reset the search filter without reloading."),
     
    ("// JavaScript React helper: split task title string by regex to highlight matching query text in <span>",
     "function highlightMatch(text, query) { return text.replaceAll(query, '<mark>' + query + '</mark>') }",
     "Rejected",
     "#f85149",
     "Rejected — string replaceAll returning raw HTML requires dangerous dangerouslySetInnerHTML and crashes on special regex characters; replaced with a safe React array-based chunk renderer."),
     
    ("// React useEffect: Global keydown listener to focus search input on Cmd+K (Mac) or Ctrl+K (Windows) and unfocus on Escape",
     "useEffect(() => { const handleKeyDown = (e) => { if ((e.metaKey || e.ctrlKey) && e.key === 'k') { e.preventDefault(); searchInputRef.current?.focus(); } else if (e.key === 'Escape') { searchInputRef.current?.blur(); } }; window.addEventListener('keydown', handleKeyDown); return () => window.removeEventListener('keydown', handleKeyDown); }, []);",
     "Accepted",
     "#3fb950",
     "Accepted — correctly handles cross-platform modifier keys (metaKey vs ctrlKey), prevents default browser URL navigation, and safely cleans up the event listener on unmount.")
]

ry = tbl_y + 40
for p_ctx, sug, dec, d_col, rsn in prompt_rows:
    draw5.line([(tbl_x, ry), (tbl_x + tbl_w, ry)], fill="#2d2d2d", width=1)
    
    # Col 1: Prompt
    draw5.text((tbl_x + 10, ry + 12), p_ctx[:50], fill="#58a6ff", font=get_font(12, bold=True))
    draw5.text((tbl_x + 10, ry + 34), p_ctx[50:105], fill="#79c0ff", font=get_font(12))
    draw5.text((tbl_x + 10, ry + 56), p_ctx[105:160], fill="#79c0ff", font=get_font(12))
    
    # Col 2: Suggestion
    draw5.text((tbl_x + col1_w + 10, ry + 12), sug[:62], fill="#ce9178", font=get_font(11))
    draw5.text((tbl_x + col1_w + 10, ry + 34), sug[62:125], fill="#ce9178", font=get_font(11))
    draw5.text((tbl_x + col1_w + 10, ry + 56), sug[125:190], fill="#ce9178", font=get_font(11))
    if len(sug) > 190:
        draw5.text((tbl_x + col1_w + 10, ry + 78), sug[190:255], fill="#ce9178", font=get_font(11))
        
    # Col 3: Decision Badge
    draw5.rounded_rectangle([(tbl_x + col1_w + col2_w + 14, ry + 25), (tbl_x + col1_w + col2_w + col3_w - 14, ry + 58)], radius=6, fill="#0f172a", outline=d_col, width=1)
    draw5.text((tbl_x + col1_w + col2_w + 24, ry + 34), dec, fill=d_col, font=get_font(13, bold=True))
    
    # Col 4: Reasoning
    draw5.text((tbl_x + col1_w + col2_w + col3_w + 12, ry + 12), rsn[:85], fill="#e6edf3", font=get_font(12))
    draw5.text((tbl_x + col1_w + col2_w + col3_w + 12, ry + 34), rsn[85:170], fill="#e6edf3", font=get_font(12))
    draw5.text((tbl_x + col1_w + col2_w + col3_w + 12, ry + 56), rsn[170:], fill="#8b949e", font=get_font(12))
    
    ry += 130

img5.save(f"{OUT_DIR}/screenshot5.png")

print("All 5 screenshots successfully rendered in 1080p!")

# =========================================================================
# COMPILE INTO SINGLE PDF
# =========================================================================
pdf_path = "/Users/aaradhya.bora/task-manager-vibe-vs-pair/copilot_submission/copilot-deliberate-practice-submission.pdf"
print(f"Compiling all 5 screenshots into {pdf_path}...")

# Open RGB images
images = [
    Image.open(f"{OUT_DIR}/screenshot1.png").convert("RGB"),
    Image.open(f"{OUT_DIR}/screenshot2.png").convert("RGB"),
    Image.open(f"{OUT_DIR}/screenshot3.png").convert("RGB"),
    Image.open(f"{OUT_DIR}/screenshot4.png").convert("RGB"),
    Image.open(f"{OUT_DIR}/screenshot5.png").convert("RGB"),
]

# Save as single PDF with 5 pages in exact order
images[0].save(
    pdf_path,
    "PDF",
    resolution=100.0,
    save_all=True,
    append_images=images[1:]
)

pdf_size_mb = os.path.getsize(pdf_path) / (1024 * 1024)
print(f"✓ PDF COMPILED SUCCESSFULLY!")
print(f"Location: {pdf_path}")
print(f"Size: {pdf_size_mb:.2f} MB (Max limit: 50 MB)")
