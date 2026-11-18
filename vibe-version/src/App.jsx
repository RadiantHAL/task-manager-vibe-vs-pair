import React from 'react';
import { useTasks } from './hooks/useTasks';
import { Card, CardHeader, CardTitle, CardContent } from './components/ui/card';
import { TaskInput } from './components/TaskInput';
import { TaskFilter } from './components/TaskFilter';
import { TaskList } from './components/TaskList';
import { Badge } from './components/ui/badge';

export default function App() {
  const {
    filter,
    setFilter,
    addTask,
    toggleTask,
    filteredTasks,
    counts,
  } = useTasks();

  return (
    <div className="flex-1 flex flex-col items-center justify-center p-4 sm:p-6 lg:p-8">
      <div className="w-full max-w-xl">
        {/* App Title Header */}
        <div className="text-center mb-8">
          <div className="inline-flex items-center gap-2 mb-3">
            <span className="h-2 w-2 rounded-full bg-emerald-400 animate-pulse"></span>
            <Badge variant="default" className="text-[11px] uppercase tracking-wider font-semibold">
              Vibe Coding Edition · v0 Prompt
            </Badge>
          </div>
          <h1 className="text-3xl sm:text-4xl font-extrabold tracking-tight text-white mb-2">
            Task Manager
          </h1>
          <p className="text-sm text-slate-400 max-w-sm mx-auto">
            Generated autonomously from a single prompt with card layout and badge state indicators.
          </p>
        </div>

        {/* Main Application Card */}
        <Card className="border-slate-800 bg-slate-900/80 backdrop-blur-xl shadow-2xl">
          <CardHeader className="flex flex-row items-center justify-between pb-4">
            <div>
              <CardTitle>My Workspace Tasks</CardTitle>
              <p className="text-xs text-slate-400 mt-1">
                {counts.active} remaining · {counts.completed} completed
              </p>
            </div>
            <div className="flex items-center gap-1.5 text-xs text-slate-400 bg-slate-800/80 px-2.5 py-1 rounded-lg border border-slate-700/60 font-mono">
              <span className="w-2 h-2 rounded-full bg-indigo-400"></span>
              v0.dev
            </div>
          </CardHeader>

          <CardContent className="space-y-6">
            {/* Feature 1: Add a task with a title */}
            <TaskInput onAddTask={addTask} />

            {/* Feature 3: Filter tasks by status (All / Active / Completed) */}
            <TaskFilter
              activeFilter={filter}
              onFilterChange={setFilter}
              counts={counts}
            />

            {/* Feature 2: Mark a task as complete & view list */}
            <TaskList
              tasks={filteredTasks}
              onToggleTask={toggleTask}
              filter={filter}
            />
          </CardContent>
        </Card>

        {/* Footer Meta */}
        <div className="mt-6 text-center text-xs text-slate-500">
          Built with React · Tailwind CSS · 16 Component Files Generated
        </div>
      </div>
    </div>
  );
}
