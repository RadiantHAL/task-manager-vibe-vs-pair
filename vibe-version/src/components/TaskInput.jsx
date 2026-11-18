import React, { useState } from 'react';
import { Input } from './ui/input';
import { Button } from './ui/button';

export function TaskInput({ onAddTask }) {
  const [title, setTitle] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!title.trim()) return;
    const success = onAddTask(title);
    if (success) {
      setTitle('');
    }
  };

  return (
    <form onSubmit={handleSubmit} className="flex gap-2.5 items-center">
      <Input
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        placeholder="What needs to be accomplished?"
        aria-label="New task title"
        autoFocus
      />
      <Button type="submit" disabled={!title.trim()}>
        <svg
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          strokeWidth="2.5"
          strokeLinecap="round"
          strokeLinejoin="round"
          className="w-4 h-4 mr-1.5"
        >
          <line x1="12" y1="5" x2="12" y2="19" />
          <line x1="5" y1="12" x2="19" y2="12" />
        </svg>
        Add Task
      </Button>
    </form>
  );
}
