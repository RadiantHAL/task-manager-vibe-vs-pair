import React from 'react';
import { cn } from '../../lib/utils';

export function Button({
  className = '',
  variant = 'default',
  size = 'default',
  disabled = false,
  children,
  ...props
}) {
  const baseStyles = 'inline-flex items-center justify-center font-medium rounded-xl transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-indigo-500/50 disabled:opacity-50 disabled:cursor-not-allowed cursor-pointer select-none';

  const variants = {
    default: 'bg-indigo-600 hover:bg-indigo-500 text-white shadow-lg shadow-indigo-600/30 active:scale-[0.98]',
    secondary: 'bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700/60',
    outline: 'border border-slate-700 bg-transparent hover:bg-slate-800/60 text-slate-300',
    ghost: 'bg-transparent hover:bg-slate-800/60 text-slate-400 hover:text-slate-100',
  };

  const sizes = {
    sm: 'text-xs px-3 py-1.5 h-8',
    default: 'text-sm px-4 py-2.5 h-11',
    lg: 'text-base px-6 py-3 h-12',
  };

  return (
    <button
      className={cn(baseStyles, variants[variant] || variants.default, sizes[size] || sizes.default, className)}
      disabled={disabled}
      {...props}
    >
      {children}
    </button>
  );
}
