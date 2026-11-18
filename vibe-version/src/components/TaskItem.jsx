import React from 'react';
import { Checkbox } from './ui/checkbox';
import { Badge } from './ui/badge';

export function TaskItem({ task, onToggle }) {
  return (
    <li
      className={`group flex items-center justify-between p-3.5 rounded-xl border transition-all duration-200 animate-fade-in ${
        task.completed
          ? 'bg-slate-900/30 border-slate-800/40 opacity-75'
          : 'bg-slate-900/70 border-slate-800 hover:border-slate-700/80 hover:bg-slate-850'
      }`}
    >
      <div className="flex items-center gap-3 min-w-0 flex-1">
        <Checkbox
          checked={task.completed}
          onChange={() => onToggle(task.id)}
          id={`task-${task.id}`}
        />
        <label
          htmlFor={`task-${task.id}`}
          className={`text-sm truncate cursor-pointer transition-all duration-200 select-none ${
            task.completed
              ? 'line-through text-slate-500 font-normal'
              : 'text-slate-200 font-medium'
          }`}
        >
          {task.title}
        </label>
      </div>

      <Badge variant={task.completed ? 'success' : 'default'} className="ml-3 shrink-0">
        {task.completed ? 'Completed' : 'Active'}
      </Badge>
    </li>
  );
}
