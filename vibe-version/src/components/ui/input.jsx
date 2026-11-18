import React from 'react';
import { cn } from '../../lib/utils';

export function Input({ className = '', type = 'text', ...props }) {
  return (
    <input
      type={type}
      className={cn(
        'w-full px-4 py-2.5 h-11 text-sm rounded-xl bg-slate-900/90 border border-slate-700/70 text-slate-100 placeholder:text-slate-500',
        'focus:outline-none focus:ring-2 focus:ring-indigo-500/50 focus:border-indigo-500 transition-all duration-200',
        className
      )}
      {...props}
    />
  );
}
