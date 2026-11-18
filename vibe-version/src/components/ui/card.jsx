import React from 'react';
import { cn } from '../../lib/utils';

export function Card({ className = '', children, ...props }) {
  return (
    <div
      className={cn(
        'rounded-2xl border border-slate-800/80 bg-slate-900/60 backdrop-blur-xl shadow-2xl shadow-black/40 overflow-hidden',
        className
      )}
      {...props}
    >
      {children}
    </div>
  );
}

export function CardHeader({ className = '', children, ...props }) {
  return (
    <div className={cn('p-6 border-b border-slate-800/60', className)} {...props}>
      {children}
    </div>
  );
}

export function CardTitle({ className = '', children, ...props }) {
  return (
    <h2 className={cn('text-xl font-bold tracking-tight text-white', className)} {...props}>
      {children}
    </h2>
  );
}

export function CardContent({ className = '', children, ...props }) {
  return (
    <div className={cn('p-6 space-y-6', className)} {...props}>
      {children}
    </div>
  );
}
