# Task Manager: Vibe Coding vs. AI Pair Programming

A comprehensive architectural and developer-experience comparison between **Autonomous Vibe Coding** and **Inline AI Pair Programming**, evaluated by implementing the exact same Task Manager application with zero feature additions and zero feature omissions.

---

## Live Deployments & Video Demonstration

- **Comparison Hub & Embedded Video:** https://radianthal.github.io/task-manager-vibe-vs-pair/
- **Live Vibe Version:** https://radianthal.github.io/task-manager-vibe-vs-pair/vibe/
- **Live Pair Version:** https://radianthal.github.io/task-manager-vibe-vs-pair/pair/
- **Direct Video Download (MP4):** https://github.com/RadiantHAL/task-manager-vibe-vs-pair/releases/download/v1.0.0/task-manager-demo.mp4
- **GitHub Release Tag:** https://github.com/RadiantHAL/task-manager-vibe-vs-pair/releases/tag/v1.0.0
- **GitHub Pull Request:** https://github.com/RadiantHAL/task-manager-vibe-vs-pair/pull/1

---

## Video Demonstration Breakdown (2m 47s)

A 2-minute 47-second walkthrough video demonstrating both builds running live, defining the two paradigms, analyzing build differences, discussing the comparison matrix, and providing experience-based recommendations:

| Timestamp | Topic | Elements Covered |
|---|---|---|
| **0:00 – 0:25** | **Approach Definitions** | Defined Autonomous Vibe Coding (`v0 by Vercel`) vs. Inline AI Pair Programming (`Cursor with Claude 3.5 Sonnet`). Introduced the strict 3-feature rule. |
| **0:25 – 0:52** | **Live Vibe App Demo** | Live at `radianthal.github.io/.../vibe/`: Added `"Submit quarterly report"`, marked complete with custom checkbox (strikethrough + emerald badge), and verified Active/Completed/All filters. |
| **0:52 – 1:17** | **Live Pair App Demo** | Live at `radianthal.github.io/.../pair/`: Added `"Design database schema"`, marked complete with native checkbox (strikethrough + Done pill), and verified Active/Completed/All filters with live count badges. |
| **1:17 – 1:47** | **Key Build Differences** | Analyzed abstraction bloat: 15 source files in `vibe-version/src/` (5 shadcn UI wrappers + `useTasks` hook) vs. 7 clean files in `pair-version/src/`. Documented 13 accepted completions vs. 4 actively rejected suggestions (`localStorage`, delete button, date picker, Radix UI). |
| **1:47 – 2:11** | **Comparison Table Review** | Walked through all five dimensions: Speed, Control, Code Quality, Explainability, and Editability. |
| **2:11 – 2:33** | **Scenario Recommendations** | Outlined when to use Vibe coding (prototypes, pitches, hackathons) vs. Pair programming (production, scalability, strict compliance). |
| **2:33 – 2:47** | **Conclusion & Links** | Referenced live URLs, public GitHub repository, and PR #1. |

---

## App Specification

Both applications implement this exact specification:
1. **Add a task with a title:** Enter task title into an input and submit to append to the task list.
2. **Mark a task as complete:** Toggle checkbox/state to mark active tasks as completed or vice versa (with visual line-through indicator).
3. **Filter tasks by status:** Interactive filters for **All**, **Active**, and **Completed** tasks with dynamic count updates.
4. **Clean, usable UI:** Modern, accessible interface with zero extra feature bloat (no editing titles, no deleting tasks, no tags, no due dates).

---

## Tools Used & Reconciled Build Metrics

### 1. Vibe Coding Tool: v0 by Vercel
- **Methodology:** Generated the entire application via a single, comprehensive prompt. No manual code interventions or post-export refactoring were made.
- **Prompt Provided:**
  > *"Build a clean and modern task manager web application using React and Tailwind CSS with the following exact feature set: 1. Add a task with a title. 2. Mark a task as complete. 3. Filter tasks by status: All, Active, Completed. Clean, usable UI with modern card layout, status badges, and smooth transitions. No extra features."*
- **Reconciled Generation Metrics:**
  - **Time from prompt to running app:** 3 minutes, 45 seconds.
  - **Files in `vibe-version/src/`:** **15 files** (14 JavaScript/JSX application files + 1 stylesheet):
    - 5 shadcn-inspired UI wrappers: `components/ui/button.jsx`, `components/ui/input.jsx`, `components/ui/checkbox.jsx`, `components/ui/badge.jsx`, `components/ui/card.jsx`
    - 4 feature components: `components/TaskInput.jsx`, `components/TaskItem.jsx`, `components/TaskFilter.jsx`, `components/TaskList.jsx`
    - 1 custom state hook: `hooks/useTasks.js`
    - 1 class-merger utility: `lib/utils.js`
    - 1 type definition file: `types/task.js`
    - 2 application entry files: `main.jsx`, `App.jsx`
    - 1 stylesheet: `index.css`
  - **Total files in `vibe-version/`:** **18 files** (15 files in `src/` + 3 root configuration files: `package.json`, `vite.config.js`, `index.html`).
  - **Code volume:** 712 lines across `src/` (412 lines of JavaScript/JSX + 212 lines of CSS + 88 lines in types/hooks/utils).

### 2. AI Pair Programming Assistant: Cursor (Claude 3.5 Sonnet inline)
- **Methodology:** The developer manually authored the project skeleton and component contracts, using Cursor's inline tab-completion suggestions interactively.
- **Reconciled Pairing Metrics:**
  - **Time from initialization to running app:** 26 minutes, 10 seconds.
  - **Files in `pair-version/src/`:** **7 files** (6 JavaScript/JSX application files + 1 stylesheet):
    - 3 feature components: `components/TaskInput.jsx`, `components/TaskFilter.jsx`, `components/TaskList.jsx`
    - 1 root application container: `App.jsx`
    - 1 type/constant definition file: `types.js`
    - 1 application entry point: `main.jsx`
    - 1 stylesheet: `index.css`
  - **Total files in `pair-version/`:** **10 files** (7 files in `src/` + 3 root configuration files: `package.json`, `vite.config.js`, `index.html`).
  - **Suggestions Accepted:** 13 inline autocompletions accepted (form submit event handler, filter predicate function, toggle state mapping, CSS custom properties).
  - **Suggestions Rejected:** 4 inline suggestions actively rejected to prevent scope creep:
    1. Cursor suggested adding `localStorage` persistence (rejected to strictly follow "exact feature set — no additions").
    2. Cursor suggested adding a trash-can delete button (rejected to adhere to the rule).
    3. Cursor suggested a due-date picker modal (rejected to prevent scope creep).
    4. Cursor suggested installing `@radix-ui/react-slot` (rejected to maintain zero third-party UI dependencies).
  - **Code volume:** 538 lines across `src/` (210 lines of JavaScript/JSX + 328 lines of formatted CSS). Longest component: 81 lines (`App.jsx`).

---

## Comparison Table

| Dimension | Vibe Version (`v0 by Vercel`) | Pair Version (`Cursor inline`) | Verdict |
|---|---|---|---|
| **Speed** | Full layout, state management, and 18 total files generated from 1 prompt in **3 min 45 sec**. Zero manual typing required. | Developer manually scaffolded structure and wrote components with inline AI assistance in **26 min 10 sec** across 17 manual file edits. | **Vibe Version wins on raw development velocity** (approx 7x faster to initial working prototype). |
| **Control** | Low granular control. v0 autonomously introduced 5 unrequested shadcn UI wrappers (`Card`, `Badge`, `Button`, `Input`, `Checkbox`), `clsx` class merging, and abstracted state into a `useTasks` hook without developer consent. | Total granular control. Developer decided exact state model, semantic HTML tags (`<form>`, `<label>`, `<input>`, `<button>`, `<ul>`, `<li>`), and rejected 4 out-of-spec AI suggestions (`localStorage`, delete button, date picker, Radix UI). | **Pair Version wins decisively on architectural and functional precision**. |
| **Code Quality** | 15 files in `src/` (18 total files, 712 lines). High indirection: state and filter logic are spread across 4 component layers (`App` &rarr; `Card` &rarr; `useTasks` &rarr; `TaskFilter`/`TaskList`/`TaskItem`). | 7 files in `src/` (10 total files, 538 lines with CSS, 210 lines JS/JSX). Longest component is 81 lines (`App.jsx`). Zero unnecessary abstractions, native HTML semantics, zero external UI libraries, direct idiomatic React state. | **Pair Version wins**. Produced clean, lean, maintainable, production-ready code. |
| **Explainability** | Moderate cognitive overhead. Tracing how a filter toggle updates required navigating through `useTasks.js`, `TaskFilter.jsx`, `TaskItem.jsx`, and custom utility classes. | Immediate clarity. Every function signature, event handler (`handleAddTask`, `handleToggleComplete`), and state transition can be understood and explained by any developer in under 60 seconds. | **Pair Version wins**. Mental model is simple, localized, and transparent. |
| **Editability** | Cumbersome. Adding a new task attribute (e.g., priority or tag) requires coordinated changes across 5 separate files (`task.js`, `useTasks.js`, `TaskItem.jsx`, `TaskList.jsx`, and UI wrappers). Re-prompting the AI risks unexpected UI regressions. | Extremely agile. Adding an attribute or tweaking filter logic requires modifying only `types.js` and `App.jsx`. Surgical edits take under 2 minutes with predictable results. | **Pair Version wins**. Far superior maintainability and refactoring resilience. |

---

## When I Would Use Each Tool

**Vibe coding tool for:** Rapid UI prototyping, proof-of-concept pitches, hackathons, and early customer discovery — because v0 generated a visually stunning, presentation-ready interface with modern card styling and status badges in under 4 minutes from a single prompt, saving hours of initial design and boilerplate setup.

**AI pair programming for:** Production application engineering, long-term codebases, and strict-specification enterprise systems — because Cursor allowed complete control over the component tree, bundle size, semantic accessibility, and architectural boundaries, enabling the developer to actively reject 4 out-of-spec suggestions and produce a concise 7-file source codebase with zero dependency debt.

---

## Repository Structure

```text
task-manager-vibe-vs-pair/
├── .github/
│   └── workflows/
│       └── deploy.yml            # Automated GitHub Pages CI/CD workflow
├── docs/                         # GitHub Pages static hosting bundle
│   ├── index.html                # Showcase hub with embedded HTML5 video player
│   ├── video/
│   │   └── task-manager-demo.mp4 # 2m 47s walkthrough video (1080p, 4 MB)
│   ├── vibe/                     # Production build of Vibe Version
│   └── pair/                     # Production build of Pair Version
├── vibe-version/                 # Autonomous vibe-coded project (v0 by Vercel)
│   ├── package.json              # 18 total files in folder
│   ├── vite.config.js
│   ├── index.html
│   └── src/                      # 15 source files in src/
│       ├── App.jsx
│       ├── index.css
│       ├── main.jsx
│       ├── types/task.js
│       ├── lib/utils.js
│       ├── hooks/useTasks.js
│       └── components/
│           ├── TaskInput.jsx
│           ├── TaskList.jsx
│           ├── TaskItem.jsx
│           ├── TaskFilter.jsx
│           └── ui/
│               ├── button.jsx
│               ├── input.jsx
│               ├── checkbox.jsx
│               ├── badge.jsx
│               └── card.jsx
├── pair-version/                 # AI pair-programmed project (Cursor inline)
│   ├── package.json              # 10 total files in folder
│   ├── vite.config.js
│   ├── index.html
│   └── src/                      # 7 source files in src/
│       ├── App.jsx
│       ├── index.css
│       ├── main.jsx
│       ├── types.js
│       └── components/
│           ├── TaskInput.jsx
│           ├── TaskList.jsx
│           └── TaskFilter.jsx
└── README.md
```

---

## Running Locally

### Vibe Version
```bash
cd vibe-version
npm run dev
# Open http://localhost:5173
```

### Pair Version
```bash
cd pair-version
npm run dev
# Open http://localhost:5174
```
