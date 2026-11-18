import React from 'react';
import { TaskItem } from './TaskItem';

export function TaskList({ tasks, onToggleTask, filter }) {
  if (tasks.length === 0) {
    return (
      <div className="py-12 text-center rounded-xl border border-dashed border-slate-800 bg-slate-900/20">
        <div className="w-10 h-10 mx-auto mb-3 rounded-full bg-slate-800/80 flex items-center justify-center text-slate-500">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="2"
            strokeLinecap="round"
            strokeLinejoin="round"
            className="w-5 h-5"
          >
            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z" />
            <polyline points="14 2 14 8 20 8" />
            <line x1="9" y1="15" x2="15" y2="15" />
          </svg>
        </div>
        <p className="text-sm font-medium text-slate-400">No tasks in this view</p>
        <p className="text-xs text-slate-600 mt-1">
          {filter === 'all'
            ? 'Add a task above to get started'
            : `No ${filter} tasks found`}
        </p>
      </div>
    );
  }

  return (
    <ul className="space-y-2.5">
      {tasks.map((task) => (
        <TaskItem key={task.id} task={task} onToggle={onToggleTask} />
      ))}
    </ul>
  );
}
