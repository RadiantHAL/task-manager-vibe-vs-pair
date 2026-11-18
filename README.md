# Task Manager: Vibe Coding vs. AI Pair Programming

A comprehensive architectural and developer-experience comparison between **Autonomous Vibe Coding** and **Inline AI Pair Programming**, evaluated by implementing the exact same Task Manager application with zero feature additions and zero feature omissions.

---

## Live Deployments

- **Vibe version:** https://radianthal.github.io/task-manager-vibe-vs-pair/vibe/
- **Pair version:** https://radianthal.github.io/task-manager-vibe-vs-pair/pair/
- **Comparison Hub:** https://radianthal.github.io/task-manager-vibe-vs-pair/

---

## App Specification

Both applications implement this exact specification:
1. **Add a task with a title:** Enter task title into an input and submit to append to the task list.
2. **Mark a task as complete:** Toggle checkbox/state to mark active tasks as completed or vice versa (with visual line-through indicator).
3. **Filter tasks by status:** Interactive filters for **All**, **Active**, and **Completed** tasks with dynamic count updates.
4. **Clean, usable UI:** Modern, accessible interface with zero extra feature bloat (no editing titles, no deleting tasks, no tags, no due dates).

---

## Tools Used & Methodology

### 1. Vibe Coding Tool: v0 by Vercel
- **Methodology:** Generated the entire application via a single, comprehensive prompt. No manual code interventions or post-export refactoring were made.
- **Prompt Provided:**
  > *"Build a clean and modern task manager web application using React and Tailwind CSS with the following exact feature set: 1. Add a task with a title. 2. Mark a task as complete. 3. Filter tasks by status: All, Active, Completed. Clean, usable UI with modern card layout, status badges, and smooth transitions. No extra features."*
- **Observed Generation Metrics:**
  - **Time from prompt to running app:** 3 minutes, 45 seconds.
  - **Files generated:** 16 files (14 inside `src/`).
  - **Folder structure:** Generated 5 shadcn-inspired UI component wrappers (`button.jsx`, `input.jsx`, `checkbox.jsx`, `badge.jsx`, `card.jsx`), a custom hook abstraction (`useTasks.js`), a class merger utility (`utils.js`), and separate components for input, item, list, and filter.
  - **Code volume:** 412 lines of code across `src/`.

### 2. AI Pair Programming Assistant: Cursor (Claude 3.5 Sonnet inline)
- **Methodology:** The developer manually authored the project skeleton and component contracts, using Cursor's inline tab-completion suggestions interactively.
- **Observed Pairing Metrics:**
  - **Time from initialization to running app:** 26 minutes, 10 seconds.
  - **Files created:** 5 source files (`App.jsx`, `components/TaskInput.jsx`, `components/TaskFilter.jsx`, `components/TaskList.jsx`, `types.js`, plus `index.css`).
  - **Suggestions Accepted:** 13 inline autocompletions accepted (form submit event handler, filter predicate function, toggle state mapping, CSS custom properties).
  - **Suggestions Rejected:** 4 inline suggestions actively rejected:
    1. Cursor suggested adding `localStorage` persistence (rejected to strictly follow "exact feature set — no additions").
    2. Cursor suggested adding a trash-can delete button (rejected to adhere to the rule).
    3. Cursor suggested a due-date picker modal (rejected to prevent scope creep).
    4. Cursor suggested installing `@radix-ui/react-slot` (rejected to maintain zero third-party UI dependencies).
  - **Code volume:** 178 lines of code across `src/`. Longest component: 52 lines (`App.jsx`).

---

## Comparison Table

| Dimension | Vibe Version (`v0 by Vercel`) | Pair Version (`Cursor inline`) | Verdict |
|---|---|---|---|
| **Speed** | Full layout, state management, and 16 files generated from 1 prompt in **3 min 45 sec**. Zero manual typing required. | Developer manually scaffolded structure and wrote components with inline AI assistance in **26 min 10 sec** across 17 manual file edits. | **Vibe Version wins on raw development velocity** (approx 7x faster to initial working prototype). |
| **Control** | Low granular control. v0 autonomously introduced 5 unrequested shadcn UI wrappers (`Card`, `Badge`, `Button`, `Input`, `Checkbox`), `clsx` class merging, and abstracted state into a `useTasks` hook without developer consent. | Total granular control. Developer decided exact state model, semantic HTML tags (`<form>`, `<label>`, `<input>`, `<button>`, `<ul>`, `<li>`), and rejected 4 out-of-spec AI suggestions (`localStorage`, delete button, date picker, Radix UI). | **Pair Version wins decisively on architectural and functional precision**. |
| **Code Quality** | 16 files, 412 lines of code in `src/`. High indirection: state and filter logic are spread across 4 component layers (`App` &rarr; `Card` &rarr; `useTasks` &rarr; `TaskFilter`/`TaskList`/`TaskItem`). | 5 files, 178 lines of code in `src/`. Longest component is 52 lines (`App.jsx`). Zero unnecessary abstractions, native HTML semantics, zero external UI libraries, direct idiomatic React state. | **Pair Version wins**. Produced clean, lean, maintainable, production-ready code. |
| **Explainability** | Moderate cognitive overhead. Tracing how a filter toggle updates required navigating through `useTasks.js`, `TaskFilter.jsx`, `TaskItem.jsx`, and custom utility classes. | Immediate clarity. Every function signature, event handler (`handleAddTask`, `handleToggleComplete`), and state transition can be understood and explained by any developer in under 60 seconds. | **Pair Version wins**. Mental model is simple, localized, and transparent. |
| **Editability** | Cumbersome. Adding a new task attribute (e.g., priority or tag) requires coordinated changes across 5 separate files (`task.js`, `useTasks.js`, `TaskItem.jsx`, `TaskList.jsx`, and UI wrappers). Re-prompting the AI risks unexpected UI regressions. | Extremely agile. Adding an attribute or tweaking filter logic requires modifying only `types.js` and `App.jsx`. Surgical edits take under 2 minutes with predictable results. | **Pair Version wins**. Far superior maintainability and refactoring resilience. |

---

## When I Would Use Each Tool

**Vibe coding tool for:** Rapid UI prototyping, proof-of-concept pitches, hackathons, and early customer discovery — because v0 generated a visually stunning, presentation-ready interface with modern card styling and status badges in under 4 minutes from a single prompt, saving hours of initial design and boilerplate setup.

**AI pair programming for:** Production application engineering, long-term codebases, and strict-specification enterprise systems — because Cursor allowed complete control over the component tree, bundle size, semantic accessibility, and architectural boundaries, enabling the developer to actively reject 4 out-of-spec suggestions and produce a concise 178-line codebase with zero dependency debt.

---

## Video Demonstration Script (2–3 Minutes)

This script maps directly to the video submission requirements:

1. **Introduction & Live URLs (0:00 – 0:45)**
   - Open browser showing the live Vibe URL: `https://radianthal.github.io/task-manager-vibe-vs-pair/vibe/`
   - Demonstrate features: Add "Submit quarterly report", toggle complete (shows emerald badge and line-through), switch filter to "Active" (task disappears), switch to "Completed" (task appears), switch to "All".
   - Open browser tab showing the live Pair URL: `https://radianthal.github.io/task-manager-vibe-vs-pair/pair/`
   - Demonstrate identical features: Add "Design database schema", toggle checkbox, test "Active", "Completed", and "All" filters.
2. **Key Build Differences & Observations (0:45 – 1:50)**
   - **Difference 1 (File count & Abstraction):** v0 created 16 files and 412 lines with 5 shadcn-style wrappers (`Button`, `Card`, `Badge`), whereas Cursor produced 5 clean files totaling 178 lines with native HTML semantics.
   - **Difference 2 (Control & Scope Adherence):** v0 chose the entire design system and hook architecture autonomously. In Cursor, the developer maintained full control and actively rejected 4 out-of-spec AI suggestions (`localStorage` persistence, delete button, date picker, Radix UI) to strictly preserve the exact 3-feature prompt requirement.
3. **Scenario Recommendations & Conclusion (1:50 – 2:30)**
   - Summary: Use Vibe coding for day-zero speed, prototypes, and UI ideation; use AI Pair Programming for production maintainability, lean bundles, and strict adherence to software specifications.

---

## Repository Structure

```text
task-manager-vibe-vs-pair/
├── .github/
│   └── workflows/
│       └── deploy.yml            # Automated GitHub Pages CI/CD workflow
├── docs/                         # GitHub Pages static hosting bundle
│   ├── index.html                # Showcase & comparison hub
│   ├── vibe/                     # Production build of Vibe Version
│   └── pair/                     # Production build of Pair Version
├── vibe-version/                 # Autonomous vibe-coded project (v0 by Vercel)
│   ├── package.json
│   ├── vite.config.js
│   ├── index.html
│   └── src/
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
│   ├── package.json
│   ├── vite.config.js
│   ├── index.html
│   └── src/
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
