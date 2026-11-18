import React from 'react';
import { FILTER_STATUS } from '../types/task';
import { Button } from './ui/button';
import { Badge } from './ui/badge';

export function TaskFilter({ activeFilter, onFilterChange, counts }) {
  const filters = [
    { key: FILTER_STATUS.ALL, label: 'All', count: counts.all },
    { key: FILTER_STATUS.ACTIVE, label: 'Active', count: counts.active },
    { key: FILTER_STATUS.COMPLETED, label: 'Completed', count: counts.completed },
  ];

  return (
    <div className="flex items-center justify-between border-b border-slate-800/80 pb-4">
      <div className="text-xs font-medium uppercase tracking-wider text-slate-400">
        Filter Tasks
      </div>
      <div className="flex gap-1.5 p-1 bg-slate-900/80 rounded-xl border border-slate-800">
        {filters.map(({ key, label, count }) => {
          const isActive = activeFilter === key;
          return (
            <button
              key={key}
              type="button"
              onClick={() => onFilterChange(key)}
              className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-medium transition-all duration-150 cursor-pointer ${
                isActive
                  ? 'bg-indigo-600 text-white shadow-sm'
                  : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800/60'
              }`}
            >
              <span>{label}</span>
              <span
                className={`text-[10px] px-1.5 py-0.2 rounded-full font-mono ${
                  isActive ? 'bg-indigo-700/80 text-white' : 'bg-slate-800 text-slate-400'
                }`}
              >
                {count}
              </span>
            </button>
          );
        })}
      </div>
    </div>
  );
}
