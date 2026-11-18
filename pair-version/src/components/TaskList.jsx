import React from 'react';

export function TaskList({ tasks, onToggleComplete, currentFilter }) {
  if (tasks.length === 0) {
    return (
      <div className="empty-state">
        <p className="empty-title">No tasks found</p>
        <p className="empty-desc">
          {currentFilter === 'all'
            ? 'Add your first task above.'
            : `There are no ${currentFilter} tasks.`}
        </p>
      </div>
    );
  }

  return (
    <ul className="task-list" aria-label="Tasks">
      {tasks.map((task) => (
        <li key={task.id} className={`task-item ${task.completed ? 'completed' : ''}`}>
          <label className="task-label">
            <input
              type="checkbox"
              className="task-checkbox"
              checked={task.completed}
              onChange={() => onToggleComplete(task.id)}
            />
            <span className="task-text">{task.title}</span>
          </label>
          <span className={`status-pill ${task.completed ? 'status-completed' : 'status-active'}`}>
            {task.completed ? 'Done' : 'Active'}
          </span>
        </li>
      ))}
    </ul>
  );
}
