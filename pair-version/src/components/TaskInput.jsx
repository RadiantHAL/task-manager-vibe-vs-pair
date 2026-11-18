import React, { useState } from 'react';

export function TaskInput({ onAddTask }) {
  const [title, setTitle] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    const trimmedTitle = title.trim();
    if (!trimmedTitle) return;

    onAddTask(trimmedTitle);
    setTitle('');
  };

  return (
    <form className="task-input-form" onSubmit={handleSubmit}>
      <label htmlFor="task-input" className="sr-only">Task title</label>
      <input
        id="task-input"
        type="text"
        className="task-input"
        placeholder="Add a new task..."
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        autoComplete="off"
      />
      <button
        type="submit"
        className="btn-primary"
        disabled={!title.trim()}
      >
        Add Task
      </button>
    </form>
  );
}
