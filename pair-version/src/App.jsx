import React, { useState } from 'react';
import { FilterStatus } from './types';
import { TaskInput } from './components/TaskInput';
import { TaskFilter } from './components/TaskFilter';
import { TaskList } from './components/TaskList';

const INITIAL_TASKS = [
  { id: 't-1', title: 'Review pull request from team', completed: true },
  { id: 't-2', title: 'Prepare presentation slides for demo', completed: false },
  { id: 't-3', title: 'Verify deployment across all environments', completed: false },
];

export default function App() {
  const [tasks, setTasks] = useState(INITIAL_TASKS);
  const [filter, setFilter] = useState(FilterStatus.ALL);

  const handleAddTask = (title) => {
    const newTask = {
      id: `task-${Date.now()}`,
      title,
      completed: false,
    };
    setTasks((prev) => [newTask, ...prev]);
  };

  const handleToggleComplete = (id) => {
    setTasks((prev) =>
      prev.map((t) => (t.id === id ? { ...t, completed: !t.completed } : t))
    );
  };

  const filteredTasks = tasks.filter((task) => {
    if (filter === FilterStatus.ACTIVE) return !task.completed;
    if (filter === FilterStatus.COMPLETED) return task.completed;
    return true;
  });

  const counts = {
    all: tasks.length,
    active: tasks.filter((t) => !t.completed).length,
    completed: tasks.filter((t) => t.completed).length,
  };

  return (
    <div className="app-container">
      <main className="task-card">
        <header className="card-header">
          <div className="badge-pill">AI Pair Programming · Cursor</div>
          <h1 className="card-title">Task Manager</h1>
          <p className="card-subtitle">
            Engineered with Cursor inline completions and semantic HTML.
          </p>
        </header>

        <section className="card-body">
          {/* Feature 1: Add a task with a title */}
          <TaskInput onAddTask={handleAddTask} />

          {/* Feature 3: Filter tasks by status (All / Active / Completed) */}
          <TaskFilter
            currentFilter={filter}
            onFilterChange={setFilter}
            counts={counts}
          />

          {/* Feature 2: Mark a task as complete & view list */}
          <TaskList
            tasks={filteredTasks}
            onToggleComplete={handleToggleComplete}
            currentFilter={filter}
          />
        </section>

        <footer className="card-footer">
          <span>{counts.active} active tasks remaining</span>
          <span>7 Clean Files in src/ · Zero UI Bloat</span>
        </footer>
      </main>
    </div>
  );
}
