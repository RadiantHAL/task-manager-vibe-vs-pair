/**
 * @typedef {'all' | 'active' | 'completed'} FilterStatus
 *
 * @typedef {Object} Task
 * @property {string} id
 * @property {string} title
 * @property {boolean} completed
 * @property {number} createdAt
 */

export const FILTER_STATUS = {
  ALL: 'all',
  ACTIVE: 'active',
  COMPLETED: 'completed',
};
