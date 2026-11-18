import React from 'react';
import { FilterStatus } from '../types';

export function TaskFilter({ currentFilter, onFilterChange, counts }) {
  const filters = [
    { key: FilterStatus.ALL, label: 'All', count: counts.all },
    { key: FilterStatus.ACTIVE, label: 'Active', count: counts.active },
    { key: FilterStatus.COMPLETED, label: 'Completed', count: counts.completed },
  ];

  return (
    <div className="filter-bar" role="toolbar" aria-label="Task status filters">
      <div className="filter-group">
        {filters.map(({ key, label, count }) => (
          <button
            key={key}
            type="button"
            className={`filter-btn ${currentFilter === key ? 'active' : ''}`}
            onClick={() => onFilterChange(key)}
            aria-pressed={currentFilter === key}
          >
            <span>{label}</span>
            <span className="filter-count">{count}</span>
          </button>
        ))}
      </div>
    </div>
  );
}
