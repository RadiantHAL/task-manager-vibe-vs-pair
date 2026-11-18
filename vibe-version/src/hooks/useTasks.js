import { useState, useMemo } from 'react';
import { FILTER_STATUS } from '../types/task';

export function useTasks() {
  const [tasks, setTasks] = useState([
    { id: '1', title: 'Review pull request from team', completed: true, createdAt: Date.now() - 3600000 },
    { id: '2', title: 'Prepare presentation slides for demo', completed: false, createdAt: Date.now() - 1800000 },
    { id: '3', title: 'Verify deployment across all environments', completed: false, createdAt: Date.now() },
  ]);

  const [filter, setFilter] = useState(FILTER_STATUS.ALL);

  const addTask = (title) => {
    const trimmed = title.trim();
    if (!trimmed) return false;

    const newTask = {
      id: `${Date.now()}-${Math.random().toString(36).substring(2, 9)}`,
      title: trimmed,
      completed: false,
      createdAt: Date.now(),
    };

    setTasks((prev) => [newTask, ...prev]);
    return true;
  };

  const toggleTask = (id) => {
    setTasks((prev) =>
      prev.map((task) =>
        task.id === id ? { ...task, completed: !task.completed } : task
      )
    );
  };

  const filteredTasks = useMemo(() => {
    switch (filter) {
      case FILTER_STATUS.ACTIVE:
        return tasks.filter((t) => !t.completed);
      case FILTER_STATUS.COMPLETED:
        return tasks.filter((t) => t.completed);
      case FILTER_STATUS.ALL:
      default:
        return tasks;
    }
  }, [tasks, filter]);

  const counts = useMemo(() => {
    const active = tasks.filter((t) => !t.completed).length;
    const completed = tasks.filter((t) => t.completed).length;
    return { all: tasks.length, active, completed };
  }, [tasks]);

  return {
    tasks,
    filter,
    setFilter,
    addTask,
    toggleTask,
    filteredTasks,
    counts,
  };
}
