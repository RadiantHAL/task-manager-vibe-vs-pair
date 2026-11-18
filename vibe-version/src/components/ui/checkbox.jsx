import React from 'react';
import { cn } from '../../lib/utils';

export function Checkbox({ checked, onChange, id, className = '' }) {
  return (
    <button
      type="button"
      role="checkbox"
      aria-checked={checked}
      id={id}
      onClick={() => onChange(!checked)}
      className={cn(
        'w-5 h-5 rounded-md border flex items-center justify-center transition-all duration-200 cursor-pointer shrink-0',
        checked
          ? 'bg-emerald-500 border-emerald-500 text-slate-950 shadow-sm shadow-emerald-500/40'
          : 'border-slate-600 bg-slate-900/60 hover:border-indigo-400',
        className
      )}
    >
      {checked && (
        <svg
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          strokeWidth="3.5"
          strokeLinecap="round"
          strokeLinejoin="round"
          className="w-3.5 h-3.5"
        >
          <polyline points="20 6 9 17 4 12" />
        </svg>
      )}
    </button>
  );
}
